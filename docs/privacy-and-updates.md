# Privacy, Telemetry & Updates

[한국어 README](../README.md) · [English README](../README.en.md)

> **조사 범위:** 활성 카탈로그 40개(2026-11-07 기준)의 상류 README와 공개 개인정보 처리 안내를 확인했습니다. 기존 항목은 2026-11-04에, Savvy Progress 항목은 2026-11-05에 확인했습니다. 2026-11-06 Claude Flightdeck을 개인 설정에서 Savvy Progress로 대체하여 아카이브했습니다. Engram은 2026-11-07 복원 시 확인했습니다. 일부 도구는 README 수준에서만 확인했으며, **소스 코드 전체 감사나 실제 네트워크 패킷 검증은 수행하지 않았습니다.** `미확인`은 기능이 없다는 뜻이 아닙니다.

**구분:** 텔레메트리(사용 통계), 버전 확인(업데이트 존재 여부 조회), 자동 업데이트(코드 설치·교체), 정상적인 API/MCP·클라우드 통신은 서로 다릅니다. 상류 문서의 기본값과 해제 방법만 사실로 표기합니다. 일반 에이전트·패키지 매니저가 별도로 만드는 네트워크 요청은 포함하지 않습니다.

| 도구 | 텔레메트리 | 업데이트·버전 확인 | 근거·해제 방법 |
|---|---|---|---|
| [Engram](../tools/context/engram.md) | 사용 통계 미확인. 로컬 저장이 기본이며 Cloud Autosync는 선택 | 일부 CLI 명령·TUI에서 GitHub Releases API 확인. 자체 설치 갱신과 구분 | 버전 확인은 `ENGRAM_NO_UPDATE_CHECK=1`로 끔. `ENGRAM_CLOUD_AUTOSYNC`는 `1`일 때만 활성화하며 설정한 서버와 동기화 · [원본](https://github.com/Gentleman-Programming/engram/blob/main/DOCS.md#environment-variables) |
| [Context Mode](../tools/context/context-mode.md) | 로컬 처리 설명, 세부 미확인 | 미확인 | Gateway는 별도 호스팅 서비스 · [원본](https://github.com/mksglu/context-mode) |
| [RTK](../tools/context/rtk.md) | 미확인 | 미확인 | 텔레메트리·자동 갱신 정책 미확인 · [원본](https://github.com/rtk-ai/rtk) |
| [TigerKit](../tools/workflows/tigerkit.md) | 미확인 | 미확인 | 상류 README에서 명시적 정책을 확인하지 못함. 설치 전에 원본 설정·코드·네트워크 동작 재확인 필요 · [원본](https://github.com/MTGVim/tiger-kit) |
| [Orca](../tools/workflows/orca.md) | 사용 통계 전송 | 기본 자동 업데이트(플랫폼별 차이) | PostHog Cloud로 익명 사용 이벤트 전송. 공식 개인정보 문서에 초기값 미명시. 1.4.148 Windows 환경에서 초기 활성화 사용자 보고가 있으나 버전 전체에 일반화할 수 없음. `Settings → Privacy`, `DO_NOT_TRACK=1`, `ORCA_TELEMETRY_DISABLED=1`로 끌 수 있음. 자동 업데이트는 공식 설치 문서 참고 · [원본](https://www.onorca.dev/docs/telemetry) |
| [Skill Creator](../tools/workflows/skill-creator.md) | 미확인 | 미확인 | 상류 README에서 명시적 정책을 확인하지 못함. 설치 전에 원본 설정·코드·네트워크 동작 재확인 필요 · [원본](https://github.com/openai/skills) |
| [Subagent Tuner](../tools/workflows/subagent-tuner.md) | 미확인 | 미확인 | 상류 README에서 명시적 정책을 확인하지 못함. 설치 전에 원본 설정·코드·네트워크 동작 재확인 필요 · [원본](https://github.com/Kruhlikau/subagent-tuner) |
| [Autoharness Codex](../tools/workflows/autoharness-codex.md) | 미확인 | 미확인 | 상류 README에서 명시적 정책을 확인하지 못함. 설치 전에 원본 설정·코드·네트워크 동작 재확인 필요 · [원본](https://github.com/arm092/autoharness-codex) |
| [Darwin Skill](../tools/workflows/darwin-skill.md) | 미확인 | 미확인 | 상류 README에서 명시적 정책을 확인하지 못함. 설치 전에 원본 설정·코드·네트워크 동작 재확인 필요 · [원본](https://github.com/alchaincyf/darwin-skill) |
| [MCP Atlassian](../tools/workflows/mcp-atlassian.md) | 미확인 | 미확인 | 상류 README에서 명시적 정책을 확인하지 못함. 설치 전에 원본 설정·코드·네트워크 동작 재확인 필요 · [원본](https://github.com/sooperset/mcp-atlassian) |
| [Next Steps](../tools/workflows/next-steps.md) | 미확인 | 미확인 | 상류 README에서 명시적 정책을 확인하지 못함. 설치 전에 원본 설정·코드·네트워크 동작 재확인 필요 · [원본](https://github.com/anthropics/claude-plugins-community) |
| [Skill Seekers](../tools/workflows/skill-seekers.md) | 미확인 | 미확인 | 상류 README에서 명시적 정책을 확인하지 못함. 설치 전에 원본 설정·코드·네트워크 동작 재확인 필요 · [원본](https://github.com/yusufkaraaslan/Skill_Seekers) |
| [Code Modernization](../tools/coding/code-modernization.md) | 미확인 | 미확인 | 상류 README에서 명시적 정책을 확인하지 못함. 설치 전에 원본 설정·코드·네트워크 동작 재확인 필요 · [원본](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/code-modernization) |
| [Codegraph](../tools/coding/codegraph.md) | 기본 활성 | 버전 확인 | 익명 명령·언어 통계. `codegraph telemetry off` 또는 `CODEGRAPH_TELEMETRY=0`/`DO_NOT_TRACK=1`. 버전 확인은 `CODEGRAPH_NO_UPDATE_CHECK=1` · [원본](https://github.com/colbymchenry/codegraph/blob/main/TELEMETRY.md) |
| [Ponytail](../tools/coding/ponytail.md) | 미확인 | 미확인 | 상류 README에서 명시적 정책을 확인하지 못함. 설치 전에 원본 설정·코드·네트워크 동작 재확인 필요 · [원본](https://github.com/dietrichgebert/ponytail) |
| [Agent Usage Guard](../tools/context/agent-usage-guard.md) | 네트워크 요청 없음 명시 | 미확인 | 원본 README 기준 자체 네트워크 요청·추가 프로세스 없음 · [원본](https://github.com/rbartoli/agent-usage-guard) |
| [Cache Tax](../tools/context/cache-tax.md) | 미확인 | 미확인 | 상류 README에서 명시적 정책을 확인하지 못함. 설치 전에 원본 설정·코드·네트워크 동작 재확인 필요 · [원본](https://github.com/karanb192/cache-tax) |
| [Chrome DevTools MCP](../tools/browser/chrome-devtools-mcp.md) | 기본 활성 | 버전 확인 | `--no-usage-statistics` 또는 `CHROME_DEVTOOLS_MCP_NO_USAGE_STATISTICS=1`; 업데이트 확인은 `CHROME_DEVTOOLS_MCP_NO_UPDATE_CHECKS=1` · [원본](https://github.com/ChromeDevTools/chrome-devtools-mcp#usage-statistics) |
| [Claude Show Your Work](../tools/browser/claude-show-your-work.md) | 선택적 공유 | 자체 버전 확인·업데이트 | PostHog로 익명 사용량 공유(설정 선택). `SHOW_YOUR_WORK_TELEMETRY=0`/`DO_NOT_TRACK=1`; `SHOW_YOUR_WORK_AUTO_UPDATE=0`으로 자체 버전 확인 끔 · [원본](https://github.com/iamumeransari/claude-show-your-work/blob/main/PRIVACY.md) |
| [Cua](../tools/browser/cua.md) | 미확인 | 미확인 | 상류 README에서 명시적 정책을 확인하지 못함. 설치 전에 원본 설정·코드·네트워크 동작 재확인 필요 · [원본](https://github.com/trycua/cua) |
| [AgentsView](../tools/ui/agentsview.md) | 기본 세션 아카이브는 로컬, 외부 기능은 선택 | 미확인 | 로컬 SQLite에 세션 보관. 클라우드 채팅 동기화, 원격 내보내기, 선택적 임베딩/시맨틱 검색은 설정에 따라 외부 전송 가능. 자동 업데이트 동작은 설치 방식별 추가 확인 필요 · [원본](https://github.com/kenn-io/agentsview) |
| [Claude Code Filetree](../tools/ui/claude-code-filetree.md) | 미확인 | 미확인 | 상류 README에서 명시적 정책을 확인하지 못함. 설치 전에 원본 설정·코드·네트워크 동작 재확인 필요 · [원본](https://github.com/data-goblin/claude-code-filetree) |
| [Claude Code Mods](../tools/ui/claude-code-mods.md) | 미확인 | 미확인 | 상류 README에서 명시적 정책을 확인하지 못함. 설치 전에 원본 설정·코드·네트워크 동작 재확인 필요 · [원본](https://github.com/hamzafer/claude-code-mods) |
| [Claude Code Paste Preview](../tools/ui/claude-code-paste-preview.md) | 미확인 | 미확인 | 상류 README에서 명시적 정책을 확인하지 못함. 설치 전에 원본 설정·코드·네트워크 동작 재확인 필요 · [원본](https://github.com/alan890104/claude-code-paste-preview) |
| [Claude HUD](../tools/ui/claude-hud.md) | 미확인 | 마켓플레이스 자동 갱신 선택 | Claude Code 서드파티 마켓플레이스 자동 갱신은 기본 비활성. 자체 텔레메트리 여부는 README에서 확인되지 않음 · [원본](https://github.com/jarrodwatts/claude-hud) |
| [Claude Image View](../tools/ui/claude-image-view.md) | 네트워크 요청 없음 명시 | 미확인 | 원본 README 기준 이미지 처리는 로컬에서 수행하고 자체 네트워크 요청 없음 · [원본](https://github.com/jarrodwatts/claude-image-view) |
| [Prompt Rail](../tools/ui/prompt-rail.md) | 미확인 | 미확인 | 상류 README에서 명시적 정책을 확인하지 못함. 설치 전에 원본 설정·코드·네트워크 동작 재확인 필요 · [원본](https://github.com/oikon48/prompt-rail) |
| [Savvy Progress](../tools/ui/savvy-progress.md) | 미확인 | 미확인 | 플러그인 README·매니페스트에 자체 텔레메트리·자동 버전 확인 정책이 명시되지 않음. 없다고 단정할 수 없으며, Claude Code 및 마켓플레이스의 통신은 별개 · [원본](https://github.com/JohnnyVizz/claude-kit/blob/main/plugins/savvy-progress/README.md) |
| [Archify](../tools/visual/archify.md) | 구성별 확인 필요 | 버전 확인(일부 설치형) | 일부 설치 경로는 신규 버전 안내를 위한 확인 수행. Hermes 스킬 통합은 원본에서 텔레메트리 없음을 명시하나 모든 배포 방식에 일반화할 수 없음 · [원본](https://github.com/tt-a1i/archify) |
| [Frontend Slides](../tools/visual/frontend-slides.md) | 미확인 | 미확인 | 상류 README에서 명시적 정책을 확인하지 못함. 설치 전에 원본 설정·코드·네트워크 동작 재확인 필요 · [원본](https://github.com/zarazhangrui/frontend-slides) |
| [Prismantis](../tools/visual/prismantis.md) | 미확인 | 미확인 | 상류 README에서 명시적 정책을 확인하지 못함. 설치 전에 원본 설정·코드·네트워크 동작 재확인 필요 · [원본](https://github.com/NahumLitvin/prismantis) |
| [Figma Desktop MCP](../tools/design/figma-desktop-mcp.md) | 미확인 | 미확인 | 상류 README에서 명시적 정책을 확인하지 못함. 설치 전에 원본 설정·코드·네트워크 동작 재확인 필요 · [원본](https://developers.figma.com/docs/figma-mcp-server/local-server-installation/) |
| [Open Design](../tools/design/open-design.md) | 미확인 | 미확인 | 로컬 실행과 외부 클라우드·BYOK 경로가 공존. 선택한 모델/클라우드 요청은 외부 서비스로 전송됨 · [원본](https://github.com/nexu-io/open-design) |
| [OpenShip](../tools/utilities/openship.md) | 미확인 | 미확인 | 상류 README에서 명시적 정책을 확인하지 못함. 설치 전에 원본 설정·코드·네트워크 동작 재확인 필요 · [원본](https://github.com/oblien/openship) |
| [ni](../tools/utilities/ni.md) | 미확인 | 미확인 | 상류 README에서 명시적 정책을 확인하지 못함. 설치 전에 원본 설정·코드·네트워크 동작 재확인 필요 · [원본](https://github.com/antfu-collective/ni) |
| [Peon Ping](../tools/utilities/peon-ping.md) | 미확인 | 미확인 | 상류 README에서 명시적 정책을 확인하지 못함. 설치 전에 원본 설정·코드·네트워크 동작 재확인 필요 · [원본](https://github.com/PeonPing/peon-ping) |
| [abtop](../tools/utilities/abtop.md) | 자체 통계 미확인 | 미확인 | 로컬 세션/프로세스 정보를 읽음. 제목·요약 생성 시 `claude --print`를 통한 모델 호출과 토큰 비용 발생 가능. 저비용 모델 지정(`ANTHROPIC_MODEL=haiku` 등)은 설치 환경에서 적용 여부 확인 필요. 자체 텔레메트리 여부는 별도 확인 필요 · [원본](https://github.com/graykode/abtop#privacy) |
| [Stats](../tools/utilities/stats.md) | 없음 명시 | 버전 확인 | 텔레메트리·분석 없음. 업데이트 확인과 공인 IP 조회를 위한 외부 API 사용 · [원본](https://github.com/exelban/stats#external-api) |
| [Vorssaint Utils](../tools/utilities/vorssaint-utils.md) | 없음 명시 | 버전 확인 | 분석·추적 없음. 업데이트 확인, 속도 테스트, Homebrew, 선택적 온라인 기능은 네트워크 사용 · [원본](https://github.com/vorssaint/vorssaint-utils/blob/main/docs/PRIVACY.md) |
| [Yazi](../tools/utilities/yazi.md) | 미확인 | 미확인 | 상류 README에서 명시적 정책을 확인하지 못함. 설치 전에 원본 설정·코드·네트워크 동작 재확인 필요 · [원본](https://github.com/sxyazi/yazi) |

## 실무 점검 절차

1. 설치하려는 정확한 패키지·버전·배포 방식을 확인합니다. 같은 도구라도 플러그인·스킬·독립 CLI의 전송 정책이 다를 수 있습니다.
2. 상류 README·Privacy/Telemetry 문서·설정 도움말을 검토하고 기본값, 수집 항목, 외부 전송, 해제 방법을 구분합니다.
3. 업데이트 **확인**과 실제 자동 **설치**를 구분합니다. Claude Code 마켓플레이스 자동 갱신 여부도 확인합니다.
4. 문서가 없으면 `미확인`으로 두고 텔레메트리가 없다고 추측하지 않습니다. 필요한 경우 실행 코드를 살피고 네트워크를 독립적으로 검사합니다.
5. 정책을 변경할 때 이 표, 관련 도구 가이드, 두 README의 안내 및 CI를 함께 검증합니다.

## 기록상 한계

- 이 표는 특정 시점의 상류 문서 조사 결과입니다. 업데이트·설치 후 실제 실행 상태는 운영체제·버전·설정에 따라 달라집니다.
- 명시적인 `없음`과 **문서에서 찾지 못함**은 다릅니다.
- 완전한 프라이버시 또는 보안 감사를 의미하지 않습니다.
