# Next Steps

<!-- catalog: {"name": "Next Steps", "upstream": "https://github.com/anthropics/claude-plugins-community", "types": ["plugin", "mod"], "agents": ["Claude Code"], "category": "workflows", "verification": "unverified", "install_mode": "manual-review", "last_reviewed": "2026-11-03"} -->

> 응답 후속 행동 제안. 설치 식별자 별도 확인 필요

- **Upstream:** https://github.com/anthropics/claude-plugins-community
- **Types:** plugin/mod
- **Agents:** Claude Code
- **Verification:** unverified
- **Install mode:** manual-review
- **Last reviewed:** 2026-11-03

## Why use it?

Claude Code의 각 턴이 끝나면 다음 작업 후보 3개까지 입력창 위에 제안합니다. 선택한 항목은 자동 제출되지 않고 초안으로 입력됩니다.

## Requirements

Claude Code의 Function Hooks 지원 버전과 터미널 TUI가 필요합니다.

## Install

원본 저장소의 `next-steps` 플러그인은 `anthropics/claude-plugins-community` 마켓플레이스에 있습니다. 아래 명령은 Claude Code CLI용입니다.

```bash
claude plugin marketplace add anthropics/claude-plugins-community
claude plugin install next-steps@claude-community
```

## Update

Claude Code의 마켓플레이스 업데이트 후 플러그인을 갱신합니다. 자동 실행 훅의 변경 사항을 확인합니다.

## Uninstall

`claude plugin uninstall next-steps@claude-community`를 사용하고 공유 마켓플레이스는 다른 플러그인 사용 여부를 확인한 뒤 정리합니다.

## Verify

완료된 턴에서 1~3개의 후속 제안이 나타나는지 확인하고, 선택 시 자동 전송 없이 프롬프트 초안만 채우는지 확인합니다.

## Caveats

`turn.complete` 시 짧은 모델 fork를 사용해 사용량을 소비합니다. 원본은 터미널 UI 이외 표면에서 제안이 보이지 않는다고 안내합니다.

## References

- [Upstream](https://github.com/anthropics/claude-plugins-community)
