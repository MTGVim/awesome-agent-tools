# Claude Auto Handoff

<!-- catalog: {"name": "Claude Auto Handoff", "upstream": "https://github.com/alexknowshtml/claude-auto-handoff", "types": ["mod"], "agents": ["Claude Code"], "category": "context", "verification": "unverified", "install_mode": "manual-review", "last_reviewed": "2026-11-03"} -->

> 컨텍스트 임계치에서 새 세션 인수인계. 특수 설치 절차 필요

- **Upstream:** https://github.com/alexknowshtml/claude-auto-handoff
- **Types:** mod
- **Agents:** Claude Code
- **Verification:** unverified
- **Install mode:** manual-review
- **Last reviewed:** 2026-11-03

## Why use it?

컨텍스트 임계치에 도달하면 Haiku로 인수인계 브리프를 만들고 `/clear` 이후 새 세션에서 이어서 작업하도록 돕는 Claude Code Mod입니다.

## Requirements

함수 훅을 지원하는 Claude Code 빌드가 필요합니다. 로컬 브리프 파일과 선택적 Tailscale 뷰어 서버를 사용합니다.

## Install

원본 README는 저장소를 로컬에 복제한 뒤 다음과 같이 플러그인 디렉터리를 로드하는 방법을 안내합니다.

```bash
claude --plugin-dir ~/claude-auto-handoff
```

먼저 복제한 실제 경로로 수정합니다. 마켓플레이스 등록을 임의로 가정하지 않습니다.

## Update

원본 변경 내역과 로컬에 복제한 설정/브리프 템플릿을 비교해 갱신합니다.

## Uninstall

시작 옵션에서 플러그인 디렉터리를 제거하고, 브리프 및 뷰어 데이터를 유지할지 별도로 결정합니다.

## Verify

긴 테스트 세션에서 브리프 생성과 새 세션 복원, 임계치 판정 및 실패 후 복구 경로를 확인합니다.

## Caveats

자체 브리프를 디스크에 작성하고, 설정에 따라 로컬 또는 Tailscale IP로 뷰어 서버를 열 수 있습니다. 민감 정보가 포함되는지 점검합니다.

## References

- [Upstream](https://github.com/alexknowshtml/claude-auto-handoff)
