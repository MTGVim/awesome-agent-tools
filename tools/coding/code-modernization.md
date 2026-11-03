# Code Modernization

<!-- catalog: {"name": "Code Modernization", "upstream": "https://github.com/anthropics/claude-plugins-official/tree/main/plugins/code-modernization", "types": ["plugin"], "agents": ["Claude Code"], "category": "coding", "verification": "metadata", "install_mode": "agent-guide", "last_reviewed": "2026-11-03"} -->

> 기존 코드를 최신 스택으로 마이그레이션

- **Upstream:** https://github.com/anthropics/claude-plugins-official/tree/main/plugins/code-modernization
- **Types:** plugin
- **Agents:** Claude Code
- **Verification:** metadata
- **Install mode:** agent-guide
- **Last reviewed:** 2026-11-03

## Why use it?

레거시 코드의 동작과 규칙을 분석하고 승인 가능한 마이그레이션 계획을 만든 뒤, 재구축 결과가 기존 입출력과 동등한지 비교합니다.

## Requirements

Claude Code의 공식 플러그인 기능이 필요합니다. 큰 코드베이스에서 다수의 서브에이전트를 사용하면 사용량이 늘 수 있습니다.

## Install

Claude Code 안에서 설치합니다.

```text
/plugin install code-modernization@claude-plugins-official
```

`/code-modernization:modernize`를 호출하고 작은 모듈로 시범 진행합니다.

## Update

Claude Code 공식 플러그인 업데이트 경로를 이용합니다. 진행 중인 마이그레이션 기록과 생성한 계획은 보존합니다.

## Uninstall

플러그인 등록만 제거합니다. 이미 생성한 코드, 테스트 및 비교 리포트는 별도로 관리합니다.

## Verify

변환 전후 동일 입력의 출력 결과와 주요 부수 효과가 일치하는지 검증합니다. 실제 도메인 규칙 검사는 별도 테스트가 필요합니다.

## Caveats

원본 README도 처음에는 작은 모듈로 시도하라고 권장합니다. 자동 코드 생성이 요구사항 검증을 대체하지 않습니다.

## References

- [Upstream](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/code-modernization)
