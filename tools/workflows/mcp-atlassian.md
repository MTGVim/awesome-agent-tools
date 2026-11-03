# MCP Atlassian

<!-- catalog: {"name": "MCP Atlassian", "upstream": "https://github.com/sooperset/mcp-atlassian", "types": ["mcp"], "agents": ["Claude Code", "Codex", "Hermes"], "category": "workflows", "verification": "unverified", "install_mode": "agent-guide", "last_reviewed": "2026-11-03"} -->

> Atlassian 서비스 연동 MCP

- **Upstream:** https://github.com/sooperset/mcp-atlassian
- **Types:** mcp
- **Agents:** Claude Code, Codex, Hermes (MCP protocol compatibility; end-to-end authentication and tool calls not independently tested)
- **Verification:** unverified
- **Install mode:** agent-guide
- **Last reviewed:** 2026-11-03

## Why use it?

Jira 이슈와 Confluence 문서에 접근할 수 있는 MCP 도구를 제공합니다. 세 에이전트 모두 MCP 클라이언트로 연결할 수 있지만, 조직별 Atlassian Cloud/Server 인증과 권한 설정은 별도로 확인해야 합니다.

## Requirements

- 원본 저장소의 `uvx` 또는 Docker 설치 방식을 확인합니다.
- Jira/Confluence URL, API 토큰 또는 PAT 및 계정 권한이 필요합니다.
- Claude Code, Codex, Hermes에서 로컬 stdio MCP 서버 연결을 지원합니다. 각각의 실제 등록 방법과 환경 변수 전달 구문은 사용 중인 CLI의 현재 도움말을 확인해야 합니다.
- 개인 토큰을 Git 저장소나 공유 문서에 직접 기록하지 않습니다.

## Install

공식 저장소의 최신 설치 안내를 확인하고, 기존 설치와 충돌 여부를 점검한 뒤 승인받아 설치합니다.

## Update

기존 설치 방식과 변경 이력을 확인한 다음 원본 저장소에서 권장하는 업데이트 절차를 적용합니다.

## Uninstall

설치 이력을 확인해 해당 도구가 추가한 파일·등록만 제거합니다. 공유 설정과 다른 도구는 보존합니다.

## Verify

1. 각 에이전트의 MCP 목록에서 서버가 등록되어 있는지 확인합니다.
2. MCP 도구 검색 및 초기화가 성공하는지 확인합니다.
3. 실제 Jira/Confluence에서 접근 권한이 있는 읽기 작업 하나를 실행합니다. 등록 성공과 인증·권한·기능 검증을 구분합니다.

## Caveats

MCP 프로토콜을 지원한다는 사실은 이 도구가 세 에이전트에서 모두 실제 검증됐다는 의미가 아닙니다. 연결 시 실행 권한·계정 권한·토큰 보관·서버가 제공하는 도구 범위를 점검하고, 사전 승인 없이 원격 스크립트나 전역 설정 변경을 실행하지 않습니다.

## References

- [Upstream](https://github.com/sooperset/mcp-atlassian)
- [Codex MCP documentation](https://developers.openai.com/learn/docs-mcp)
- [Hermes MCP documentation](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp)
