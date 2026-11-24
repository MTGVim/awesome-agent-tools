# agent-top

<!-- catalog: {"name": "agent-top", "upstream": "https://github.com/kannandreams/agent-top", "types": ["tool"], "agents": [], "category": "utilities", "verification": "metadata", "install_mode": "cli", "last_reviewed": "2026-11-24"} -->

> 코딩 에이전트 세션·프로세스·MCP 서버·토큰 비용을 함께 보는 로컬 터미널 대시보드

- **Upstream:** https://github.com/kannandreams/agent-top
- **Types:** tool (독립 CLI)
- **Agents:** 독립 CLI. Claude Code, Codex, Gemini CLI, OpenCode, Kodelet 세션 감지
- **Verification:** metadata (상류 문서 확인, 사용자 환경에서 실행 검증하지 않음)
- **Install mode:** cli
- **Last reviewed:** 2026-11-24

## Why use it?

여러 코딩 에이전트의 로컬 세션 기록과 OS 프로세스 표를 읽어 실행·대기 상태, 토큰·추정 비용, 프로세스 트리와 MCP 서버를 표시합니다. 세션별 도구 지연·실패, 고아 MCP 서버, 캐시 비용을 점검할 수 있고 `agent-top report`로 기간별 비용도 집계합니다. 별도 LLM을 호출해 제목이나 요약을 생성하는 방식이 아니라 기존 기록에서 계산합니다.

## Requirements

macOS 및 Linux의 터미널에서 사용할 수 있는 Rust 기반 CLI입니다. 설치 방식에 따라 Homebrew 또는 Rust Cargo/binstall이 필요합니다. Windows 지원·배포 방식은 현 버전 원본 문서에서 재확인하세요. 실행 대상 에이전트의 로컬 transcript와 프로세스 정보를 읽을 수 있어야 합니다. Hermes 세션 감지는 상류 지원 목록에 없습니다.

## Install

상류 README에 명시된 macOS/Linux Homebrew 설치:

```bash
brew install kannandreams/tap/agent-top
agent-top
```

다른 설치 경로로 `cargo binstall agent-top`을 안내합니다. 실행·설치 전 환경에 맞는 배포 경로를 확인하세요.

## Update

Homebrew 설치라면 `brew upgrade agent-top`으로 갱신합니다. 다른 설치 방식은 해당 패키지 관리자의 갱신 절차를 확인합니다.

## Uninstall

Homebrew 설치라면 `brew uninstall agent-top`으로 제거합니다. `agent-top sync` 실행으로 만들어진 로컬 SQLite 데이터는 별도 확인 후 정리해야 할 수 있습니다.

## Verify

실제 Claude Code나 Codex 세션 실행 중 `agent-top` 또는 `agent-top --once`로 세션·비용·프로세스가 표시되는지 확인합니다. 비용은 기록된 토큰과 가격표 기반 추정치이므로 청구액과 다를 수 있습니다.

## Privacy & Updates

2026-11-24 상류 README 확인: 기본 모니터링은 로컬 파일 및 프로세스 정보를 읽고 별도 모델 호출이나 서버 상주를 요구하지 않는다고 안내합니다. 다만 **하루 한 번 업데이트 확인 네트워크 요청**이 기본이며 `AGENT_TOP_NO_UPDATE_CHECK=1`로 끌 수 있습니다. `agent-top trace --endpoint <url>`은 사용자가 명시한 서버로 OTLP 추적 정보를 전송합니다. `sync`는 세션 통계를 로컬 SQLite에 저장하며, `ui`는 로컬 웹 대시보드를 엽니다. 소스 전체 감사·패킷 검증은 수행하지 않았습니다.

## Caveats

기본 사용은 읽기 전용이지만, `sync`·내보내기는 로컬 데이터를 생성하고 `trace --endpoint`는 명시한 목적지에 전송합니다. 모니터링 범위는 지원하는 에이전트 및 남아 있는 기록에 한정됩니다. btop은 시스템 전반의 자원 모니터로 역할이 다르며, agent-top은 세션·도구·MCP·비용 분석에 초점을 둡니다.

## References

- [Upstream README](https://github.com/kannandreams/agent-top)
- [Official docs](https://agenttop.dev/)
