# Claude Code Mods

<!-- catalog: {"name": "Claude Code Mods", "upstream": "https://github.com/hamzafer/claude-code-mods", "types": ["mod"], "agents": ["Claude Code"], "category": "ui", "verification": "unverified", "install_mode": "agent-guide", "last_reviewed": "2026-11-03"} -->

> Claude Code 모드 컬렉션

- **Upstream:** https://github.com/hamzafer/claude-code-mods
- **Types:** mod
- **Agents:** Claude Code
- **Verification:** unverified
- **Install mode:** agent-guide
- **Last reviewed:** 2026-11-03

## Why use it?

Claude Code 함수 훅 기반의 상태 바·사용량 가드·도구 패널 등 다양한 모드를 체크박스로 골라 설치하는 배포기입니다.

## Requirements

Claude Code 2.1.287+가 필요합니다. 각 모드가 자체적으로 읽는 정보와 권한 범위는 다릅니다.

## Install

원본 README는 대화형 설치기를 안내합니다.

```bash
npx claude-code-mods@latest
```

모드를 선택하기 전에 기능과 훅 권한을 확인합니다.

## Update

설치기를 다시 실행해 기존 설치 상태와 변경 사항을 확인합니다. 모드별 업데이트 경로가 다를 수 있습니다.

## Uninstall

설치기의 관리 기능 및 각 플러그인의 설치 기록을 확인해 선택한 모드만 제거합니다.

## Verify

선택한 모드가 Claude Code에서 로드되고 요청한 화면·가드 기능이 동작하는지 확인합니다.

## Caveats

한 프로젝트에 여러 UI Mod를 동시에 설치하면 화면 영역과 훅 이벤트가 충돌할 수 있습니다. 설치기 자체와 개별 모드를 구분합니다.

## References

- [Upstream](https://github.com/hamzafer/claude-code-mods)
