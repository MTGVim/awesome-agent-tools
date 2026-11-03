# Agent Usage Guard

<!-- catalog: {"name": "Agent Usage Guard", "upstream": "https://github.com/rbartoli/agent-usage-guard", "types": ["plugin"], "agents": ["Claude Code"], "category": "context", "verification": "metadata", "install_mode": "agent-guide", "last_reviewed": "2026-11-03"} -->

> 서브에이전트 사용량 급증 방지

- **Upstream:** https://github.com/rbartoli/agent-usage-guard
- **Types:** plugin
- **Agents:** Claude Code
- **Verification:** metadata
- **Install mode:** agent-guide
- **Last reviewed:** 2026-11-03

## Why use it?

Claude Code가 과도한 서브에이전트 생성, 컨텍스트 반복 처리, 재시도 루프로 사용량을 급격히 소모하지 않도록 실행 전에 확인하거나 제한합니다.

## Requirements

Claude Code 2.1.287+와 Mods 함수 훅이 필요합니다.

## Install

```text
/plugin marketplace add rbartoli/agent-usage-guard
/plugin install agent-usage-guard@agent-usage-guard
/reload-plugins
```

## Update

`claude plugin marketplace update agent-usage-guard` 후 플러그인 업데이트를 확인합니다.

## Uninstall

`claude plugin uninstall agent-usage-guard@agent-usage-guard`로 등록을 제거합니다.

## Verify

`/agent-guard`를 실행해 현재 감지·제한 상태와 승인 대화상자를 확인합니다.

## Caveats

계정 사용량을 조회하며 제한 조건에 따라 도구 호출을 막을 수 있습니다. 훅 권한을 검토합니다.

## References

- [Upstream](https://github.com/rbartoli/agent-usage-guard)
