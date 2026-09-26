#!/usr/bin/env python3
"""Validate prompt data: model settings, adult-only wording, banned terms, and README freshness."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

# Terms that must never appear in prompts (youth, real-person or non-consent framing).
BANNED = re.compile(
    r"\b(teen\w*|school\s?girl|school uniform|student|loli\w*|shota|child\w*|kid|minor|underage|"
    r"young[- ]looking|petite|little girl|chibi|celebrity|drunk|asleep|unconscious|forced|"
    r"non-?consensual|incest|step-?(sister|mom|brother|dad)|undress(ing)? (her|him|a photo))\b",
    re.IGNORECASE,
)
ADULT_MARKER = re.compile(
    r"\b(adult|in (her|his|their) (early |late )?(20s|30s|40s)|woman in her|man in his|mature female|"
    r"<trigger word>, the same adult)\b",
    re.IGNORECASE,
)
DURATIONS = {
    "wan22": {5, 8}, "wan22lora": {5, 8}, "wan26": {5, 10, 15},
    "ltx23": set(range(3, 21)), "sd15": set(range(4, 13)), "sd20mini": set(range(4, 16)),
    "sd20fast": set(range(4, 16)), "sd20": set(range(4, 16)), "sd25": set(range(4, 31)),
    "h3": set(range(3, 16)), "vidu": set(range(1, 17)), "wan27": set(range(2, 16)),
}


def main() -> int:
    models = json.loads((DATA / "models.json").read_text())["models"]
    video = json.loads((DATA / "video-prompts.json").read_text())
    images = json.loads((DATA / "image-prompts.json").read_text())
    errors: list[str] = []

    ids = [p["id"] for p in video["prompts"]] + [p["id"] for p in images["prompts"]]
    dupes = {i for i in ids if ids.count(i) > 1}
    if dupes:
        errors.append(f"duplicate ids: {sorted(dupes)}")

    cats = {c["key"] for c in video["categories"]}
    for p in video["prompts"]:
        pid, m = p["id"], models.get(p["model"])
        if p["cat"] not in cats:
            errors.append(f"{pid}: unknown category {p['cat']}")
        if m is None or "prices" not in m:
            errors.append(f"{pid}: unknown video model {p['model']}")
            continue
        if p["res"] not in m["prices"]:
            errors.append(f"{pid}: {p['res']} not offered by {m['name']} ({list(m['prices'])})")
        if p["dur"] not in DURATIONS[p["model"]]:
            errors.append(f"{pid}: {p['dur']} s not valid for {m['name']} ({m['durations']})")
        text = " ".join([p["prompt"], p["frame"], p["title"]])
        if BANNED.search(text):
            errors.append(f"{pid}: banned term '{BANNED.search(text).group(0)}'")
        is_template = p["cat"] in ("motion",) or pid == "L06"
        if not is_template and not ADULT_MARKER.search(p["prompt"]):
            errors.append(f"{pid}: prompt does not state an adult subject")
        ratios = m.get("aspect_ratios")
        if ratios and p["ar"] != "any" and p["ar"] not in ratios:
            errors.append(f"{pid}: aspect ratio {p['ar']} not accepted by {m['name']}")
        words = len(p["prompt"].split())
        if words > 110:
            errors.append(f"{pid}: prompt too long ({words} words)")

    for p in images["prompts"]:
        m = models.get(p["model"])
        if m is None or "per_image" not in m:
            errors.append(f"{p['id']}: unknown image model {p['model']}")
        elif "sizes" in m and p["size"].replace("x", "*") not in m["sizes"]:
            errors.append(f"{p['id']}: size {p['size']} not offered by {m['name']}")
        elif "max_side" in m and max(int(v) for v in p["size"].split("x")) > m["max_side"]:
            errors.append(f"{p['id']}: size {p['size']} exceeds {m['max_side']} px for {m['name']}")
        if BANNED.search(p["prompt"]):
            errors.append(f"{p['id']}: banned term '{BANNED.search(p['prompt']).group(0)}'")
        if not ADULT_MARKER.search(p["prompt"]):
            errors.append(f"{p['id']}: prompt does not state an adult subject")

    # README must be regenerated after data changes.
    before = (ROOT / "README.md").read_text()
    subprocess.run([sys.executable, str(ROOT / "scripts" / "build_readme.py")], check=True, capture_output=True)
    if (ROOT / "README.md").read_text() != before:
        errors.append("README.md was stale; it has been regenerated, commit the result")

    for e in errors:
        print("ERROR", e)
    print(f"checked {len(video['prompts'])} video + {len(images['prompts'])} image prompts: "
          f"{'OK' if not errors else f'{len(errors)} problem(s)'}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
