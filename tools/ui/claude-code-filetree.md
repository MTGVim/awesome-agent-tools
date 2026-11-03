# Claude Code Filetree

<!-- catalog: {"name": "Claude Code Filetree", "upstream": "https://github.com/data-goblin/claude-code-filetree", "types": ["mod"], "agents": ["Claude Code"], "category": "ui", "verification": "metadata", "install_mode": "agent-guide", "last_reviewed": "2026-11-03"} -->

> Git 상태와 변경 파일의 트리 표현

- **Upstream:** https://github.com/data-goblin/claude-code-filetree
- **Types:** mod
- **Agents:** Claude Code
- **Verification:** metadata
- **Install mode:** agent-guide
- **Last reviewed:** 2026-11-03

## Why use it?

Claude Code가 읽거나 수정하는 파일을 IDE형 파일 트리로 표시하고 Git 상태, 미리보기, diff 및 treemap 기능을 제공합니다.

## Requirements

Claude Code 2.1.306+가 필요합니다. 터미널 사이드바에는 fullscreen 모드와 110열 이상의 너비가 필요하며 데스크톱 앱은 별도 도킹 방식입니다.

## Install

```bash
claude plugin marketplace add data-goblin/claude-code-filetree
claude plugin install filetree@claude-code-filetree
```

Claude Code에서 `/filetree`를 사용해 표시 여부를 전환합니다.

## Update

원본 릴리스와 플러그인 마켓플레이스를 갱신하고 관련 UI 옵션을 보존합니다.

## Uninstall

`claude plugin uninstall filetree@claude-code-filetree`로 등록을 제거합니다.

## Verify

Claude Code에서 파일 읽기·편집 중 사이드 트리 표시, Git 상태와 diff를 확인합니다.

## Caveats

좁은 터미널에서는 패널이 표시되지 않을 수 있습니다. 데스크톱 WSL 세션 등 일부 환경에서 Mods가 로드되지 않는다는 원본 제약을 확인합니다.

## References

- [Upstream](https://github.com/data-goblin/claude-code-filetree)
