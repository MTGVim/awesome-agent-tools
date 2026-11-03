# Vorssaint Utils

<!-- catalog: {"name": "Vorssaint Utils", "upstream": "https://github.com/vorssaint/vorssaint-utils", "types": ["tool"], "agents": [], "category": "utilities", "verification": "personal", "install_mode": "agent-guide", "last_reviewed": "2026-11-03"} -->

> 단축키·창 관리 등 유틸리티 묶음

- **Upstream:** https://github.com/vorssaint/vorssaint-utils
- **Types:** tool
- **Agents:** No agent-specific integration documented
- **Verification:** personal
- **Install mode:** agent-guide
- **Last reviewed:** 2026-11-03

## Why use it?

macOS 메뉴 막대에서 창 전환·스냅, 음량 믹서, 클립보드, 파일 관리, 캡처, 시스템 상태 등 선택적 유틸리티를 묶어 제공합니다.

## Requirements

macOS Apple Silicon 등 현재 릴리스의 시스템 요건을 확인합니다. 접근성·화면 녹화·입력 모니터링 같은 권한은 사용 기능에 따라 다릅니다.

## Install

현재 공식 저장소는 `vorssaint/vorssaint-utils`이며, macOS Homebrew cask로 설치할 수 있습니다.

```bash
brew install --cask vorssaint
```

원본 GitHub Releases의 DMG도 제공합니다.

## Update

Homebrew cask나 앱 내 공식 업데이트 기능을 통해 갱신합니다. 기능별 권한과 내보낸 설정을 보존합니다.

## Uninstall

`brew uninstall --cask vorssaint`로 앱을 제거할 수 있습니다. 설정·권한까지 완전히 지우는 원본 스크립트는 내용을 확인하고 실행합니다.

## Verify

선택한 창 관리·클립보드·메뉴 막대 기능만 활성화하고 해당 기능이 작동하는지 확인합니다.

## Caveats

AI 에이전트 전용 확장이 아닌 macOS 독립 유틸리티입니다. 포함된 AI 에이전트 사용량 표시 기능은 부가 요소이며 기본 성격을 오인해서는 안 됩니다.

## References

- [Upstream](https://github.com/vorssaint/vorssaint-utils)
