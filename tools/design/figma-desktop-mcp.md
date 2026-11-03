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

Figma Desktop의 로컬 MCP 연동. 앱 및 서버 실행 필요 초기 큐레이션은 개인적인 사용 경험과 관심을 바탕으로 하며, 독립적인 성능 검증을 뜻하지는 않습니다.

## Requirements

원본 README의 OS·에이전트 버전·권한·터미널 호환성 조건을 확인해야 합니다.

## Install

Figma Desktop에서 로컬 MCP 서버를 켠 뒤 아래 중 사용하는 에이전트의 명령만 실행합니다.

```sh
claude mcp add --scope user --transport http figma-desktop http://127.0.0.1:3845/mcp
codex mcp add figma-desktop --url http://127.0.0.1:3845/mcp
```

Hermes의 현재 MCP 등록 방식은 공식 문서를 확인한 뒤 적용합니다.

## Update

기존 설치 방식과 변경 이력을 확인한 다음 원본 저장소에서 권장하는 업데이트 절차를 적용합니다.

## Uninstall

설치 이력을 확인해 해당 도구가 추가한 파일·등록만 제거합니다. 공유 설정과 다른 도구는 보존합니다.

## Verify

Figma Desktop 서버를 실행한 상태에서 각 에이전트의 MCP 목록 및 연결을 확인합니다.

## Caveats

검증 상태가 `personal`이 아닌 경우, 메타데이터 확인과 실제 설치·기능 테스트를 구분해야 합니다. 사전 승인 없이 원격 스크립트를 실행하거나 전역 설정을 수정하지 않습니다.

## References

- [Upstream](https://developers.figma.com/docs/figma-mcp-server/local-server-installation/)
