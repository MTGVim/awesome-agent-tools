#!/usr/bin/env python3
from pathlib import Path
import re,sys,json,json
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
        skills_cli='img.shields.io/badge/Skills_CLI-' in cells[2]
        if skills_cli and not re.search(r'\]\(https://github.com/vercel-labs/skills\)', cells[2]): errors.append('Skills CLI badge must link to installer docs: '+name)
        rows[name]=(url,badge_agents,skills_cli,cells[3],guide.group(1) if guide else None,demo.group(1) if demo else None)
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

# Guide metadata is the source of truth for supported agents and verification.
allowed_agents={'Claude Code','Codex','Hermes'}
allowed_types={'skill','plugin','mod','mcp','tool'}
allowed_verification={'personal','metadata','trial','unverified'}
allowed_install={'cli','agent-guide','manual-review'}
expected_badges={'Claude Code':'Claude_Code','Codex':'Codex','Hermes':'Hermes'}
for p in (root/'tools').rglob('*.md'):
    content=p.read_text(encoding='utf-8')
    metadata=re.search(r'<!--\s*catalog:\s*(\{[^\n]+\})\s*-->',content)
    if not metadata:
        errors.append(f'{p.relative_to(root)}: missing catalog JSON')
        continue
    try: meta=json.loads(metadata.group(1))
    except json.JSONDecodeError:
        errors.append(f'{p.relative_to(root)}: invalid catalog JSON')
        continue
    required=('name','upstream','types','agents','category','verification','install_mode','last_reviewed')
    for key in required:
        if key not in meta:errors.append(f'{p.relative_to(root)}: missing {key}')
    if 'tier' in meta:errors.append(f'{p.relative_to(root)}: retired tier metadata')
    if not set(meta.get('agents',[]))<=allowed_agents:
        errors.append(f'{p.relative_to(root)}: unsupported agent labels')
    if not set(meta.get('types',[]))<=allowed_types:
        errors.append(f'{p.relative_to(root)}: unsupported type')
    if meta.get('verification') not in allowed_verification:
        errors.append(f'{p.relative_to(root)}: invalid verification')
    if meta.get('install_mode') not in allowed_install:
        errors.append(f'{p.relative_to(root)}: invalid install_mode')
    name=meta.get('name')
    if name not in korean_catalog:
        errors.append(f'{p.relative_to(root)}: catalog name not indexed: {name}')
        continue
    row=korean_catalog[name]
    actual=set(row[1])
    expected={expected_badges[a] for a in meta.get('agents',[]) if a in expected_badges}
    if actual!=expected:
        errors.append(f'{p.relative_to(root)}: agent badges differ from guide: {actual} vs {expected}')
    installers=meta.get('installers',[])
    if not isinstance(installers,list) or any(i not in {'skills-cli'} for i in installers):
        errors.append(f'{p.relative_to(root)}: unsupported installer metadata')
    if bool(row[2]) != ('skills-cli' in installers):
        errors.append(f'{p.relative_to(root)}: Skills CLI badge differs from guide installers metadata')
    if 'skills-cli' in installers and 'skill' not in meta.get('types',[]):
        errors.append(f'{p.relative_to(root)}: Skills CLI installer requires a skill type')
    if row[0]!=meta.get('upstream'):
        errors.append(f'{p.relative_to(root)}: upstream URL disagrees with README')
    if p.name!='tigerkit.md' and ('큐레이터가 직접 관리하는 프로젝트' in content or 'maintained by the curator' in content.lower()):
        errors.append(f'{p.relative_to(root)}: incorrectly claims curator ownership')

archive_index=(root/'archive/README.md').read_text(encoding='utf-8')
for p in (root/'archive').glob('*.md'):
    if p.name=='README.md':continue
    if f'({p.name})' not in archive_index and f'(./{p.name})' not in archive_index:
        errors.append(f'archive/{p.name}: missing archive index reference')
print('\n'.join(errors) if errors else f'OK: {len(list(root.rglob("*.md")))} Markdown files validated')
sys.exit(bool(errors))
