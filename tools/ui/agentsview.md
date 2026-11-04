# AgentsView

<!-- catalog: {"name": "AgentsView", "upstream": "https://github.com/kenn-io/agentsview", "types": ["app", "cli"], "agents": ["Standalone app", "Standalone CLI"], "category": "ui", "verification": "metadata", "install_mode": "agent-guide", "last_reviewed": "2026-11-04"} -->

> 로컬 에이전트 세션 탐색, 토큰·비용 분석 및 도구 사용 인사이트

- **Upstream:** https://github.com/kenn-io/agentsview
- **Types:** standalone app/CLI
- **Agents:** Standalone app, Standalone CLI (Claude Code, Codex 등 세션 데이터 분석)
- **Verification:** metadata
- **Install mode:** agent-guide
- **Last reviewed:** 2026-11-04

## Why use it?

Claude Code, Codex 등 여러 코딩 에이전트의 세션을 한곳에서 검색하고, 모델별·세션별 토큰 소비량과 추정 비용, 도구 호출·실패·재시도 패턴을 분석합니다. 특정 플러그인의 고정 오버헤드나 반복적인 도구 호출을 조사할 때 근거 자료로 활용할 수 있습니다. MCP 읽기 도구도 제공하지만, 에이전트에 연결할지는 별도로 선택합니다.

## Requirements

상류 문서에 따르면 macOS, Linux용 CLI와 macOS·Windows 데스크톱 앱, Windows 설치 스크립트 및 Docker 배포를 지원합니다. 세션을 읽으려면 해당 에이전트의 로컬 세션 데이터에 접근할 수 있어야 합니다.

## Install

상류 공식 문서의 설치 절차를 확인한 후 선택한 배포 방식으로 설치합니다. macOS에서는 Homebrew cask `brew install --cask agentsview`를 사용할 수 있으며, CLI 설치와 Docker 방식도 제공합니다. 원격 설치 스크립트는 실행 전에 내용을 검토합니다.

## Update

[공식 릴리스](https://github.com/kenn-io/agentsview/releases)와 [변경 기록](https://agentsview.io/docs/changelog/)을 확인하고 선택한 설치 방식의 업데이트 절차를 따릅니다.

## Uninstall

설치 방식에 맞춰 앱 또는 CLI를 제거합니다. 로컬 SQLite 세션 아카이브 및 설정을 보존할지 별도로 결정하고, 다른 에이전트의 원본 세션 폴더는 삭제하지 않습니다.

## Verify

`agentsview session list`, `agentsview report usage daily`, `agentsview report stats` 및 웹 UI에서 실제 세션·토큰 통계가 표시되는지 확인합니다. 비용 수치는 모델 가격 및 로그 정보에 따른 추정치이며, 모델별 누락 데이터가 있을 수 있습니다.

## Caveats

- 기본 세션 아카이브는 로컬 SQLite에 저장되지만, Claude.ai/클라우드 채팅 동기화, 원격 저장소·내보내기, 선택적 시맨틱 검색/임베딩 등은 설정에 따라 외부 데이터 전송이 발생할 수 있습니다. 사용 전에 각 기능의 전송 범위와 자격 증명을 검토합니다.
- 웹 UI를 localhost 외부에 노출할 경우 인증을 활성화하고 원격 접근 설정을 검토합니다.
- 기본 세션 수집과 일부 CLI 명령은 백그라운드 데몬·파일 감시를 시작할 수 있으므로, 일회성 조회만 원할 때 동작 방식을 확인합니다.
- 세션을 분석하는 독립 도구이며 코딩 에이전트의 실행 토큰 사용량을 직접 줄여 주는 기능으로 이해해서는 안 됩니다.

## References

- [Upstream README](https://github.com/kenn-io/agentsview)
- [Documentation](https://agentsview.io/docs/)
- [Configuration](https://agentsview.io/docs/configuration/)
