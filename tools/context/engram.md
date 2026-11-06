# Engram

<!-- catalog: {"name": "Engram", "upstream": "https://github.com/Gentleman-Programming/engram", "types": ["tool", "mcp"], "agents": ["Claude Code", "Codex"], "category": "context", "verification": "personal", "install_mode": "agent-guide", "last_reviewed": "2026-11-07"} -->

> 코딩 에이전트가 세션을 넘어 프로젝트 결정과 작업 중 얻은 지식을 저장하고 검색하는 로컬 메모리 도구입니다.

- **Upstream:** https://github.com/Gentleman-Programming/engram
- **Types:** tool, mcp
- **Agents:** Claude Code, Codex
- **Verification:** personal (Claude Code에서 이전 사용 기록 확인)
- **Install mode:** agent-guide
- **Last reviewed:** 2026-11-07

## Why use it?

현재 작업 중인 에이전트가 보존할 결정과 해결책을 골라 저장합니다. Engram은 SQLite FTS5로 검색하며, 별도 임베딩이나 요약 모델 없이 기본 저장과 검색을 수행합니다. 에이전트가 관련 검색어를 여러 개 골랐다면 `mem_search`에 `match_mode: "any"`를 지정해 한 단어라도 포함한 메모를 찾을 수 있습니다.

## Requirements

- Engram 바이너리가 필요합니다. [설치 문서](https://github.com/Gentleman-Programming/engram/blob/main/docs/INSTALLATION.md)에서 운영체제별 배포 방식을 확인합니다.
- Claude Code 전체 플러그인 설정에는 `jq`와 `curl`이 필요합니다. Claude Code와 Codex는 공식 설정 경로가 있습니다. Hermes는 [stdio MCP 등록](https://hermes-agent.nousresearch.com/docs/reference/mcp-config-reference)으로 연결할 수 있는 구성이나, Engram 전용 설정과 실제 호출은 확인하지 않았습니다.
- 로컬 데이터는 기본적으로 프로젝트 저장소 밖의 `~/.engram/engram.db`에 저장합니다. `ENGRAM_DATA_DIR`로 디렉터리를 지정할 수 있습니다.

## Install

- Homebrew를 쓰는 환경에서는 `brew install gentleman-programming/tap/engram`으로 바이너리를 설치합니다.
- 공식 전체 설정은 Claude Code의 `engram setup claude-code`, Codex의 `engram setup codex`입니다. 기존 등록과 훅을 먼저 확인하고 설정 후 에이전트를 재시작합니다.
- Claude Code에서 지연을 비교하려면 Engram 플러그인 훅을 비활성화하고, 기존 stdio MCP 등록을 확인합니다. 등록이 없으면 [공식 Bare MCP 절차](https://github.com/Gentleman-Programming/engram/blob/main/docs/AGENT-SETUP.md#claude-code)에 따라 `claude mcp add --transport stdio --scope user engram -- <absolute-engram-path> mcp --tools=agent`로 등록합니다. 이 구성에서는 플러그인의 자동 세션 관리와 컨텍스트 복구가 빠집니다.

## Update

[릴리스 노트](https://github.com/Gentleman-Programming/engram/releases/latest)를 먼저 확인합니다. Homebrew 설치본은 `brew update && brew upgrade engram`으로 갱신합니다. Claude Code에서 바이너리를 갱신해도 플러그인 훅은 별도로 갱신해야 합니다. 전체 통합을 사용한다면 `engram setup claude-code`로 사용자 범위 플러그인을 갱신한 뒤 Claude Code를 재시작합니다. 별도로 실행 중인 서버는 [업데이트 후 절차](https://github.com/Gentleman-Programming/engram/blob/main/docs/INSTALLATION.md#after-upgrading)를 따릅니다.

## Uninstall

데이터를 보존해야 하면 먼저 백업합니다. 설치할 때 추가한 에이전트 설정과 플러그인만 제거합니다. Claude Code의 사용자 범위 MCP 등록은 `claude mcp remove engram --scope user`로 제거할 수 있습니다. 바이너리는 기존 설치 방식에 따라 제거하고, 메모리 DB는 별도로 관리합니다.

## Verify

`engram version`으로 바이너리를 확인하고, 새 에이전트 세션에서 Engram MCP 연결과 도구 노출을 확인합니다. 프로젝트를 확인한 뒤 테스트 메모를 저장하고 다음 세션에서 다시 검색해 연결과 기능을 구분해 검증합니다. 훅 지연을 확인할 때는 같은 프롬프트로 전체 통합과 Bare MCP의 첫 응답을 비교합니다.

## Caveats

### 개인 사용 기록

- **2026-11-06 보관:** 개인 환경의 7일 기록에서 첫 프롬프트 훅이 10초 제한에 걸린 사례가 243건 있었습니다. 긴 프롬프트를 처리하는 Bash 훅을 로컬에서 수정한 뒤 해당 측정은 약 0.06초로 줄었습니다. 당시에는 훅과 상주 서비스의 관리 부담 때문에 보관했습니다. 한국어, 누적 데이터량, 최신 배포판에서의 재현 여부는 확인되지 않았습니다.
- **2026-11-07 복원:** 현재 에이전트가 메모를 직접 고르고 여러 키워드를 한 번에 검색하는 기존 흐름을 유지하기 위해 다시 사용하기로 했습니다. 지연이 재발하면 Bare MCP로 분리해 비교합니다. 재활성화 후 지연은 아직 측정하지 않았습니다.

## Privacy & Updates

2026-11-07 상류 문서와 버전 확인 코드를 검토했습니다. 사용 통계 전송 정책은 미확인입니다. 기본 저장은 로컬입니다. 선택형 Cloud Autosync는 활성화한 경우 설정한 Engram Cloud 서버와 메모리 변경분을 동기화합니다. `ENGRAM_CLOUD_AUTOSYNC`를 설정하지 않거나 `1` 이외의 값으로 두면 비활성입니다. Git 동기화 역시 별도 기능이므로 저장소에 내보내는 데이터 범위를 확인합니다.

일부 CLI 명령과 TUI는 GitHub Releases API에 버전 확인 요청을 보냅니다. `ENGRAM_NO_UPDATE_CHECK=1`로 끌 수 있습니다. 이 버전 확인은 설치 파일을 교체하지 않습니다. Claude Code 통합의 사용자 범위 플러그인 갱신은 위 설정 명령을 다시 실행할 때 수행됩니다. [상류 환경 변수 문서](https://github.com/Gentleman-Programming/engram/blob/main/DOCS.md#environment-variables)

## References

- [Engram README](https://github.com/Gentleman-Programming/engram)
- [Agent Setup](https://github.com/Gentleman-Programming/engram/blob/main/docs/AGENT-SETUP.md)
- [Claude Code 플러그인과 훅](https://github.com/Gentleman-Programming/engram/blob/main/docs/PLUGINS.md)
- [Git·Cloud 동기화](https://github.com/Gentleman-Programming/engram/blob/main/docs/codebase/sync-and-cloud.md)
