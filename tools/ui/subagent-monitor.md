# Subagent Monitor

<!-- catalog: {"name": "Subagent Monitor", "upstream": "https://github.com/blogchik/subagent-monitor", "types": ["plugin", "mod"], "agents": ["Claude Code"], "category": "ui", "verification": "personal", "install_mode": "agent-guide", "last_reviewed": "2026-11-17"} -->

> Claude Code 서브에이전트의 실시간 활동과 모델·effort·토큰 컨텍스트를 표시하는 패널

- **Upstream:** https://github.com/blogchik/subagent-monitor
- **Types:** plugin/mod
- **Agents:** Claude Code
- **Verification:** personal (큐레이터 사용 확인; 이번 작업에서는 실행 미검증)
- **Install mode:** agent-guide
- **Last reviewed:** 2026-11-17

## Why use it?

서브에이전트별 진행 상태, 현재 도구, 모델과 effort, 토큰 컨텍스트, 경과 시간 및 대화 기록을 확인합니다. 2026-11-17 큐레이터가 Flightdeck 대신 사용한다고 확인했습니다. Flightdeck의 전체 비용·권한 검사 기능과 동등하다는 뜻은 아닙니다.

## Requirements

Claude Code의 Mod(function hook) 지원이 필요합니다. Upstream은 2.1.309에서 개발·시험했다고 명시하며, 이는 최소 버전 보장이 아닙니다. 확인한 manifest 버전은 0.4.0입니다.

## Install

Claude Code 터미널에서:

```text
/plugin install subagent-monitor --marketplace blogchik/subagent-monitor
```

마켓플레이스 추가와 설치 범위를 확인합니다. 셸에서는 `claude plugin install subagent-monitor --marketplace blogchik/subagent-monitor`를 사용합니다. 실제 설치는 별도 승인을 받습니다.

## Update

```bash
claude plugin update subagent-monitor
```

열린 세션에서는 `/reload-plugins`를 실행합니다. manifest 버전이 동일한 커밋의 반영 여부는 확인이 필요합니다.

## Uninstall

```bash
claude plugin uninstall subagent-monitor
```

다른 플러그인이나 공유 설정은 제거하지 않습니다.

## Verify

서브에이전트를 실행하여 패널 자동 열기, 도구 활동·모델·effort·토큰 표시 및 대화 기록 열기를 확인합니다. 닫은 패널은 `/subagents`로 다시 엽니다.

## Caveats

- Mods API는 early access이므로 Claude Code 갱신 후 호환성을 확인합니다.
- 토큰 수는 최신 모델 요청의 컨텍스트 크기이며 누적 과금량이 아닙니다.
- 원격 workflow 에이전트는 표시되지 않으며 로컬 workflow 에이전트의 대화 기록도 제한됩니다.
- 에이전트를 중지하는 버튼은 없습니다. 새 세션에서는 목록이 초기화됩니다.
- Upstream 패널 그림은 실제 스크린샷이 아닌 설명용 일러스트입니다.

## Privacy & Updates

2026-11-17 README·manifest·`hooks/register.tsx`를 정적으로 확인했습니다. 세션 이벤트와 대화 기록을 읽고 세션 상태에 표시 정보를 유지합니다. 자체 텔레메트리 송신, 수신처, opt-out, 자동 업데이트 및 버전 확인 정책은 미확인입니다. 수동 플러그인 갱신은 지원하며 호스트의 마켓플레이스 통신과 구분합니다. 소스 전체 감사나 네트워크 실행 검증은 수행하지 않았습니다.

## References

- [README](https://github.com/blogchik/subagent-monitor)
- [설치 및 갱신](https://github.com/blogchik/subagent-monitor#install)
- [작동 방식](https://github.com/blogchik/subagent-monitor#how-it-works)
- [제한 사항](https://github.com/blogchik/subagent-monitor#limitations)
