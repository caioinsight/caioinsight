# COWY — MASTER STATE (read first / /start)

Single canonical source of truth for the Cowy business. The cofounder brain. If you are an AI assistant reading this, treat it as full context from day one.

**Canonical home and edit rule (root-cause fix for past drift):** this file in the caioinsight/caioinsight repo (root) is canonical. The copy in the Cowy working folder is a mirror. Change this file in ONE place only, the repo (via the cloned working copy). Push it, then overwrite the working-folder mirror from the pushed version. Never edit the two copies independently. Past drift happened because the folder copy was edited with file tools and the repo copy with the shell in the same session.

Last updated: 2026-06-11

## House style: brand voice, zero AI tells (non-negotiable for all copy and all prompts)
Every word that ships, on the website, the free check, the intake form, the report, llms.txt, emails, landing pages, and the dashboard, must read like a person wrote it.
- No em dashes or en dashes. Do not use the long dash characters or their HTML entities. Use a period, a comma, or the word "and".
- No one or two word sentence fragments, and no staccato triads such as "Find. Fix. Prove." Write complete sentences.
- No mid sentence colon used as a dramatic pivot. No "it is not X, it is Y" filler. No rhythmic paired or tripled phrases.
- No AI openers such as "in today's world" or "in the age of AI". No hype words such as revolutionary, game changer, seamless, unlock, supercharge, elevate. No filler such as very, really, simply, just.
- Hard facts only, cited. Never invent a statistic, a quote, or an AI answer.
- Voice. Cowy, the public baby and kids brand, is plain, parent aware, accuracy led, anti hype, calm, and concrete. CAIO Insight, the internal DTC and cannabis dashboard, is direct and operator to operator, with active verbs and hard numbers.
- Test before shipping. Read it aloud. If it sounds like a chatbot wrote it, rewrite it.

## What Cowy is
A done for you AI accuracy service for baby and kids consumable DTC brands on Shopify. When AI assistants (ChatGPT, Perplexity, Gemini, Google AI Overviews) talk about a brand, Cowy makes sure they tell the truth. We find every wrong, outdated, or misattributed answer, fix the sources behind it, and prove the correction. Founder: Patrick O'Brien (Carlsbad, CA), solo operator, replacing about $160K of salary.

Pivot v2 (2026-06-09): we dropped the "get recommended" or "AI visibility" promise. It is un winnable and un provable for a small founder brand, and it is being commoditized by Shopify and Perplexity free programs. Accuracy on branded queries is winnable, provable, and a real safety and liability stake on kids products.

## Positioning
- Headline, live: "When parents ask AI about your baby and kids brand, does it get the facts right?"
- Eyebrow: "AI Accuracy for Baby & Kids Brands"
- Method: Find, Trace, Fix, Prove.

## Flagship offer, active since 2026-06-10
The AI Accuracy Audit, the activated Pivot 1.
- What it is. A 48 hour fixed price audit of what AI says about a brand's products across ChatGPT, Perplexity, Gemini, and Google AI Overviews. We find every wrong, outdated, or misattributed fact, trace each one to the source AI reads, fix the sources we control, out publish the ones we do not, and prove the correction.
- Why now. Agentic storefronts went live in June 2026 across the major engines, so accurate product data is the surface that matters.
- Funnel. Free check, then the $1,500 AI Accuracy Report (credited toward the first month if they continue), then AI Watchdog at $79 a month, then Done For You at $2,500 a month.
- Deliverable. The AI Accuracy Report at templates/report-template.html.
- First targets. Warm Tier 1 baby and kids prospects such as Tubby Todd, each with one real free check finding.

## Niche
Baby and kids consumables on Shopify: formula, baby food and pouches, diapers, wipes, skincare and bath, kids vitamins. Adjacent expansion later. Tooling stays category agnostic.

## CAIO Insight (DTC and cannabis), internal
The DTC and cannabis intelligence lives in the gated dashboard at cowy.ai/dashboard.html, not on the public Cowy site. Cannabis is framed as compliance and accuracy liability, never visibility, because AI surfaces only about 1.2 percent of dispensaries on ChatGPT and the rate is falling.

## Saved prompts (repo prompts/ directory)
- /verify, at prompts/verify.md. Launch-readiness deep scan of all assets (business-plan truth, accuracy, consistency, brand voice, launch ready). Reports findings, then offers to fix.
- /pivot, at prompts/pivot.md. Ranks the top 5 pivots per vertical from the latest dashboard-data.json and recommends go now versus schedule.
- /activate, at prompts/activate.md. Implements the GO NOW pivots across all business assets, with a required accuracy and house style review before it asks for approval to push.
- Older CAIO hub and spoke set: CAIO_AUDIT, CAIO_CAMPAIGN, CAIO_INTEL, CAIO_PIVOT, CAIO_POST, CAIO_RESEARCH, CAIO_SITE, CAIO_STRATEGY.
- Strategy prompts (Business Plan Stress Test, Goldmine Scan, Marketing Plan, AI Visibility Audit) are documented in the Notion Master State.

## Infrastructure and systems of record
- Repo: github.com/caioinsight/caioinsight, private. A Cloudflare Worker auto deploys on push and serves the repo root minus .assetsignore.
- Domain: cowy.ai. Public pages: the homepage (index.html and site/index.html, kept identical), check.html (the free check), and site/intake-form.html.
- Gated behind Basic Auth (user caioadmin, password is the Cloudflare secret INTERNAL_PASSWORD): /internal/*, /dashboard.html, /glossary.html, /dashboard-data.json.
- Daily intel: dashboard-data.json is regenerated each morning at 6am PT by the Cowork task cowy-dashboard-daily-6am and by a GitHub Actions cron that runs scripts/generate_dashboard_data.py. Both are framed to accuracy.
- Systems of record, one job each: the repo is production plus canonical state, Notion is the cockpit (CRM, research, playbooks), the Cowy folder is the operating layer and the state mirror. See FILING.md.
- Security: never store the GitHub token or any secret in any doc.

## Status, 2026-06-11
Live and accuracy aligned: homepage, free check, intake, report template, llms.txt, and the dashboard pitch and Pivot Plan tab. The flagship AI Accuracy Audit is active. The first real free check ran on Tubby Todd, and the finding was that two engines disagree on whether the All Over Ointment is an eczema treatment.
Open blockers for launch: create the five Stripe payment links and wire them into check.html, fill the legal placeholders in terms.html and refund.html (legal business name, state, contact email, effective date), revoke the cowy-dashboard-bot token, and finish GitHub Actions (add the workflow file and the ANTHROPIC_API_KEY secret). Copy voice is clean and all visibility framing is removed from the public pages.

## Session protocol (/start)
On /start, read this doc, the repo, and the relevant Notion pages (the Cowy Clients tracker). Then reply with a three line status (what is live, what is in progress, top three next actions) and wait.

## Operating discipline (always)
No hallucination, hard facts only. Validate output before presenting it. Trusted sources only, and cite non obvious facts. No speculation, and mark unknowns as assumptions. Enforce the house style on all copy. Confirm before anything destructive, anything that spends money, anything outbound, and any change to the public site.

## Changelog (condensed)
- 2026-06-11 (pm): made the report What happens next CTA a real Stripe checkout button (wired in fill_report.py from a client cta object with dfy_url and watchdog_url; falls back to the email line when no link is set). Fixed the homepage This is already a liability band, which left an empty gap with four cards in a three-column grid, by switching it to a clean two-by-two. Stripe links themselves still need to be created in Patrick's Stripe account.
- 2026-06-11 (pm): extended the Tubby Todd audit beyond the hero SKU to a catalog sample (Bye-Bye Cradle Cap, Sweet Cheeks Diaper Paste, Everyday Lotion) on Google AI Overviews. Google states the hard specs correctly, including the two OTC drug actives. Corrected two of our own calls: the outdated-formula finding was wrong (the Original Formula is a real product) and the invented-scent candidate was wrong (Sweet Peach + Jasmine is real). Score revised up to 78 of 100, findings reduced to three real ones plus a catalog-correct note. Honest read: well-documented brands are mostly accurate, gaps cluster on Perplexity and framing, not hard specs.
- 2026-06-11 (pm): added a transparent revenue-at-risk model. The report now shows a What these gaps are worth box driven by product price, monthly units, and a labeled conservative deterrence range, framed as exposure not billed loss, wired into scripts/fill_report.py from a client stakes object. Added an optional monthly-units field and payload to check.html and site/intake-form.html so the number comes from the brand. The Tubby Todd box renders an illustrative $1,800 to $5,400 a month at 5,000 units.
- 2026-06-11 (pm): ran the full live AI capture for Tubby Todd across Google AI Overviews (11 queries) and Perplexity, with a partial ChatGPT capture and Gemini not cleanly extractable this run. Scored accuracy at 71 of 100 and built the full report at outputs/tubby-todd-accuracy-report.html. Findings: the scented Lavender Rosemary version is omitted on fragrance questions, the product is understated as a moisturizer rather than the OTC eczema treatment it is, and it is left off best for newborns lists. Added a lead override and a diagnostic stage to scripts/fill_report.py and saved the verbatim capture log at prospects/tubby-todd-full-capture.md.
- 2026-06-11 (pm): added a freecheck mode to scripts/fill_report.py and generated the Tubby Todd free check report from the real Perplexity captures, with no fabricated score or claimed work since the sample is one engine only.
- 2026-06-11 (pm): removed the last visibility framing from every public page (free check section, FAQ and its JSON-LD, the steps, the grader copy, and the intake labels), widened the /verify scan to catch broader visibility phrasings, shipped a one command report fill (scripts/fill_report.py with template anchors, clients/, and a sample), added the customer email template set at ops/email-templates.md, and stopped serving the internal dirs (prompts, templates, scripts, clients, prospects, ops) publicly.
- 2026-06-11: reconciled this doc into one clean canonical version, added the house style rule and the single edit path rule that fixes the drift, added a review gate to /activate, and reviewed the June 11 auto pivots.
- 2026-06-10: activated the flagship AI Accuracy Audit across all assets (homepage product cards, report template, intake form, check.html, llms.txt), added the Pivot Plan dashboard tab and the /pivot and /activate prompts, and ran the first Tubby Todd free check.
- 2026-06-09: shipped Pivot v2 from visibility to accuracy on the live site, reframed cannabis to compliance and accuracy, hardened security (private repo, gating, closed two public leaks), added a Tier field to the CRM, and built the pipeline dashboard.
- 2026-06-06 to 08: site build and positioning, the cross chat state system, the intel dashboard, and the strategy work (existential risk, Watchdog first test, pressure test).
