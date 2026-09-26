#!/usr/bin/env python3
"""Refresh prices in data/models.json from the SpicyAPI public catalog, then rebuild README.md."""

from __future__ import annotations

import datetime as dt
import json
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOG = "https://api.spicyapi.ai/console/v1/catalog/models?locale=en"


def main() -> int:
    req = urllib.request.Request(CATALOG, headers={"User-Agent": "nsfw-ai-video-prompts/refresh"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        items = {i["model"]: i for i in json.load(resp)["data"]["items"]}
    path = ROOT / "data" / "models.json"
    data = json.loads(path.read_text())
    changes = []
    for key, model in data["models"].items():
        live = items.get(model["id"])
        if live is None:
            changes.append(f"MISSING from catalog: {model['id']} ({key}) - update prompts that use it")
            continue
        variants = (live.get("price") or {}).get("variants") or []
        if "per_image" in model:
            new = float(live["price"]["amount"])
            if new != model["per_image"]:
                changes.append(f"{key}: ${model['per_image']} -> ${new} per image")
                model["per_image"] = new
            continue
        prices: dict[str, float] = {}
        for v in variants:
            fields = dict(part.split("=", 1) for part in v["variant"].split(";") if "=" in part)
            res = fields.get("resolution", v["variant"])
            if fields.get("generate_audio") == "true" and res in prices:
                continue  # keep the no-audio tier when audio is priced separately
            prices.setdefault(res, float(v["amount"]))
        if prices and prices != model["prices"]:
            changes.append(f"{key}: {model['prices']} -> {prices}")
            model["prices"] = prices
    data["read_on"] = dt.date.today().isoformat()
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print("\n".join(changes) or "no price changes")
    subprocess.run([sys.executable, str(ROOT / "scripts" / "build_readme.py")], check=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
