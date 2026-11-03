# Prismantis

<!-- catalog: {"name": "Prismantis", "upstream": "https://github.com/NahumLitvin/prismantis", "types": ["plugin", "mod"], "agents": ["Claude Code", "Codex"], "category": "visual", "verification": "metadata", "install_mode": "agent-guide", "last_reviewed": "2026-11-03"} -->

> 표·코드·Mermaid·차트 렌더링

- **Upstream:** https://github.com/NahumLitvin/prismantis
- **Types:** plugin/mod
- **Agents:** Claude Code, Codex
- **Verification:** metadata
- **Install mode:** agent-guide
- **Last reviewed:** 2026-11-03

## Why use it?

Claude Code의 표·코드·Mermaid·차트·LaTeX 등을 터미널에서 읽기 쉬운 테마 기반 출력으로 렌더링합니다. Codex용 버전도 제공됩니다.

## Requirements

Claude Code 2.1.287+가 필요합니다. Codex는 원본 `codex/README.md`의 별도 설치와 기능 제한을 따릅니다. 수식 그래픽 렌더링은 kitty/Ghostty 등에서 최적화됩니다.

## Install

Claude Code에서는 다음 명령을 사용합니다.

```text
/plugin marketplace add NahumLitvin/prismantis
/plugin install prismantis@prismantis
```

설치 후 `/prismantis setup`을 실행합니다. Codex는 원본 `codex/README.md`의 별도 절차를 확인합니다.

## Update

Claude Code에서는 마켓플레이스와 `prismantis@prismantis`를 갱신합니다. Codex 구현은 별도 설치 절차를 따라야 합니다.

## Uninstall

`claude plugin uninstall prismantis@prismantis`를 사용합니다. Codex에서는 해당 환경에 설치한 파일만 제거합니다.

## Verify

표·코드·다이어그램·수식 출력과 테마 설정이 표시되는지 확인합니다.

## Caveats

### 개인 셋업 메모 (2026-11-03)

현재 개인 Daily Setup에서는 꺼두었습니다. 사용자 환경에서 Show Your Work와 전역 출력 렌더러가 충돌했고, `next()` 없이 명령 출력 줄을 처리해 후속 렌더러를 막는 현상이 관찰되었습니다. 모든 버전에서 동일하다는 뜻은 아닙니다.

Codex와 Claude Code의 기능은 완전히 동일하지 않습니다. 다른 터미널 렌더러 모드와 동시 사용 시 충돌할 수 있습니다.

## References

- [Upstream](https://github.com/NahumLitvin/prismantis)
