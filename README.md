# awesome-agent-tools

[한국어](README.md) | [English](README.en.md)

AI 코딩 에이전트에 활용할 만한 **Skills·Plugins·Mods·MCP 서버·개발 도구**를 엄선한 큐레이션입니다. 도구의 용도를 한 줄로 설명하고, 설치·업데이트·삭제·검증 절차를 개별 문서에 정리합니다.

> 이 목록은 큐레이터가 선별한 도구를 소개합니다. 포함 여부는 호환성이나 안전성 보증이 아닙니다.

**개인정보·네트워크 점검:** 활성 도구 38개의 텔레메트리·업데이트 확인·해제 방법은 [Privacy, Telemetry & Updates](docs/privacy-and-updates.md)에 정리했습니다. 정책이 확인되지 않은 항목은 `미확인`으로 구분합니다.

**🧑‍💻 = My Daily Setup에서 현재 사용하는 도구입니다.** 일반 카탈로그에서만 표시하며, 추천 등급이나 호환성 보증을 의미하지 않습니다.

## 시작하기

1. 아래 표에서 필요한 기능과 **무엇을 하나요?** 설명을 확인합니다.
2. 도구의 **가이드**에서 요구 사항과 설치·업데이트·삭제 절차를 확인합니다.
3. 에이전트에게 [AGENTS.md](AGENTS.md)와 해당 도구 문서를 읽고 현재 환경부터 점검하도록 요청합니다.
4. 전역 설정 변경·원격 스크립트 실행·파일 삭제 전에는 계획을 확인하고 승인합니다.

## 큐레이션 상태

- **Active:** 사용해 볼 가치가 있다고 판단해 현재 목록에 소개하는 도구입니다.
- **Archived:** 현재 추천 목록에서 제외하되 [제외 사유](archive/README.md)를 보존한 도구입니다.

**에이전트 태그:** Claude Code·Codex·Hermes 배지는 확인된 지원 대상을 나타냅니다. **Skills CLI** 배지는 `npx skills` 설치 경로가 확인된 스킬을 뜻하며, 모든 에이전트에서 기능이 검증되었다는 의미는 아닙니다. 독립 실행 프로그램은 `독립 CLI`·`독립 앱`·`SDK·플랫폼`으로 따로 표시합니다. 호환성이 검증되지 않은 항목만 `—`로 표시합니다. 이는 미지원이나 추천 제외를 뜻하지 않습니다. MCP 배지는 호스트의 프로토콜 연결 가능성을 나타내며, 실제 인증·동작 검증은 가이드에서 구분합니다.

**검증 정보:** README 표에서는 별도로 표시하지 않습니다. 실제 사용 경험·메타데이터 확인·시험 중·미검증 등은 각 도구 가이드에 남깁니다.

**GitHub 활동:** Stars와 최근 커밋은 Shields.io 동적 배지이므로 표시가 지연될 수 있습니다. 최근 커밋과 설치 가이드 검증일은 다르며, 활동 수치는 품질이나 추천 여부를 의미하지 않습니다.

## My Daily Setup

실제로 사용 중인 조합(2026-11-06 기준)입니다. 추천 등급과는 별개이며, 사용 환경에 따라 달라집니다.

| 도구 | 용도 |
|---|---|
| [TigerKit](https://github.com/MTGVim/tiger-kit) | 개발·리뷰·검증을 위한 Claude Code·Codex·Hermes 통합 스킬 |
| [Orca](https://github.com/stablyai/orca) | 에이전트 병렬 개발 환경 |
| [Autoharness](https://github.com/tigerless-labs/autoharness) | 스킬 자동 관리 |
| [Subagent Tuner](https://github.com/Kruhlikau/subagent-tuner) | 서브에이전트 모델·effort 조정 |
| [Agent Usage Guard](https://github.com/rbartoli/agent-usage-guard) | 에이전트 폭주 방지·큰 컨텍스트에서 Compact 제안 |
| [Codegraph](https://github.com/colbymchenry/codegraph) | 코드 그래프 탐색 |
| [Ponytail](https://github.com/dietrichgebert/ponytail) | 과도한 구현 억제 |
| [Cache Tax](https://github.com/karanb192/cache-tax) | 프롬프트 캐시 유지 |
| [Engram](https://github.com/Gentleman-Programming/engram) | 세션 메모리 |
| [Claude Show Your Work](https://github.com/iamumeransari/claude-show-your-work) | 미디어·QA 시각화 |
| [Claude Code Paste Preview](https://github.com/alan890104/claude-code-paste-preview) | 이미지 편집·미리보기 |
| [Savvy Progress](https://github.com/JohnnyVizz/claude-kit/tree/main/plugins/savvy-progress) | 서브에이전트 진행 현황 패널 (시험 운영) |
| [Claude Flightdeck](https://github.com/scasella/claude-flightdeck) | 서브에이전트 대시보드 |
| [Claude HUD](https://github.com/jarrodwatts/claude-hud) | 컨텍스트·사용량 statusLine |
| [Prompt Rail](https://github.com/oikon48/prompt-rail) | 이전 프롬프트 탐색 |
| [ni](https://github.com/antfu-collective/ni) | 패키지 매니저 통합 |
| [Peon Ping](https://github.com/PeonPing/peon-ping) | 작업 알림 |
| [abtop](https://github.com/graykode/abtop) | 터미널 모니터링 |
| [Yazi](https://github.com/sxyazi/yazi) | 터미널 파일 관리 |

### 설정 메모

- **[abtop](tools/utilities/abtop.md):** 세션 제목·요약 생성에 `claude --print`를 사용하므로 추가 AI 토큰이 소모될 수 있습니다. 비용 절감을 위해 `ANTHROPIC_MODEL=haiku abtop`처럼 저비용 모델을 지정해 실행하는 방법을 검토합니다. 실제 모델 적용 여부는 실행 환경에서 확인합니다.


현재 구성에서 조정하거나 확인해 둔 사항입니다. 도구별 설치·업데이트·삭제 방법은 아래 카탈로그의 가이드에서 확인할 수 있습니다.

- **[Show Your Work](tools/browser/claude-show-your-work.md):** Prismantis도 함께 활성화한다면 Claude Code 설정의 `enabledPlugins`에서 Show Your Work를 앞에 둡니다. 이는 출력 처리 순서에 관한 사용자 환경의 우회 방법으로, 모든 렌더러 조합에서 정상 동작을 보장하지는 않습니다. `/show-your-work`의 **Don't share** 또는 `SHOW_YOUR_WORK_TELEMETRY=0`으로 사용 통계 전송을 끌 수 있습니다. 자체 버전 확인·업데이트를 끄려면 `SHOW_YOUR_WORK_AUTO_UPDATE=0`을 설정합니다.
- **[Paste Preview](tools/ui/claude-code-paste-preview.md):** Image View와 같은 이미지 미리보기 영역을 사용하므로 하나만 활성화합니다.
- **[Flightdeck](tools/ui/claude-flightdeck.md):** 사이드 패널은 Glowup과 겹칩니다. 펄스 표시에는 `motion: while-active`를 사용합니다.
- **[Claude HUD](tools/ui/claude-hud.md):** `statusLine` 설정은 HUD의 정상 기능입니다. 다른 플러그인이 기존 설정을 덮어쓰는지만 확인합니다.
- **[Claude Code · Cache Tax · Agent Usage Guard](tools/context/cache-tax.md):** `idleCompaction: false`로 유휴 압축만 끄고 일반 autocompact는 유지합니다. Cache Tax는 `keepwarm: always`, `guard: warn`(비용 경고만 표시)으로, Agent Usage Guard는 `AGENT_GUARD_DORMANT_SECONDS=21600`(6시간)으로 설정했습니다. Cache Tax 변경은 새 세션의 `/cache-tax`에서 `guard warn only` 표시 확인이 남았습니다. 캐시 유지에도 토큰 비용이 듭니다.
- **[Orca · Paste Preview · Prismantis](tools/workflows/orca.md):** 편집 이미지 전송이나 Mermaid pie 출력 뒤 inline image의 base64가 보이면 `Ctrl+L`로 다시 그립니다. 반복 시 조건부 지연 redraw shim을 임시로 고려합니다.
- **[Savvy Progress](tools/ui/savvy-progress.md):** 일반 서브에이전트 실행 시에도 패널을 자동으로 열려면 `autoOpen: any`를 설정합니다. 현재는 기본값 `savvy`로 관찰됐으며 `/agents-info`로 수동으로 열 수 있습니다.
- **[Claude Code Filetree](tools/ui/claude-code-filetree.md):** 활성화 시 화면 전반의 클릭 좌표가 왼쪽으로 어긋나 개인 환경에서 사용을 중단하고 플러그인·마켓플레이스·캐시를 제거했습니다.

## 내 프로젝트 · My Works

큐레이터가 직접 유지보수하는 프로젝트입니다. 개인 프로젝트라는 사실을 구분해 표시하며, 독립적인 평가를 의미하지 않습니다.

| 도구 | 설명 · 가이드 | 지원 에이전트 | GitHub 활동 |
|---|---|---|---|
| [TigerKit](https://github.com/MTGVim/tiger-kit) 🧑‍💻 | Claude Code·Codex·Hermes용 개발·리뷰·검증 워크플로 스킬 모음<br>[가이드](tools/workflows/tigerkit.md) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) ![Codex](https://img.shields.io/badge/Codex-111111?style=flat-square&logo=openai&logoColor=white) ![Hermes](https://img.shields.io/badge/Hermes-9A641C?style=flat-square) [![Skills CLI](https://img.shields.io/badge/Skills_CLI-multi--agent-5965A8?style=flat-square)](https://github.com/vercel-labs/skills) | ![Stars](https://img.shields.io/github/stars/MTGVim/tiger-kit?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/MTGVim/tiger-kit?style=flat-square&label=%20) |

## 워크플로·에이전트

| 도구 | 설명 · 가이드 | 지원 에이전트 | GitHub 활동 |
|---|---|---|---|
| [Orca](https://github.com/stablyai/orca) 🧑‍💻 | Claude Code·Codex·Hermes를 워크트리별로 병렬 실행·편집·리뷰하는 통합 개발 환경<br>[가이드](tools/workflows/orca.md) · [시연](https://github.com/stablyai/orca/blob/main/docs/assets/readme-hero.jpg) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) ![Codex](https://img.shields.io/badge/Codex-111111?style=flat-square&logo=openai&logoColor=white) ![Hermes](https://img.shields.io/badge/Hermes-9A641C?style=flat-square) | ![Stars](https://img.shields.io/github/stars/stablyai/orca?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/stablyai/orca?style=flat-square&label=%20) |
| [Autoharness](https://github.com/tigerless-labs/autoharness) 🧑‍💻 | Claude Code 세션에서 스킬을 학습하고 중복 병합·갱신·정리<br>[가이드](tools/workflows/autoharness.md) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) | ![Stars](https://img.shields.io/github/stars/tigerless-labs/autoharness?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/tigerless-labs/autoharness?style=flat-square&label=%20) |
| [Skill Creator](https://github.com/openai/skills) | Codex 스킬 제작·개선 도구. 기존 openai/skills 저장소는 폐기 안내 중<br>[가이드](tools/workflows/skill-creator.md) | ![Codex](https://img.shields.io/badge/Codex-111111?style=flat-square&logo=openai&logoColor=white) | ![Stars](https://img.shields.io/github/stars/openai/skills?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/openai/skills?style=flat-square&label=%20) |
| [Subagent Tuner](https://github.com/Kruhlikau/subagent-tuner) 🧑‍💻 | Claude Code 서브에이전트마다 모델·추론 수준 자동 선택<br>[가이드](tools/workflows/subagent-tuner.md) · [시연](https://github.com/Kruhlikau/subagent-tuner/blob/main/docs/media/demo.gif) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) | ![Stars](https://img.shields.io/github/stars/Kruhlikau/subagent-tuner?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/Kruhlikau/subagent-tuner?style=flat-square&label=%20) |
| [Autoharness Codex](https://github.com/arm092/autoharness-codex) | Codex 세션 기록으로 스킬을 학습·검증·정리<br>[가이드](tools/workflows/autoharness-codex.md) | ![Codex](https://img.shields.io/badge/Codex-111111?style=flat-square&logo=openai&logoColor=white) | ![Stars](https://img.shields.io/github/stars/arm092/autoharness-codex?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/arm092/autoharness-codex?style=flat-square&label=%20) |
| [Darwin Skill](https://github.com/alchaincyf/darwin-skill) | 실험·평가를 반복해 Agent Skills를 최적화<br>[가이드](tools/workflows/darwin-skill.md) | [![Skills CLI](https://img.shields.io/badge/Skills_CLI-multi--agent-5965A8?style=flat-square)](https://github.com/vercel-labs/skills) | ![Stars](https://img.shields.io/github/stars/alchaincyf/darwin-skill?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/alchaincyf/darwin-skill?style=flat-square&label=%20) |
| [MCP Atlassian](https://github.com/sooperset/mcp-atlassian) | Jira·Confluence의 이슈와 문서를 MCP로 연결<br>[가이드](tools/workflows/mcp-atlassian.md) · [시연](https://github.com/sooperset/mcp-atlassian#quick-start) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) ![Codex](https://img.shields.io/badge/Codex-111111?style=flat-square&logo=openai&logoColor=white) ![Hermes](https://img.shields.io/badge/Hermes-9A641C?style=flat-square) | ![Stars](https://img.shields.io/github/stars/sooperset/mcp-atlassian?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/sooperset/mcp-atlassian?style=flat-square&label=%20) |
| [Next Steps](https://github.com/anthropics/claude-plugins-community) | Claude Code 응답 끝에 실행 가능한 후속 작업 선택지 제안<br>[가이드](tools/workflows/next-steps.md) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) | ![Stars](https://img.shields.io/github/stars/anthropics/claude-plugins-community?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/anthropics/claude-plugins-community?style=flat-square&label=%20) |
| [Skill Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) | 문서·Git·PDF·영상 등을 스킬·RAG 지식으로 변환<br>[가이드](tools/workflows/skill-seekers.md) | `독립 CLI` | ![Stars](https://img.shields.io/github/stars/yusufkaraaslan/Skill_Seekers?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/yusufkaraaslan/Skill_Seekers?style=flat-square&label=%20) |

## 코딩·코드 탐색

| 도구 | 설명 · 가이드 | 지원 에이전트 | GitHub 활동 |
|---|---|---|---|
| [Code Modernization](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/code-modernization) | 레거시 코드 현대화와 기존 동작의 동등성 검증<br>[가이드](tools/coding/code-modernization.md) · [시연](https://github.com/anthropics/claude-plugins-official/blob/main/plugins/code-modernization/assets/media/report-glance.jpg) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) | ![Stars](https://img.shields.io/github/stars/anthropics/claude-plugins-official?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/anthropics/claude-plugins-official?style=flat-square&label=%20) |
| [Codegraph](https://github.com/colbymchenry/codegraph) 🧑‍💻 | 코드베이스의 의미 관계를 로컬 그래프로 분석하고 에이전트에 제공<br>[가이드](tools/coding/codegraph.md) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) ![Codex](https://img.shields.io/badge/Codex-111111?style=flat-square&logo=openai&logoColor=white) ![Hermes](https://img.shields.io/badge/Hermes-9A641C?style=flat-square) | ![Stars](https://img.shields.io/github/stars/colbymchenry/codegraph?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/colbymchenry/codegraph?style=flat-square&label=%20) |
| [Ponytail](https://github.com/dietrichgebert/ponytail) 🧑‍💻 | 과한 추상화·코딩을 줄이는 간결한 구현·리뷰 보조<br>[가이드](tools/coding/ponytail.md) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) ![Codex](https://img.shields.io/badge/Codex-111111?style=flat-square&logo=openai&logoColor=white) | ![Stars](https://img.shields.io/github/stars/dietrichgebert/ponytail?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/dietrichgebert/ponytail?style=flat-square&label=%20) |

## 컨텍스트·세션

| 도구 | 설명 · 가이드 | 지원 에이전트 | GitHub 활동 |
|---|---|---|---|
| [Agent Usage Guard](https://github.com/rbartoli/agent-usage-guard) 🧑‍💻 | Claude Code의 과도한 에이전트 호출·재시도·사용량 급증 방지<br>[가이드](tools/context/agent-usage-guard.md) · [시연](https://github.com/rbartoli/agent-usage-guard) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) | ![Stars](https://img.shields.io/github/stars/rbartoli/agent-usage-guard?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/rbartoli/agent-usage-guard?style=flat-square&label=%20) |
| [Cache Tax](https://github.com/karanb192/cache-tax) 🧑‍💻 | Claude Code 프롬프트 캐시 유지·만료 비용 경고<br>[가이드](tools/context/cache-tax.md) · [시연](https://github.com/karanb192/cache-tax/blob/main/site/assets/refusal.gif) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) | ![Stars](https://img.shields.io/github/stars/karanb192/cache-tax?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/karanb192/cache-tax?style=flat-square&label=%20) |
| [Engram](https://github.com/Gentleman-Programming/engram) 🧑‍💻 | 여러 코딩 에이전트를 위한 지속 메모리·프로젝트별 검색<br>[가이드](tools/context/engram.md) · [시연](https://github.com/Gentleman-Programming/engram/blob/main/assets/tui-dashboard.png) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) ![Codex](https://img.shields.io/badge/Codex-111111?style=flat-square&logo=openai&logoColor=white) ![Hermes](https://img.shields.io/badge/Hermes-9A641C?style=flat-square) | ![Stars](https://img.shields.io/github/stars/Gentleman-Programming/engram?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/Gentleman-Programming/engram?style=flat-square&label=%20) |

## 브라우저·QA

| 도구 | 설명 · 가이드 | 지원 에이전트 | GitHub 활동 |
|---|---|---|---|
| [Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp) | Chrome 브라우저 디버깅·성능 분석·자동화를 MCP와 CLI로 제공<br>[가이드](tools/browser/chrome-devtools-mcp.md) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) ![Codex](https://img.shields.io/badge/Codex-111111?style=flat-square&logo=openai&logoColor=white) ![Hermes](https://img.shields.io/badge/Hermes-9A641C?style=flat-square) | ![Stars](https://img.shields.io/github/stars/ChromeDevTools/chrome-devtools-mcp?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/ChromeDevTools/chrome-devtools-mcp?style=flat-square&label=%20) |
| [Claude Show Your Work](https://github.com/iamumeransari/claude-show-your-work) 🧑‍💻 | Claude Code 안에서 이미지·영상·Playwright QA 결과 시각화<br>[가이드](tools/browser/claude-show-your-work.md) · [시연](https://github.com/iamumeransari/claude-show-your-work/blob/main/docs/homepage.jpg) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) | ![Stars](https://img.shields.io/github/stars/iamumeransari/claude-show-your-work?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/iamumeransari/claude-show-your-work?style=flat-square&label=%20) |
| [Cua](https://github.com/trycua/cua) | AI 에이전트용 가상 데스크톱·GUI 드라이버·컴퓨터 사용 SDK<br>[가이드](tools/browser/cua.md) | `SDK·플랫폼` | ![Stars](https://img.shields.io/github/stars/trycua/cua?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/trycua/cua?style=flat-square&label=%20) |

## 터미널 UI

| 도구 | 설명 · 가이드 | 지원 에이전트 | GitHub 활동 |
|---|---|---|---|
| [AgentsView](https://github.com/kenn-io/agentsview) | 코딩 에이전트 세션 검색·토큰 비용·도구 실행 패턴 분석<br>[가이드](tools/ui/agentsview.md) | `독립 앱 / CLI` | ![Stars](https://img.shields.io/github/stars/kenn-io/agentsview?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/kenn-io/agentsview?style=flat-square&label=%20) |
| [Claude Code Filetree](https://github.com/data-goblin/claude-code-filetree) | Claude Code가 읽고 수정하는 파일을 실시간 강조하고 Git 상태·diff를 표시<br>[가이드](tools/ui/claude-code-filetree.md) · [시연](https://github.com/data-goblin/claude-code-filetree/blob/main/media/filetree-shimmer.gif) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) | ![Stars](https://img.shields.io/github/stars/data-goblin/claude-code-filetree?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/data-goblin/claude-code-filetree?style=flat-square&label=%20) |
| [Claude Code Mods](https://github.com/hamzafer/claude-code-mods) | Claude Code 모드·훅·화면 확장을 선택 설치하는 CLI<br>[가이드](tools/ui/claude-code-mods.md) · [시연](https://github.com/hamzafer/claude-code-mods/blob/main/images/mission-control.gif) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) | ![Stars](https://img.shields.io/github/stars/hamzafer/claude-code-mods?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/hamzafer/claude-code-mods?style=flat-square&label=%20) |
| [Claude Code Paste Preview](https://github.com/alan890104/claude-code-paste-preview) 🧑‍💻 | 이미지 붙여넣기 미리보기·주석·자르기 지원<br>[가이드](tools/ui/claude-code-paste-preview.md) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) | ![Stars](https://img.shields.io/github/stars/alan890104/claude-code-paste-preview?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/alan890104/claude-code-paste-preview?style=flat-square&label=%20) |
| [Claude Flightdeck](https://github.com/scasella/claude-flightdeck) 🧑‍💻 | Claude Code 컨텍스트·비용·권한·서브에이전트 실시간 대시보드<br>[가이드](tools/ui/claude-flightdeck.md) · [시연](https://github.com/scasella/claude-flightdeck/blob/main/docs/media/demo.gif) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) | ![Stars](https://img.shields.io/github/stars/scasella/claude-flightdeck?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/scasella/claude-flightdeck?style=flat-square&label=%20) |
| [Claude HUD](https://github.com/jarrodwatts/claude-hud) 🧑‍💻 | Claude Code 입력창 아래 사용량·컨텍스트·도구 상태 표시<br>[가이드](tools/ui/claude-hud.md) · [시연](https://github.com/jarrodwatts/claude-hud/blob/main/claude-hud-preview-5-2.png) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) | ![Stars](https://img.shields.io/github/stars/jarrodwatts/claude-hud?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/jarrodwatts/claude-hud?style=flat-square&label=%20) |
| [Claude Image View](https://github.com/jarrodwatts/claude-image-view) | 붙여넣은 이미지 썸네일을 원본 비율로 표시<br>[가이드](tools/ui/claude-image-view.md) · [시연](https://github.com/jarrodwatts/claude-image-view/blob/main/claude-image-view.png) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) | ![Stars](https://img.shields.io/github/stars/jarrodwatts/claude-image-view?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/jarrodwatts/claude-image-view?style=flat-square&label=%20) |
| [Prompt Rail](https://github.com/oikon48/prompt-rail) 🧑‍💻 | 이전 프롬프트를 미리 보고 해당 대화로 이동<br>[가이드](tools/ui/prompt-rail.md) · [시연](https://github.com/oikon48/prompt-rail/blob/main/docs/demo.gif) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) | ![Stars](https://img.shields.io/github/stars/oikon48/prompt-rail?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/oikon48/prompt-rail?style=flat-square&label=%20) |
| [Savvy Progress](https://github.com/JohnnyVizz/claude-kit/tree/main/plugins/savvy-progress) | Claude Code 작업 진행률·서브에이전트별 모델·컨텍스트·추정 비용 패널<br>[가이드](tools/ui/savvy-progress.md) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) | ![Stars](https://img.shields.io/github/stars/JohnnyVizz/claude-kit?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/JohnnyVizz/claude-kit?style=flat-square&label=%20) |

## 시각화·콘텐츠

| 도구 | 설명 · 가이드 | 지원 에이전트 | GitHub 활동 |
|---|---|---|---|
| [Archify](https://github.com/tt-a1i/archify) | 설명·계획·코드 구조를 탐색 가능한 인터랙티브 HTML로 제작<br>[가이드](tools/visual/archify.md) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) ![Codex](https://img.shields.io/badge/Codex-111111?style=flat-square&logo=openai&logoColor=white) ![Hermes](https://img.shields.io/badge/Hermes-9A641C?style=flat-square) [![Skills CLI](https://img.shields.io/badge/Skills_CLI-multi--agent-5965A8?style=flat-square)](https://github.com/vercel-labs/skills) | ![Stars](https://img.shields.io/github/stars/tt-a1i/archify?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/tt-a1i/archify?style=flat-square&label=%20) |
| [Frontend Slides](https://github.com/zarazhangrui/frontend-slides) | HTML 발표자료 제작·시각적 테마 선택·PPT 변환 스킬<br>[가이드](tools/visual/frontend-slides.md) · [시연](https://www.youtube.com/watch?v=372Iksaz8b0) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) | ![Stars](https://img.shields.io/github/stars/zarazhangrui/frontend-slides?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/zarazhangrui/frontend-slides?style=flat-square&label=%20) |
| [Prismantis](https://github.com/NahumLitvin/prismantis) | Claude Code 터미널의 표·코드·Mermaid·차트·LaTeX 렌더링<br>[가이드](tools/visual/prismantis.md) · [시연](https://github.com/NahumLitvin/prismantis/blob/main/docs/tour.gif) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) ![Codex](https://img.shields.io/badge/Codex-111111?style=flat-square&logo=openai&logoColor=white) | ![Stars](https://img.shields.io/github/stars/NahumLitvin/prismantis?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/NahumLitvin/prismantis?style=flat-square&label=%20) |

## 디자인

| 도구 | 설명 · 가이드 | 지원 에이전트 | GitHub 활동 |
|---|---|---|---|
| [Figma Desktop MCP](https://developers.figma.com/docs/figma-mcp-server/local-server-installation/) | Figma 데스크톱 Dev Mode 디자인 정보·에셋을 MCP로 제공<br>[가이드](tools/design/figma-desktop-mcp.md) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) ![Codex](https://img.shields.io/badge/Codex-111111?style=flat-square&logo=openai&logoColor=white) ![Hermes](https://img.shields.io/badge/Hermes-9A641C?style=flat-square) | — |
| [Open Design](https://github.com/nexu-io/open-design) | AI 에이전트와 프로토타입·웹·슬라이드를 제작·피드백하는 워크스페이스<br>[가이드](tools/design/open-design.md) · [시연](https://github.com/nexu-io/open-design/blob/main/docs/assets/readme-hero-design-agent.webp) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) ![Codex](https://img.shields.io/badge/Codex-111111?style=flat-square&logo=openai&logoColor=white) ![Hermes](https://img.shields.io/badge/Hermes-9A641C?style=flat-square) | ![Stars](https://img.shields.io/github/stars/nexu-io/open-design?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/nexu-io/open-design?style=flat-square&label=%20) |

## 개발 유틸리티

| 도구 | 설명 · 가이드 | 지원 에이전트 | GitHub 활동 |
|---|---|---|---|
| [OpenShip](https://github.com/oblien/openship) | Git 프로젝트 빌드·배포·라우팅·TLS를 관리하는 셀프호스팅 CI/CD<br>[가이드](tools/utilities/openship.md) · [시연](https://github.com/oblien/openship/blob/main/docs/screenshots/screen.png) | `독립 앱` | ![Stars](https://img.shields.io/github/stars/oblien/openship?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/oblien/openship?style=flat-square&label=%20) |
| [ni](https://github.com/antfu-collective/ni) 🧑‍💻 | 프로젝트에 맞는 npm·pnpm·yarn·bun 패키지 명령 자동 선택<br>[가이드](tools/utilities/ni.md) | `독립 CLI` | ![Stars](https://img.shields.io/github/stars/antfu-collective/ni?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/antfu-collective/ni?style=flat-square&label=%20) |
| [Peon Ping](https://github.com/PeonPing/peon-ping) 🧑‍💻 | 에이전트 완료·승인 대기를 게임 음성과 화면 알림으로 안내<br>[가이드](tools/utilities/peon-ping.md) · [시연](https://github.com/PeonPing/peon-ping/blob/main/docs/peon-hero.gif) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) ![Codex](https://img.shields.io/badge/Codex-111111?style=flat-square&logo=openai&logoColor=white) | ![Stars](https://img.shields.io/github/stars/PeonPing/peon-ping?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/PeonPing/peon-ping?style=flat-square&label=%20) |
| [abtop](https://github.com/graykode/abtop) 🧑‍💻 | Claude Code·Codex·OpenCode 세션의 토큰·한도·프로세스 실시간 모니터<br>[가이드](tools/utilities/abtop.md) · [시연](https://github.com/graykode/abtop/blob/main/assets/demo.gif) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) ![Codex](https://img.shields.io/badge/Codex-111111?style=flat-square&logo=openai&logoColor=white) | ![Stars](https://img.shields.io/github/stars/graykode/abtop?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/graykode/abtop?style=flat-square&label=%20) |
| [Stats](https://github.com/exelban/stats) | macOS 메뉴 막대의 CPU·GPU·메모리·네트워크 모니터<br>[가이드](tools/utilities/stats.md) · [시연](https://github.com/exelban/stats) | `독립 앱` | ![Stars](https://img.shields.io/github/stars/exelban/stats?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/exelban/stats?style=flat-square&label=%20) |
| [Vorssaint Utils](https://github.com/vorssaint/vorssaint-utils) | 창 관리·볼륨·클립보드·모니터링을 통합한 macOS 메뉴 막대 앱<br>[가이드](tools/utilities/vorssaint-utils.md) · [시연](https://github.com/vorssaint/vorssaint-utils/blob/main/docs/assets/readme/window-switcher.gif) | `독립 앱` | ![Stars](https://img.shields.io/github/stars/vorssaint/vorssaint-utils?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/vorssaint/vorssaint-utils?style=flat-square&label=%20) |
| [Yazi](https://github.com/sxyazi/yazi) 🧑‍💻 | 비동기 파일 탐색·미리보기·플러그인을 지원하는 Rust 터미널 파일 관리자<br>[가이드](tools/utilities/yazi.md) · [시연](https://github.com/sxyazi/yazi) | `독립 CLI` | ![Stars](https://img.shields.io/github/stars/sxyazi/yazi?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/sxyazi/yazi?style=flat-square&label=%20) |

## Cool Finds

당장 데일리 셋업에 넣거나 추천 목록으로 승격하지는 않았지만, 흥미로워서 기록한 프로젝트입니다. **설치·업데이트·삭제 가이드와 사용 검증은 제공하지 않습니다.**

**[Kilobat CLI](https://github.com/seifip/kilobat-cli)**: JSON 출력을 지원하는 macOS 네트워크 진단 CLI와 로컬 stdio MCP 서버입니다. CLI는 GPL-3.0-only이며 별도의 데스크톱 앱은 독점 소프트웨어입니다.

**[ArtCraft](https://getartcraft.com/)**: 오픈소스 창작 도구 생태계입니다. AI 이미지·영상 제작을 위한 [ArtCraft Studio](https://github.com/storytold/artcraft)와 앱 설치·업데이트를 돕는 [ArtCraft Launcher](https://github.com/storytold/craft-launcher)를 비롯해 아래 Crafting Apps를 제공합니다. [전체 제품 소개](https://getartcraft.com/apps)를 참고하세요.

| 제작 도구 | 무엇을 하나요? |
|---|---|
| [PhotoCraft](https://github.com/storytold/photocraft) | 이미지·레이어·PSD 편집 |
| [VectorCraft](https://github.com/storytold/vectorcraft) | 벡터 일러스트 제작 |
| [FilmCraft](https://github.com/storytold/filmcraft) | 영상 편집·색 보정·사운드 |
| [LightCraft](https://github.com/storytold/lightcraft) | 사진 라이브러리·RAW 현상 |
| [PdfCraft](https://github.com/storytold/pdfcraft) | PDF 읽기·정리·병합·보호 |
| [EffectCraft](https://github.com/storytold/effectcraft) | 모션 그래픽·시각 효과 |
| [DesignCraft](https://github.com/storytold/designcraft) | 페이지 레이아웃·출판물 제작 |
| [FigCraft](https://github.com/storytold/figcraft) | UI 디자인·프로토타이핑 |
| [TextureCraft](https://github.com/storytold/texturecraft) | 3D 텍스처 페인팅 |
| [MaterialCraft](https://github.com/storytold/materialcraft) | 노드 기반 절차적 재질 제작 |
| [WordCraft](https://github.com/storytold/wordcraft) | 문서 작성·워드 프로세싱 |
| [SoundCraft](https://github.com/storytold/soundcraft) | 오디오 녹음·편집·믹싱 |
| [DeckCraft](https://github.com/storytold/deckcraft) | 프레젠테이션·슬라이드 제작 |
| [CADCraft](https://github.com/storytold/cadcraft) | CAD 설계·도면 작성 |
| [GridCraft](https://github.com/storytold/gridcraft) | 스프레드시트·데이터 분석 |
| [Craft Anything](https://github.com/storytold/craft-anything) | 소프트웨어 분석·유사 구현 |

*앱별 개발 단계와 지원 플랫폼은 서로 다릅니다. 이 목록은 존재와 용도만 소개하며, 완성도·안전성·에이전트 호환성을 보증하지 않습니다.*

**[Replay Theater](https://github.com/anthropics/claude-code-playground/tree/main/claude-code/mods/replay-theater)**: Claude Code에서 마지막 턴의 파일 편집을 순서대로 넘기며 각 단계의 diff를 검토하는 시각화 Mod입니다. `/replay`로 열 수 있으며, 실제 편집을 되돌리는 기능은 아닙니다. 모드 설치·실행은 아직 검증하지 않았습니다.

**[wterm](https://github.com/vercel-labs/wterm)**: Vercel Labs의 웹 터미널 에뮬레이터입니다. Zig·WASM 코어와 DOM 렌더링을 사용하며, React·Vue·Svelte 연동 및 선택형 Ghostty 기반 터미널 코어를 제공합니다.

## Archived · 추천 제외

[추천 제외 도구와 사유 보기](archive/README.md). 제외는 개인적인 큐레이션 판단이며 원본 프로젝트가 중단되었다는 뜻은 아닙니다.

## 기여와 관리

문서 변경 시 [AGENTS.md의 검토 체크리스트](AGENTS.md#documentation-review-checklist)를 확인합니다. `python3 scripts/validate.py`는 필요할 때 실행하는 선택적 검증 도구이며, GitHub Actions는 수동 실행만 지원합니다. Push·PR에 자동 CI가 실행되거나 성공 판정이 요구되지는 않습니다. 실제 확인한 항목과 미검증 사항을 변경 결과에 명시합니다.

도구를 추가·갱신·제외하려면 [CONTRIBUTING.md](CONTRIBUTING.md)와 [AGENTS.md](AGENTS.md)의 절차를 참고하세요.

## 라이선스

이 저장소에는 [MIT 라이선스](LICENSE)가 적용됩니다. 연결된 외부 프로젝트에는 각각의 라이선스가 적용됩니다.

