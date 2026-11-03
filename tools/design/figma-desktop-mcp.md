# Figma Desktop MCP

<!-- catalog: {"name": "Figma Desktop MCP", "upstream": "https://developers.figma.com/docs/figma-mcp-server/local-server-installation/", "types": ["mcp"], "agents": ["Claude Code", "Codex", "Hermes"], "category": "design", "verification": "personal", "install_mode": "cli", "last_reviewed": "2026-11-03"} -->

> Figma Desktop의 로컬 MCP 연동. 앱 및 서버 실행 필요

- **Upstream:** https://developers.figma.com/docs/figma-mcp-server/local-server-installation/
- **Types:** mcp
- **Agents:** Claude Code, Codex, Hermes
- **Verification:** personal
- **Install mode:** cli
- **Last reviewed:** 2026-11-03

## Why use it?

Figma 데스크톱 앱의 Dev Mode에서 선택한 디자인의 구조·이미지·컴포넌트 컨텍스트를 로컬 MCP 서버로 제공합니다.

## Requirements

Figma 데스크톱 앱, Dev Mode, 적격 Dev 또는 Full 좌석이 필요합니다. 로컬 서버 주소는 `http://127.0.0.1:3845/mcp`입니다. 이 서버는 캔버스 쓰기를 지원하지 않습니다.

## Install

Figma 데스크톱에서 MCP 서버를 켠 다음 사용 중인 클라이언트에 연결합니다. Claude Code 공식 예시:

```bash
claude mcp add --transport http figma-desktop http://127.0.0.1:3845/mcp
```

Codex는 Settings → MCP servers에서 Streamable HTTP 서버로 등록합니다. Hermes는 현재 MCP CLI 도움말로 등록 방법을 확인합니다.

## Update

Figma 앱 업데이트 후 데스크톱 서버가 실행 중인지 확인하고, 연결 클라이언트의 MCP 설정을 갱신합니다.

## Uninstall

클라이언트에서 `figma-desktop` MCP 등록을 해제한 뒤 Figma 데스크톱 앱의 로컬 서버를 끕니다. Figma 파일은 삭제하지 않습니다.

## Verify

Figma Dev Mode에서 서버를 켜고 클라이언트 MCP 목록에 도구가 나타나는지 확인한 뒤 `get_design_context`를 읽기 전용으로 실행합니다.

## Caveats

원본 공식 문서는 별도 원격 서버를 대부분의 사용자에게 추천합니다. 원격 서버와 데스크톱 서버는 제공 기능과 좌석 요건이 다릅니다.

## References

- [Upstream](https://developers.figma.com/docs/figma-mcp-server/local-server-installation/)
