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
- SYSTEMS OF RECORD (one job each, see FILING.md in Cowy folder): repo = production + canonical COWY_STATE.md; Notion = cockpit (CRM, final reports, research, playbooks); Cowy folder = op