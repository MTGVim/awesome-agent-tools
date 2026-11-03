# Claude HUD

<!-- catalog: {"name": "Claude HUD", "upstream": "https://github.com/jarrodwatts/claude-hud", "types": ["plugin"], "agents": ["Claude Code"], "category": "ui", "verification": "personal", "install_mode": "agent-guide", "last_reviewed": "2026-11-03"} -->

> Claude Code 상태 표시 도구

- **Upstream:** https://github.com/jarrodwatts/claude-hud
- **Types:** plugin
- **Agents:** Claude Code
- **Verification:** personal
- **Install mode:** agent-guide
- **Last reviewed:** 2026-11-03

## Why use it?

Claude Code 프롬프트 아래 컨텍스트 사용량, 속도 제한, 도구·서브에이전트 상태 및 할 일 진행 상황을 표시합니다.

## Requirements

Claude Code와 Node.js 22.18+가 필요합니다. HUD는 Claude Code status line 설정에 연결됩니다.

## Install

```text
/plugin marketplace add jarrodwatts/claude-hud
/plugin install claude-hud
/reload-plugins
/hud
```

`/hud`가 상태 표시줄 연결을 확인하고 사용자 동의를 받습니다.

## Update

`claude plugin marketplace update claude-hud` 및 `claude plugin update claude-hud@claude-hud`로 갱신하고 `/reload-plugins`를 호출합니다.

## Uninstall

`claude plugin uninstall claude-hud@claude-hud` 후 HUD가 변경한 status line 설정만 기존 값으로 복구합니다.

## Verify

`/hud`를 실행하고 사용량·도구 사용·에이전트 실행에 따라 상태 줄이 갱신되는지 확인합니다.

## Caveats

status line을 사용하는 다른 확장과 설정 충돌이 있을 수 있습니다. 기존 사용자 설정을 백업해야 합니다.

## References

- [Upstream](https://github.com/jarrodwatts/claude-hud)
