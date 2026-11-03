# awesome-agent-tools

A curated collection of **AI coding-agent skills, plugins, mods, MCP servers, and developer tools** with agent-friendly lifecycle guides.

> Korean-first initial catalog. Recommendations are personal and provisional, not blanket compatibility guarantees.

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

**Verification is independent of tier:** `personal` = reported hands-on use, `metadata` = upstream installation/metadata reviewed, `trial` = currently trying, `unverified` = candidate not yet confirmed. No tool in this initial import is marked independently benchmarked. Maintainer-owned tools appear separately under **My Works**. Their tiers are subjective curator assessments, not independent benchmarks. **Install modes:** `cli`, `agent-guide`, `manual-review`.

**GitHub activity:** Stars and Last Commit badges are fetched live from Shields.io for GitHub repositories. They are **not historical snapshots**, may be delayed by caching, and do not determine recommendation tiers. “Last Commit” means latest commit on the upstream repository’s default branch, not the date this guide was verified. Non-GitHub sources are shown as `—`.

**Scope:** agent-related extensions first, adjacent developer utilities second. Personal terminal colors, fonts, local paths, and unsafe wrapper commands are deliberately excluded.

## My Works

Projects maintained by the curator are listed separately from third-party recommendations. Inclusion and tiers are subjective, not independent endorsements.

| Tool | Types | Agents | Tier | Verified | Stars | Last Commit | Guide |
|---|---|---|---|---|---|---|---|
| [TigerKit](https://github.com/MTGVim/tiger-kit) | skill | Claude Code, Codex, Hermes | **S** | personal | ![Stars](https://img.shields.io/github/stars/MTGVim/tiger-kit?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/MTGVim/tiger-kit?style=flat-square&label=%20) | [Guide](tools/workflows/tigerkit.md) |

## Workflow & Agents

| Tool | Types | Agents | Tier | Verified | Stars | Last Commit | Guide |
|---|---|---|---|---|---|---|---|
| [Autoharness](https://github.com/tigerless-labs/autoharness) | plugin/skill | Claude Code | **A** | personal | ![Stars](https://img.shields.io/github/stars/tigerless-labs/autoharness?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/tigerless-labs/autoharness?style=flat-square&label=%20) | [Guide](tools/workflows/autoharness.md) |
| [Skill Creator](https://github.com/openai/skills) | skill | Codex, Cross-agent | **A** | personal | ![Stars](https://img.shields.io/github/stars/openai/skills?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/openai/skills?style=flat-square&label=%20) | [Guide](tools/workflows/skill-creator.md) |
| [Subagent Tuner](https://github.com/Kruhlikau/subagent-tuner) | plugin/mod | Claude Code | **A** | personal | ![Stars](https://img.shields.io/github/stars/Kruhlikau/subagent-tuner?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/Kruhlikau/subagent-tuner?style=flat-square&label=%20) | [Guide](tools/workflows/subagent-tuner.md) |
| [Autoharness Codex](https://github.com/arm092/autoharness-codex) | skill | Codex | **B** | unverified | ![Stars](https://img.shields.io/github/stars/arm092/autoharness-codex?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/arm092/autoharness-codex?style=flat-square&label=%20) | [Guide](tools/workflows/autoharness-codex.md) |
| [Darwin Skill](https://github.com/alchaincyf/darwin-skill) | skill | Cross-agent | **B** | unverified | ![Stars](https://img.shields.io/github/stars/alchaincyf/darwin-skill?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/alchaincyf/darwin-skill?style=flat-square&label=%20) | [Guide](tools/workflows/darwin-skill.md) |
| [Inbox](https://github.com/petekp/inbox) | plugin | Claude Code | **B** | metadata | ![Stars](https://img.shields.io/github/stars/petekp/inbox?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/petekp/inbox?style=flat-square&label=%20) | [Guide](tools/workflows/inbox.md) |
| [MCP Atlassian](https://github.com/sooperset/mcp-atlassian) | mcp | Cross-agent | **B** | unverified | ![Stars](https://img.shields.io/github/stars/sooperset/mcp-atlassian?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/sooperset/mcp-atlassian?style=flat-square&label=%20) | [Guide](tools/workflows/mcp-atlassian.md) |
| [Next Steps](https://github.com/anthropics/claude-plugins-community) | plugin/mod | Claude Code | **B** | unverified | ![Stars](https://img.shields.io/github/stars/anthropics/claude-plugins-community?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/anthropics/claude-plugins-community?style=flat-square&label=%20) | [Guide](tools/workflows/next-steps.md) |
| [OpenShip](https://github.com/oblien/openship) | tool | Cross-agent | **B** | trial | ![Stars](https://img.shields.io/github/stars/oblien/openship?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/oblien/openship?style=flat-square&label=%20) | [Guide](tools/workflows/openship.md) |
| [Skill Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) | skill/tool | Cross-agent | **B** | trial | ![Stars](https://img.shields.io/github/stars/yusufkaraaslan/Skill_Seekers?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/yusufkaraaslan/Skill_Seekers?style=flat-square&label=%20) | [Guide](tools/workflows/skill-seekers.md) |

## Coding & Code Intelligence

| Tool | Types | Agents | Tier | Verified | Stars | Last Commit | Guide |
|---|---|---|---|---|---|---|---|
| [Code Modernization](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/code-modernization) | plugin | Claude Code | **B** | metadata | ![Stars](https://img.shields.io/github/stars/anthropics/claude-plugins-official?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/anthropics/claude-plugins-official?style=flat-square&label=%20) | [Guide](tools/coding/code-modernization.md) |
| [Codegraph](https://github.com/colbymchenry/codegraph) | tool | Cross-agent | **B** | unverified | ![Stars](https://img.shields.io/github/stars/colbymchenry/codegraph?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/colbymchenry/codegraph?style=flat-square&label=%20) | [Guide](tools/coding/codegraph.md) |
| [Ponytail](https://github.com/dietrichgebert/ponytail) | plugin/mod | Claude Code | **B** | metadata | ![Stars](https://img.shields.io/github/stars/dietrichgebert/ponytail?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/dietrichgebert/ponytail?style=flat-square&label=%20) | [Guide](tools/coding/ponytail.md) |

## Context & Sessions

| Tool | Types | Agents | Tier | Verified | Stars | Last Commit | Guide |
|---|---|---|---|---|---|---|---|
| [Agent Usage Guard](https://github.com/rbartoli/agent-usage-guard) | plugin | Claude Code | **B** | metadata | ![Stars](https://img.shields.io/github/stars/rbartoli/agent-usage-guard?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/rbartoli/agent-usage-guard?style=flat-square&label=%20) | [Guide](tools/context/agent-usage-guard.md) |
| [Cache Tax](https://github.com/karanb192/cache-tax) | plugin/mod | Claude Code | **B** | metadata | ![Stars](https://img.shields.io/github/stars/karanb192/cache-tax?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/karanb192/cache-tax?style=flat-square&label=%20) | [Guide](tools/context/cache-tax.md) |
| [Claude Auto Handoff](https://github.com/alexknowshtml/claude-auto-handoff) | mod | Claude Code | **B** | unverified | ![Stars](https://img.shields.io/github/stars/alexknowshtml/claude-auto-handoff?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/alexknowshtml/claude-auto-handoff?style=flat-square&label=%20) | [Guide](tools/context/claude-auto-handoff.md) |
| [Engram](https://github.com/Gentleman-Programming/engram) | tool | Cross-agent | **B** | unverified | ![Stars](https://img.shields.io/github/stars/Gentleman-Programming/engram?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/Gentleman-Programming/engram?style=flat-square&label=%20) | [Guide](tools/context/engram.md) |
| [Session Titles](https://github.com/zhangbububu/session-titles) | mod | Claude Code | **B** | unverified | ![Stars](https://img.shields.io/github/stars/zhangbububu/session-titles?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/zhangbububu/session-titles?style=flat-square&label=%20) | [Guide](tools/context/session-titles.md) |

## Browser & QA

| Tool | Types | Agents | Tier | Verified | Stars | Last Commit | Guide |
|---|---|---|---|---|---|---|---|
| [Orca](https://github.com/stablyai/orca) | tool | Cross-agent | **A** | personal | ![Stars](https://img.shields.io/github/stars/stablyai/orca?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/stablyai/orca?style=flat-square&label=%20) | [Guide](tools/browser/orca.md) |
| [Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp) | mcp | Cross-agent | **B** | metadata | ![Stars](https://img.shields.io/github/stars/ChromeDevTools/chrome-devtools-mcp?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/ChromeDevTools/chrome-devtools-mcp?style=flat-square&label=%20) | [Guide](tools/browser/chrome-devtools-mcp.md) |
| [Claude Show Your Work](https://github.com/iamumeransari/claude-show-your-work) | plugin | Claude Code | **B** | metadata | ![Stars](https://img.shields.io/github/stars/iamumeransari/claude-show-your-work?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/iamumeransari/claude-show-your-work?style=flat-square&label=%20) | [Guide](tools/browser/claude-show-your-work.md) |
| [Cua](https://github.com/trycua/cua) | tool | Cross-agent | **B** | trial | ![Stars](https://img.shields.io/github/stars/trycua/cua?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/trycua/cua?style=flat-square&label=%20) | [Guide](tools/browser/cua.md) |

## Terminal UI

| Tool | Types | Agents | Tier | Verified | Stars | Last Commit | Guide |
|---|---|---|---|---|---|---|---|
| [Claude Code Filetree](https://github.com/data-goblin/claude-code-filetree) | mod | Claude Code | **B** | metadata | ![Stars](https://img.shields.io/github/stars/data-goblin/claude-code-filetree?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/data-goblin/claude-code-filetree?style=flat-square&label=%20) | [Guide](tools/ui/claude-code-filetree.md) |
| [Claude Code Mods](https://github.com/hamzafer/claude-code-mods) | mod | Claude Code | **B** | unverified | ![Stars](https://img.shields.io/github/stars/hamzafer/claude-code-mods?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/hamzafer/claude-code-mods?style=flat-square&label=%20) | [Guide](tools/ui/claude-code-mods.md) |
| [Claude Code Paste Preview](https://github.com/alan890104/claude-code-paste-preview) | plugin/mod | Claude Code | **B** | metadata | ![Stars](https://img.shields.io/github/stars/alan890104/claude-code-paste-preview?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/alan890104/claude-code-paste-preview?style=flat-square&label=%20) | [Guide](tools/ui/claude-code-paste-preview.md) |
| [Claude Flightdeck](https://github.com/scasella/claude-flightdeck) | plugin/mod | Claude Code | **B** | trial | ![Stars](https://img.shields.io/github/stars/scasella/claude-flightdeck?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/scasella/claude-flightdeck?style=flat-square&label=%20) | [Guide](tools/ui/claude-flightdeck.md) |
| [Claude HUD](https://github.com/jarrodwatts/claude-hud) | plugin | Claude Code | **B** | personal | ![Stars](https://img.shields.io/github/stars/jarrodwatts/claude-hud?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/jarrodwatts/claude-hud?style=flat-square&label=%20) | [Guide](tools/ui/claude-hud.md) |
| [Claude Image View](https://github.com/jarrodwatts/claude-image-view) | plugin/mod | Claude Code | **B** | metadata | ![Stars](https://img.shields.io/github/stars/jarrodwatts/claude-image-view?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/jarrodwatts/claude-image-view?style=flat-square&label=%20) | [Guide](tools/ui/claude-image-view.md) |
| [Claude Skins](https://github.com/hellosverre/claude-skins) | plugin/mod | Claude Code | **B** | metadata | ![Stars](https://img.shields.io/github/stars/hellosverre/claude-skins?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/hellosverre/claude-skins?style=flat-square&label=%20) | [Guide](tools/ui/claude-skins.md) |
| [Glowup](https://github.com/NovusEdge/glowup) | plugin/mod | Claude Code | **B** | metadata | ![Stars](https://img.shields.io/github/stars/NovusEdge/glowup?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/NovusEdge/glowup?style=flat-square&label=%20) | [Guide](tools/ui/glowup.md) |
| [Prompt Rail](https://github.com/oikon48/prompt-rail) | plugin/mod | Claude Code | **B** | metadata | ![Stars](https://img.shields.io/github/stars/oikon48/prompt-rail?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/oikon48/prompt-rail?style=flat-square&label=%20) | [Guide](tools/ui/prompt-rail.md) |
| [Savvy Progress](https://github.com/JohnnyVizz/claude-kit/tree/main/plugins/savvy-progress) | plugin | Claude Code | **B** | metadata | ![Stars](https://img.shields.io/github/stars/JohnnyVizz/claude-kit?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/JohnnyVizz/claude-kit?style=flat-square&label=%20) | [Guide](tools/ui/savvy-progress.md) |

## Visual & Content

| Tool | Types | Agents | Tier | Verified | Stars | Last Commit | Guide |
|---|---|---|---|---|---|---|---|
| [Archify](https://github.com/tt-a1i/archify) | tool | Cross-agent | **A** | personal | ![Stars](https://img.shields.io/github/stars/tt-a1i/archify?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/tt-a1i/archify?style=flat-square&label=%20) | [Guide](tools/visual/archify.md) |
| [Frontend Slides](https://github.com/zarazhangrui/frontend-slides) | skill/tool | Cross-agent | **B** | trial | ![Stars](https://img.shields.io/github/stars/zarazhangrui/frontend-slides?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/zarazhangrui/frontend-slides?style=flat-square&label=%20) | [Guide](tools/visual/frontend-slides.md) |
| [Prismantis](https://github.com/NahumLitvin/prismantis) | plugin/mod | Claude Code | **B** | metadata | ![Stars](https://img.shields.io/github/stars/NahumLitvin/prismantis?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/NahumLitvin/prismantis?style=flat-square&label=%20) | [Guide](tools/visual/prismantis.md) |

## Design

| Tool | Types | Agents | Tier | Verified | Stars | Last Commit | Guide |
|---|---|---|---|---|---|---|---|
| [Figma Desktop MCP](https://developers.figma.com/docs/figma-mcp-server/local-server-installation/) | mcp | Claude Code, Codex, Hermes | **B** | personal | — | — | [Guide](tools/design/figma-desktop-mcp.md) |
| [Open Design](https://github.com/nexu-io/open-design) | tool | Cross-agent | **B** | trial | ![Stars](https://img.shields.io/github/stars/nexu-io/open-design?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/nexu-io/open-design?style=flat-square&label=%20) | [Guide](tools/design/open-design.md) |

## Developer Utilities

| Tool | Types | Agents | Tier | Verified | Stars | Last Commit | Guide |
|---|---|---|---|---|---|---|---|
| [ni](https://github.com/antfu-collective/ni) | tool | Cross-agent | **A** | personal | ![Stars](https://img.shields.io/github/stars/antfu-collective/ni?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/antfu-collective/ni?style=flat-square&label=%20) | [Guide](tools/utilities/ni.md) |
| [Peon Ping](https://github.com/PeonPing/peon-ping) | tool | Cross-agent | **A** | personal | ![Stars](https://img.shields.io/github/stars/PeonPing/peon-ping?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/PeonPing/peon-ping?style=flat-square&label=%20) | [Guide](tools/utilities/peon-ping.md) |
| [abtop](https://github.com/graykode/abtop) | tool | Cross-agent | **B** | trial | ![Stars](https://img.shields.io/github/stars/graykode/abtop?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/graykode/abtop?style=flat-square&label=%20) | [Guide](tools/utilities/abtop.md) |
| [Stats](https://github.com/exelban/stats) | tool | Cross-agent | **B** | personal | ![Stars](https://img.shields.io/github/stars/exelban/stats?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/exelban/stats?style=flat-square&label=%20) | [Guide](tools/utilities/stats.md) |
| [Vorssaint Utils](https://github.com/vorssaintapp/vorssaint-utils) | tool | Cross-agent | **B** | personal | ![Stars](https://img.shields.io/github/stars/vorssaintapp/vorssaint-utils?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/vorssaintapp/vorssaint-utils?style=flat-square&label=%20) | [Guide](tools/utilities/vorssaint-utils.md) |
| [Yazi](https://github.com/sxyazi/yazi) | tool | Cross-agent | **B** | personal | ![Stars](https://img.shields.io/github/stars/sxyazi/yazi?style=flat-square&label=%20) | ![Last commit](https://img.shields.io/github/last-commit/sxyazi/yazi?style=flat-square&label=%20) | [Guide](tools/utilities/yazi.md) |

## Archived

[Archived tools and reasons](archive/README.md). Archived does not necessarily mean the upstream project is abandoned; it may simply be unsuitable for this curator's workflow.

## Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md). All tool documentation is a point-in-time snapshot; check upstream before running commands.

## License

The catalog text is released under [CC0-1.0](LICENSE). Each linked project retains its own license.
