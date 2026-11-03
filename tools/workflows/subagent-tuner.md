# Subagent Tuner

<!-- catalog: {"name": "Subagent Tuner", "upstream": "https://github.com/Kruhlikau/subagent-tuner", "types": ["plugin", "mod"], "agents": ["Claude Code"], "category": "workflows", "verification": "personal", "install_mode": "cli", "last_reviewed": "2026-11-03"} -->

> 서브에이전트 모델 및 실행 강도 조정

- **Upstream:** https://github.com/Kruhlikau/subagent-tuner
- **Types:** plugin/mod
- **Agents:** Claude Code
- **Verification:** personal
- **Install mode:** cli
- **Last reviewed:** 2026-11-03

## Why use it?

Claude Code 서브에이전트를 실행할 때 모델과 reasoning effort를 작업별 추천, 기본값 또는 수동 선택으로 지정합니다.

## Requirements

원본 README 기준 Claude Code 2.1.295 이상에서 작동하는 함수 훅 모드입니다.

## Install

Claude Code 안에서 아래 명령을 실행합니다.

```text
/plugin install subagent-tuner --marketplace Kruhlikau/subagent-tuner
```

## Update

마켓플레이스를 최신화한 뒤 `subagent-tuner@subagent-tuner` 플러그인 업데이트를 확인합니다. 활성 세션에서 다시 로드해야 할 수 있습니다.

## Uninstall

`claude plugin uninstall subagent-tuner@subagent-tuner`로 등록을 제거하고 저장된 사용자 설정을 별도로 확인합니다.

## Verify

서브에이전트를 하나 시작해 Manual/Auto 설정에 맞춰 모델과 추론 수준이 결정되는지 확인합니다.

## Caveats

메인 세션 모델 변경 도구가 아닙니다. 자동 라우팅과 수동 승인 모드의 동작 차이를 확인해야 합니다.

## References

- [Upstream](https://github.com/Kruhlikau/subagent-tuner)
