# Claude Flightdeck

<!-- catalog: {"name": "Claude Flightdeck", "upstream": "https://github.com/scasella/claude-flightdeck", "types": ["plugin", "mod"], "agents": ["Claude Code"], "category": "ui", "verification": "personal", "install_mode": "agent-guide", "last_reviewed": "2026-11-10"} -->

> Claude Code의 컨텍스트·비용·권한 검사·서브에이전트를 보여주는 실시간 패널

- **Upstream:** https://github.com/scasella/claude-flightdeck
- **Types:** plugin/mod
- **Agents:** Claude Code
- **Verification:** personal
- **Install mode:** agent-guide
- **Last reviewed:** 2026-11-10

## Why use it?

메인 모델 상태, 컨텍스트·비용, advisor 호출, 권한 검사와 서브에이전트 상태를 카드·스윔레인으로 보여줍니다. 2026-11-10 큐레이터가 Savvy Progress 사용을 중단하고 Flightdeck을 다시 사용한다고 확인하여 Daily Setup으로 복원했습니다. Savvy Progress의 추천 철회나 두 도구의 기능 동등성을 뜻하지 않습니다.

## Requirements

확인한 upstream 0.6.1은 Claude Code 2.1.289+를 요구합니다. Mods는 early-access 기능이므로 버전별 호환성을 다시 확인합니다. VS Code 확장에서는 패널이 보이지 않을 수 있으며, upstream은 통합 터미널 실행을 안내합니다.

## Install

Claude Code 내부에서 실행하는 공식 설치 절차입니다. 설치·설정 변경은 별도 승인을 받은 뒤 수행합니다.

```text
/plugin marketplace add scasella/claude-flightdeck
/plugin install flightdeck@claude-flightdeck
/reload-plugins
/flightdeck
```

## Update

Claude Code 플러그인 관리에서 해당 마켓플레이스와 `flightdeck@claude-flightdeck`의 갱신 경로를 확인합니다. 기존 사용자 설정은 보존하고, 갱신 후 `/reload-plugins`와 `/flightdeck`으로 표시를 확인합니다. 상태 형식 변경으로 카운터가 초기화될 수 있습니다.

## Uninstall

`claude plugin uninstall flightdeck@claude-flightdeck`로 이 플러그인만 제거합니다. 마켓플레이스나 다른 플러그인은 자동 제거하지 않습니다. 사용자 설정을 지울 필요가 있다면 해당 도구가 만든 항목과 범위를 먼저 확인합니다.

## Verify

`/flightdeck`으로 패널을 열고 실제 서브에이전트 실행·권한 검사 뒤 카드·로그가 갱신되는지 확인합니다. 사용자 사용 확인과 이번 작업의 정적 문서 조사는 구분하며, 이번 유지보수에서 설치나 실행을 재검증하지 않았습니다.

## Caveats

- `openOnStart`가 켜져 있어도 터미널 너비 144열 미만에서는 `/flightdeck`으로 직접 엽니다.
- Team·Enterprise 로그인이나 managed settings의 내장 guard는 일부 hook을 제한합니다. 권한 모드가 누락·지연되거나 compaction 횟수가 추정치로 표시될 수 있습니다.
- 사용자 설정의 키는 설치 방식에 따라 다릅니다. 마켓플레이스 설치는 `pluginConfigs["flightdeck@claude-flightdeck"].options`, `--plugin-dir`은 `pluginConfigs["flightdeck"].options`를 사용하며 프로젝트 설정은 읽지 않는다고 설명합니다.
- 과거 개인 설정에서 `motion: while-active`를 사용했습니다. 현재 설정값을 이번 작업에서 직접 확인하지는 않았습니다.
- 컨텍스트·비용·권한·프롬프트 일부 등 민감할 수 있는 세션 정보를 패널이 읽습니다. 일부 수치는 추정치이며 다른 패널과의 화면 충돌은 환경별로 확인합니다.

## Privacy & Updates

2026-11-10 upstream README는 hook의 세션 이벤트를 관찰하고 짧은 요약을 세션 상태에만 보관하며, 자체 네트워크 요청·프로세스 실행·파일 읽기/쓰기·세션 간 저장·모델 호출을 하지 않는다고 설명합니다. 문서 설명 기준으로 자체 텔레메트리 송신 대상이나 opt-out은 해당하지 않습니다. 자체 버전 확인·자동 코드 업데이트는 별도 정책을 확인하지 못했으며, Claude Code 본체와 마켓플레이스의 통신·갱신은 구분해야 합니다. 소스 전체 감사나 실행 중 네트워크 검증은 수행하지 않았습니다.

[Privacy, Telemetry & Updates](../../docs/privacy-and-updates.md)에서 다른 도구와 구분합니다.

## References

- [확인한 README](https://github.com/scasella/claude-flightdeck/blob/bf433171558f63a2fef46e8b92560968b2033e4f/README.md)
- [플러그인 manifest](https://github.com/scasella/claude-flightdeck/blob/bf433171558f63a2fef46e8b92560968b2033e4f/.claude-plugin/plugin.json)
- [Changelog](https://github.com/scasella/claude-flightdeck/blob/bf433171558f63a2fef46e8b92560968b2033e4f/CHANGELOG.md)

## 큐레이션 이력

2026-11-06에는 Savvy Progress로 대체하여 `superseded`로 보관했습니다. 2026-11-10에는 사용자의 실제 사용 재개 확인에 따라 복원했습니다. 과거 보관은 upstream의 결함이나 중단 판정이 아니었습니다.
