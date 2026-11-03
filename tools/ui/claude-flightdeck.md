# Claude Flightdeck

<!-- catalog: {"name": "Claude Flightdeck", "upstream": "https://github.com/scasella/claude-flightdeck", "types": ["plugin", "mod"], "agents": ["Claude Code"], "category": "ui", "verification": "trial", "install_mode": "agent-guide", "last_reviewed": "2026-11-03"} -->

> 컨텍스트·비용·권한·서브에이전트 모니터링

- **Upstream:** https://github.com/scasella/claude-flightdeck
- **Types:** plugin/mod
- **Agents:** Claude Code
- **Verification:** trial
- **Install mode:** agent-guide
- **Last reviewed:** 2026-11-03

## Why use it?

Claude Code의 메인 모델 상태, 컨텍스트·비용, 권한 검사와 서브에이전트 상태를 카드·스윔레인으로 보여주는 실시간 패널입니다.

## Requirements

Claude Code 2.1.287+의 Function Hooks가 필요합니다. 데스크톱과 터미널에서 보이는 배치가 다를 수 있습니다.

## Install

```bash
claude plugin marketplace add scasella/claude-flightdeck
claude plugin install flightdeck@claude-flightdeck
```

Claude Code에서 `/flightdeck`을 실행합니다.

## Update

마켓플레이스와 `flightdeck@claude-flightdeck` 플러그인을 갱신한 뒤 설정을 확인합니다.

## Uninstall

`claude plugin uninstall flightdeck@claude-flightdeck`로 등록을 제거합니다.

## Verify

한 세션에서 서브에이전트 실행과 권한 확인을 테스트해 실시간 패널과 기록이 갱신되는지 확인합니다.

## Caveats

### 텔레메트리와 네트워크 (2026-11-04 문서 확인)

상류 README는 세션 정보를 로컬에서 처리하며 자체 네트워크 요청을 하지 않는다고 설명합니다. 호스트의 API·플러그인 업데이트 통신은 별개입니다. [Upstream README](https://github.com/scasella/claude-flightdeck)

상태 비교: [Privacy, Telemetry & Updates](../../docs/privacy-and-updates.md). 실제 설치된 버전의 설정을 다시 확인합니다.

### 개인 셋업 메모 (2026-11-03)

Glowup과 사이드 패널 영역이 겹칩니다. 사용자 설정에서는 펄스를 `motion: while-active`로 활성화했습니다. 위쪽 선은 메인 턴, `┬`·`┴`는 서브에이전트 활동을 나타냅니다.

표시되는 일부 사용량·컨텍스트 수치는 원본에 명시된 추정치일 수 있습니다. 원본은 로컬 세션 데이터 기반으로 동작한다고 설명합니다.

## References

- [Upstream](https://github.com/scasella/claude-flightdeck)
