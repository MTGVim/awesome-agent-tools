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
readme_ko=(root/'README.md').read_text(encoding='utf-8')
readme=(root/'README.en.md').read_text(encoding='utf-8')
def catalog_rows(content):
    rows={}
    for line in content.splitlines():
        if not line.startswith('| ['): continue
        cells=[x.strip() for x in line.strip('|').split('|')]
        if len(cells)!=4:
            errors.append('catalog row must have 4 cells: '+line[:80])
            continue
        m=re.match(r'\[([^]]+)\]\(([^)]+)\)',cells[0])
        if not m: errors.append('bad catalog tool link');continue
        name,url=m.groups()
        if name in rows: errors.append('duplicate tool: '+name)
        if len(cells[1])<12: errors.append('description too short: '+name)
        if '<br>' not in cells[1]: errors.append('missing description/links line break: '+name)
        if cells[3]!='—' and '<br>' not in cells[3]: errors.append('missing activity badge line break: '+name)
        guide=re.search(r'\[(?:Guide|가이드)\]\(([^)]+)\)',cells[1])
        if not guide: errors.append('missing guide: '+name)
        demo=re.search(r'\[(?:Demo|시연)\]\(([^)]+)\)',cells[1])
        badge_agents=tuple(re.findall(r'img.shields.io/badge/(Claude_Code|Codex|Hermes)',cells[2]))
        rows[name]=(url,badge_agents,cells[3],guide.group(1) if guide else None,demo.group(1) if demo else None)
    return rows
# Markdown tables must be contiguous: a blank line after the separator ends the table.
for label,content in [('README.md',readme_ko),('README.en.md',readme)]:
    lines=content.splitlines()
    for index,line in enumerate(lines[:-2]):
        if re.fullmatch(r'\|(?:\s*:?-{3,}:?\s*\|){4}',line) and not lines[index+1].startswith('| ['):
            errors.append(f'{label}:{index+2}: catalog table row must immediately follow separator')
        if line.startswith('| [') and index>0 and lines[index-1].strip()=='' and index>1 and lines[index-2].startswith('|---|'):
            errors.append(f'{label}:{index+1}: blank line splits Markdown table')
english_catalog=catalog_rows(readme)
korean_catalog=catalog_rows(readme_ko)
if english_catalog!=korean_catalog:
    errors.append('English and Korean catalog entries or metadata diverge')
for name,content in [('README.en.md',readme),('README.md',readme_ko)]:
    if '| Tier |' in content or '| 티어 |' in content or '| Verified |' in content or '| 검증 |' in content: errors.append(name+': remove ranking and verification columns')
    if '`범용`' in content: errors.append(name+': generic agent label is forbidden')
    if '[English](README.en.md)' not in content or '[한국어](README.md)' not in content:errors.append(name+': missing language link')
for p in (root/'tools').rglob('*.md'):
    rel=p.relative_to(root).as_posix()
    for label,content in [('README.en.md',readme),('README.md',readme_ko)]:
        count=content.count(f'({rel})')
        if count!=1:errors.append(f'{rel}: expected one {label} reference, got {count}')
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
