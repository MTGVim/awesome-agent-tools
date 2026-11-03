#!/usr/bin/env python3
from pathlib import Path
import re,sys
root=Path(__file__).resolve().parents[1]
errors=[]
for p in root.rglob('*.md'):
    txt=p.read_text(encoding='utf-8')
    for dest in re.findall(r'(?<!!)\[[^]]+\]\(([^)]+)\)',txt):
        if dest.startswith(('http://','https://','#','mailto:')):continue
        target=(p.parent/dest.split('#')[0]).resolve()
        if not target.exists():errors.append(f'{p.relative_to(root)}: missing {dest}')
for p in (root/'tools').rglob('*.md'):
    content=p.read_text(encoding='utf-8')
    for section in ('## Why use it?', '## Requirements','## Install','## Update','## Uninstall','## Verify','## Caveats','## References'):
        if section not in content:errors.append(f'{p.relative_to(root)}: missing {section}')
# Catalog index invariants: every active guide linked exactly once; no active/archive overlap.
readme=(root/'README.md').read_text(encoding='utf-8')
for p in (root/'tools').rglob('*.md'):
    rel=p.relative_to(root).as_posix()
    count=readme.count(f'({rel})')
    if count!=1:errors.append(f'{rel}: expected one README reference, got {count}')
    if p.name=='tigerkit.md' and '## My Works' in readme:
        my=readme.split('## My Works',1)[1].split('## Workflow & Agents',1)[0]
        if f'({rel})' not in my: errors.append('TigerKit must be under My Works')
archive_index=(root/'archive/README.md').read_text(encoding='utf-8')
for p in (root/'archive').glob('*.md'):
    if p.name=='README.md':continue
    if f'({p.name})' not in archive_index and f'(./{p.name})' not in archive_index:
        errors.append(f'archive/{p.name}: missing archive index reference')
print('\n'.join(errors) if errors else f'OK: {len(list(root.rglob("*.md")))} Markdown files validated')
sys.exit(bool(errors))
