# Prompt Rail

<!-- catalog: {"name": "Prompt Rail", "upstream": "https://github.com/oikon48/prompt-rail", "types": ["plugin", "mod"], "agents": ["Claude Code"], "category": "ui", "verification": "metadata", "install_mode": "agent-guide", "last_reviewed": "2026-11-03"} -->

> 이전 프롬프트 탐색 및 미리보기

- **Upstream:** https://github.com/oikon48/prompt-rail
- **Types:** plugin/mod
- **Agents:** Claude Code
- **Verification:** metadata
- **Install mode:** agent-guide
- **Last reviewed:** 2026-11-03

## Why use it?

Claude Code의 이전 사용자 프롬프트를 레일에 표시하고, 마우스로 내용을 미리 보거나 클릭해 과거 턴으로 이동합니다.

## Requirements

Claude Code 2.1.287+가 필요합니다. 마우스 인터랙션에는 `tui: fullscreen` 설정이 유리합니다.

## Install

```bash
claude plugin marketplace add oikon48/prompt-rail
claude plugin install prompt-rail@oikon48
```

새 Claude Code 세션을 시작하면 레일이 표시됩니다.

## Update

마켓플레이스를 갱신한 후 `prompt-rail@oikon48`를 업데이트합니다.

## Uninstall

`claude plugin uninstall prompt-rail@oikon48` 후 레일 레이아웃 사용자 설정을 검토합니다.

## Verify

프롬프트를 여러 번 작성한 세션에서 레일의 hover/클릭·키보드 이동·레이아웃 전환을 확인합니다.

## Caveats

좁은 터미널과 마우스 입력이 없는 환경에서는 기능이 제한될 수 있습니다.

## References

- [Upstream](https://github.com/oikon48/prompt-rail)
