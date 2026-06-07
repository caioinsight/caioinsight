# COWY — MASTER STATE (read first / /start)

Single source of truth for the Cowy business. The cofounder brain. Updated inline whenever a fact changes. If you are an AI assistant reading this: treat it as full context from day one.

Last updated: 2026-06-06

## What Cowy is
Done-for-you AEO / AI-visibility service for baby & kids consumable DTC brands on Shopify. Makes AI assistants (ChatGPT, Perplexity, Gemini, Google AI Overviews) recommend the brand AND get its facts right. Sells accuracy + recommendation share (being chosen + never misquoted), not generic visibility. Founder: Patrick O'Brien (Carlsbad CA), solo operator, replacing ~$160K salary.

## Positioning & voice
- Headline (live): "61% of parents now ask AI what to buy. Does it recommend you, and get you right?"
- Eyebrow: "AI Visibility for Baby & Kids Brands"
- Voice: plain, parent-aware, accuracy-led, anti-hype, no fluff.

## Niche (do not broaden lightly)
Baby & kids consumables on Shopify: formula, baby food & pouches, diapers, wipes, skincare & bath, kids vitamins. Adjacent expansion later (pet, supplements, clean beauty). Tooling stays category-agnostic.

## Offer ladder / pricing
- Free check — 30s AI visibility check + score + top gaps (lead magnet).
- Full Report — $1,500 one-time; audit + first fixes; credited if monthly within 7 days.
- AI Watchdog — $79/mo (or $806/yr); monitoring + alerts; strategic SaaS hinge.
- Done-For-You — $2,500/mo (or $25,500/yr); monthly fixes + proof of lift; "no lift you don't pay."

## Revenue / exit
~$200K gross by Y2 = ~5 DFY + ~25 Watchdog + ~15 reports. Constraint = sales throughput, not niche size. Exit: Watchdog -> SaaS; at ~100 subs the conversation shifts to acquisition (Profound, Scrunch, Semrush, Adobe).

## Acquisition channels
1. Organic AEO niche-leadership (primary, low-CAC): own "AI visibility for baby & kids brands" via pillar + cluster pages, FAQ + schema, llms.txt. Practicing what we sell = live proof.
2. Direct outreach: 36 tiered prospects in Notion tracker; Tubby Todd = first reference audit.
3. Passive: schema/FAQ/llms.txt DIY kit ($200-400) + disclosed tool-affiliate fees.

## Brand system
Mint #A3E2C9, mint-deep #5FBF9B, page bg gradient ~#EFF6F2 -> #E4EFE9, ink #1C2521, card #FFF. Fonts Nunito + Geist Mono. Logo brown cow-head + "cowy" wordmark (44:40). Internal dashboards brown.

## Infrastructure & where everything lives
- Site repo: github.com/caioinsight/caioinsight (main). Worker "caioinsight" auto-deploys on push. Homepage = repo root index.html + site/index.html (synced).
- Domain: cowy.ai (live, Cloudflare; Porkbun registrar). caioinsight.ai -> redirect later.
- Internal tools (live): cowy.ai/internal/{intelligence-dashboard,console,audit-runner,action-board}.html
- AEO infra (live): FAQ + Organization/Service/FAQPage JSON-LD on homepage; robots.txt (allows AI crawlers); llms.txt.
- Notion: Cowy Clients tracker — prospects, video scripts, video playbook, keyword/AEO criteria, master state.
- SYSTEMS OF RECORD (one job each, see FILING.md in Cowy folder): repo = production + canonical COWY_STATE.md; Notion = cockpit (CRM, final reports, research, playbooks); Cowy folder = operating layer (live working state copy, in-flight drafts, templates I fill, 00_inbox). Repo is canonical for state; Notion Master State + local copy are mirrors I keep synced (repo wins on conflict). NOTE: no GitHub write path yet (token dead, no connector) — local copy is freshest between pushes; push to repo to make official.
- SECURITY: never store the GitHub token in any doc. The token previously pasted in chat is broad-scope and is now rotated/dead; the new one lives outside docs (password manager / repo secret).

## Status (2026-06-06)
LIVE: cowy.ai site (positioning, 6-stat band, sticky nav, brown logo, gradient bg + button depth, pricing groups + annual toggle, 4-rung how-it-works ladder incl. Watchdog, FAQ + schema, robots/llms.txt). Intel dashboard updated. Keyword/AEO criteria + business model codified. 6 video scripts saved (Notion + repo examples/).
OPEN / NEXT: 5 Stripe payment links -> wire into intake form; finish Zapier -> Notion intake; legal pages (fill brackets + lawyer); Tubby Todd Path B audit (run the 12 queries); build pillar + cluster pages; finish rotating GitHub token + store securely; wire a GitHub connector so the assistant can sync local->repo; trademark "Cowy".

## Session protocol (/start)
On /start: read this doc + (if file tools available) the repo + relevant Notion pages (Cowy Clients tracker). Then reply with a 3-line status — what's live / what's in progress / top 3 next actions — and wait.

## Operating discipline (always, non-negotiable)
- No hallucination. Hard facts only. Never invent numbers, quotes, AI answers, competitor moves, or capabilities.
- Validate output before presenting (code: parse/lint before push; claims: confirm against a real source).
- Trusted, relevant sources only; cite non-obvious facts; prefer primary sources.
- No speculation. If something isn't known or verifiable with available tools, say so and mark it as an assumption/open question rather than stating it as fact.

## Keeping state current (the assistant's job, not the user's)
Update the Status section + add a dated changelog line INLINE, in the same turn, whenever a fact changes (a change ships, a price moves, a decision is made, a prospect converts). Do not wait for end of session; flush before a chat ends/fills. User's only jobs: (a) type /start, (b) one-line heads-up on anything done OUTSIDE the chat. Never store secrets in plaintext.

## Tooling note
ideabrowser is RETIRED from the workflow (idea discovery/validation complete; keyword tool gated; its context files only fire inside ideabrowser skills, not Cowork/Projects). Keyword volume/competition validation is Ahrefs' job. Workflow container: Cowork (primary, included on Max) + a lightweight Project for quick asks; both share this /start brain.

## Changelog
- 2026-06-06 — Filing system established: Cowy folder skeleton created (00_inbox, clients, prospects, content/{pillar-cluster,video,linkedin,email}, templates, ops, assets/brand) + FILING.md map; systems-of-record defined (repo canonical for state, Notion = cockpit, folder = operating layer); confirmed Cowy folder is a plain folder, not a clone of caioinsight. OPEN: wire a GitHub connector so I can sync local->repo directly.
- 2026-06-06 — Site polish + positioning locked; AEO infra (FAQ/schema/llms.txt) live; how-it-works ladder gained Watchdog rung; keyword/AEO criteria + business model codified; cross-chat state/workflow system created; COWY_STATE.md added to repo via web UI (token rotated/dead).
