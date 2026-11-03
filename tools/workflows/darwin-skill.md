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

Agent Skills의 지침을 실험과 평가 결과에 따라 반복 수정하는 최적화 워크플로입니다. 실험 과제에 대한 평가 기준을 먼저 정해야 의미 있는 개선을 판단할 수 있습니다.

## Requirements

원본은 `npx skills add alchaincyf/darwin-skill` 설치 경로를 제공합니다. 에이전트별 실행 환경에서 스크립트와 평가 도구의 사용 가능 여부는 별도로 확인합니다.

## Install

```bash
npx skills add alchaincyf/darwin-skill --list
npx skills add alchaincyf/darwin-skill
```

첫 명령으로 설치 가능한 스킬을 조회하고 대상 에이전트와 위치를 결정한 뒤 설치합니다.

## Update

Skills CLI와 원본 저장소의 최신 설치 문서를 확인해 기존 선택한 에이전트와 범위를 유지하며 갱신합니다.

## Uninstall

Skills CLI가 관리한 스킬 등록만 제거하고, 사용자 평가 결과나 별도로 작성한 실험 로그는 유지합니다.

## Verify

설치한 스킬의 지침을 읽고 실제 평가를 시작하기 전 변경 대상·측정 지표·복원 방법을 확인합니다.

## Caveats

Skills CLI 배지는 설치 도구가 여러 에이전트를 지원한다는 뜻이며, 이 최적화 스킬을 모든 에이전트에서 실측 검증했다는 의미는 아닙니다.

## References

- [Upstream](https://github.com/alchaincyf/darwin-skill)
- [Skills CLI supported agents](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)
- [Skills CLI commands](https://github.com/vercel-labs/skills/blob/main/docs/commands.md)
