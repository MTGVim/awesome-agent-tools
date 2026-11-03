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

Jira와 Confluence의 이슈·문서를 표준 MCP 서버를 통해 조회하거나 수정합니다. Atlassian Cloud와 Server/Data Center 구성을 지원합니다.

## Requirements

Atlassian 인스턴스 URL과 API 토큰 또는 PAT, 로컬 stdio MCP 서버 실행 환경이 필요합니다. 인증과 도구 호출은 연결 대상별로 확인해야 합니다.

## Install

원본 README는 `uvx mcp-atlassian` 실행 명령과 MCP 클라이언트별 `command`/`args`/`env` 구성을 제공합니다. 실제 토큰을 저장소에 기록하지 않고 사용 중인 Claude Code·Codex·Hermes의 MCP 등록 인터페이스에 연결합니다.

## Update

패키지 관리자(uvx/pip/Docker)와 설치된 런타임 버전을 확인한 뒤 원본 릴리스 안내에 따라 갱신합니다. 에이전트의 MCP 설정과 사용자 자격증명은 보존합니다.

## Uninstall

MCP 클라이언트에서 `mcp-atlassian` 등록을 제거한 뒤 실제 패키지·컨테이너를 사용하지 않는지 확인합니다. Jira/Confluence API 토큰의 폐기 여부는 별도로 결정합니다.

## Verify

서버 등록, 초기화·도구 목록 조회, 실제 Jira/Confluence 읽기 작업을 차례로 확인합니다.

## Caveats

MCP 연결 성공과 인증 성공은 별개입니다. 도구에 쓰기 권한이 있는 경우 승인 정책을 확인합니다.

## References

- [Upstream](https://github.com/sooperset/mcp-atlassian)
- [Codex MCP documentation](https://developers.openai.com/learn/docs-mcp)
- [Hermes MCP documentation](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp)
