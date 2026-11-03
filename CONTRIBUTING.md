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

## Required CI verification

1. Run `python3 scripts/validate.py` locally before committing changes. Resolve all reported errors.
2. Push the commit or open a PR, then inspect the matching commit's `Validate catalog` workflow run in GitHub Actions (not an earlier green run).
3. Wait for a **successful** conclusion. If CI fails, read the failing job logs, repair the cause, push the fix, and confirm the latest workflow succeeds.
4. Never mark an update complete with failing, pending, skipped, or unobserved CI. If CI is inaccessible or cannot finish, state the blocker and exact run URL; do not claim success.
5. Apply this to documentation-only changes too, including one-row catalog changes, guide updates, translations and archive moves.
