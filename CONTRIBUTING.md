# Contributing

AI maintainers: start with [AGENTS.md](AGENTS.md) for the complete request-to-change workflow and document consistency rules. This repository uses `AGENTS.md` only; no additional vendor-specific agent instruction files are necessary.

Contributions and corrections are welcome. New tools are either **Active** (included) or **Archived** (excluded with a retained reason). Keep verification details in the individual guide, not public index tables.

## Adding or updating a guide

- Add one Markdown file under `tools/<capability>/` with a unique name, an upstream link, supported agents and types.
- Keep sections: Why use it?, Requirements, Install, Update, Uninstall, Verify, Caveats, References.
- Prefer official lifecycle commands and exact identifiers. Where not verified, provide a safe agent-guided procedure instead of guessed commands.
- Add the same entry to both README catalogs with localized, functional one-line descriptions. Keep agent tags, upstream links, guide destinations and activity badges in sync; retain verification only in the guide.
- Clearly mark any feature requiring tokens, extra API keys, remote shell execution, broad filesystem permissions, or third-party services.

## Multi-agent skill distribution

- Label a tool as **Skills CLI** only after checking the upstream SKILL.md and an explicit, usable `npx skills` installation path. It indicates installer reach, not guaranteed functionality on all agents.
- Keep confirmed agent support badges separate from distribution badges. Update the Korean and English indexes and the canonical guide together.
- Ensure the `Why use it?` section is genuinely tool-specific rather than generic copy.

## Archiving

Move the entry to `archive/` and document a reason (`superseded`, `incompatible`, `low-value`, `integrated`, `unmaintained`, `security`, `unverified`, `needs-review`), timestamp, and optional replacement. Archiving is a **curation decision**, not a statement that a project is abandoned.

## Review hygiene

Fix broken URLs, distinguish personal experience from repeatable testing, and never publish credentials, private paths, or unsafe permission-bypass instructions.

## Documentation review checklist

Documentation changes do **not** require a passing GitHub Actions workflow. Before publishing, use the detailed checklist in [AGENTS.md](AGENTS.md#documentation-review-checklist). Review applicable items and describe anything not checked.

- [ ] Confirm the upstream URL, installation identifiers, actual feature scope and any user-facing caveats.
- [ ] Keep both README catalogs synchronized, including upstream links, category, badges and the canonical guide.
- [ ] Verify active guide metadata, required sections and the privacy/update audit row; avoid duplicate Active or Archived entries.
- [ ] Review the diff, Markdown links and tables, installation side effects and unsupported claims.
- [ ] When a checkout is available, optionally run `python3 scripts/validate.py` and `git diff --check`. Fix any errors actually found.
- [ ] In the result report, state what was reviewed, what was skipped or unverified and the commit/PR reference.

`.github/workflows/validate.yml` supports on-demand `workflow_dispatch` only. Pushes and PRs do not automatically run the workflow; no CI result is required to mark a documentation update complete.

## Privacy and update policy

Before adding or modifying tools, review upstream telemetry, analytics, update checks, and opt-out procedures. Update [Privacy, Telemetry & Updates](docs/privacy-and-updates.md) for every active entry; record `미확인` when policy is undocumented. Do not conflate privacy telemetry with normal API use, version checks or automatic code upgrades. Follow the manual checklist and explicitly report any checks not performed.
