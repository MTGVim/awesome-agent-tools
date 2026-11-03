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

Chrome 브라우저의 개발자 도구 기능을 MCP 서버와 CLI로 제공해 네트워크 오류, 콘솔, 성능 트레이스 및 페이지 동작을 조사합니다.

## Requirements

원본은 Chrome/Chrome for Testing을 공식 지원합니다. 다른 Chromium 브라우저와 개인정보가 노출되는 세션은 주의가 필요합니다.

## Install

원본 README에서 MCP 클라이언트 구성 및 Claude Code 마켓플레이스 플러그인을 안내합니다.

```text
/plugin marketplace add ChromeDevTools/chrome-devtools-mcp
/plugin install chrome-devtools-mcp@chrome-devtools-plugins
```

다른 에이전트에서는 해당 클라이언트의 MCP 등록 문서를 사용합니다.

## Update

npm MCP 서버와 Claude Code 플러그인의 설치 경로를 구분해 갱신합니다. 기존 브라우저 연결 설정을 보존합니다.

## Uninstall

등록한 MCP 서버/플러그인만 제거하며 Chrome 브라우저와 사용자 프로필은 삭제하지 않습니다.

## Verify

MCP 도구 검색 후 읽기 전용 콘솔·네트워크 검사, 선택적 트레이스 기록을 실제 브라우저에서 확인합니다.

## Caveats

### 텔레메트리와 네트워크 (2026-11-04 문서 확인)

사용 통계 전송은 기본 활성입니다. `--no-usage-statistics` 또는 `CHROME_DEVTOOLS_MCP_NO_USAGE_STATISTICS=1`로 끄며, 별도 버전 확인은 `CHROME_DEVTOOLS_MCP_NO_UPDATE_CHECKS=1`로 중단합니다. 실제 패키지 자동 갱신은 호스트·설치 방식에 따라 달라집니다. [Upstream README](https://github.com/ChromeDevTools/chrome-devtools-mcp)

상태 비교: [Privacy, Telemetry & Updates](../../docs/privacy-and-updates.md). 실제 설치된 버전의 설정을 다시 확인합니다.

브라우저 데이터가 MCP 클라이언트에 전달됩니다. 성능 기능이 CrUX API를 조회할 수 있으므로 필요 시 `--no-performance-crux`를 검토합니다.

## References

- [Upstream](https://github.com/ChromeDevTools/chrome-devtools-mcp)
