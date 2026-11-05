# awesome-agent-tools

[한국어](README.md) | [English](README.en.md)

A curated collection of **AI coding-agent skills, plugins, mods, MCP servers, and developer tools** with agent-friendly lifecycle guides.

> English edition. [한국어 기본 카탈로그](README.md). This is a curated list, not a compatibility or security guarantee.

**Privacy & network audit:** See [Privacy, Telemetry & Updates](docs/privacy-and-updates.md) for telemetry, update checks and opt-outs across all 38 active entries. Unknowns remain explicitly marked.

**🧑‍💻 = A tool currently in My Daily Setup.** Shown only in the general catalog; it is not a quality rating or compatibility guarantee.

## Quick start

For tool additions, removal, or guide maintenance, an agent should first read [AGENTS.md](AGENTS.md). You can give the agent a GitHub URL and ask it to add, update, archive, or remove that entry.

1. Find a tool by capability below.
2. Open its **Guide** for requirements and install/update/uninstall/verification notes.
3. Ask your coding agent: **"Read AGENTS.md and tools/<category>/<tool>.md in this repository. Inspect my current environment, propose changes, ask before writing or deleting, then install and verify."**
4. For removal, ask the agent to preserve unrelated settings and to explain the rollback.

## Curation status

- **Active:** Tools currently featured as worth exploring.
- **Archived:** Tools removed from active recommendations, with [reasons preserved](archive/README.md).

**Verification details are kept in individual guides, not the public index.** Verification status: `personal` = reported hands-on use, `metadata` = upstream installation/metadata reviewed, `trial` = currently trying, `unverified` = candidate not yet confirmed. No tool in this initial import is marked independently benchmarked. Maintainer-owned tools appear separately under **My Works** and are disclosed as such. **Install modes:** `cli`, `agent-guide`, `manual-review`.

**GitHub activity:** Stars and Last Commit badges are fetched live from Shields.io for GitHub repositories. They are **not historical snapshots**, may be delayed by caching, and do not determine quality or inclusion. “Last Commit” means latest commit on the upstream repository’s default branch, not the date this guide was verified. Non-GitHub sources are shown as `—`.

**Agent tags:** Claude Code, Codex and Hermes badges indicate documented agent-specific support. The **Skills CLI** badge means the skill provides a documented installation path using `npx skills`, which supports many agent hosts; it does not guarantee runtime compatibility with every host. Standalone programs are labeled `Standalone CLI`, `Standalone app`, or `SDK / Platform` instead of being presented as unsupported agents. Unknown integrations remain `—`. MCP badges indicate protocol connectivity, not tested authentication or tool operation.

**Scope:** agent-related extensions first, adjacent developer utilities second. Personal terminal colors, fonts, local paths, and unsafe wrapper commands are deliberately excluded.

## My Daily Setup

Tools reported as actively used (as of 2026-11-03). This is separate from recommendations and may vary by environment.

| Tool | Purpose |
|---|---|
| [TigerKit](https://github.com/MTGVim/tiger-kit) | Development, review and verification skills across Claude Code, Codex and Hermes |
| [Orca](https://github.com/stablyai/orca) | Parallel agent workspace |
| [Autoharness](https://github.com/tigerless-labs/autoharness) | Skill lifecycle manager |
| [Subagent Tuner](https://github.com/Kruhlikau/subagent-tuner) | Subagent model and effort tuning |
| [Agent Usage Guard](https://github.com/rbartoli/agent-usage-guard) | Agent usage guardrails with a compact-before-send option |
| [Codegraph](https://github.com/colbymchenry/codegraph) | Code graph exploration |
| [Ponytail](https://github.com/dietrichgebert/ponytail) | Overengineering guard |
| [Cache Tax](https://github.com/karanb192/cache-tax) | Prompt cache maintenance |
| [Engram](https://github.com/Gentleman-Programming/engram) | Cross-session memory |
| [Claude Show Your Work](https://github.com/iamumeransari/claude-show-your-work) | Media and visual QA |
| [Claude Code Paste Preview](https://github.com/alan890104/claude-code-paste-preview) | Image preview and annotation |
| [Claude Flightdeck](https://github.com/scasella/claude-flightdeck) | Subagent status cockpit |
| [Claude HUD](https://github.com/jarrodwatts/claude-hud) | Usage and context statusLine |
| [Prompt Rail](https://github.com/oikon48/prompt-rail) | Prompt history navigation |
| [ni](https://github.com/antfu-collective/ni) | Unified package manager commands |
| [Peon Ping](https://github.com/PeonPing/peon-ping) | Task notifications |
| [abtop](https://github.com/graykode/abtop) | Terminal resource monitor |
| [Yazi](https://github.com/sxyazi/yazi) | Terminal file manager |

### Setup notes

- **[abtop](tools/utilities/abtop.md):** Generating session titles and summaries can invoke `claude --print` and consume extra model tokens. Consider `ANTHROPIC_MODEL=haiku abtop` to select a lower-cost model, and verify that the model override actually takes effect in your environment.


These are adjustments and caveats from this particular environment. For installation, updates and removal, see the tool guides in the catalog below.

- **[Show Your Work](tools/browser/claude-show-your-work.md):** If Prismantis is also enabled, place Show Your Work before it in Claude Code's `enabledPlugins` ordering. This is an observed ordering workaround, not a guarantee of renderer interoperability. Disable usage statistics through `/show-your-work` → **Don't share**, or `SHOW_YOUR_WORK_TELEMETRY=0`. Set `SHOW_YOUR_WORK_AUTO_UPDATE=0` to disable its own version checks and updates.
- **[Paste Preview](tools/ui/claude-code-paste-preview.md):** It shares the image-preview region with Image View; enable one at a time.
- **[Flightdeck](tools/ui/claude-flightdeck.md):** Its side panel overlaps with Glowup. Use `motion: while-active` for pulses.
- **[Claude HUD](tools/ui/claude-hud.md):** Configuring `statusLine` is its intended behavior. Check only whether another plugin replaces an existing setting.
- **[Cache Tax](tools/context/cache-tax.md):** Cache warming uses tokens. Review `idleCompaction` when using `/keepwarm`.

## My Works

Projects maintained by the curator are listed separately from third-party recommendations. Inclusion is the curator's decision, not an independent endorsement.

| Tool | Description · Guide | Agents | GitHub Activity |
|---|---|---|---|
| [TigerKit](https://github.com/MTGVim/tiger-kit) 🧑‍💻 | Development, review and verification skills for Claude Code, Codex and Hermes<br>[Guide](tools/workflows/tigerkit.md) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) ![Codex](https://img.shields.io/badge/Codex-111111?style=flat-square&logo=openai&logoColor=white) ![Hermes](https://img.shields.io/badge/Hermes-9A641C?style=flat-square) [![Skills CLI](https://img.shields.io/badge/Skills_CLI-multi--agent-5965A8?style=flat-square)](https://github.com/vercel-labs/skills) | ![Stars](https://img.shields.io/github/stars/MTGVim/tiger-kit?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/MTGVim/tiger-kit?style=flat-square&label=%20) |

## Workflow & Agents

| Tool | Description · Guide | Agents | GitHub Activity |
|---|---|---|---|
| [Orca](https://github.com/stablyai/orca) 🧑‍💻 | AI development workspace for parallel agents, worktrees, editing and review<br>[Guide](tools/workflows/orca.md) · [Demo](https://github.com/stablyai/orca/blob/main/docs/assets/readme-hero.jpg) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) ![Codex](https://img.shields.io/badge/Codex-111111?style=flat-square&logo=openai&logoColor=white) ![Hermes](https://img.shields.io/badge/Hermes-9A641C?style=flat-square) | ![Stars](https://img.shields.io/github/stars/stablyai/orca?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/stablyai/orca?style=flat-square&label=%20) |
| [Autoharness](https://github.com/tigerless-labs/autoharness) 🧑‍💻 | Learns, merges, updates and prunes skills from Claude Code sessions<br>[Guide](tools/workflows/autoharness.md) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) | ![Stars](https://img.shields.io/github/stars/tigerless-labs/autoharness?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/tigerless-labs/autoharness?style=flat-square&label=%20) |
| [Skill Creator](https://github.com/openai/skills) | Codex skill authoring tool; original openai/skills repository is deprecated<br>[Guide](tools/workflows/skill-creator.md) | ![Codex](https://img.shields.io/badge/Codex-111111?style=flat-square&logo=openai&logoColor=white) | ![Stars](https://img.shields.io/github/stars/openai/skills?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/openai/skills?style=flat-square&label=%20) |
| [Subagent Tuner](https://github.com/Kruhlikau/subagent-tuner) 🧑‍💻 | Chooses models and reasoning effort per Claude Code subagent<br>[Guide](tools/workflows/subagent-tuner.md) · [Demo](https://github.com/Kruhlikau/subagent-tuner/blob/main/docs/media/demo.gif) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) | ![Stars](https://img.shields.io/github/stars/Kruhlikau/subagent-tuner?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/Kruhlikau/subagent-tuner?style=flat-square&label=%20) |
| [Autoharness Codex](https://github.com/arm092/autoharness-codex) | Learns, verifies and consolidates skills from Codex sessions<br>[Guide](tools/workflows/autoharness-codex.md) | ![Codex](https://img.shields.io/badge/Codex-111111?style=flat-square&logo=openai&logoColor=white) | ![Stars](https://img.shields.io/github/stars/arm092/autoharness-codex?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/arm092/autoharness-codex?style=flat-square&label=%20) |
| [Darwin Skill](https://github.com/alchaincyf/darwin-skill) | Optimizes Agent Skills through repeated experiments and evaluation<br>[Guide](tools/workflows/darwin-skill.md) | [![Skills CLI](https://img.shields.io/badge/Skills_CLI-multi--agent-5965A8?style=flat-square)](https://github.com/vercel-labs/skills) | ![Stars](https://img.shields.io/github/stars/alchaincyf/darwin-skill?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/alchaincyf/darwin-skill?style=flat-square&label=%20) |
| [MCP Atlassian](https://github.com/sooperset/mcp-atlassian) | Connects Jira and Confluence issues and pages through MCP<br>[Guide](tools/workflows/mcp-atlassian.md) · [Demo](https://github.com/sooperset/mcp-atlassian#quick-start) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) ![Codex](https://img.shields.io/badge/Codex-111111?style=flat-square&logo=openai&logoColor=white) ![Hermes](https://img.shields.io/badge/Hermes-9A641C?style=flat-square) | ![Stars](https://img.shields.io/github/stars/sooperset/mcp-atlassian?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/sooperset/mcp-atlassian?style=flat-square&label=%20) |
| [Next Steps](https://github.com/anthropics/claude-plugins-community) | Adds actionable next-step suggestions to Claude Code replies<br>[Guide](tools/workflows/next-steps.md) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) | ![Stars](https://img.shields.io/github/stars/anthropics/claude-plugins-community?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/anthropics/claude-plugins-community?style=flat-square&label=%20) |
| [Skill Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) | Converts documentation, repos, PDFs and videos into skills and RAG data<br>[Guide](tools/workflows/skill-seekers.md) | `Standalone CLI` | ![Stars](https://img.shields.io/github/stars/yusufkaraaslan/Skill_Seekers?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/yusufkaraaslan/Skill_Seekers?style=flat-square&label=%20) |

## Coding & Code Intelligence

| Tool | Description · Guide | Agents | GitHub Activity |
|---|---|---|---|
| [Code Modernization](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/code-modernization) | Modernizes legacy code and checks behavioral equivalence<br>[Guide](tools/coding/code-modernization.md) · [Demo](https://github.com/anthropics/claude-plugins-official/blob/main/plugins/code-modernization/assets/media/report-glance.jpg) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) | ![Stars](https://img.shields.io/github/stars/anthropics/claude-plugins-official?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/anthropics/claude-plugins-official?style=flat-square&label=%20) |
| [Codegraph](https://github.com/colbymchenry/codegraph) 🧑‍💻 | Builds local semantic code graphs for coding agents<br>[Guide](tools/coding/codegraph.md) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) ![Codex](https://img.shields.io/badge/Codex-111111?style=flat-square&logo=openai&logoColor=white) ![Hermes](https://img.shields.io/badge/Hermes-9A641C?style=flat-square) | ![Stars](https://img.shields.io/github/stars/colbymchenry/codegraph?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/colbymchenry/codegraph?style=flat-square&label=%20) |
| [Ponytail](https://github.com/dietrichgebert/ponytail) 🧑‍💻 | Promotes lean code and review instead of overengineering<br>[Guide](tools/coding/ponytail.md) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) ![Codex](https://img.shields.io/badge/Codex-111111?style=flat-square&logo=openai&logoColor=white) | ![Stars](https://img.shields.io/github/stars/dietrichgebert/ponytail?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/dietrichgebert/ponytail?style=flat-square&label=%20) |

## Context & Sessions

| Tool | Description · Guide | Agents | GitHub Activity |
|---|---|---|---|
| [Agent Usage Guard](https://github.com/rbartoli/agent-usage-guard) 🧑‍💻 | Guards against excessive Claude Code agents, retries and usage<br>[Guide](tools/context/agent-usage-guard.md) · [Demo](https://github.com/rbartoli/agent-usage-guard) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) | ![Stars](https://img.shields.io/github/stars/rbartoli/agent-usage-guard?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/rbartoli/agent-usage-guard?style=flat-square&label=%20) |
| [Cache Tax](https://github.com/karanb192/cache-tax) 🧑‍💻 | Keeps Claude Code prompt caches warm and warns about expiration costs<br>[Guide](tools/context/cache-tax.md) · [Demo](https://github.com/karanb192/cache-tax/blob/main/site/assets/refusal.gif) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) | ![Stars](https://img.shields.io/github/stars/karanb192/cache-tax?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/karanb192/cache-tax?style=flat-square&label=%20) |
| [Engram](https://github.com/Gentleman-Programming/engram) 🧑‍💻 | Persistent project-aware memory and search for coding agents<br>[Guide](tools/context/engram.md) · [Demo](https://github.com/Gentleman-Programming/engram/blob/main/assets/tui-dashboard.png) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) ![Codex](https://img.shields.io/badge/Codex-111111?style=flat-square&logo=openai&logoColor=white) ![Hermes](https://img.shields.io/badge/Hermes-9A641C?style=flat-square) | ![Stars](https://img.shields.io/github/stars/Gentleman-Programming/engram?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/Gentleman-Programming/engram?style=flat-square&label=%20) |

## Browser & QA

| Tool | Description · Guide | Agents | GitHub Activity |
|---|---|---|---|
| [Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp) | Exposes Chrome debugging, performance analysis and automation via MCP and CLI<br>[Guide](tools/browser/chrome-devtools-mcp.md) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) ![Codex](https://img.shields.io/badge/Codex-111111?style=flat-square&logo=openai&logoColor=white) ![Hermes](https://img.shields.io/badge/Hermes-9A641C?style=flat-square) | ![Stars](https://img.shields.io/github/stars/ChromeDevTools/chrome-devtools-mcp?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/ChromeDevTools/chrome-devtools-mcp?style=flat-square&label=%20) |
| [Claude Show Your Work](https://github.com/iamumeransari/claude-show-your-work) 🧑‍💻 | Shows images, video and Playwright QA inside Claude Code<br>[Guide](tools/browser/claude-show-your-work.md) · [Demo](https://github.com/iamumeransari/claude-show-your-work/blob/main/docs/homepage.jpg) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) | ![Stars](https://img.shields.io/github/stars/iamumeransari/claude-show-your-work?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/iamumeransari/claude-show-your-work?style=flat-square&label=%20) |
| [Cua](https://github.com/trycua/cua) | Agent computer environments, GUI drivers and computer-use SDKs<br>[Guide](tools/browser/cua.md) | `SDK / Platform` | ![Stars](https://img.shields.io/github/stars/trycua/cua?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/trycua/cua?style=flat-square&label=%20) |

## Terminal UI

| Tool | Description · Guide | Agents | GitHub Activity |
|---|---|---|---|
| [AgentsView](https://github.com/kenn-io/agentsview) | Search coding-agent sessions and analyze token costs and tool-call patterns<br>[Guide](tools/ui/agentsview.md) | `독립 앱 / CLI` | ![Stars](https://img.shields.io/github/stars/kenn-io/agentsview?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/kenn-io/agentsview?style=flat-square&label=%20) |
| [Claude Code Filetree](https://github.com/data-goblin/claude-code-filetree) | Live highlights of files Claude reads and edits, with Git status and diffs<br>[Guide](tools/ui/claude-code-filetree.md) · [Demo](https://github.com/data-goblin/claude-code-filetree/blob/main/media/filetree-shimmer.gif) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) | ![Stars](https://img.shields.io/github/stars/data-goblin/claude-code-filetree?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/data-goblin/claude-code-filetree?style=flat-square&label=%20) |
| [Claude Code Mods](https://github.com/hamzafer/claude-code-mods) | Interactive installer of Claude Code mods, hooks and UI extensions<br>[Guide](tools/ui/claude-code-mods.md) · [Demo](https://github.com/hamzafer/claude-code-mods/blob/main/images/mission-control.gif) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) | ![Stars](https://img.shields.io/github/stars/hamzafer/claude-code-mods?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/hamzafer/claude-code-mods?style=flat-square&label=%20) |
| [Claude Code Paste Preview](https://github.com/alan890104/claude-code-paste-preview) 🧑‍💻 | Previews and annotates pasted images before submitting<br>[Guide](tools/ui/claude-code-paste-preview.md) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) | ![Stars](https://img.shields.io/github/stars/alan890104/claude-code-paste-preview?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/alan890104/claude-code-paste-preview?style=flat-square&label=%20) |
| [Claude Flightdeck](https://github.com/scasella/claude-flightdeck) 🧑‍💻 | Real-time Claude Code dashboard of context, cost, permissions and agents<br>[Guide](tools/ui/claude-flightdeck.md) · [Demo](https://github.com/scasella/claude-flightdeck/blob/main/docs/media/demo.gif) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) | ![Stars](https://img.shields.io/github/stars/scasella/claude-flightdeck?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/scasella/claude-flightdeck?style=flat-square&label=%20) |
| [Claude HUD](https://github.com/jarrodwatts/claude-hud) 🧑‍💻 | Claude Code status line for usage, context and active tools<br>[Guide](tools/ui/claude-hud.md) · [Demo](https://github.com/jarrodwatts/claude-hud/blob/main/claude-hud-preview-5-2.png) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) | ![Stars](https://img.shields.io/github/stars/jarrodwatts/claude-hud?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/jarrodwatts/claude-hud?style=flat-square&label=%20) |
| [Claude Image View](https://github.com/jarrodwatts/claude-image-view) | Shows original-aspect thumbnails of pasted images<br>[Guide](tools/ui/claude-image-view.md) · [Demo](https://github.com/jarrodwatts/claude-image-view/blob/main/claude-image-view.png) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) | ![Stars](https://img.shields.io/github/stars/jarrodwatts/claude-image-view?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/jarrodwatts/claude-image-view?style=flat-square&label=%20) |
| [Prompt Rail](https://github.com/oikon48/prompt-rail) 🧑‍💻 | Previews past prompts and jumps to transcript turns<br>[Guide](tools/ui/prompt-rail.md) · [Demo](https://github.com/oikon48/prompt-rail/blob/main/docs/demo.gif) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) | ![Stars](https://img.shields.io/github/stars/oikon48/prompt-rail?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/oikon48/prompt-rail?style=flat-square&label=%20) |
| [Savvy Progress](https://github.com/JohnnyVizz/claude-kit/tree/main/plugins/savvy-progress) | Claude Code progress bar and agent panel showing models, context and estimated cost<br>[Guide](tools/ui/savvy-progress.md) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) | ![Stars](https://img.shields.io/github/stars/JohnnyVizz/claude-kit?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/JohnnyVizz/claude-kit?style=flat-square&label=%20) |

## Visual & Content

| Tool | Description · Guide | Agents | GitHub Activity |
|---|---|---|---|
| [Archify](https://github.com/tt-a1i/archify) | Creates explorable interactive HTML for explanations, plans and code<br>[Guide](tools/visual/archify.md) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) ![Codex](https://img.shields.io/badge/Codex-111111?style=flat-square&logo=openai&logoColor=white) ![Hermes](https://img.shields.io/badge/Hermes-9A641C?style=flat-square) [![Skills CLI](https://img.shields.io/badge/Skills_CLI-multi--agent-5965A8?style=flat-square)](https://github.com/vercel-labs/skills) | ![Stars](https://img.shields.io/github/stars/tt-a1i/archify?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/tt-a1i/archify?style=flat-square&label=%20) |
| [Frontend Slides](https://github.com/zarazhangrui/frontend-slides) | Skill for HTML presentations, visual style selection and PPT conversion<br>[Guide](tools/visual/frontend-slides.md) · [Demo](https://www.youtube.com/watch?v=372Iksaz8b0) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) | ![Stars](https://img.shields.io/github/stars/zarazhangrui/frontend-slides?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/zarazhangrui/frontend-slides?style=flat-square&label=%20) |
| [Prismantis](https://github.com/NahumLitvin/prismantis) | Renders tables, code, Mermaid, charts and LaTeX in Claude Code<br>[Guide](tools/visual/prismantis.md) · [Demo](https://github.com/NahumLitvin/prismantis/blob/main/docs/tour.gif) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) ![Codex](https://img.shields.io/badge/Codex-111111?style=flat-square&logo=openai&logoColor=white) | ![Stars](https://img.shields.io/github/stars/NahumLitvin/prismantis?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/NahumLitvin/prismantis?style=flat-square&label=%20) |

## Design

| Tool | Description · Guide | Agents | GitHub Activity |
|---|---|---|---|
| [Figma Desktop MCP](https://developers.figma.com/docs/figma-mcp-server/local-server-installation/) | Exposes Figma desktop Dev Mode design context and assets via MCP<br>[Guide](tools/design/figma-desktop-mcp.md) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) ![Codex](https://img.shields.io/badge/Codex-111111?style=flat-square&logo=openai&logoColor=white) ![Hermes](https://img.shields.io/badge/Hermes-9A641C?style=flat-square) | — |
| [Open Design](https://github.com/nexu-io/open-design) | Collaborative AI design workspace for prototypes, apps and slides<br>[Guide](tools/design/open-design.md) · [Demo](https://github.com/nexu-io/open-design/blob/main/docs/assets/readme-hero-design-agent.webp) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) ![Codex](https://img.shields.io/badge/Codex-111111?style=flat-square&logo=openai&logoColor=white) ![Hermes](https://img.shields.io/badge/Hermes-9A641C?style=flat-square) | ![Stars](https://img.shields.io/github/stars/nexu-io/open-design?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/nexu-io/open-design?style=flat-square&label=%20) |

## Developer Utilities

| Tool | Description · Guide | Agents | GitHub Activity |
|---|---|---|---|
| [OpenShip](https://github.com/oblien/openship) | Self-hosted CI/CD platform for build, deploy, routing and TLS<br>[Guide](tools/utilities/openship.md) · [Demo](https://github.com/oblien/openship/blob/main/docs/screenshots/screen.png) | `Standalone app` | ![Stars](https://img.shields.io/github/stars/oblien/openship?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/oblien/openship?style=flat-square&label=%20) |
| [ni](https://github.com/antfu-collective/ni) 🧑‍💻 | Runs the appropriate npm, pnpm, yarn or bun commands<br>[Guide](tools/utilities/ni.md) | `Standalone CLI` | ![Stars](https://img.shields.io/github/stars/antfu-collective/ni?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/antfu-collective/ni?style=flat-square&label=%20) |
| [Peon Ping](https://github.com/PeonPing/peon-ping) 🧑‍💻 | Game voice and overlay alerts for agent completion and approvals<br>[Guide](tools/utilities/peon-ping.md) · [Demo](https://github.com/PeonPing/peon-ping/blob/main/docs/peon-hero.gif) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) ![Codex](https://img.shields.io/badge/Codex-111111?style=flat-square&logo=openai&logoColor=white) | ![Stars](https://img.shields.io/github/stars/PeonPing/peon-ping?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/PeonPing/peon-ping?style=flat-square&label=%20) |
| [abtop](https://github.com/graykode/abtop) 🧑‍💻 | TUI monitoring tokens, limits and processes across coding agents<br>[Guide](tools/utilities/abtop.md) · [Demo](https://github.com/graykode/abtop/blob/main/assets/demo.gif) | ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) ![Codex](https://img.shields.io/badge/Codex-111111?style=flat-square&logo=openai&logoColor=white) | ![Stars](https://img.shields.io/github/stars/graykode/abtop?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/graykode/abtop?style=flat-square&label=%20) |
| [Stats](https://github.com/exelban/stats) | macOS menu-bar CPU, GPU, memory and network monitor<br>[Guide](tools/utilities/stats.md) · [Demo](https://github.com/exelban/stats) | `Standalone app` | ![Stars](https://img.shields.io/github/stars/exelban/stats?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/exelban/stats?style=flat-square&label=%20) |
| [Vorssaint Utils](https://github.com/vorssaint/vorssaint-utils) | macOS menu bar toolkit for windows, sound, clipboard and monitoring<br>[Guide](tools/utilities/vorssaint-utils.md) · [Demo](https://github.com/vorssaint/vorssaint-utils/blob/main/docs/assets/readme/window-switcher.gif) | `Standalone app` | ![Stars](https://img.shields.io/github/stars/vorssaint/vorssaint-utils?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/vorssaint/vorssaint-utils?style=flat-square&label=%20) |
| [Yazi](https://github.com/sxyazi/yazi) 🧑‍💻 | Asynchronous Rust terminal file manager with previews and plugins<br>[Guide](tools/utilities/yazi.md) · [Demo](https://github.com/sxyazi/yazi) | `Standalone CLI` | ![Stars](https://img.shields.io/github/stars/sxyazi/yazi?style=flat-square&label=%20)<br>![Last commit](https://img.shields.io/github/last-commit/sxyazi/yazi?style=flat-square&label=%20) |

## Cool Finds

Interesting projects noted for later exploration, **not yet promoted to the main recommendations or Daily Setup**. These finds do not come with verified installation, update or removal guides.

**[Kilobat CLI](https://github.com/seifip/kilobat-cli)**: macOS network diagnostics CLI with JSON output and a local stdio MCP server. The CLI is GPL-3.0-only; the separate desktop app is proprietary.

**[ArtCraft](https://getartcraft.com/)**: An open-source creative software ecosystem, including [ArtCraft Studio](https://github.com/storytold/artcraft) for AI image and video production and [ArtCraft Launcher](https://github.com/storytold/craft-launcher) for installing and updating apps. See the [full lineup](https://getartcraft.com/apps).

| Crafting app | What it does |
|---|---|
| [PhotoCraft](https://github.com/storytold/photocraft) | Photo editing, layers and PSD files |
| [VectorCraft](https://github.com/storytold/vectorcraft) | Vector illustration |
| [FilmCraft](https://github.com/storytold/filmcraft) | Video editing, color and sound |
| [LightCraft](https://github.com/storytold/lightcraft) | Photo library and RAW processing |
| [PdfCraft](https://github.com/storytold/pdfcraft) | PDF reading, organizing and protection |
| [EffectCraft](https://github.com/storytold/effectcraft) | Motion graphics and VFX |
| [DesignCraft](https://github.com/storytold/designcraft) | Page layout and publishing |
| [FigCraft](https://github.com/storytold/figcraft) | Interface design and prototyping |
| [TextureCraft](https://github.com/storytold/texturecraft) | 3D texture painting |
| [MaterialCraft](https://github.com/storytold/materialcraft) | Node-based procedural materials |
| [WordCraft](https://github.com/storytold/wordcraft) | Word processing and documents |
| [SoundCraft](https://github.com/storytold/soundcraft) | Audio recording, editing and mixing |
| [DeckCraft](https://github.com/storytold/deckcraft) | Presentations and slide decks |
| [CADCraft](https://github.com/storytold/cadcraft) | CAD modeling and drafting |
| [GridCraft](https://github.com/storytold/gridcraft) | Spreadsheets and data analysis |
| [Craft Anything](https://github.com/storytold/craft-anything) | Software exploration and recreation |

*Development maturity and supported platforms vary by app. Inclusion here does not certify quality, security, or agent compatibility.*

**[Replay Theater](https://github.com/anthropics/claude-code-playground/tree/main/claude-code/mods/replay-theater)**: A Claude Code visualization mod for stepping through the previous turn's file edits and inspecting each diff with `/replay`. It does not undo edits; installation and runtime behavior have not been independently tested.

**[wterm](https://github.com/vercel-labs/wterm)**: A web terminal emulator from Vercel Labs with a Zig/WASM core, DOM rendering, React/Vue/Svelte integrations, and an optional Ghostty-powered terminal core.

## Archived

[Archived tools and reasons](archive/README.md). Archived does not necessarily mean the upstream project is abandoned; it may simply be unsuitable for this curator's workflow.

## Contribute

Review documentation changes against the [maintenance checklist](AGENTS.md#documentation-review-checklist). `python3 scripts/validate.py` is an optional structural check, and GitHub Actions can be triggered manually when useful. There is no automatic push/PR CI or required passing workflow. Report checks performed and outstanding uncertainties.

See [CONTRIBUTING.md](CONTRIBUTING.md). All tool documentation is a point-in-time snapshot; check upstream before running commands.

## License

The repository is licensed under [MIT](LICENSE). Each linked project retains its own license.
