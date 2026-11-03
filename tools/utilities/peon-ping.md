# Peon Ping

<!-- catalog: {"name": "Peon Ping", "upstream": "https://github.com/PeonPing/peon-ping", "types": ["tool"],  "agents": ["Claude Code", "Codex"], "category": "utilities", "verification": "personal", "install_mode": "agent-guide", "last_reviewed": "2026-11-03"} -->

> 작업 알림 사운드

- **Upstream:** https://github.com/PeonPing/peon-ping
- **Types:** tool
- **Agents:** Claude Code, Codex
- **Verification:** personal
- **Install mode:** agent-guide
- **Last reviewed:** 2026-11-03

## Why use it?

코딩 에이전트의 작업 완료·승인 대기 등을 게임 캐릭터 음성, 오버레이, 시스템 알림으로 알려줍니다.

## Requirements

macOS·Linux·Windows 및 SSH 환경을 대상으로 하며, 에이전트별 훅 또는 MCP 연동을 설정합니다. 사운드 출력과 화면 알림 권한이 필요할 수 있습니다.

## Install

원본 README는 Homebrew와 플랫폼별 설치 스크립트를 제공합니다. macOS Homebrew 예시는 다음과 같습니다.

```bash
brew install PeonPing/tap/peon-ping
```

설치 후 `peon setup`을 통해 에이전트별 연동을 확인합니다.

## Update

원본 릴리스에 따라 갱신하고 기존 팩·사운드·훅 구성을 보존합니다.

## Uninstall

원본 제거 절차로 도구가 추가한 훅만 해제합니다. 다른 에이전트의 기존 훅을 삭제하지 않습니다.

## Verify

Claude Code와 Codex에서 완료·승인 이벤트가 발생할 때 소리와 알림이 원하는 방식으로 출력되는지 확인합니다.

## Caveats

Hook 등록이 자동으로 수행되는 경우가 있으므로 기존 에이전트 설정의 병합 방식과 알림 관련 권한을 확인합니다.

## References

- [Upstream](https://github.com/PeonPing/peon-ping)
