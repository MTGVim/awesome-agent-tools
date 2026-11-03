# Inbox

<!-- catalog: {"name": "Inbox", "upstream": "https://github.com/petekp/inbox", "types": ["plugin"], "agents": ["Claude Code","Codex"], "category": "workflows", "verification": "personal", "install_mode": "agent-guide", "last_reviewed": "2026-11-03"} -->

> 질문 및 확인 요청을 패널에 수집

- **Upstream:** https://github.com/petekp/inbox
- **Types:** plugin
- **Agents:** Claude Code, Codex
- **Verification:** personal
- **Install mode:** agent-guide
- **Last reviewed:** 2026-11-03

## Why use it?

에이전트가 답변을 기다리는 질문과 결정·발견 사항을 정리해 사용자에게 선택지를 보여줍니다. Claude Code와 Codex에 별도 구현이 있습니다.

## Requirements

Codex용 구현은 Claude Code 플러그인 설치 명령과 다릅니다. 각 플랫폼별 설치 섹션을 읽어야 합니다.

## Install

Claude Code는 원본 문서에서 다음 설치 명령을 안내합니다.

```text
/plugin install inbox --marketplace petekp/inbox
```

Codex에서는 같은 명령을 사용하지 않으며, 원본 README의 `Install → Codex` 절차를 따릅니다.

## Update

기존 설치 방식과 변경 이력을 확인한 다음 원본 저장소에서 권장하는 업데이트 절차를 적용합니다.

## Uninstall

설치 이력을 확인해 해당 도구가 추가한 파일·등록만 제거합니다. 공유 설정과 다른 도구는 보존합니다.

## Verify

설치 목록 또는 명령 도움말을 확인하고, 핵심 기능을 최소 한 번 실행해 봅니다.

## Caveats

Codex용 구현은 Claude Code 플러그인 설치 명령과 다릅니다. 각 플랫폼별 설치 섹션을 읽어야 합니다.

설치 안내를 확인한 것이지 실제 사용자 환경에서 작동을 검증했다는 뜻은 아닙니다.

## References

- [Upstream](https://github.com/petekp/inbox)

## Archived decision

- **Archived on:** 2026-11-03
- **Previous state:** Active
- **Reason:** `superseded`
- **Curator observation:** Orca의 ask 마크와 기존 질문 처리 도구가 현재 워크플로에 더 자연스럽습니다.
- **Scope:** This is a curator-specific judgment, not a universal claim that upstream is broken.
