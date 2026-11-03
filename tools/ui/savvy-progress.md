# Savvy Progress

<!-- catalog: {"name": "Savvy Progress", "upstream": "https://github.com/JohnnyVizz/claude-kit/tree/main/plugins/savvy-progress", "types": ["plugin"], "agents": ["Claude Code"], "category": "ui", "verification": "metadata", "install_mode": "agent-guide", "last_reviewed": "2026-11-03"} -->

> 작업 진행률 및 서브에이전트 상태 시각화

- **Upstream:** https://github.com/JohnnyVizz/claude-kit/tree/main/plugins/savvy-progress
- **Types:** plugin
- **Agents:** Claude Code
- **Verification:** metadata
- **Install mode:** agent-guide
- **Last reviewed:** 2026-11-03

## Why use it?

Claude Code 프롬프트 위에 작업 진행 바와 서브에이전트 진행 상태 패널을 표시합니다. `savvy-flow`와 결합하면 작업 흐름도 연동됩니다.

## Requirements

Claude Code Function Hooks를 지원하는 모드 환경이 필요합니다. 저장소의 여러 플러그인은 별개로 설치합니다.

## Install

원본 `JohnnyVizz/claude-kit` 마켓플레이스에서 `savvy-progress@claude-kit`만 선택해 설치합니다.

```text
/plugin marketplace add johnnyvizz/claude-kit
/plugin install savvy-progress@claude-kit
```

## Update

`claude-kit` 마켓플레이스와 `savvy-progress@claude-kit` 플러그인을 갱신합니다.

## Uninstall

`claude plugin uninstall savvy-progress@claude-kit`로 진행 상태 모드만 제거합니다.

## Verify

서브에이전트를 시작해 진행 바와 실행 상태가 변경되는지 확인합니다.

## Caveats

`savvy-flow`는 별도의 워크플로 스킬입니다. 두 도구는 서로 연동할 수 있지만 각각 독립적으로 설치 가능합니다.

## References

- [Upstream](https://github.com/JohnnyVizz/claude-kit/tree/main/plugins/savvy-progress)
