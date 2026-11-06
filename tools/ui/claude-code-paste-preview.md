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

### 개인 셋업 메모 (2026-11-03)

Image View와 동일한 이미지 미리보기 영역을 사용하므로 하나만 켭니다. macOS에서는 Xcode `swiftc`가 필요하고 첫 세션에 편집기를 컴파일했습니다. 사용자 측정에서는 상주 편집기 프로세스가 세션마다 약 85MB를 사용했습니다.

macOS에서는 네이티브 편집기를 빌드할 수 있으며, Linux·Windows에서는 브라우저 앱 창을 사용할 수 있습니다. 그래픽 미지원 터미널은 대체 텍스트를 표시할 수 있습니다.

### Orca 터미널에서 이미지 표시 문제 (2026-11-06)

개인 Orca 환경에서 편집 이미지 전송 직후 inline image의 base64 문자열이 그대로 표시됐습니다. Ctrl+L로 화면을 다시 그리면 정상화됩니다. 반복된다면 이미지 전송 이벤트 뒤 약 1초 후 조건부 화면 재그리기를 수행하는 임시 shim을 고려할 수 있습니다. 터미널 핸들 확인, 다른 mod의 훅 실행 보장, 우회책 제거 기준은 [Orca 가이드](../workflows/orca.md)를 참고합니다.

## References

- [Upstream](https://github.com/alan890104/claude-code-paste-preview)
