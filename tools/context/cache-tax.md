# Cache Tax

<!-- catalog: {"name": "Cache Tax", "upstream": "https://github.com/karanb192/cache-tax", "types": ["plugin", "mod"], "agents": ["Claude Code"], "category": "context", "verification": "metadata", "install_mode": "agent-guide", "last_reviewed": "2026-11-03"} -->

> 프롬프트 캐시 유지와 만료 시 비용 경고. 캐시 유지에 토큰 사용

- **Upstream:** https://github.com/karanb192/cache-tax
- **Types:** plugin/mod
- **Agents:** Claude Code
- **Verification:** metadata
- **Install mode:** agent-guide
- **Last reviewed:** 2026-11-03

## Why use it?

Claude Code 세션이 유휴 상태일 때 프롬프트 캐시를 유지하고, 캐시가 식은 뒤 입력할 경우 예상 재작성 비용을 알려줍니다.

## Requirements

Claude Code 2.1.287+, 1시간 캐시 유지 설정, 실행 중인 Claude Code 세션이 필요합니다.

## Install

```bash
claude plugin marketplace add karanb192/claude-code-mods
claude plugin install cache-tax@claude-code-mods
```

이후 Claude Code에서 `/keepwarm 90m` 등 원하는 시간만 활성화합니다.

## Update

원본 `claude-code-mods` 마켓플레이스와 `cache-tax@claude-code-mods` 플러그인을 각각 최신화합니다.

## Uninstall

`/keepwarm off`로 먼저 비활성화한 뒤 `claude plugin uninstall cache-tax@claude-code-mods`를 실행합니다.

## Verify

`/keepwarm` 상태와 캐시 ping 결과를 확인하되, ping 자체에 토큰이 사용된다는 점을 기록합니다.

## Caveats

캐시 유지 ping은 실제 토큰을 소비합니다. API 키 기반 환경은 기본 캐시 수명이 짧을 수 있어 TTL 확인이 필수입니다.

## References

- [Upstream](https://github.com/karanb192/cache-tax)
