#!/usr/bin/env python3
"""Render README.md from README.template.md and the JSON files in data/."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
UTM = "utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts"
GALLERY_SIZE = 12


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


def render_verified(items: list[dict]) -> str:
    featured = sorted(items, key=lambda i: (i["rating"] != "suggestive", i["model"]))[:GALLERY_SIZE]
    cells = []
    for it in featured:
        media = it["media"]
        cells.append(
            f'<td align="center" valign="top" width="33%">'
            f'<a href="{media["url"]}"><img src="{media["posterUrl"]}" alt="{it["alt"]}" width="260"></a><br>'
            f'<b>{it["title"]}</b><br>'
            f'<sub><a href="https://spicyapi.ai/models/{it["familyPageSlug"]}?{UTM}&utm_content=verified">'
            f'{it["familyDisplayName"]}</a> · reviewed {it["reviewedOn"]}</sub></td>'
        )
    rows = ["<table>"]
    for i in range(0, len(cells), 3):
        rows.append("<tr>" + "".join(cells[i:i + 3]) + "</tr>")
    rows.append("</table>")
    rows.append("")
    rows.append(f"<details><summary><b>Show all {len(items)} verified prompts (full text)</b></summary>\n")
    for it in sorted(items, key=lambda i: (i["familyDisplayName"], i["title"])):
        needs = " · needs your own first frame" if it["hasInputMedia"] else ""
        rows.append(f"**{it['title']}** · `{it['model']}`{needs} · [▶ output]({it['media']['url']})\n")
        rows.append("```text\n" + it["prompt"].strip() + "\n```\n")
    rows.append("</details>")
    return "\n".join(rows)


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
    verified = load("verified-examples.json")["items"]

    toc, prompts = render_prompts(video, models)
    replacements = {
        "{{READ_ON}}": catalog["read_on"],
        "{{VIDEO_COUNT}}": str(len(video["prompts"])),
        "{{IMAGE_COUNT}}": str(len(images["prompts"])),
        "{{VERIFIED_COUNT}}": str(len(verified)),
        "{{MODEL_TABLE}}": render_model_table(models),
        "{{VERIFIED}}": render_verified(verified),
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
    print(f"README.md written: {len(video['prompts'])} video, {len(images['prompts'])} image, {len(verified)} verified")


if __name__ == "__main__":
    main()
