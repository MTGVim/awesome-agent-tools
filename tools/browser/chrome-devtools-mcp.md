# Chrome DevTools MCP

<!-- catalog: {"name": "Chrome DevTools MCP", "upstream": "https://github.com/ChromeDevTools/chrome-devtools-mcp", "types": ["mcp"], "agents": ["Claude Code", "Codex", "Hermes"], "category": "browser", "verification": "metadata", "install_mode": "agent-guide", "last_reviewed": "2026-11-03"} -->

> Chrome DevTools 기반 브라우저 검증 서버

- **Upstream:** https://github.com/ChromeDevTools/chrome-devtools-mcp
- **Types:** mcp
- **Agents:** Claude Code, Codex, Hermes (MCP protocol compatibility; end-to-end authentication and tool calls not independently tested)
- **Verification:** metadata
- **Install mode:** agent-guide
- **Last reviewed:** 2026-11-03

## Why use it?

Chrome DevTools 기반의 페이지 검사·성능 분석·브라우저 자동화 기능을 MCP 클라이언트에 연결합니다. 세 에이전트 모두 표준 MCP 서버와 통신할 수 있지만, 각 환경의 브라우저 연결 및 기능 검증은 별도로 필요합니다.

## Requirements

원본 README의 OS·에이전트 버전·권한·터미널 호환성 조건을 확인해야 합니다.

## Install

공식 저장소의 최신 설치 안내를 확인하고, 기존 설치와 충돌 여부를 점검한 뒤 승인받아 설치합니다.

## Update

기존 설치 방식과 변경 이력을 확인한 다음 원본 저장소에서 권장하는 업데이트 절차를 적용합니다.

## Uninstall

설치 이력을 확인해 해당 도구가 추가한 파일·등록만 제거합니다. 공유 설정과 다른 도구는 보존합니다.

## Verify

MCP 서버 등록 여부, 도구 검색, 실제 Chrome 페이지 연결과 읽기 전용 검사 동작을 순서대로 확인합니다. 브라우저 실행 환경과 보안 제약을 점검합니다.

## Caveats

MCP 프로토콜을 지원한다는 사실은 이 도구가 세 에이전트에서 모두 실제 검증됐다는 의미가 아닙니다. 연결 시 실행 권한·계정 권한·토큰 보관·서버가 제공하는 도구 범위를 점검하고, 사전 승인 없이 원격 스크립트나 전역 설정 변경을 실행하지 않습니다.

## References

- [Upstream](https://github.com/ChromeDevTools/chrome-devtools-mcp)
