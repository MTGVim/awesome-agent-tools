# Prismantis

<!-- catalog: {"name": "Prismantis", "upstream": "https://github.com/NahumLitvin/prismantis", "types": ["plugin", "mod"], "agents": ["Claude Code", "Codex"], "category": "visual", "verification": "personal", "install_mode": "agent-guide", "last_reviewed": "2026-11-03"} -->

> 표·코드·Mermaid·차트 렌더링

- **Upstream:** https://github.com/NahumLitvin/prismantis
- **Types:** plugin/mod
- **Agents:** Claude Code, Codex
- **Verification:** personal
- **Install mode:** agent-guide
- **Last reviewed:** 2026-11-03

## Why use it?

Claude Code의 표·코드·Mermaid·차트·LaTeX 등을 터미널에서 읽기 쉬운 테마 기반 출력으로 렌더링합니다. Codex용 버전도 제공됩니다.

## Requirements

Claude Code 2.1.287+가 필요합니다. Codex는 원본 `codex/README.md`의 별도 설치와 기능 제한을 따릅니다. 수식 그래픽 렌더링은 kitty/Ghostty 등에서 최적화됩니다.

## Install

Claude Code에서는 다음 명령을 사용합니다.

```text
/plugin marketplace add NahumLitvin/prismantis
/plugin install prismantis@prismantis
```

설치 후 `/prismantis setup`을 실행합니다. Codex는 원본 `codex/README.md`의 별도 절차를 확인합니다.

## Update

Claude Code에서는 마켓플레이스와 `prismantis@prismantis`를 갱신합니다. Codex 구현은 별도 설치 절차를 따라야 합니다.

## Uninstall

`claude plugin uninstall prismantis@prismantis`를 사용합니다. Codex에서는 해당 환경에 설치한 파일만 제거합니다.

## Verify

표·코드·다이어그램·수식 출력과 테마 설정이 표시되는지 확인합니다.

## Caveats

**출력 처리 순서 (사용자 관찰):** Show Your Work와 함께 켜는 경우 Claude Code의 `enabledPlugins`에서 Show Your Work를 Prismantis 앞에 배치해 보세요. 후킹 순서에 따른 우회 방법이며, 두 렌더러가 항상 호환된다는 의미는 아닙니다.


### 토큰 비용 재평가 (2026-11-04, 사용자 세션 분석)

사용자 환경에서 턴당 약 500~600토큰의 고정 오버헤드가 관찰되었습니다. 그러나 실제 세션 전체 토큰 소비량에서 차지하는 비중은 약 2%로 분석되어, 출력 가독성 개선 효과를 고려하면 감내 가능한 수준일 수 있다고 판단했습니다. 따라서 **카탈로그 Active 상태를 유지**합니다. 이는 사용자 세션의 측정·평가로, 모든 환경의 일반적인 비용 또는 독립 검증 수치가 아닙니다. 장기 세션의 사용성과 비용은 추후 다시 평가합니다.

### 개인 셋업 메모 (2026-11-03)

2026-11-03 당시에는 개인 Daily Setup에서 비활성화했지만, 2026-11-06 사용자가 현재 사용 중이라고 확인하여 Daily Setup에 다시 포함했습니다. 이전 충돌 사례는 당시의 기록이며, 현재 환경에서도 동일한 문제가 지속된다고 단정하지 않습니다. 사용자 환경에서 Show Your Work와 전역 출력 렌더러가 충돌했고, `next()` 없이 명령 출력 줄을 처리해 후속 렌더러를 막는 현상이 관찰되었습니다. 모든 버전에서 동일하다는 뜻은 아닙니다.

Codex와 Claude Code의 기능은 완전히 동일하지 않습니다. 다른 터미널 렌더러 모드와 동시 사용 시 충돌할 수 있습니다.

### Orca 터미널에서 Mermaid pie 표시 문제 (2026-11-06)

Mermaid pie 차트를 출력할 때 inline image의 base64 문자열이 그대로 표시되는 사례가 있었습니다. Ctrl+L로 화면을 다시 그리면 정상화됩니다. 반복된다면 pie가 포함된 답변이 끝난 뒤 약 1초 지연하여 화면을 다시 그리는 임시 shim을 고려할 수 있습니다. 터미널 핸들 확인과 다른 mod의 훅 실행 보장, 제거 조건은 [Orca 가이드](../workflows/orca.md)를 참고합니다.

## References

- [Upstream](https://github.com/NahumLitvin/prismantis)

### 설정 갱신 (2026-11-06)

현재 사용 중이며 `diagramHints: false`로 설정했습니다. 힌트 주입량 약 630토큰/프롬프트와 주간 비용 약 1%는 개인 환경의 관찰·추정치입니다. 과거 500~600토큰 및 전체 약 2% 분석과는 기준이 다릅니다.
