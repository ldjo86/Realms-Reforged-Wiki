#!/usr/bin/env python3
"""Check that the generated documentation is internally consistent. Python 3.10+."""
from pathlib import Path
import json,re,zipfile,hashlib
root=Path(__file__).resolve().parents[1]
enc=json.loads((root/'inventory/enchantments-verified-from-jar.json').read_text(encoding='utf8'))
rec=json.loads((root/'inventory/recipes-verified-from-jar.json').read_text(encoding='utf8'))
assert len(enc)==72 and len({e['id'] for e in enc})==72
assert len(rec)==44 and len({e['id'] for e in rec})==44
assert len(list((root/'assets/textures').rglob('*.png')))==82
# The included 1.13.1 / 26.x source JAR has 16 named golem textures but 4 unique PNG contents.
# This is an audit warning about the specific archive, NOT proof of all versions' appearances.
golem_pngs=list((root/'assets/textures/golems').glob('*.png'))
assert len(golem_pngs)==16
hash_inventory=json.loads((root/'inventory/golem-texture-sha256.json').read_text(encoding='utf8'))
assert hash_inventory['png_file_count']==16
assert hash_inventory['sha256_by_filename']=={f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted(golem_pngs)}
assert hash_inventory['unique_image_sha256_count']==len(set(hash_inventory['sha256_by_filename'].values()))
unique_go_golem=len({hashlib.sha256(f.read_bytes()).digest() for f in golem_pngs})
if unique_go_golem<16:
 assert 'identiques' in (root/'docs/Golems-FR.md').read_text(encoding='utf8')
 assert 'identical' in (root/'docs/Material-Golems-EN.md').read_text(encoding='utf8')
for readme in ('README.md','README.fr.md'):
 assert '<p><img src="assets/textures/golems/' not in (root/readme).read_text(encoding='utf8')
assert '1.21' in (root/'docs/Version-et-provenance.md').read_text(encoding='utf8')
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
print(f'OK: {len(mds)} Markdown files, {len(enc)} enchants, {len(rec)} recipes, 82 PNG; golem source textures unique={unique_go_golem}/16; internal links valid.')
