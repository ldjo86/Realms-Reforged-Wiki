#!/usr/bin/env python3
"""Validate Realms Reforged wiki documentation without revealing custom entities."""
from pathlib import Path
import json, re

root = Path(__file__).resolve().parents[1]
enc = json.loads((root / "inventory/enchantments-verified-from-jar.json").read_text(encoding="utf8"))
recipes = json.loads((root / "inventory/recipes-verified-from-jar.json").read_text(encoding="utf8"))

assert len(enc) == 72 and len({x["id"] for x in enc}) == 72
assert len(recipes) == 44 and len({x["id"] for x in recipes}) == 44
assert all((root / f'docs/enchantments/fr/{x["id"]}.md').exists() for x in enc)
assert all((root / f'docs/enchantments/en/{x["id"]}.md').exists() for x in enc)
assert any(x["target_fr"] == "Haches" and x["id"] == "abattage" for x in enc)
assert any(x["target_fr"] == "Bateaux et radeaux" and x["id"] == "amarrage" for x in enc)
assert "1.21" in (root / "docs/Version-et-provenance.md").read_text(encoding="utf8")

assets = root / "assets/textures"
items = list((assets / "items").rglob("*.png"))
blocks = list((assets / "blocks").rglob("*.png"))
assert len(items) == 31, "Item illustrations unexpectedly missing"
assert len(blocks) == 26, "Block illustrations unexpectedly missing"
assert len(list(assets.rglob("*.png"))) == 57, "Unexpected textures: entity images must stay unpublished"
for category in ("creatures", "golems"):
    assert not any((assets / category).rglob("*")), f'Entity appearances unexpectedly present: {category}'

all_markdown = list(root.rglob("*.md"))
missing = []
for page in all_markdown:
    body = page.read_text(encoding="utf8")
    if re.search(r"assets/textures/(creatures|golems)/", body):
        raise AssertionError(f"Creature texture referenced in {page.relative_to(root)}")
    # Inspect Markdown links and inline embedded images.
    refs = re.findall(r"!?(?:\[[^\]]*\])\(([^)]+)\)", body)
    refs += re.findall(r'(?:src|href)="([^"]+)"', body)
    for target in refs:
        dest = target.split("#", 1)[0]
        if not dest or dest.startswith(("http://", "https://", "mailto:", "#")):
            continue
        if not (page.parent / dest).exists():
            missing.append((str(page.relative_to(root)), dest))
assert not missing, missing[:15]

print(f"OK: {len(all_markdown)} Markdown pages, 72 enchants, 44 recipes, "
      f"{len(blocks)} block + {len(items)} item illustrations, no public creature textures.")
