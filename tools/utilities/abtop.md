# abtop

<!-- catalog: {"name": "abtop", "upstream": "https://github.com/graykode/abtop", "types": ["tool"],  "agents": ["Claude Code", "Codex"], "category": "utilities", "verification": "trial", "install_mode": "agent-guide", "last_reviewed": "2026-11-03"} -->

> 터미널 모니터링 도구

- **Upstream:** https://github.com/graykode/abtop
- **Types:** tool
- **Agents:** Claude Code, Codex
- **Verification:** trial
- **Install mode:** agent-guide
- **Last reviewed:** 2026-11-03

## Why use it?

여러 Claude Code·Codex CLI·OpenCode 세션을 TUI에서 보여주며 토큰, 컨텍스트, 사용 한도, 하위 프로세스와 열린 포트를 모니터링합니다.

## Requirements

macOS·Linux·Windows에서 사용하며, 프로세스·로컬 파일 상태를 조회할 권한이 필요합니다. Linux에서 OpenCode 모니터링에는 sqlite3가 필요합니다.

## Install

Rust Cargo 방식이 공식 안내에 포함되어 있습니다.

```bash
cargo install abtop
```

운영체제별 사전 빌드 릴리스 설치기도 원본 README에서 확인할 수 있습니다.

## Update

설치한 채널의 최신 안정 릴리스로 갱신하고 기존 사용자 설정을 보존합니다.

## Uninstall

Cargo로 설치했다면 해당 Cargo 패키지를 제거하며, 릴리스 설치기를 사용했다면 그 설치 경로를 확인합니다.

## Verify

실행 중인 Claude Code 또는 Codex 세션을 시작하고 abtop에 세션과 자원 상태가 표시되는지 확인합니다.

## Caveats

모니터링 대상은 원본에서 명시한 세션들입니다. Hermes의 세션을 감지한다고 가정해서는 안 됩니다.

## References

- [Upstream](https://github.com/graykode/abtop)
