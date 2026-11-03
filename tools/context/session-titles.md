# Session Titles

<!-- catalog: {"name": "Session Titles", "upstream": "https://github.com/zhangbububu/session-titles", "types": ["mod"], "agents": ["Claude Code"], "category": "context", "verification": "unverified", "install_mode": "agent-guide", "last_reviewed": "2026-11-03"} -->

> 세션 제목 관리

- **Upstream:** https://github.com/zhangbububu/session-titles
- **Types:** mod
- **Agents:** Claude Code
- **Verification:** unverified
- **Install mode:** agent-guide
- **Last reviewed:** 2026-11-03

## Why use it?

입력한 최신 프롬프트를 바탕으로 Claude Code의 세션 제목을 갱신합니다. 데스크톱에서는 짧은 제목을 Haiku가 생성합니다.

## Requirements

함수 훅이 있는 Claude Code 빌드가 필요합니다. 원본은 2.1.289에서 개발되었다고 안내합니다.

## Install

```text
/plugin marketplace add zhangbububu/session-titles
/plugin install last-prompt-title@session-titles
```

## Update

마켓플레이스와 `last-prompt-title@session-titles`의 최신 버전을 확인한 후 갱신합니다.

## Uninstall

`claude plugin uninstall last-prompt-title@session-titles`를 사용합니다.

## Verify

새 프롬프트를 입력하고 CLI 제목과 데스크톱 사이드바 제목이 기대한 방식으로 갱신되는지 확인합니다.

## Caveats

데스크톱 사이드바 제목 생성을 위해 프롬프트마다 Haiku 호출이 추가됩니다. 직접 설정한 제목을 덮어쓸 수 있습니다.

## References

- [Upstream](https://github.com/zhangbububu/session-titles)
