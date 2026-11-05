# Savvy Progress

<!-- catalog: {"name": "Savvy Progress", "upstream": "https://github.com/JohnnyVizz/claude-kit/tree/main/plugins/savvy-progress", "types": ["mod"], "agents": ["Claude Code"], "category": "ui", "verification": "metadata", "install_mode": "agent-guide", "last_reviewed": "2026-11-05"} -->

> Claude Code 작업 진행률 표시와 서브에이전트 상태 패널

- **Upstream:** https://github.com/JohnnyVizz/claude-kit/tree/main/plugins/savvy-progress
- **Types:** mod
- **Agents:** Claude Code
- **Verification:** metadata
- **Install mode:** agent-guide
- **Last reviewed:** 2026-11-05

## Why use it?

Claude Code 입력창 위에 작업 진행률 막대를 표시하고, `/agents-info`로 실행 중·완료·예정된 서브에이전트의 모델, effort, 작업 단계, 컨텍스트, 추정 비용·소요 시간을 확인합니다. [savvy-flow](https://github.com/JohnnyVizz/claude-kit/tree/main/plugins/savvy-flow)와 함께 사용하면 계획·작업 수락 현황이 진행률에 반영되지만, **savvy-progress 자체는 독립적으로 설치**할 수 있으며 일반 서브에이전트도 패널에서 표시합니다.

[Claude Flightdeck](claude-flightdeck.md)과 비교해 볼 시험 사용 후보입니다. Flightdeck이 제공하는 모든 컨텍스트·권한 정보를 그대로 대체한다고 가정하지 않습니다.

## Requirements

Claude Code의 Mod/Function Hooks 지원 환경이 필요합니다. 상류 claude-kit 문서는 Claude Code 2.1.286에서 시험했다고 밝히지만, 해당 API는 초기 단계라 이후 버전에서도 호환성을 다시 확인해야 합니다. marketplace 설치 후 세션을 재시작합니다.

## Install

Claude Code 내부에서 다음 명령을 사용합니다.

```text
/plugin marketplace add johnnyvizz/claude-kit
/plugin install savvy-progress@claude-kit
```

진행률 계획과 단계 보고를 시험하려면 **선택적으로** `/plugin install savvy-flow@claude-kit`를 추가합니다. 처음에는 Progress만 설치하고 일반 서브에이전트 표시를 확인해도 됩니다. 패널은 `/agents-info`로 열거나 닫으며, `/agents-info open`은 닫지 않고 열거나 앞으로 가져옵니다.

## Update

`claude-kit` 마켓플레이스의 최신 버전과 `savvy-progress` 플러그인 변경 사항을 확인한 뒤 Claude Code의 플러그인 관리 절차로 갱신합니다. 수동 `--plugin-dir` 설치를 선택했다면 원본 저장소 갱신과 마켓플레이스 갱신을 혼동하지 않습니다.

## Uninstall

Claude Code 플러그인 관리에서 `savvy-progress@claude-kit`만 제거합니다. `savvy-flow` 또는 다른 claude-kit 플러그인까지 자동으로 삭제하지 않습니다. 마켓플레이스 자체는 다른 플러그인이 사용 중인지 확인한 뒤 별도로 관리합니다.

## Verify

1. 세션을 재시작하고 `/agents-info`로 패널이 열리는지 확인합니다.
2. 일반 서브에이전트를 실행하고 실행·완료 상태와 모델 정보를 확인합니다.
3. `savvy-flow`를 설치했다면 계획 단계와 수락된 작업 수가 진행률에 반영되는지 확인합니다.
4. Flightdeck과는 **각각 단독 실행**해 패널 가독성, 중복 표시 및 추가 도구 호출·토큰 사용량을 비교합니다.

## Caveats

- **시험 사용 예정:** 상류 문서와 매니페스트만 확인했습니다. 실제 설치·동작, Flightdeck 대체 적합성은 아직 검증하지 않았습니다.
- 기본 `autoOpen: savvy`는 savvy-flow 작업 또는 계획 보고 시 패널을 자동으로 열고, `autoOpen: any`는 일반 서브에이전트 시작 시에도 엽니다. 일반 작업의 계획 진행률은 자동으로 정확하게 생성되는 값이 아니며, 보고가 없는 작업자는 컨텍스트 사용량이 회색으로 표시될 수 있습니다.
- 비용 표시는 모델별 내장 가격표에 따른 **추정치**이며 실제 청구액이 아닙니다. 상류 문서의 가격표 기준일은 2026-10-10입니다.
- 다른 Mod와 동일한 입력창 위 영역·패널을 사용한다면 화면 충돌 여부를 별도로 확인해야 합니다.

## Privacy & Updates

2026-11-05 기준 상류 README와 모드 설명에서 별도의 텔레메트리 수집·자동 버전 확인 정책을 확인하지 못했습니다. **외부 전송 없음으로 단정할 수 없습니다.** 패널이 보여주는 토큰·모델·비용 정보는 로컬 세션 정보를 바탕으로 표시하지만, 전체 코드에 대한 네트워크 감사나 실행 중 패킷 확인은 수행하지 않았습니다. Claude Code 본체 및 플러그인 마켓플레이스의 통신·갱신 정책은 별개입니다.

## References

- [Savvy Progress README](https://github.com/JohnnyVizz/claude-kit/blob/main/plugins/savvy-progress/README.md)
- [claude-kit 설치 안내](https://github.com/JohnnyVizz/claude-kit/blob/main/README.md)
- [Savvy Progress 플러그인 매니페스트](https://github.com/JohnnyVizz/claude-kit/blob/main/plugins/savvy-progress/.claude-plugin/plugin.json)
