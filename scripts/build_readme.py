#!/usr/bin/env python3
"""Render README.md from README.template.md and the JSON files in data/."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
UTM = "utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts"


def load(name: str) -> dict:
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def anchor(title: str) -> str:
    """Reproduce GitHub's heading anchor algorithm closely enough for our titles."""
    slug = title.strip().lower()
    slug = re.sub(r"[^\w\- ]", "", slug)
    return slug.replace(" ", "-")


def model_link(model: dict, content: str) -> str:
    return f"[{model['name']}](https://spicyapi.ai/models/{model['page']}?{UTM}&utm_content={content})"


def money(value: float) -> str:
    text = f"{value:.5f}".rstrip("0").rstrip(".")
    if "." in text and len(text.split(".")[1]) == 1:
        text += "0"
    return f"${text}"


def clip_cost(model: dict, res: str, dur: int) -> float:
    return model["prices"][res] * dur


def render_model_table(models: dict) -> str:
    rows = ["| Model | API model ID | Duration | From (per second) |", "|---|---|---|---|"]
    for key, m in models.items():
        if "prices" not in m:
            continue
        cheapest_res, cheapest = min(m["prices"].items(), key=lambda kv: kv[1])
        rows.append(
            f"| {model_link(m, 'model-table')} | `{m['id']}` | {m['durations']} | "
            f"{money(cheapest)} ({cheapest_res}) |"
        )
    rows.append("")
    rows.append("First-frame image models: " + ", ".join(
        f"{model_link(m, 'model-table')} ({money(m['per_image'])} per image)"
        for m in models.values() if "per_image" in m
    ) + ".")
    return "\n".join(rows)


FAMILY_ORDER = [
    "Wan 2.2 Spicy", "Wan 2.2 Spicy LoRA", "LTX 2.3 Spicy", "LTX 2.3 Spicy LoRA", "Seedance 1.5 Pro Spicy",
    "Seedance 2.0 Mini Spicy", "Seedance 2.0 Fast Spicy", "Seedance 2.0 Spicy", "Seedance 2.5 Spicy",
    "MiniMax H3 Spicy", "Vidu Q3 Spicy", "Wan 2.6 Spicy", "Wan 2.7 Spicy",
    "Z-Image Spicy", "Z-Image Spicy Pro", "Qwen Image Edit Spicy", "Prefect Pony XL",
]


def render_showcase(items: list[dict]) -> tuple[str, str]:
    """Return (family index line, full showcase body)."""
    families: dict[str, list[dict]] = {}
    for it in items:
        families.setdefault(it["family"], []).append(it)
    order = [f for f in FAMILY_ORDER if f in families] + sorted(set(families) - set(FAMILY_ORDER))
    index = " · ".join(f"[{f}](#showcase-{anchor(f)}) ({len(families[f])})" for f in order)
    body = []
    for fam in order:
        group = families[fam]
        page = group[0]["page"]
        body.append(f'<a id="showcase-{anchor(fam)}"></a>\n')
        body.append(f"### {fam}\n")
        body.append(f"[Model page](https://spicyapi.ai/models/{page}?{UTM}&utm_content=showcase) · "
                    f"`{'` · `'.join(sorted({g['model'] for g in group}))}`\n")
        shown = [g for g in group if g["preview"]]
        if shown:
            body.append("<table>")
            for i in range(0, len(shown), 3):
                cells = []
                for g in shown[i:i + 3]:
                    alt = (g.get("alt") or g["title"]).replace('"', "'")
                    cells.append(
                        f'<td align="center" valign="top" width="33%"><a href="{g["media"]}">'
                        f'<img src="{g["preview"]}" alt="{alt}" width="240"></a><br>'
                        f'<sub><b>{g["title"]}</b></sub></td>'
                    )
                body.append("<tr>" + "".join(cells) + "</tr>")
            body.append("</table>\n")
        for g in group:
            label = "▶ full clip" if g["mime"] == "video/mp4" else "full-size image"
            if g.get("excluded"):
                head = (f"<b>{g['title']}</b> · preview not shown on GitHub · "
                        f"<a href=\"https://spicyapi.ai/models/{page}?{UTM}&utm_content=showcase\">view on spicyapi.ai</a>")
            else:
                head = f"<b>{g['title']}</b> · <a href=\"{g['media']}\">{label}</a>"
            body.append(f"<details><summary>{head}</summary>\n")
            prompt = (g.get("input") or {}).get("prompt")
            if prompt:
                body.append("```text\n" + prompt.strip() + "\n```\n")
            if g.get("note") and not g["note"].startswith("The exact request behind the clip on this page"):
                body.append(f"**Why it works:** {g['note']}\n")
            request = {"model": g["model"], "input": g.get("input") or {}}
            body.append("Exact request (`POST /api/v1/jobs/createTask`):\n")
            body.append("```json\n" + json.dumps(request, indent=2, ensure_ascii=False) + "\n```\n")
            body.append("</details>\n")
    return index, "\n".join(body)


def render_prompts(data: dict, models: dict) -> tuple[str, str]:
    toc, body = [], []
    for cat in data["categories"]:
        items = [p for p in data["prompts"] if p["cat"] == cat["key"]]
        title = cat["title"]
        toc.append(f"  - [{title}](#{anchor(title)}) ({len(items)})")
        body.append(f"### {title}\n\n{cat['intro']}\n")
        for p in items:
            m = models[p["model"]]
            cost = money(clip_cost(m, p["res"], p["dur"]))
            ar = "any aspect ratio" if p["ar"] == "any" else p["ar"]
            body.append(f"#### {p['id']} · {p['title']}\n")
            body.append("```text\n" + p["prompt"] + "\n```\n")
            body.append("| Model | Settings | Cost per run | Level |")
            body.append("|---|---|---|---|")
            body.append(f"| {model_link(m, p['id'].lower())} | {p['res']} · {p['dur']} s · {ar} | {cost} | {p['level']} |\n")
            body.append(f"**First frame:** {p['frame']}  ")
            body.append(f"**Tip:** {p['tip']}\n")
    return "\n".join(toc), "\n".join(body)


def render_image_prompts(data: dict, models: dict) -> str:
    out = []
    for p in data["prompts"]:
        m = models[p["model"]]
        out.append(f"#### {p['id']} · {p['title']}\n")
        out.append("```text\n" + p["prompt"] + "\n```\n")
        w, h = p["size"].split("x")
        params = f"`size={w}*{h}`" if "sizes" in m else f"`width={w}` `height={h}`"
        out.append(f"{model_link(m, p['id'].lower())} · {params} · {money(m['per_image'])} per image\n")
    return "\n".join(out)


def main() -> None:
    catalog = load("models.json")
    models = catalog["models"]
    video = load("video-prompts.json")
    images = load("image-prompts.json")
    showcase = load("showcase.json")["items"]

    toc, prompts = render_prompts(video, models)
    showcase_index, showcase_body = render_showcase(showcase)
    replacements = {
        "{{READ_ON}}": catalog["read_on"],
        "{{VIDEO_COUNT}}": str(len(video["prompts"])),
        "{{IMAGE_COUNT}}": str(len(images["prompts"])),
        "{{SHOWCASE_COUNT}}": str(len(showcase)),
        "{{PREVIEW_COUNT}}": str(sum(1 for i in showcase if i["preview"])),
        "{{MODEL_TABLE}}": render_model_table(models),
        "{{SHOWCASE_INDEX}}": showcase_index,
        "{{SHOWCASE}}": showcase_body,
        "{{PROMPTS_TOC}}": toc,
        "{{PROMPTS}}": prompts,
        "{{IMAGE_INTRO}}": images["intro"],
        "{{IMAGE_PROMPTS}}": render_image_prompts(images, models),
    }
    text = (ROOT / "README.template.md").read_text(encoding="utf-8")
    for key, value in replacements.items():
        text = text.replace(key, value)
    leftover = re.findall(r"\{\{[A-Z_]+\}\}", text)
    if leftover:
        raise SystemExit(f"Unfilled placeholders: {leftover}")
    (ROOT / "README.md").write_text(text, encoding="utf-8")
    print(f"README.md written: {len(video['prompts'])} video, {len(images['prompts'])} image, {len(showcase)} showcase")


if __name__ == "__main__":
    main()
