# Ponytail

<!-- catalog: {"name": "Ponytail", "upstream": "https://github.com/dietrichgebert/ponytail", "types": ["plugin", "mod"], "agents": ["Claude Code", "Codex"], "category": "coding", "verification": "metadata", "install_mode": "agent-guide", "last_reviewed": "2026-11-03"} -->

> 과도한 구현을 억제하는 코딩 스타일 보조

- **Upstream:** https://github.com/dietrichgebert/ponytail
- **Types:** plugin/mod
- **Agents:** Claude Code, Codex
- **Verification:** metadata
- **Install mode:** agent-guide
- **Last reviewed:** 2026-11-03

## Why use it?

실제 변경 코드에 대해 과도한 추상화, 불필요한 구현 및 위험한 로직을 줄이도록 구현·리뷰·감사를 돕는 코딩 보조 도구입니다.

## Requirements

Claude Code와 Codex에는 전용 플러그인 설치 절차가 있고, 다른 에이전트는 AGENTS.md 또는 SKILL.md 기반의 수동 통합을 제공합니다.

## Install

Claude Code:

```text
/plugin marketplace add DietrichGebert/ponytail
/plugin install ponytail@ponytail
```

Codex:

```bash
codex plugin marketplace add DietrichGebert/ponytail
codex plugin add ponytail@ponytail
```

Codex는 `/hooks`에서 해당 라이프사이클 훅을 확인·신뢰해야 합니다.

## Update

해당 에이전트의 플러그인 관리 기능으로 갱신하며, 수동 복사한 스킬은 원본과 비교하여 필요한 파일만 갱신합니다.

## Uninstall

Claude Code 또는 Codex에서 플러그인 등록을 제거합니다. 수동 AGENTS.md 병합본은 사용자 지침을 보존한 채 Ponytail 부분만 되돌립니다.

## Verify

코딩 지시나 리뷰 호출로 실제 출력이 간결해지고 위험한 변경에 경고가 나타나는지 확인합니다.

## Caveats

원본의 성능 수치는 제작자 발표 값입니다. 다른 에이전트에서 AGENTS.md를 읽을 수 있다는 사실과 플러그인 훅 기능이 동일하다는 주장은 구분해야 합니다.

## References

- [Upstream](https://github.com/dietrichgebert/ponytail)
