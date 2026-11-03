# Claude Image View

<!-- catalog: {"name": "Claude Image View", "upstream": "https://github.com/jarrodwatts/claude-image-view", "types": ["plugin", "mod"], "agents": ["Claude Code"], "category": "ui", "verification": "metadata", "install_mode": "cli", "last_reviewed": "2026-11-03"} -->

> 붙여넣은 이미지 썸네일 미리보기

- **Upstream:** https://github.com/jarrodwatts/claude-image-view
- **Types:** plugin/mod
- **Agents:** Claude Code
- **Verification:** metadata
- **Install mode:** cli
- **Last reviewed:** 2026-11-03

## Why use it?

Claude Code에 붙여넣은 이미지의 원본 비율 썸네일을 프롬프트 위에 표시합니다. 원본 이미지의 내용을 수정하지는 않습니다.

## Requirements

Claude Code의 모드 지원 빌드와 kitty 그래픽 프로토콜을 지원하는 터미널이 필요합니다. macOS/Linux가 주 지원 환경이며 Windows는 일부 제한이 있습니다.

## Install

```text
/plugin marketplace add jarrodwatts/claude-image-view
/plugin install image-view
/reload-plugins
```

## Update

`claude plugin marketplace update claude-image-view`, `claude plugin update image-view@claude-image-view`를 확인합니다.

## Uninstall

`claude plugin uninstall image-view@claude-image-view` 후 재시작하거나 플러그인을 다시 로드합니다.

## Verify

이미지 여러 개를 붙여넣어 프롬프트 위에 원본 비율 썸네일이 표시되는지 확인합니다.

## Caveats

터미널 그래픽 지원이 없으면 썸네일이 표시되지 않을 수 있습니다. 이미지 내용을 수정하는 Paste Preview와는 기능이 다릅니다.

## References

- [Upstream](https://github.com/jarrodwatts/claude-image-view)
