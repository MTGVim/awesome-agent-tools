# Claude Image View

<!-- catalog: {"name": "Claude Image View", "upstream": "https://github.com/jarrodwatts/claude-image-view", "types": ["plugin", "mod"], "agents": ["Claude Code"], "category": "ui", "tier": "B", "verification": "metadata", "install_mode": "cli", "last_reviewed": "2026-11-03"} -->

> 붙여넣은 이미지 썸네일 미리보기

- **Upstream:** https://github.com/jarrodwatts/claude-image-view
- **Types:** plugin/mod
- **Agents:** Claude Code
- **Tier:** B (initial, provisional)
- **Verification:** metadata
- **Install mode:** cli
- **Last reviewed:** 2026-11-03

## Why use it?

붙여넣은 이미지 썸네일 미리보기 추천 등급은 개인 노트의 관심도와 사용 경험을 바탕으로 정한 초기 분류이며, 객관적인 성능 검증 결과는 아닙니다.

## Requirements

원본 README의 OS·에이전트 버전·권한·터미널 호환성 조건을 확인해야 합니다.

## Install

```sh
claude plugin marketplace add jarrodwatts/claude-image-view
claude plugin install image-view@claude-image-view
```

실행 전 Claude Code와 터미널 요구 사항을 확인합니다.

## Update

```sh
claude plugin marketplace update claude-image-view
claude plugin update image-view@claude-image-view
```

## Uninstall

```sh
claude plugin uninstall image-view@claude-image-view
```

마켓플레이스 제거는 다른 플러그인이 사용하지 않을 때만 별도 검토합니다.

## Verify

`claude plugin list`에서 설치 여부를 확인하고, 이미지 입력 시 썸네일을 확인합니다.

## Caveats

검증 상태가 `personal`이 아닌 경우, 메타데이터 확인과 실제 설치·기능 테스트를 구분해야 합니다. 사전 승인 없이 원격 스크립트를 실행하거나 전역 설정을 수정하지 않습니다.

## References

- [Upstream](https://github.com/jarrodwatts/claude-image-view)
