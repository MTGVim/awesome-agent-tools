# Claude Code Filetree

<!-- catalog: {"name": "Claude Code Filetree", "upstream": "https://github.com/data-goblin/claude-code-filetree", "types": ["mod"], "agents": ["Claude Code"], "category": "ui", "verification": "metadata", "install_mode": "agent-guide", "last_reviewed": "2026-11-05"} -->

> Claude Code 파일 읽기·수정의 실시간 표시와 Git diff

- **Upstream:** https://github.com/data-goblin/claude-code-filetree
- **Types:** mod
- **Agents:** Claude Code
- **Verification:** metadata
- **Install mode:** agent-guide
- **Last reviewed:** 2026-11-05

## Why use it?

Claude Code가 **읽는 파일(보라색), 수정하는 파일(주황색), 커밋한 파일(초록색)**을 트리에서 실시간 애니메이션으로 표시합니다. 접힌 폴더도 작업 파일에 맞춰 펼쳐지며 Git 상태·파일별 diff·내용 검색·미리보기·디렉터리 treemap을 함께 확인할 수 있습니다. 단순 디렉터리 브라우저가 아니라 작업 중인 파일을 추적하는 UI입니다.

## Requirements

Claude Code 2.1.306+와 Git이 필요합니다. 터미널 사이드바에는 `/tui fullscreen` 모드와 **110열 이상의 너비**가 필요합니다. Claude Desktop 앱에서는 자체 도킹 방식으로 표시합니다. macOS·Linux·Windows를 지원한다고 상류에서 안내하며, Desktop의 WSL 세션에서는 Mod가 로드되지 않습니다.

## Install

```bash
claude plugin marketplace add data-goblin/claude-code-filetree
claude plugin install filetree@claude-code-filetree
```

Claude Code에서 `/filetree`로 표시 여부를 전환하고, `/filetree open`으로 기존 패널을 앞으로 가져올 수 있습니다. `/filetree <path>`는 트리의 루트 폴더를 지정합니다.

## Update

원본 릴리스와 마켓플레이스 갱신 내용을 검토한 뒤 Claude Code 플러그인 관리 절차에 따라 갱신합니다. `Follow work`, `Claude activity`, `Guard` 등 기존 사용자 설정을 보존합니다.

## Uninstall

`claude plugin uninstall filetree@claude-code-filetree`로 등록을 제거합니다.

## Verify

1. `/tui fullscreen` 및 110열 이상의 터미널 너비를 확인하고 `/filetree`를 엽니다.
2. Claude Code로 서로 다른 파일을 읽고 수정해 트리의 색상 강조, 자동 펼침 및 Git 상태 갱신을 확인합니다.
3. 변경 파일에서 `d`를 눌러 diff를 확인하고, 필요하면 `s`·`i`·`q` 검색을 시험합니다.

## Caveats

- **개인 환경에서 시험 후 사용 중단 (2026-11-06):** 활성화 시 Claude Code 화면 전체의 클릭 위치가 왼쪽으로 어긋났으며, Filetree를 숨기면 정상으로 돌아왔습니다. 이후 플러그인·마켓플레이스·캐시를 제거했습니다. 정확한 원인 및 다른 환경에서의 재현 여부는 미확인입니다. 카탈로그는 Active로 유지하되 환경별 호환성 문제로 기록합니다.
- 좁은 터미널에서는 패널이 표시되지 않습니다. Desktop 앱에는 split preview·treemap이 없고, WSL 데스크톱 세션에서는 Mod가 로드되지 않습니다.
- `Follow work` 옵션을 활성화하면 Claude가 다른 저장소를 집중적으로 다룰 때 세션 디렉터리를 `/cd`로 이동시킬 수 있습니다. 의도치 않은 작업 디렉터리 변경이 없는지 확인합니다.
- `Guard` 기능은 편집 보호 경로를 지정합니다. 실제 파일 보호 범위는 독립적으로 검증해야 합니다.
- 상류 README에서는 자체 텔레메트리와 자동 업데이트 정책을 명시적으로 확인하지 못했습니다. 미확인을 비활성화로 해석하지 않습니다.

## References

- [Upstream](https://github.com/data-goblin/claude-code-filetree)
- [Claude activity](https://github.com/data-goblin/claude-code-filetree/blob/main/docs/activity.md)
- [Sidebar / terminal requirements](https://github.com/data-goblin/claude-code-filetree/blob/main/docs/sidebar.md)
