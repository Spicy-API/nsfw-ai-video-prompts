#!/usr/bin/env python3
"""Render README.md from README.template.md and the JSON files in data/."""

from __future__ import annotations

import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
UTM_BASE = "utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts"
UTM = UTM_BASE
LANGS = ["", "ja", "ko", "fr", "es"]
LANG = ""          # set per render pass
I18N: dict = {}    # data/i18n/<lang>.json for the current pass


def L(key: str, default: str) -> str:
    return I18N.get("labels", {}).get(key, default)


def site(path: str, content: str) -> str:
    prefix = f"/{LANG}" if LANG else ""
    suffix = f"-{LANG}" if LANG else ""
    return f"https://spicyapi.ai{prefix}{path}?{UTM_BASE}&utm_content={content}{suffix}"


def load(name: str) -> dict:
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def anchor(title: str) -> str:
    """Reproduce GitHub's heading anchor algorithm closely enough for our titles."""
    slug = title.strip().lower()
    slug = re.sub(r"[^\w\- ]", "", slug)
    return slug.replace(" ", "-")


def model_link(model: dict, content: str) -> str:
    return f"[{model['name']}]({site('/models/' + model['page'], content)})"


def money(value: float) -> str:
    text = f"{value:.5f}".rstrip("0").rstrip(".")
    if "." in text and len(text.split(".")[1]) == 1:
        text += "0"
    return f"${text}"


def clip_cost(model: dict, res: str, dur: int) -> float:
    return model["prices"][res] * dur


TASK_ABBR = {"image-to-video": "I2V", "text-to-video": "T2V", "reference-to-video": "Ref2V", "video-extend": "Extend",
             "character-animation": "Animate", "text-to-image": "T2I", "edit": "Edit"}
UNIT = {"per_second": "/s", "per_image": "/image", "per_request": "/request"}


def _duration(fam: dict) -> str:
    for ep in fam["endpoints"]:
        d = [x for x in (ep.get("durations") or []) if isinstance(x, (int, float)) and x > 0]
        if not d:
            continue
        lo, hi = min(d), max(d)
        if ep.get("duration_kind") == "range" or (len(d) > 2 and sorted(d) == list(range(int(lo), int(hi) + 1))):
            return f"{int(lo)}–{int(hi)} s"
        return ", ".join(str(int(x)) for x in sorted(d)) + " s"
    return "—"


def render_model_table(catalog: dict) -> str:
    """Catalog order = SpicyAPI's own popularity/version ordering. Spicy editions plus
    standard families whose generation endpoints are tier `unrestricted`."""
    out = []
    for modality, title in (("video", L("video_models", "**Video models**")),
                            ("image", L("image_models", "**Image models** (first frames and stills)"))):
        out.append(title + "\n")
        head = (f"| {L('col_model', 'Model')} | {L('col_type', 'Type')} | {L('col_tasks', 'Tasks')} | "
                + (f"{L('col_duration', 'Duration')} | " if modality == "video" else "") + f"{L('col_from', 'From')} |")
        out += [head, "|---|---|---|" + ("---|" if modality == "video" else "") + "---|"]
        for fam in catalog["families"]:
            if fam["modality"] != modality:
                continue
            ep = min(fam["endpoints"], key=lambda e: e["from"])
            price = f"${ep['from']:.5f}".rstrip("0").rstrip(".") + UNIT.get(ep["unit"], "")
            tasks = ", ".join(dict.fromkeys(TASK_ABBR.get(e["task"], e["task"]) for e in fam["endpoints"]))
            kind = "🌶️ Spicy" if fam["spicy"] else L("standard", "Standard")
            cells = [f"[{fam['name']}]({site('/models/' + fam['page'], 'model-table')})", kind, tasks]
            cells += [_duration(fam)] if modality == "video" else []
            cells.append(price)
            out.append("| " + " | ".join(cells) + " |")
        out.append("")
    return "\n".join(out)


def render_showcase(items: list[dict]) -> str:
    """One row per case: the preview on the left, its title and prompt on the right.
    Families keep catalog order (SpicyAPI's popularity/version ordering)."""
    body, seen = [], []
    for it in items:
        if it["family"] not in seen:
            seen.append(it["family"])
    for fam in seen:
        group = [g for g in items if g["family"] == fam]
        page = group[0]["page"]
        kind = (L("spicy_edition", "🌶️ Spicy edition") if group[0]["type"] == "spicy"
                else L("standard_unrestricted", "Standard model, catalog tier: unrestricted"))
        link = site(f"/models/{page}", "showcase")
        body.append(f"### {fam}\n")
        body.append(f"<sub>{kind} · <a href=\"{link}\">{L('model_page', 'model page')}</a></sub>\n")
        body.append("<table>")
        for g in group:
            if g["preview"]:
                left = (f'<a href="{g["media"]}"><img src="{g["preview"]}" alt="{html.escape(g.get("alt") or g["title"])}" '
                        f'width="230"></a>')
            else:
                left = (f'<sub>{L("preview_hidden", "Preview not shown on GitHub.")}<br>'
                        f'<a href="{link}">{L("see_on_site", "See it on spicyapi.ai")}</a></sub>')
            label = L("full_clip", "▶ full clip") if g["mime"] == "video/mp4" else L("full_size", "full size")
            clip = f' · <a href="{g["media"]}">{label}</a>' if g["preview"] else ""
            right = (f'<b>{html.escape(g["title"])}</b><br><sub><code>{g["model"]}</code>{clip}</sub><br><br>'
                     f'{html.escape(g["prompt"].strip())}')
            body.append(f'<tr><td width="250" align="center" valign="top">{left}</td><td valign="top">{right}</td></tr>')
        body.append("</table>\n")
    return "\n".join(body)


def render_prompts(data: dict, models: dict) -> tuple[str, str]:
    toc, body = [], []
    tr_cat = I18N.get("categories", {})
    tr_p = I18N.get("prompts", {})
    levels = I18N.get("labels", {}).get("levels", {})
    for cat in data["categories"]:
        items = [p for p in data["prompts"] if p["cat"] == cat["key"]]
        title = tr_cat.get(cat["key"], {}).get("title", cat["title"])
        intro = tr_cat.get(cat["key"], {}).get("intro", cat["intro"])
        toc.append(f"  - [{title}](#{anchor(title)}) ({len(items)})")
        body.append(f"### {title}\n\n{intro}\n")
        for p in items:
            m = models[p["model"]]
            cost = money(clip_cost(m, p["res"], p["dur"]))
            t = tr_p.get(p["id"], {})
            ar = L("any_aspect", "any aspect ratio") if p["ar"] == "any" else p["ar"]
            body.append(f"#### {p['id']} · {t.get('title', p['title'])}\n")
            body.append("```text\n" + p["prompt"] + "\n```\n")
            body.append(f"| {L('col_model', 'Model')} | {L('col_settings', 'Settings')} | "
                        f"{L('col_cost', 'Cost per run')} | {L('col_level', 'Level')} |")
            body.append("|---|---|---|---|")
            body.append(f"| {model_link(m, p['id'].lower())} | {p['res']} · {p['dur']} s · {ar} | {cost} | "
                        f"{levels.get(p['level'], p['level'])} |\n")
            colon = L("colon", ":")
            body.append(f"**{L('first_frame', 'First frame')}{colon}** {t.get('frame', p['frame'])}  ")
            body.append(f"**{L('tip', 'Tip')}{colon}** {t.get('tip', p['tip'])}\n")
    return "\n".join(toc), "\n".join(body)


def render_image_prompts(data: dict, models: dict) -> str:
    out = []
    tr = I18N.get("images", {})
    for p in data["prompts"]:
        m = models[p["model"]]
        out.append(f"#### {p['id']} · {tr.get(p['id'], {}).get('title', p['title'])}\n")
        out.append("```text\n" + p["prompt"] + "\n```\n")
        if "aspect_ratio" in p:
            params = f"`aspect_ratio={p['aspect_ratio']}` `resolution=1k`"
        else:
            w, h = p["size"].split("x")
            params = f"`size={w}*{h}`" if "sizes" in m else f"`width={w}` `height={h}`"
        out.append(f"{model_link(m, p['id'].lower())} · {params} · {money(m['per_image'])} {L('per_image', 'per image')}\n")
    return "\n".join(out)


def render(lang: str) -> str | None:
    global LANG, I18N
    template_path = ROOT / ("README.template.md" if not lang else f"README.template.{lang}.md")
    if not template_path.exists():
        return None
    LANG = lang
    i18n_path = DATA / "i18n" / f"{lang}.json"
    I18N = json.loads(i18n_path.read_text(encoding="utf-8")) if lang and i18n_path.exists() else {}
    catalog = load("models.json")
    models = catalog["models"]
    video = load("video-prompts.json")
    images = load("image-prompts.json")
    showcase = load("showcase.json")["items"]
    toc, prompts = render_prompts(video, models)
    replacements = {
        "{{READ_ON}}": catalog["read_on"],
        "{{VIDEO_COUNT}}": str(len(video["prompts"])),
        "{{IMAGE_COUNT}}": str(len(images["prompts"])),
        "{{SHOWCASE_COUNT}}": str(len(showcase)),
        "{{PREVIEW_COUNT}}": str(sum(1 for i in showcase if i["preview"])),
        "{{MODEL_TABLE}}": render_model_table(load("catalog.json")),
        "{{SHOWCASE}}": render_showcase(showcase),
        "{{PROMPTS_TOC}}": toc,
        "{{PROMPTS}}": prompts,
        "{{IMAGE_INTRO}}": I18N.get("images", {}).get("intro", images["intro"]),
        "{{IMAGE_PROMPTS}}": render_image_prompts(images, models),
    }
    text = template_path.read_text(encoding="utf-8")
    for key, value in replacements.items():
        text = text.replace(key, value)
    leftover = re.findall(r"\{\{[A-Z_]+\}\}", text)
    if leftover:
        raise SystemExit(f"{template_path.name}: unfilled placeholders {leftover}")
    out = ROOT / ("README.md" if not lang else f"README.{lang}.md")
    out.write_text(text, encoding="utf-8")
    return out.name


def main() -> None:
    written = [name for name in (render(lang) for lang in LANGS) if name]
    print("written:", ", ".join(written))


if __name__ == "__main__":
    main()
