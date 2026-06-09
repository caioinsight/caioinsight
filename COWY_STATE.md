# COWY — MASTER STATE (read first / /start)

Single source of truth for the Cowy business. The cofounder brain. Updated inline whenever a fact changes. If you are an AI assistant reading this: treat it as full context from day one.

Last updated: 2026-06-09

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

## Strategic posture (2026-06-09) — from Notion strategy work
- #1 EXISTENTIAL RISK: the monitoring FEATURE is commoditizable; the moat is NOT the tool. Shopify/Profound/Scrunch/Semrush could add "alert me when AI gets my brand wrong" as a checkbox. Defensibility lives in: (1) niche depth + judgment (which AI errors are regulatory/safety vs cosmetic, and writing the fix), (2) done-for-you OUTCOMES (not another dashboard), (3) references / being the known name in baby & kids (NOT YET BUILT — priority), (4) a proprietary niche dataset = the "Baby & Kids AI Visibility Index". Watchdog = recurring-revenue mechanic + on-ramp, NOT the defense. Cheapest resolving test: land 1–2 real paying baby brands, observe whether they're buying the TOOL (fragile) or the JUDGMENT + OUTCOMES (durable).
- Shopify signal [ASSUMPTION — verify scope before betting/publishing]: a 2026-06-08 AI-search result claims Shopify now offers native Agentic Storefront (auto-push catalog to AI channels) + a free Knowledge Base App (see how often AI asks about the brand, curate facts). Cuts both ways: threatens the "get me into AI" entry offer; validates Watchdog (cross-engine, adversarial, drift-over-time monitoring is what Shopify does NOT do). Implication: stop leading with "get into AI"; lead with accuracy + competitor-displacement + drift. VERIFY Agentic Storefront + Knowledge Base App actually exist/scope before rewriting public copy.
- Watchdog-first test (2026-06-08, reversible, live site unchanged): lead with $79/mo monitoring, not the $1,500 report. Pass = 1 paid Watchdog sub per 20 outreaches (each paired with a real free-check finding; funnel = free check delivered → paid, self-serve, no demo/call). Below that after 20 = don't rewrite the live site.
- Pressure-test verdicts (2026-06-08, partly ASSUMPTION): niche + positioning = strongest (Hold). Pricing math / acquisition sequencing / exit thesis = over-claimed (Revise — $200K is a model not a forecast; lead near-term with outreach not organic AEO; exit = optionality not a milestone). Solo + DFY at $2,500/mo is hours-capped. Top 3 business-breakers to validate first: (1) buyers pay for accuracy/rec-share, (2) enough qualified baby/kids Shopify brands convert, (3) platforms don't commoditize before references exist.
- Reference material lives in Notion (not duplicated here): reusable skills (Business Plan Stress Test, Goldmine Scan, Marketing Plan Watchdog-first, AI Visibility Audit), the Marketing Plan page, the AI-visibility audit question template + scoring grid, Watchdog test collateral drafts.

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

## Status (2026-06-09)
LIVE: cowy.ai site (positioning, 6-stat band, sticky nav, brown logo, gradient bg + button depth, pricing groups + annual toggle, 4-rung how-it-works ladder incl. Watchdog, FAQ + schema, robots/llms.txt). Keyword/AEO criteria + business model codified. 6 video scripts saved (Notion + repo examples/). SECURITY: repo now PRIVATE; .assetsignore stops cowy.ai from serving internal docs; /internal/* gated by Worker Basic Auth (caioadmin + Cloudflare secret). Live Notion-driven CRM pipeline dashboard (Cowork artifact); Clients DB has a real Tier field (T1/T2/T3) backfilled.
OPEN / NEXT: SET the Cloudflare secret INTERNAL_PASSWORD to unlock /internal/; refresh repo internal/intelligence-dashboard.html for 6/9 (Today's Read + execution + strategic posture); 5 Stripe payment links -> wire into intake form; finish Zapier -> Notion intake; legal pages (fill brackets + lawyer); Tubby Todd Path B audit (run the 12 queries); build pillar + cluster pages; rotate GitHub token + store securely; trademark "Cowy".

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
- 2026-06-09 — State reconciliation: merged the 2026-06-08 strategy work from the Notion Master State into this canonical repo doc (added "Strategic posture" section: #1 existential risk + moat, Shopify signal [ASSUMPTION], Watchdog-first test, pressure-test verdicts). Repo doc had been ~2 days behind Notion because the 6/8 chats lacked file/Chrome tools. Verbose skill prompts/templates remain Notion-only.
- 2026-06-09 — SECURITY hardening: (1) Found cowy.ai served the whole repo root publicly (assets dir ".") — COWY_STATE.md/FILING.md were downloadable at cowy.ai/<file>. Pushed .assetsignore; verified both now 404. (2) Repo made PRIVATE (Patrick). (3) Added _worker.js Basic Auth gate on /internal/* (run_worker_first in wrangler.jsonc); verified deployed + fail-safe (401 "Authentication required." until secret set). Username caioadmin in code; password = Cloudflare secret INTERNAL_PASSWORD (NOT in repo). PENDING: Patrick sets the Cloudflare secret to unlock /internal/.
- 2026-06-07 — CRM cleanup (additive): added a real "Tier" select (T1/T2/T3) to the Notion Clients DB and backfilled all 36 tiered prospects (T1:14, T2:15, T3:7) from the Next-action text. Dashboard updated to read the Tier field + exclude the "Example Client (Active)" placeholder from metrics. HELD for explicit OK (destructive): deleting the placeholder row; removing the 3 meta doc rows (Master State, Video Scripts, Keyword criteria) from the Clients DB.
- 2026-06-06 — Live "Cowy Client Pipeline" dashboard built as a Cowork artifact (pulls Notion Clients DB on open: MRR/one-time/active/in-progress/prospect scorecards + sortable tables grouped by Tier 1/2/3). Reopenable each session. NOTE: distinct from the planned public daily intel dashboard (deployed URL) — that's still OPEN.
- 2026-06-06 — Filing system established: Cowy folder skeleton created (00_inbox, clients, prospects, content/{pillar-cluster,video,linkedin,email}, templates, ops, assets/brand) + FILING.md map; systems-of-record defined (repo canonical for state, Notion = cockpit, folder = operating layer); confirmed Cowy folder is a plain folder, not a clone of caioinsight. OPEN: wire a GitHub connector so I can sync local->repo directly.
- 2026-06-06 — Site polish + positioning locked; AEO infra (FAQ/schema/llms.txt) live; how-it-works ladder gained Watchdog rung; keyword/AEO criteria + business model codified; cross-chat state/workflow system created; COWY_STATE.md added to repo via web UI (token rotated/dead).
