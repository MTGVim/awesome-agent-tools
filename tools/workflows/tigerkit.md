# TigerKit

<!-- catalog: {"name": "TigerKit", "upstream": "https://github.com/MTGVim/tiger-kit", "types": ["skill"], "agents": ["Claude Code","Codex","Hermes"], "category": "my-works", "verification": "personal", "install_mode": "agent-guide", "installers": ["skills-cli"], "last_reviewed": "2026-11-03"} -->

> 사용자가 개발·유지보수하는 에이전트 워크플로우 스킬 컬렉션

- **Upstream:** https://github.com/MTGVim/tiger-kit
- **Types:** skill
- **Agents:** Claude Code, Codex, Hermes
- **Verification:** personal
- **Install mode:** agent-guide
- **Last reviewed:** 2026-11-03

## Why use it?

Claude Code·Codex·Hermes Agent에서 필요한 개발, 리뷰, 브라우저 검증, 설명 제작 스킬을 선택적으로 설치하는 모음입니다. 각 스킬의 의존성까지 함께 설치해야 하므로 단일 SKILL.md를 복사하는 것만으로 충분하지 않을 수 있습니다.

## Requirements

Node.js 기반 Skills CLI와 대상 에이전트가 필요합니다. 소스 및 설치본 검사와 일부 도우미에는 Python 3.9+와 PyYAML이 필요합니다.

## Install

원본 README에 공개된 전체 설치 명령입니다. 설치 대상·전역 범위·덮어쓰기 여부를 확인한 후 실행합니다.

```bash
npx --yes skills@1.7.4 add MTGVim/tiger-kit --global --agent claude-code codex hermes-agent --skill '*' --copy
```

선택 설치 및 종속 스킬 구성은 `tk-setup-skills`를 사용합니다.

## Update

전체 설치를 갱신할 때는 기존 선택·설치 범위를 확인한 뒤 위 고정 버전 설치 절차를 다시 적용합니다. 선택 설치는 `tk-setup-skills`가 의존성을 포함하도록 안내합니다.

## Uninstall

Skills CLI 또는 대상 에이전트의 스킬 설치 위치에서 TigerKit에 속한 스킬만 확인해 제거합니다. 다른 스킬이 공유하는 파일이나 설정은 삭제하지 않습니다.

## Verify

`tk-setup-skills`가 참조하는 의존성 스킬을 확인하고, 설치한 에이전트에서 대표 스킬을 호출해 정상 로드되는지 점검합니다.

## Caveats

Skills CLI가 스킬 간 의존성을 자동 해결하지 않습니다. 사용자 스킬과 참조 스킬의 종속 관계를 먼저 확인해야 합니다.

## References

- [Upstream](https://github.com/MTGVim/tiger-kit)
