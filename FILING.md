# Cowy — Filing Map (read this to know where anything goes)

Three systems, one job each. No overlap. When in doubt, this file decides.

## Who owns what

| System | Job | Holds | Canonical? |
|---|---|---|---|
| **caioinsight repo** (GitHub) | Production only | Site, internal tools, llms.txt, schema, published pages, `COWY_STATE.md` | **Yes — system of record** |
| **Notion** | The cockpit | Clients CRM, client reports/deliverables (final), prospect research, playbooks, reference pages | Yes for CRM + reports |
| **Cowy folder** (this folder) | Operating layer + brain | Live working copy of state, drafts in-flight, templates/SOPs I fill, inbox | Working mirror, not record |

Rule of thumb: **if it deploys → repo. If it's living business data a human reads → Notion. If it's in-progress or a thing I work from → this folder.**

## State sync model

`COWY_STATE.md` is canonical **in the repo**. The copy in this folder is my live working copy — I edit it every turn as facts change. The Notion "Master State" page is a human-readable mirror.

Flow: I update the local copy inline → it gets pushed to the repo (by Patrick, or by me once a GitHub connector is wired) → Notion mirror synced. The repo always wins if two disagree.

> Until a GitHub write path exists, treat the local copy as freshest between pushes, and push it to the repo to make it official.

## Folders

- `00_inbox/` — dump zone. Drop anything unfiled here; I sweep and file on request. Not safe long-term.
- `clients/` — one folder per paying client. In-flight deliverables (audit drafts, report working copies, query outputs). Final → Notion; deployable → repo.
- `prospects/` — research/audit drafts for not-yet-paying brands. Mirrors Notion Clients DB prospect rows. Convert → move to `clients/`.
- `content/` — marketing drafts before they ship.
  - `pillar-cluster/` — AEO page drafts (ship to repo as live pages)
  - `video/` — 60s scripts (canonical in Notion)
  - `linkedin/` — post drafts
  - `email/` — outreach + nurture drafts
- `templates/` — reusable masters I fill per engagement (report template, 12-query audit list, email templates, SOP checklists). Canonical report template = Notion.
- `ops/` — pricing, legal drafts, SOPs, checklists, decisions log. Not client-facing.
- `assets/` — logos, brand kit, screenshots. `brand/` = canonical visual identity.

## Non-negotiables

- **Secrets never go in any doc** (repo, Notion, or this folder). Tokens live in a password manager / repo secret only.
- **I keep state current** — update `COWY_STATE.md` Status + changelog inline whenever a fact changes, not end-of-session.
- **Confirm before** anything destructive, anything that spends money, anything outbound.

_Last updated: 2026-06-06_
