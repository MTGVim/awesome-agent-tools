# Agent Usage Guard

<!-- catalog: {"name": "Agent Usage Guard", "upstream": "https://github.com/rbartoli/agent-usage-guard", "types": ["plugin"], "agents": ["Claude Code"], "category": "context", "verification": "personal", "install_mode": "agent-guide", "last_reviewed": "2026-11-03"} -->

> 서브에이전트 사용량 급증 방지

- **Upstream:** https://github.com/rbartoli/agent-usage-guard
- **Types:** plugin
- **Agents:** Claude Code
- **Verification:** personal
- **Install mode:** agent-guide
- **Last reviewed:** 2026-11-03

## Why use it?

사용자 실사용 평가: 과도한 에이전트 실행을 제어하는 기능뿐 아니라 컨텍스트가 커졌을 때 **Compact 후 전송**을 제안하는 선택지가 유용했습니다. 사용자 판단을 거쳐 계속 진행하거나 압축할 수 있습니다.

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

`/agent-guard`를 실행해 현재 감지·제한 상태와 승인 대화상자를 확인합니다. `AGENT_GUARD_DORMANT_SECONDS=21600` 적용 여부와 유휴 6시간 전후의 확인 동작도 검증합니다.

## Caveats

### 텔레메트리와 네트워크 (2026-11-04 문서 확인)

상류 README는 자체 네트워크 요청과 별도 프로세스가 없다고 명시합니다. Claude Code 자체 통신·업데이트 정책과는 구분해야 합니다. [Upstream README](https://github.com/rbartoli/agent-usage-guard)

상태 비교: [Privacy, Telemetry & Updates](../../docs/privacy-and-updates.md). 실제 설치된 버전의 설정을 다시 확인합니다.

**Daily Setup (2026-11-06):** 사용 중입니다. 컨텍스트가 커질 때 압축 여부를 먼저 제안하는 점을 긍정적으로 평가했습니다. `AGENT_GUARD_DORMANT_SECONDS=21600`으로 휴면 기준을 6시간으로 설정해, 6시간 이하 유휴 시 확인을 건너뛰고 6시간을 초과하면 해당 가드가 한 번 질문하도록 구성했습니다. 이는 Cache Tax의 `guard: warn`(비용 표시만 수행)과 별개의 역할입니다. 실제 압축은 사용자 선택에 따르며 휴면 동작은 설치된 버전에서 별도 검증이 필요합니다.

계정 사용량을 조회하며 제한 조건에 따라 도구 호출을 막을 수 있습니다. 훅 권한을 검토합니다.

## References

- [Upstream](https://github.com/rbartoli/agent-usage-guard)
