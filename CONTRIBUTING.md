# Contributing

AI maintainers: start with [AGENTS.md](AGENTS.md) for the complete request-to-change workflow and document consistency rules. This repository uses `AGENTS.md` only; no additional vendor-specific agent instruction files are necessary.

Contributions and corrections are welcome. Add candidates at tier B unless hands-on evidence supports A or S. Always keep **tier** and **verification** separate. A useful tool can remain B indefinitely.

## Adding or updating a guide

- Add one Markdown file under `tools/<capability>/` with a unique name, an upstream link, supported agents and types.
- Keep sections: Why use it?, Requirements, Install, Update, Uninstall, Verify, Caveats, References.
- Prefer official lifecycle commands and exact identifiers. Where not verified, provide a safe agent-guided procedure instead of guessed commands.
- Add the same entry to both README catalogs with localized, functional one-line descriptions. Keep agent tags, tiers, upstream links and guides in sync; retain verification only in the guide.
- Clearly mark any feature requiring tokens, extra API keys, remote shell execution, broad filesystem permissions, or third-party services.

## Archiving

Move the entry to `archive/` and document a reason (`superseded`, `incompatible`, `low-value`, `integrated`, `unmaintained`, `security`, `unverified`, `needs-review`), timestamp, and optional replacement. Archiving is a **curation decision**, not a statement that a project is abandoned.

## Review hygiene

Fix broken URLs, distinguish personal experience from repeatable testing, and never publish credentials, private paths, or unsafe permission-bypass instructions.
