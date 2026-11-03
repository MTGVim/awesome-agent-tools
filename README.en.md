# awesome-agent-tools

[한국어](README.md) | [English](README.en.md)

A curated collection of **AI coding-agent skills, plugins, mods, MCP servers, and developer tools** with agent-friendly lifecycle guides.

> English edition. [Korean full catalog](README.md). Recommendations are subjective, not blanket compatibility guarantees.

## Quick start

For tool additions, removal, re-tiering, or guide maintenance, an agent should first read [AGENTS.md](AGENTS.md). You can give the agent a GitHub URL and ask it to add, update, archive, or remove that entry.

1. Find a tool by capability below.
2. Open its **Guide** for requirements and install/update/uninstall/verification notes.
3. Ask your coding agent: **"Read AGENTS.md and tools/<category>/<tool>.md in this repository. Inspect my current environment, propose changes, ask before writing or deleting, then install and verify."**
4. For removal, ask the agent to preserve unrelated settings and to explain the rollback.

## Recommendation tiers

| Tier | Meaning |
|---|---|
| **S** | Strongly recommended after repeated practical verification |
| **A** | Recommended for a clear use case; may be based on hands-on experience |
| **B** | Worth evaluating; including untested candidates |
| **Archived** | Removed from recommendations, with a retained reason in [archive/](archive/) |

**Verification details are kept in individual guides, not the public index.** Verification is independent of tier: `personal` = reported hands-on use, `metadata` = upstream installation/metadata reviewed, `trial` = currently trying, `unverified` = candidate not yet confirmed. No tool in this initial import is marked independently benchmarked. Maintainer-owned tools appear separately under **My Works**. Their tiers are subjective curator assessments, not independent benchmarks. **Install modes:** `cli`, `agent-guide`, `manual-review`.

**GitHub activity:** Stars and Last Commit badges are fetched live from Shields.io for GitHub repositories. They are **not historical snapshots**, may be delayed by caching, and do not determine recommendation tiers. “Last Commit” means latest commit on the upstream repository’s default branch, not the date this guide was verified. Non-GitHub sources are shown as `—`.

**Agent tags:** `Claude Code`, `Codex`, `Hermes` indicate documented targets; `범용` means a generic/cross-agent tool, not confirmed support for all three.

**Scope:** agent-related extensions first, adjacent developer utilities second. Personal terminal colors, fonts, local paths, and unsafe wrapper commands are deliberately excluded.

## My Works

Projects maintained by the curator are listed separately from third-party recommendations. Inclusion and tiers are subjective, not independent endorsements.

| Tool | What it does | Type | Agents | Tier | Stars | Last Commit | Guide |
|---|---|---|---|---|---|---|---|
| [TigerKit](https://github.com/MTGVim/tiger-kit) | Agent Skills for planning, implementation, review, and verification | skill | `Claude Code` `Codex` `Hermes` | **S** | ![Stars](https://img.shields.io/github/stars/MTGVim/tiger-kit?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/MTGVim/tiger-kit?style=flat-square&label=%20) | [Guide](tools/workflows/tigerkit.md) |

## Workflow & Agents

| Tool | What it does | Type | Agents | Tier | Stars | Last Commit | Guide |
|---|---|---|---|---|---|---|---|
| [Autoharness](https://github.com/tigerless-labs/autoharness) | A harness for creating and managing agent skills | plugin/skill | `Claude Code` | **A** | ![Stars](https://img.shields.io/github/stars/tigerless-labs/autoharness?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/tigerless-labs/autoharness?style=flat-square&label=%20) | [Guide](tools/workflows/autoharness.md) |
| [Skill Creator](https://github.com/openai/skills) | Guides creation and improvement of agent skills | skill | `Codex` `범용` | **A** | ![Stars](https://img.shields.io/github/stars/openai/skills?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/openai/skills?style=flat-square&label=%20) | [Guide](tools/workflows/skill-creator.md) |
| [Subagent Tuner](https://github.com/Kruhlikau/subagent-tuner) | Adjusts models and effort for Claude Code subagents | plugin/mod | `Claude Code` | **A** | ![Stars](https://img.shields.io/github/stars/Kruhlikau/subagent-tuner?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/Kruhlikau/subagent-tuner?style=flat-square&label=%20) | [Guide](tools/workflows/subagent-tuner.md) |
| [Autoharness Codex](https://github.com/arm092/autoharness-codex) | Adapts Autoharness workflows for Codex | skill | `Codex` | **B** | ![Stars](https://img.shields.io/github/stars/arm092/autoharness-codex?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/arm092/autoharness-codex?style=flat-square&label=%20) | [Guide](tools/workflows/autoharness-codex.md) |
| [Darwin Skill](https://github.com/alchaincyf/darwin-skill) | Supports iterative skill improvement using feedback | skill | `범용` | **B** | ![Stars](https://img.shields.io/github/stars/alchaincyf/darwin-skill?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/alchaincyf/darwin-skill?style=flat-square&label=%20) | [Guide](tools/workflows/darwin-skill.md) |
| [Inbox](https://github.com/petekp/inbox) | Collects session questions and action items | plugin | `Claude Code` | **B** | ![Stars](https://img.shields.io/github/stars/petekp/inbox?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/petekp/inbox?style=flat-square&label=%20) | [Guide](tools/workflows/inbox.md) |
| [MCP Atlassian](https://github.com/sooperset/mcp-atlassian) | Connects agents to Jira and Confluence through MCP | mcp | `범용` | **B** | ![Stars](https://img.shields.io/github/stars/sooperset/mcp-atlassian?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/sooperset/mcp-atlassian?style=flat-square&label=%20) | [Guide](tools/workflows/mcp-atlassian.md) |
| [Next Steps](https://github.com/anthropics/claude-plugins-community) | Suggests actionable next steps after a task | plugin/mod | `Claude Code` | **B** | ![Stars](https://img.shields.io/github/stars/anthropics/claude-plugins-community?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/anthropics/claude-plugins-community?style=flat-square&label=%20) | [Guide](tools/workflows/next-steps.md) |
| [OpenShip](https://github.com/oblien/openship) | Explores agent-driven development workflows | tool | `범용` | **B** | ![Stars](https://img.shields.io/github/stars/oblien/openship?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/oblien/openship?style=flat-square&label=%20) | [Guide](tools/workflows/openship.md) |
| [Skill Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) | Converts documentation into agent skills | skill/tool | `범용` | **B** | ![Stars](https://img.shields.io/github/stars/yusufkaraaslan/Skill_Seekers?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/yusufkaraaslan/Skill_Seekers?style=flat-square&label=%20) | [Guide](tools/workflows/skill-seekers.md) |

## Coding & Code Intelligence

| Tool | What it does | Type | Agents | Tier | Stars | Last Commit | Guide |
|---|---|---|---|---|---|---|---|
| [Code Modernization](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/code-modernization) | Modernizes legacy code and checks behavioral changes | plugin | `Claude Code` | **B** | ![Stars](https://img.shields.io/github/stars/anthropics/claude-plugins-official?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/anthropics/claude-plugins-official?style=flat-square&label=%20) | [Guide](tools/coding/code-modernization.md) |
| [Codegraph](https://github.com/colbymchenry/codegraph) | Explores code structure and relationships as a graph | tool | `범용` | **B** | ![Stars](https://img.shields.io/github/stars/colbymchenry/codegraph?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/colbymchenry/codegraph?style=flat-square&label=%20) | [Guide](tools/coding/codegraph.md) |
| [Ponytail](https://github.com/dietrichgebert/ponytail) | Encourages simpler code and avoids overengineering | plugin/mod | `Claude Code` | **B** | ![Stars](https://img.shields.io/github/stars/dietrichgebert/ponytail?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/dietrichgebert/ponytail?style=flat-square&label=%20) | [Guide](tools/coding/ponytail.md) |

## Context & Sessions

| Tool | What it does | Type | Agents | Tier | Stars | Last Commit | Guide |
|---|---|---|---|---|---|---|---|
| [Agent Usage Guard](https://github.com/rbartoli/agent-usage-guard) | Guards against excessive subagent calls and retry loops | plugin | `Claude Code` | **B** | ![Stars](https://img.shields.io/github/stars/rbartoli/agent-usage-guard?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/rbartoli/agent-usage-guard?style=flat-square&label=%20) | [Guide](tools/context/agent-usage-guard.md) |
| [Cache Tax](https://github.com/karanb192/cache-tax) | Keeps prompt caches warm and warns about expiration costs | plugin/mod | `Claude Code` | **B** | ![Stars](https://img.shields.io/github/stars/karanb192/cache-tax?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/karanb192/cache-tax?style=flat-square&label=%20) | [Guide](tools/context/cache-tax.md) |
| [Claude Auto Handoff](https://github.com/alexknowshtml/claude-auto-handoff) | Hands off work to a new session before context fills | mod | `Claude Code` | **B** | ![Stars](https://img.shields.io/github/stars/alexknowshtml/claude-auto-handoff?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/alexknowshtml/claude-auto-handoff?style=flat-square&label=%20) | [Guide](tools/context/claude-auto-handoff.md) |
| [Engram](https://github.com/Gentleman-Programming/engram) | Stores and retrieves persistent agent memories | tool | `범용` | **B** | ![Stars](https://img.shields.io/github/stars/Gentleman-Programming/engram?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/Gentleman-Programming/engram?style=flat-square&label=%20) | [Guide](tools/context/engram.md) |
| [Session Titles](https://github.com/zhangbububu/session-titles) | Makes Claude Code sessions easier to identify by title | mod | `Claude Code` | **B** | ![Stars](https://img.shields.io/github/stars/zhangbububu/session-titles?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/zhangbububu/session-titles?style=flat-square&label=%20) | [Guide](tools/context/session-titles.md) |

## Browser & QA

| Tool | What it does | Type | Agents | Tier | Stars | Last Commit | Guide |
|---|---|---|---|---|---|---|---|
| [Orca](https://github.com/stablyai/orca) | Automates computer use through desktop interaction | tool | `범용` | **A** | ![Stars](https://img.shields.io/github/stars/stablyai/orca?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/stablyai/orca?style=flat-square&label=%20) | [Guide](tools/browser/orca.md) |
| [Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp) | Exposes Chrome debugging capabilities through MCP | mcp | `범용` | **B** | ![Stars](https://img.shields.io/github/stars/ChromeDevTools/chrome-devtools-mcp?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/ChromeDevTools/chrome-devtools-mcp?style=flat-square&label=%20) | [Guide](tools/browser/chrome-devtools-mcp.md) |
| [Claude Show Your Work](https://github.com/iamumeransari/claude-show-your-work) | Previews media and test results in the terminal | plugin | `Claude Code` | **B** | ![Stars](https://img.shields.io/github/stars/iamumeransari/claude-show-your-work?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/iamumeransari/claude-show-your-work?style=flat-square&label=%20) | [Guide](tools/browser/claude-show-your-work.md) |
| [Cua](https://github.com/trycua/cua) | Automates computer use with screen and input control | tool | `범용` | **B** | ![Stars](https://img.shields.io/github/stars/trycua/cua?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/trycua/cua?style=flat-square&label=%20) | [Guide](tools/browser/cua.md) |

## Terminal UI

| Tool | What it does | Type | Agents | Tier | Stars | Last Commit | Guide |
|---|---|---|---|---|---|---|---|
| [Claude Code Filetree](https://github.com/data-goblin/claude-code-filetree) | Shows a file tree with Git state and active files | mod | `Claude Code` | **B** | ![Stars](https://img.shields.io/github/stars/data-goblin/claude-code-filetree?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/data-goblin/claude-code-filetree?style=flat-square&label=%20) | [Guide](tools/ui/claude-code-filetree.md) |
| [Claude Code Mods](https://github.com/hamzafer/claude-code-mods) | Collects mods that extend Claude Code UI and behavior | mod | `Claude Code` | **B** | ![Stars](https://img.shields.io/github/stars/hamzafer/claude-code-mods?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/hamzafer/claude-code-mods?style=flat-square&label=%20) | [Guide](tools/ui/claude-code-mods.md) |
| [Claude Code Paste Preview](https://github.com/alan890104/claude-code-paste-preview) | Previews and annotates pasted images before sending | plugin/mod | `Claude Code` | **B** | ![Stars](https://img.shields.io/github/stars/alan890104/claude-code-paste-preview?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/alan890104/claude-code-paste-preview?style=flat-square&label=%20) | [Guide](tools/ui/claude-code-paste-preview.md) |
| [Claude Flightdeck](https://github.com/scasella/claude-flightdeck) | Shows context, cost, permissions, and subagents in a panel | plugin/mod | `Claude Code` | **B** | ![Stars](https://img.shields.io/github/stars/scasella/claude-flightdeck?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/scasella/claude-flightdeck?style=flat-square&label=%20) | [Guide](tools/ui/claude-flightdeck.md) |
| [Claude HUD](https://github.com/jarrodwatts/claude-hud) | Displays Claude Code session status and usage | plugin | `Claude Code` | **B** | ![Stars](https://img.shields.io/github/stars/jarrodwatts/claude-hud?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/jarrodwatts/claude-hud?style=flat-square&label=%20) | [Guide](tools/ui/claude-hud.md) |
| [Claude Image View](https://github.com/jarrodwatts/claude-image-view) | Shows pasted-image thumbnails above the prompt | plugin/mod | `Claude Code` | **B** | ![Stars](https://img.shields.io/github/stars/jarrodwatts/claude-image-view?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/jarrodwatts/claude-image-view?style=flat-square&label=%20) | [Guide](tools/ui/claude-image-view.md) |
| [Claude Skins](https://github.com/hellosverre/claude-skins) | Customizes Claude Code terminal themes and output | plugin/mod | `Claude Code` | **B** | ![Stars](https://img.shields.io/github/stars/hellosverre/claude-skins?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/hellosverre/claude-skins?style=flat-square&label=%20) | [Guide](tools/ui/claude-skins.md) |
| [Glowup](https://github.com/NovusEdge/glowup) | Displays file changes, Git diffs, and context in a panel | plugin/mod | `Claude Code` | **B** | ![Stars](https://img.shields.io/github/stars/NovusEdge/glowup?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/NovusEdge/glowup?style=flat-square&label=%20) | [Guide](tools/ui/glowup.md) |
| [Prompt Rail](https://github.com/oikon48/prompt-rail) | Previews prior prompts and navigates session history | plugin/mod | `Claude Code` | **B** | ![Stars](https://img.shields.io/github/stars/oikon48/prompt-rail?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/oikon48/prompt-rail?style=flat-square&label=%20) | [Guide](tools/ui/prompt-rail.md) |
| [Savvy Progress](https://github.com/JohnnyVizz/claude-kit/tree/main/plugins/savvy-progress) | Displays task progress and subagent execution status | plugin | `Claude Code` | **B** | ![Stars](https://img.shields.io/github/stars/JohnnyVizz/claude-kit?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/JohnnyVizz/claude-kit?style=flat-square&label=%20) | [Guide](tools/ui/savvy-progress.md) |

## Visual & Content

| Tool | What it does | Type | Agents | Tier | Stars | Last Commit | Guide |
|---|---|---|---|---|---|---|---|
| [Archify](https://github.com/tt-a1i/archify) | Creates structured diagrams and HTML explanations | tool | `범용` | **A** | ![Stars](https://img.shields.io/github/stars/tt-a1i/archify?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/tt-a1i/archify?style=flat-square&label=%20) | [Guide](tools/visual/archify.md) |
| [Frontend Slides](https://github.com/zarazhangrui/frontend-slides) | Helps create slides using frontend tooling | skill/tool | `범용` | **B** | ![Stars](https://img.shields.io/github/stars/zarazhangrui/frontend-slides?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/zarazhangrui/frontend-slides?style=flat-square&label=%20) | [Guide](tools/visual/frontend-slides.md) |
| [Prismantis](https://github.com/NahumLitvin/prismantis) | Renders Mermaid, tables, and math in the terminal | plugin/mod | `Claude Code` | **B** | ![Stars](https://img.shields.io/github/stars/NahumLitvin/prismantis?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/NahumLitvin/prismantis?style=flat-square&label=%20) | [Guide](tools/visual/prismantis.md) |

## Design

| Tool | What it does | Type | Agents | Tier | Stars | Last Commit | Guide |
|---|---|---|---|---|---|---|---|
| [Figma Desktop MCP](https://developers.figma.com/docs/figma-mcp-server/local-server-installation/) | Connects agents to Figma desktop design context | mcp | `Claude Code` `Codex` `Hermes` | **B** | — | — | [Guide](tools/design/figma-desktop-mcp.md) |
| [Open Design](https://github.com/nexu-io/open-design) | Offers tools and workflows for design creation | tool | `범용` | **B** | ![Stars](https://img.shields.io/github/stars/nexu-io/open-design?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/nexu-io/open-design?style=flat-square&label=%20) | [Guide](tools/design/open-design.md) |

## Developer Utilities

| Tool | What it does | Type | Agents | Tier | Stars | Last Commit | Guide |
|---|---|---|---|---|---|---|---|
| [ni](https://github.com/antfu-collective/ni) | Unifies package commands across package managers | tool | `범용` | **A** | ![Stars](https://img.shields.io/github/stars/antfu-collective/ni?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/antfu-collective/ni?style=flat-square&label=%20) | [Guide](tools/utilities/ni.md) |
| [Peon Ping](https://github.com/PeonPing/peon-ping) | Plays sound notifications for agent activity | tool | `범용` | **A** | ![Stars](https://img.shields.io/github/stars/PeonPing/peon-ping?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/PeonPing/peon-ping?style=flat-square&label=%20) | [Guide](tools/utilities/peon-ping.md) |
| [abtop](https://github.com/graykode/abtop) | Monitors agent-related activity in the terminal | tool | `범용` | **B** | ![Stars](https://img.shields.io/github/stars/graykode/abtop?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/graykode/abtop?style=flat-square&label=%20) | [Guide](tools/utilities/abtop.md) |
| [Stats](https://github.com/exelban/stats) | Monitors macOS system resources in the menu bar | tool | `범용` | **B** | ![Stars](https://img.shields.io/github/stars/exelban/stats?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/exelban/stats?style=flat-square&label=%20) | [Guide](tools/utilities/stats.md) |
| [Vorssaint Utils](https://github.com/vorssaintapp/vorssaint-utils) | A collection of macOS productivity utilities | tool | `범용` | **B** | ![Stars](https://img.shields.io/github/stars/vorssaintapp/vorssaint-utils?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/vorssaintapp/vorssaint-utils?style=flat-square&label=%20) | [Guide](tools/utilities/vorssaint-utils.md) |
| [Yazi](https://github.com/sxyazi/yazi) | A terminal file manager | tool | `범용` | **B** | ![Stars](https://img.shields.io/github/stars/sxyazi/yazi?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/sxyazi/yazi?style=flat-square&label=%20) | [Guide](tools/utilities/yazi.md) |

## Archived

[Archived tools and reasons](archive/README.md). Archived does not necessarily mean the upstream project is abandoned; it may simply be unsuitable for this curator's workflow.

## Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md). All tool documentation is a point-in-time snapshot; check upstream before running commands.

## License

The repository is licensed under [MIT](LICENSE). Each linked project retains its own license.
