# Claude Skins

<!-- catalog: {"name": "Claude Skins", "upstream": "https://github.com/hellosverre/claude-skins", "types": ["plugin", "mod"], "agents": ["Claude Code"], "category": "ui", "verification": "metadata", "install_mode": "agent-guide", "last_reviewed": "2026-11-03"} -->

> Claude Code 테마·렌더링

- **Upstream:** https://github.com/hellosverre/claude-skins
- **Types:** plugin/mod
- **Agents:** Claude Code
- **Verification:** metadata
- **Install mode:** agent-guide
- **Last reviewed:** 2026-11-03

## Why use it?

Claude Code에 16종 테마, 도구 호출 카드, 편집 diff, 표·코드·Mermaid 차트 및 사용량 표시를 적용합니다.

## Requirements

Claude Code 2.1.287+가 필요합니다. 일부 모드나 테마와 렌더러 훅 충돌이 발생할 수 있습니다.

## Install

```text
/plugin marketplace add hellosverre/claude-skins
/plugin install skins@hellosverre-mods
```

설치 후 Claude Code를 다시 실행하고 `/skin`으로 테마를 선택합니다.

## Update

`claude plugin marketplace update hellosverre-mods` 및 `claude plugin update skins@hellosverre-mods`를 실행합니다.

## Uninstall

`claude plugin uninstall skins@hellosverre-mods` 후 테마 설정 보존 여부를 확인합니다.

## Verify

`/skin`에서 테마를 바꾸고, 표·코드·Mermaid·도구 실행 결과가 의도한 스타일로 나타나는지 확인합니다.

## Caveats

시각화 렌더러를 교체하는 도구이므로 다른 터미널 꾸미기 모드와 충돌할 수 있습니다.

## References

- [Upstream](https://github.com/hellosverre/claude-skins)
