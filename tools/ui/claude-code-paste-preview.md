# Claude Code Paste Preview

<!-- catalog: {"name": "Claude Code Paste Preview", "upstream": "https://github.com/alan890104/claude-code-paste-preview", "types": ["plugin", "mod"], "agents": ["Claude Code"], "category": "ui", "verification": "metadata", "install_mode": "agent-guide", "last_reviewed": "2026-11-03"} -->

> 이미지 붙여넣기 미리보기 및 마크업

- **Upstream:** https://github.com/alan890104/claude-code-paste-preview
- **Types:** plugin/mod
- **Agents:** Claude Code
- **Verification:** metadata
- **Install mode:** agent-guide
- **Last reviewed:** 2026-11-03

## Why use it?

Claude Code의 이미지 붙여넣기를 썸네일로 확인하고 전송 전에 펜·도형·텍스트·자르기 등의 편집을 제공합니다.

## Requirements

Claude Code 2.1.291+가 필요합니다. 썸네일은 kitty 그래픽 프로토콜 터미널을 권장하며, 운영체제별 편집기 런타임 조건이 다릅니다.

## Install

```text
/plugin install paste-preview --marketplace alan890104/claude-code-paste-preview
```

기존 입력 중인 이미지에 실시간으로 편집기를 표시합니다.

## Update

마켓플레이스 업데이트 후 변경된 편집기 의존성과 훅 동작을 확인해 갱신합니다.

## Uninstall

Claude Code에서 플러그인 등록을 제거하고 도구의 임시 편집 이미지가 남아 있는지 확인합니다.

## Verify

이미지를 붙여넣고 썸네일과 편집기에서 주석을 추가한 뒤 전송 이미지가 기대한 결과인지 확인합니다.

## Caveats

macOS에서는 네이티브 편집기를 빌드할 수 있으며, Linux·Windows에서는 브라우저 앱 창을 사용할 수 있습니다. 그래픽 미지원 터미널은 대체 텍스트를 표시할 수 있습니다.

## References

- [Upstream](https://github.com/alan890104/claude-code-paste-preview)
