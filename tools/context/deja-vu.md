# Déjà Vu

<!-- catalog: {"name": "Déjà Vu", "upstream": "https://github.com/vshulcz/deja-vu", "types": ["tool", "mcp"], "agents": ["Claude Code", "Codex", "Hermes"], "category": "context", "verification": "trial", "install_mode": "agent-guide", "last_reviewed": "2026-11-24"} -->

> 로컬 코딩 에이전트 기록의 검색·복구·에이전트 간 인계를 지원하는 세션 메모리 도구

- **Upstream:** https://github.com/vshulcz/deja-vu
- **Types:** tool, mcp
- **Agents:** Claude Code, Codex, Hermes 등 (상류 문서의 통합 대상 기준; 실제 동작은 호스트별로 검증 필요)
- **Verification:** trial (사용자가 시험 사용 중, 장기 안정성은 미확인)
- **Install mode:** agent-guide
- **Last reviewed:** 2026-11-24

## Why use it?

기존 Claude Code·Codex·Hermes 등 코딩 에이전트의 로컬 세션 기록을 색인하고 키워드로 검색합니다. 별도 LLM이나 원격 추론 없이 검색하고, `deja handoff`로 다른 에이전트에 작업을 넘기거나 `deja restore`로 로그에 남은 편집 내용을 복구할 수 있습니다. 압축 후 한정된 복구 컨텍스트 주입과 MCP·훅 연동도 지원합니다.

Engram 대신 사용을 시험 중입니다. Engram 사용 중 매 세션 컨텍스트 주입량과 자동 업데이트 후 안정성에 불편을 느꼈다는 개인 경험이 교체 계기이며, Déjà Vu가 장기적으로 이 문제를 해결한다고 검증한 것은 아닙니다.

## Requirements

Go 기반 독립 실행 파일. macOS·Linux와 Windows 배포를 제공합니다. 지원되는 에이전트의 로컬 대화 기록과 설정 파일에 접근할 권한이 필요합니다. 설치 통합 방식에 따라 훅·MCP 등록·전역 지침 파일이 수정될 수 있습니다.

## Install

상류에서 안내하는 간편 설치:

```sh
npx @vshulcz/deja-vu install --auto
```

이 명령은 감지된 에이전트에 통합을 설정하므로, **기존 MCP·훅·AGENTS.md/CLAUDE.md 및 전역 지침을 먼저 확인하고 승인한 뒤** 실행합니다. 바이너리만 쓰는 경우 상류의 Homebrew `brew install deja-vu`, Windows Scoop/winget, 릴리스 패키지를 확인하세요. `deja install --all --no-guidance`는 지침 주입을 제외하고 MCP를 설정하는 선택지입니다. `deja install --all`은 session-start 훅 없이 MCP 연동을 구성한다고 안내합니다.

## Update

설치 채널에 맞게 갱신하며, 수동 갱신 전 릴리스와 기존 훅/MCP 구성을 비교합니다. `deja update`는 명시적으로 실행하는 업데이트 명령입니다. 일반적인 버전 확인과 바이너리 교체를 혼동하지 않습니다.

## Uninstall

상류 설치 가이드에서 에이전트별 등록 해제 및 배포 채널별 제거법을 확인합니다. 통합을 해제하더라도 `~/.cache/deja`의 로컬 인덱스와 수동 내보낸 `.deja/memory.jsonl`은 따로 확인하고, 검토 없이 삭제하지 않습니다.

## Verify

`deja doctor`로 통합 상태를 확인한 뒤, 기존 세션 검색 `deja "검색어"`와 압축 복구 컨텍스트 크기, 훅 추가 지연, 업데이트 후 MCP·훅 상태를 직접 비교합니다. 시험 사용 중인 도구이므로 개인 환경 장기 안정성은 아직 검증되지 않았습니다.

## Caveats

기본 기록 검색은 별도 LLM 호출이 없지만, 자동 컨텍스트 복구 훅을 사용하면 세션에 텍스트가 주입될 수 있습니다. 기존 기록 인덱스는 비밀 정보 패턴을 가리지만 보안 감사가 완료된 것으로 간주해서는 안 됩니다. `deja repo add`는 승인한 메모를 저장소의 `.deja/memory.jsonl`로 내보내므로 커밋 여부를 직접 통제해야 합니다.

## Privacy & Updates

2026-11-24 상류 README 확인. 기본 인덱싱·검색은 로컬에서 수행합니다. 원격 요청은 `deja update`, SSH 동기화, `deja doctor`의 버전 확인, 명시한 임베딩 엔드포인트 및 일일 릴리스 확인 등에 발생할 수 있습니다. `DEJA_OFFLINE=1` 또는 `DEJA_NO_UPDATE_NOTICE=1`로 일일 릴리스 확인을 비활성화할 수 있다고 안내합니다(두 옵션의 범위는 상류 문서 확인). 전체 코드 감사·네트워크 패킷 검증은 수행하지 않았습니다.

## References

- [README 및 설치 안내](https://github.com/vshulcz/deja-vu)
- [아키텍처](https://github.com/vshulcz/deja-vu/blob/main/docs/ARCHITECTURE.md)
- [보안 모델](https://github.com/vshulcz/deja-vu/blob/main/docs/SECURITY-MODEL.md)
