# awesome-agent-tools

[한국어](README.ko.md) | [English](README.md)

AI 코딩 에이전트에 활용할 만한 **Skills·Plugins·Mods·MCP 서버·개발 도구**를 엄선한 큐레이션입니다. 도구의 용도를 한 줄로 설명하고, 설치·업데이트·삭제·검증 절차를 개별 문서에 정리합니다.

> 이 목록의 추천 등급은 큐레이터의 판단이며, 호환성이나 안전성을 보증하지 않습니다.

## 시작하기

1. 아래 표에서 필요한 기능과 **무엇을 하나요?** 설명을 확인합니다.
2. 도구의 **가이드**에서 요구 사항과 설치·업데이트·삭제 절차를 확인합니다.
3. 에이전트에게 [AGENTS.md](AGENTS.md)와 해당 도구 문서를 읽고 현재 환경부터 점검하도록 요청합니다.
4. 전역 설정 변경·원격 스크립트 실행·파일 삭제 전에는 계획을 확인하고 승인합니다.

## 추천 티어

| 티어 | 의미 |
|---|---|
| **S** | 반복 사용 경험을 바탕으로 강력 추천합니다. |
| **A** | 명확한 용도에 추천할 만합니다. |
| **B** | 시험해 볼 만한 후보입니다. |
| **Archived** | 현재 추천하지 않으며 [제외 사유](archive/README.md)를 보존합니다. |

**에이전트 태그:** `Claude Code`, `Codex`, `Hermes`는 확인된 지원 대상을 뜻합니다. `범용`은 에이전트 관련 범용 도구라는 뜻으로, 세 에이전트 모두 지원한다는 의미는 아닙니다.

**검증 정보:** README 표에서는 별도로 표시하지 않습니다. 실제 사용 경험·메타데이터 확인·시험 중·미검증 등은 각 도구 가이드에 남깁니다.

**GitHub 활동:** Stars와 최근 커밋은 Shields.io 동적 배지이므로 표시가 지연될 수 있습니다. 최근 커밋과 설치 가이드 검증일은 다르며, 활동 수치가 추천 티어를 결정하지 않습니다.

## 내 프로젝트 · My Works

큐레이터가 직접 유지보수하는 프로젝트입니다. 추천 티어는 독립적인 평가 결과가 아닙니다.

| 도구 | 무엇을 하나요? | 유형 | 지원 에이전트 | 티어 | Stars | 최근 커밋 | 설치 가이드 |
|---|---|---|---|---|---|---|---|

| [TigerKit](https://github.com/MTGVim/tiger-kit) | 개발 작업의 계획·구현·리뷰·검증을 지원하는 통합 Agent Skills | skill | `Claude Code` `Codex` `Hermes` | **S** | ![Stars](https://img.shields.io/github/stars/MTGVim/tiger-kit?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/MTGVim/tiger-kit?style=flat-square&label=%20) | [가이드](tools/workflows/tigerkit.md) |

## 워크플로·에이전트

| 도구 | 무엇을 하나요? | 유형 | 지원 에이전트 | 티어 | Stars | 최근 커밋 | 설치 가이드 |
|---|---|---|---|---|---|---|---|

| [Autoharness](https://github.com/tigerless-labs/autoharness) | 실행 경험을 바탕으로 스킬을 생성·관리하는 하네스 | plugin/skill | `Claude Code` | **A** | ![Stars](https://img.shields.io/github/stars/tigerless-labs/autoharness?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/tigerless-labs/autoharness?style=flat-square&label=%20) | [가이드](tools/workflows/autoharness.md) |
| [Skill Creator](https://github.com/openai/skills) | 에이전트 스킬의 작성과 개선 절차를 안내 | skill | `Codex` `범용` | **A** | ![Stars](https://img.shields.io/github/stars/openai/skills?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/openai/skills?style=flat-square&label=%20) | [가이드](tools/workflows/skill-creator.md) |
| [Subagent Tuner](https://github.com/Kruhlikau/subagent-tuner) | Claude Code 서브에이전트의 모델과 추론 수준을 조정 | plugin/mod | `Claude Code` | **A** | ![Stars](https://img.shields.io/github/stars/Kruhlikau/subagent-tuner?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/Kruhlikau/subagent-tuner?style=flat-square&label=%20) | [가이드](tools/workflows/subagent-tuner.md) |
| [Autoharness Codex](https://github.com/arm092/autoharness-codex) | Autoharness 워크플로를 Codex에 적용 | skill | `Codex` | **B** | ![Stars](https://img.shields.io/github/stars/arm092/autoharness-codex?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/arm092/autoharness-codex?style=flat-square&label=%20) | [가이드](tools/workflows/autoharness-codex.md) |
| [Darwin Skill](https://github.com/alchaincyf/darwin-skill) | 실행 경험을 바탕으로 스킬을 반복 개선하도록 지원 | skill | `범용` | **B** | ![Stars](https://img.shields.io/github/stars/alchaincyf/darwin-skill?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/alchaincyf/darwin-skill?style=flat-square&label=%20) | [가이드](tools/workflows/darwin-skill.md) |
| [Inbox](https://github.com/petekp/inbox) | 세션에서 발생한 질문과 사용자 확인 사항을 수집 | plugin | `Claude Code` | **B** | ![Stars](https://img.shields.io/github/stars/petekp/inbox?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/petekp/inbox?style=flat-square&label=%20) | [가이드](tools/workflows/inbox.md) |
| [MCP Atlassian](https://github.com/sooperset/mcp-atlassian) | Jira와 Confluence를 에이전트에 연결하는 MCP 서버 | mcp | `범용` | **B** | ![Stars](https://img.shields.io/github/stars/sooperset/mcp-atlassian?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/sooperset/mcp-atlassian?style=flat-square&label=%20) | [가이드](tools/workflows/mcp-atlassian.md) |
| [Next Steps](https://github.com/anthropics/claude-plugins-community) | 작업 완료 후 후속 행동을 선택지로 제안 | plugin/mod | `Claude Code` | **B** | ![Stars](https://img.shields.io/github/stars/anthropics/claude-plugins-community?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/anthropics/claude-plugins-community?style=flat-square&label=%20) | [가이드](tools/workflows/next-steps.md) |
| [OpenShip](https://github.com/oblien/openship) | 에이전트 기반 개발 워크플로를 실험하는 도구 | tool | `범용` | **B** | ![Stars](https://img.shields.io/github/stars/oblien/openship?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/oblien/openship?style=flat-square&label=%20) | [가이드](tools/workflows/openship.md) |
| [Skill Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) | 문서와 자료를 에이전트 스킬로 변환 | skill/tool | `범용` | **B** | ![Stars](https://img.shields.io/github/stars/yusufkaraaslan/Skill_Seekers?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/yusufkaraaslan/Skill_Seekers?style=flat-square&label=%20) | [가이드](tools/workflows/skill-seekers.md) |

## 코딩·코드 탐색

| 도구 | 무엇을 하나요? | 유형 | 지원 에이전트 | 티어 | Stars | 최근 커밋 | 설치 가이드 |
|---|---|---|---|---|---|---|---|

| [Code Modernization](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/code-modernization) | 레거시 코드를 현대화하고 변경 결과를 검증 | plugin | `Claude Code` | **B** | ![Stars](https://img.shields.io/github/stars/anthropics/claude-plugins-official?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/anthropics/claude-plugins-official?style=flat-square&label=%20) | [가이드](tools/coding/code-modernization.md) |
| [Codegraph](https://github.com/colbymchenry/codegraph) | 코드 구조와 관계를 그래프로 탐색 | tool | `범용` | **B** | ![Stars](https://img.shields.io/github/stars/colbymchenry/codegraph?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/colbymchenry/codegraph?style=flat-square&label=%20) | [가이드](tools/coding/codegraph.md) |
| [Ponytail](https://github.com/dietrichgebert/ponytail) | 과도한 설계를 줄이고 간결한 코드 작성을 유도 | plugin/mod | `Claude Code` | **B** | ![Stars](https://img.shields.io/github/stars/dietrichgebert/ponytail?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/dietrichgebert/ponytail?style=flat-square&label=%20) | [가이드](tools/coding/ponytail.md) |

## 컨텍스트·세션

| 도구 | 무엇을 하나요? | 유형 | 지원 에이전트 | 티어 | Stars | 최근 커밋 | 설치 가이드 |
|---|---|---|---|---|---|---|---|

| [Agent Usage Guard](https://github.com/rbartoli/agent-usage-guard) | 서브에이전트의 과도한 호출과 반복 실행을 제한 | plugin | `Claude Code` | **B** | ![Stars](https://img.shields.io/github/stars/rbartoli/agent-usage-guard?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/rbartoli/agent-usage-guard?style=flat-square&label=%20) | [가이드](tools/context/agent-usage-guard.md) |
| [Cache Tax](https://github.com/karanb192/cache-tax) | 프롬프트 캐시를 유지하고 만료 비용을 안내 | plugin/mod | `Claude Code` | **B** | ![Stars](https://img.shields.io/github/stars/karanb192/cache-tax?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/karanb192/cache-tax?style=flat-square&label=%20) | [가이드](tools/context/cache-tax.md) |
| [Claude Auto Handoff](https://github.com/alexknowshtml/claude-auto-handoff) | 컨텍스트가 가득 차기 전에 새 세션으로 작업을 인계 | mod | `Claude Code` | **B** | ![Stars](https://img.shields.io/github/stars/alexknowshtml/claude-auto-handoff?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/alexknowshtml/claude-auto-handoff?style=flat-square&label=%20) | [가이드](tools/context/claude-auto-handoff.md) |
| [Engram](https://github.com/Gentleman-Programming/engram) | 에이전트가 작업 정보를 저장하고 회수하는 메모리 도구 | tool | `범용` | **B** | ![Stars](https://img.shields.io/github/stars/Gentleman-Programming/engram?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/Gentleman-Programming/engram?style=flat-square&label=%20) | [가이드](tools/context/engram.md) |
| [Session Titles](https://github.com/zhangbububu/session-titles) | Claude Code 세션에 식별하기 쉬운 제목을 부여 | mod | `Claude Code` | **B** | ![Stars](https://img.shields.io/github/stars/zhangbububu/session-titles?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/zhangbububu/session-titles?style=flat-square&label=%20) | [가이드](tools/context/session-titles.md) |

## 브라우저·QA

| 도구 | 무엇을 하나요? | 유형 | 지원 에이전트 | 티어 | Stars | 최근 커밋 | 설치 가이드 |
|---|---|---|---|---|---|---|---|

| [Orca](https://github.com/stablyai/orca) | 화면을 보고 데스크톱 GUI를 조작하는 자동화 도구 | tool | `범용` | **A** | ![Stars](https://img.shields.io/github/stars/stablyai/orca?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/stablyai/orca?style=flat-square&label=%20) | [가이드](tools/browser/orca.md) |
| [Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp) | 브라우저 디버깅 기능을 MCP로 제공 | mcp | `범용` | **B** | ![Stars](https://img.shields.io/github/stars/ChromeDevTools/chrome-devtools-mcp?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/ChromeDevTools/chrome-devtools-mcp?style=flat-square&label=%20) | [가이드](tools/browser/chrome-devtools-mcp.md) |
| [Claude Show Your Work](https://github.com/iamumeransari/claude-show-your-work) | 미디어와 테스트 결과를 터미널에서 시각적으로 확인 | plugin | `Claude Code` | **B** | ![Stars](https://img.shields.io/github/stars/iamumeransari/claude-show-your-work?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/iamumeransari/claude-show-your-work?style=flat-square&label=%20) | [가이드](tools/browser/claude-show-your-work.md) |
| [Cua](https://github.com/trycua/cua) | 화면과 입력 장치를 이용해 컴퓨터 작업을 자동화 | tool | `범용` | **B** | ![Stars](https://img.shields.io/github/stars/trycua/cua?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/trycua/cua?style=flat-square&label=%20) | [가이드](tools/browser/cua.md) |

## 터미널 UI

| 도구 | 무엇을 하나요? | 유형 | 지원 에이전트 | 티어 | Stars | 최근 커밋 | 설치 가이드 |
|---|---|---|---|---|---|---|---|

| [Claude Code Filetree](https://github.com/data-goblin/claude-code-filetree) | Git 상태와 작업 중인 파일을 트리로 표시 | mod | `Claude Code` | **B** | ![Stars](https://img.shields.io/github/stars/data-goblin/claude-code-filetree?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/data-goblin/claude-code-filetree?style=flat-square&label=%20) | [가이드](tools/ui/claude-code-filetree.md) |
| [Claude Code Mods](https://github.com/hamzafer/claude-code-mods) | Claude Code의 인터페이스와 동작을 확장하는 모드 모음 | mod | `Claude Code` | **B** | ![Stars](https://img.shields.io/github/stars/hamzafer/claude-code-mods?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/hamzafer/claude-code-mods?style=flat-square&label=%20) | [가이드](tools/ui/claude-code-mods.md) |
| [Claude Code Paste Preview](https://github.com/alan890104/claude-code-paste-preview) | 이미지 붙여넣기 미리보기와 마크업을 지원 | plugin/mod | `Claude Code` | **B** | ![Stars](https://img.shields.io/github/stars/alan890104/claude-code-paste-preview?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/alan890104/claude-code-paste-preview?style=flat-square&label=%20) | [가이드](tools/ui/claude-code-paste-preview.md) |
| [Claude Flightdeck](https://github.com/scasella/claude-flightdeck) | 컨텍스트·비용·권한·서브에이전트를 사이드 패널에 표시 | plugin/mod | `Claude Code` | **B** | ![Stars](https://img.shields.io/github/stars/scasella/claude-flightdeck?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/scasella/claude-flightdeck?style=flat-square&label=%20) | [가이드](tools/ui/claude-flightdeck.md) |
| [Claude HUD](https://github.com/jarrodwatts/claude-hud) | Claude Code 작업 상태와 사용량을 화면에 표시 | plugin | `Claude Code` | **B** | ![Stars](https://img.shields.io/github/stars/jarrodwatts/claude-hud?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/jarrodwatts/claude-hud?style=flat-square&label=%20) | [가이드](tools/ui/claude-hud.md) |
| [Claude Image View](https://github.com/jarrodwatts/claude-image-view) | 붙여넣은 이미지의 썸네일을 프롬프트 위에 표시 | plugin/mod | `Claude Code` | **B** | ![Stars](https://img.shields.io/github/stars/jarrodwatts/claude-image-view?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/jarrodwatts/claude-image-view?style=flat-square&label=%20) | [가이드](tools/ui/claude-image-view.md) |
| [Claude Skins](https://github.com/hellosverre/claude-skins) | Claude Code 터미널 테마와 출력 표현을 변경 | plugin/mod | `Claude Code` | **B** | ![Stars](https://img.shields.io/github/stars/hellosverre/claude-skins?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/hellosverre/claude-skins?style=flat-square&label=%20) | [가이드](tools/ui/claude-skins.md) |
| [Glowup](https://github.com/NovusEdge/glowup) | 파일 변경·Git diff·컨텍스트 정보를 사이드 패널에 표시 | plugin/mod | `Claude Code` | **B** | ![Stars](https://img.shields.io/github/stars/NovusEdge/glowup?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/NovusEdge/glowup?style=flat-square&label=%20) | [가이드](tools/ui/glowup.md) |
| [Prompt Rail](https://github.com/oikon48/prompt-rail) | 이전 프롬프트를 미리 보고 대화 위치로 이동 | plugin/mod | `Claude Code` | **B** | ![Stars](https://img.shields.io/github/stars/oikon48/prompt-rail?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/oikon48/prompt-rail?style=flat-square&label=%20) | [가이드](tools/ui/prompt-rail.md) |
| [Savvy Progress](https://github.com/JohnnyVizz/claude-kit/tree/main/plugins/savvy-progress) | 작업 진행률과 서브에이전트별 실행 상태를 표시 | plugin | `Claude Code` | **B** | ![Stars](https://img.shields.io/github/stars/JohnnyVizz/claude-kit?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/JohnnyVizz/claude-kit?style=flat-square&label=%20) | [가이드](tools/ui/savvy-progress.md) |

## 시각화·콘텐츠

| 도구 | 무엇을 하나요? | 유형 | 지원 에이전트 | 티어 | Stars | 최근 커밋 | 설치 가이드 |
|---|---|---|---|---|---|---|---|

| [Archify](https://github.com/tt-a1i/archify) | 기술 설명을 위한 구조화된 다이어그램과 HTML 표현 지원 | tool | `범용` | **A** | ![Stars](https://img.shields.io/github/stars/tt-a1i/archify?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/tt-a1i/archify?style=flat-square&label=%20) | [가이드](tools/visual/archify.md) |
| [Frontend Slides](https://github.com/zarazhangrui/frontend-slides) | 프론트엔드 기반 발표 슬라이드 제작을 지원 | skill/tool | `범용` | **B** | ![Stars](https://img.shields.io/github/stars/zarazhangrui/frontend-slides?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/zarazhangrui/frontend-slides?style=flat-square&label=%20) | [가이드](tools/visual/frontend-slides.md) |
| [Prismantis](https://github.com/NahumLitvin/prismantis) | 터미널에서 Mermaid·표·수식 등을 렌더링 | plugin/mod | `Claude Code` | **B** | ![Stars](https://img.shields.io/github/stars/NahumLitvin/prismantis?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/NahumLitvin/prismantis?style=flat-square&label=%20) | [가이드](tools/visual/prismantis.md) |

## 디자인

| 도구 | 무엇을 하나요? | 유형 | 지원 에이전트 | 티어 | Stars | 최근 커밋 | 설치 가이드 |
|---|---|---|---|---|---|---|---|

| [Figma Desktop MCP](https://developers.figma.com/docs/figma-mcp-server/local-server-installation/) | Figma 데스크톱 디자인 정보를 에이전트에 제공 | mcp | `Claude Code` `Codex` `Hermes` | **B** | — | — | [가이드](tools/design/figma-desktop-mcp.md) |
| [Open Design](https://github.com/nexu-io/open-design) | 디자인 제작 관련 도구와 워크플로를 제공 | tool | `범용` | **B** | ![Stars](https://img.shields.io/github/stars/nexu-io/open-design?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/nexu-io/open-design?style=flat-square&label=%20) | [가이드](tools/design/open-design.md) |

## 개발 유틸리티

| 도구 | 무엇을 하나요? | 유형 | 지원 에이전트 | 티어 | Stars | 최근 커밋 | 설치 가이드 |
|---|---|---|---|---|---|---|---|

| [ni](https://github.com/antfu-collective/ni) | 패키지 매니저를 감지하여 실행 명령을 통일 | tool | `범용` | **A** | ![Stars](https://img.shields.io/github/stars/antfu-collective/ni?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/antfu-collective/ni?style=flat-square&label=%20) | [가이드](tools/utilities/ni.md) |
| [Peon Ping](https://github.com/PeonPing/peon-ping) | 에이전트의 작업 상태를 효과음으로 알림 | tool | `범용` | **A** | ![Stars](https://img.shields.io/github/stars/PeonPing/peon-ping?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/PeonPing/peon-ping?style=flat-square&label=%20) | [가이드](tools/utilities/peon-ping.md) |
| [abtop](https://github.com/graykode/abtop) | 터미널에서 에이전트 관련 활동을 모니터링 | tool | `범용` | **B** | ![Stars](https://img.shields.io/github/stars/graykode/abtop?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/graykode/abtop?style=flat-square&label=%20) | [가이드](tools/utilities/abtop.md) |
| [Stats](https://github.com/exelban/stats) | macOS의 하드웨어 자원 사용량을 메뉴 막대에서 확인 | tool | `범용` | **B** | ![Stars](https://img.shields.io/github/stars/exelban/stats?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/exelban/stats?style=flat-square&label=%20) | [가이드](tools/utilities/stats.md) |
| [Vorssaint Utils](https://github.com/vorssaintapp/vorssaint-utils) | macOS용 생산성 유틸리티를 묶어 제공 | tool | `범용` | **B** | ![Stars](https://img.shields.io/github/stars/vorssaintapp/vorssaint-utils?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/vorssaintapp/vorssaint-utils?style=flat-square&label=%20) | [가이드](tools/utilities/vorssaint-utils.md) |
| [Yazi](https://github.com/sxyazi/yazi) | 터미널에서 파일을 탐색하고 관리하는 파일 관리자 | tool | `범용` | **B** | ![Stars](https://img.shields.io/github/stars/sxyazi/yazi?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/sxyazi/yazi?style=flat-square&label=%20) | [가이드](tools/utilities/yazi.md) |

## Archived · 추천 제외

[추천 제외 도구와 사유 보기](archive/README.md). 제외는 개인적인 큐레이션 판단이며 원본 프로젝트가 중단되었다는 뜻은 아닙니다.

## 기여와 관리

도구를 추가·갱신·제외하려면 [CONTRIBUTING.md](CONTRIBUTING.md)와 [AGENTS.md](AGENTS.md)의 절차를 참고하세요.

## 라이선스

이 저장소에는 [MIT 라이선스](LICENSE)가 적용됩니다. 연결된 외부 프로젝트에는 각각의 라이선스가 적용됩니다.

