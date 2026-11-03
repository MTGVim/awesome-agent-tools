# Darwin Skill

<!-- catalog: {"name": "Darwin Skill", "upstream": "https://github.com/alchaincyf/darwin-skill", "types": ["skill"], "agents": [], "category": "workflows", "verification": "unverified", "install_mode": "cli", "installers": ["skills-cli"], "last_reviewed": "2026-11-03"} -->

> 스킬 개선을 위한 실험 후보

- **Upstream:** https://github.com/alchaincyf/darwin-skill
- **Types:** skill
- **Agents:** Agent-specific compatibility not verified
- **Verification:** unverified
- **Install mode:** cli
- **Distribution:** Skills CLI (`npx skills`), as documented upstream
- **Last reviewed:** 2026-11-03

## Why use it?

스킬 개선을 위한 실험 후보 소개된 기능과 실제 호환성은 원본 문서 및 설치 환경에서 별도로 확인해야 합니다.

## Requirements

원본 README의 OS·에이전트 버전·권한·터미널 호환성 조건을 확인해야 합니다.

## Install

원본 README에 다음 설치 방법이 명시되어 있습니다. 실제 설치 전에 대상 환경과 CLI 옵션을 확인합니다.

```bash
npx skills add alchaincyf/darwin-skill --list
npx skills add alchaincyf/darwin-skill
```

첫 번째 명령은 설치 가능한 스킬을 조회합니다. 두 번째 명령은 대화형으로 설치 위치와 에이전트를 선택할 수 있습니다. Claude Code·Codex·Hermes에 설치할 수 있는 CLI 경로가 제공되지만, 세 에이전트에서 스킬의 기능을 실제로 검증한 것은 아닙니다.

## Update

기존 설치 방식과 변경 이력을 확인한 다음 원본 저장소에서 권장하는 업데이트 절차를 적용합니다.

## Uninstall

설치 이력을 확인해 해당 도구가 추가한 파일·등록만 제거합니다. 공유 설정과 다른 도구는 보존합니다.

## Verify

설치 목록 또는 명령 도움말을 확인하고, 핵심 기능을 최소 한 번 실행해 봅니다.

## Caveats

검증 상태가 `personal`이 아닌 경우, 메타데이터 확인과 실제 설치·기능 테스트를 구분해야 합니다. 사전 승인 없이 원격 스크립트를 실행하거나 전역 설정을 수정하지 않습니다.

## References

- [Upstream](https://github.com/alchaincyf/darwin-skill)
- [Skills CLI supported agents](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)
- [Skills CLI commands](https://github.com/vercel-labs/skills/blob/main/docs/commands.md)
