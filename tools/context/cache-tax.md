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

`/keepwarm` 상태와 캐시 ping 결과를 확인하되, ping 자체에 토큰이 사용된다는 점을 기록합니다. 새 세션의 `/cache-tax` 카드에서 `guard warn only` 표시 여부와 일반 autocompact의 유지 여부를 별도로 검증합니다.

## Caveats

### 개인 셋업 메모 (2026-11-06)

기존 사용자 환경에서는 `/keepwarm` 사용 중 약 54분 후 idle compaction이 발생했습니다. 현재는 Claude Code의 `"idleCompaction": false`로 유휴 압축만 끄고 일반 autocompact는 유지합니다. Cache Tax는 `keepwarm: always`, `guard: warn`으로 설정해 캐시 비용만 표시하고 차단은 하지 않습니다. **가드 설정은 파일로 반영했으나 새 세션의 `/cache-tax` 카드에서 `guard warn only`가 표시되는지 검증이 필요합니다.** 캐시 유지 ping에도 토큰이 소비되며 `always`가 캐시 영구 보존을 뜻하지는 않습니다.

Agent Usage Guard는 별도로 `AGENT_GUARD_DORMANT_SECONDS=21600`(6시간)을 설정했습니다. 유휴 상태가 6시간 이내일 때는 휴면 확인을 생략하고, 6시간 초과 시 해당 가드만 확인하는 구성을 의도했습니다. 관련 내용은 [Agent Usage Guard](agent-usage-guard.md)에 기록했습니다.

캐시 유지 ping은 실제 토큰을 소비합니다. API 키 기반 환경은 기본 캐시 수명이 짧을 수 있어 TTL 확인이 필수입니다.

## References

- [Upstream](https://github.com/karanb192/cache-tax)
