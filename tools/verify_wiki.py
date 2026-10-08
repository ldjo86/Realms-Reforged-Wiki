#!/usr/bin/env python3
"""Check that the generated documentation is internally consistent. Python 3.10+."""
from pathlib import Path
import json,re,zipfile
root=Path(__file__).resolve().parents[1]
enc=json.loads((root/'inventory/enchantments-verified-from-jar.json').read_text(encoding='utf8'))
rec=json.loads((root/'inventory/recipes-verified-from-jar.json').read_text(encoding='utf8'))
assert len(enc)==72 and len({e['id'] for e in enc})==72
assert len(rec)==44 and len({e['id'] for e in rec})==44
assert len(list((root/'assets/textures').rglob('*.png')))==82
assert all((root/f'docs/enchantments/fr/{e["id"]}.md').exists() for e in enc)
assert all((root/f'docs/enchantments/en/{e["id"]}.md').exists() for e in enc)
assert any(e['target_fr']=='Haches' and e['id']=='abattage' for e in enc)
assert any(e['target_fr']=='Bateaux et radeaux' and e['id']=='amarrage' for e in enc)
mds=list(root.rglob('*.md'))
missing=[]
for file in mds:
 txt=file.read_text(encoding='utf8')
 for link in re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)',txt):
  link=link.split('#')[0]
  if link and not link.startswith(('https://','http://','mailto:','#')) and not (file.parent/link).exists():missing.append((file.relative_to(root).as_posix(),link))
 for link in re.findall(r'!\[[^\]]*\]\(([^)]+)\)',txt):
  link=link.split('#')[0]
  if link and not link.startswith(('https://','http://')) and not (file.parent/link).exists():missing.append((file.relative_to(root).as_posix(),link))
assert not missing,missing[:15]
print(f'OK: {len(mds)} Markdown files, {len(enc)} enchants, {len(rec)} recipes, 82 PNG; internal links valid.')
