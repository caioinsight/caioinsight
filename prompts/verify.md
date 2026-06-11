# /verify — Launch-readiness deep scan of all assets

PURPOSE: Audit the website and every other asset for five things: true to the business plan, factually accurate, internally consistent, on brand voice, and ready to launch. Produce a findings report with severity, file, line, and the fix. Do not change anything. Report only, then offer to fix.

HOW TO RUN: clone the repo. Read COWY_STATE.md (positioning, flagship offer, house style, pricing) and PIVOT_LOG.md (override authority). Scan every asset below against the checklist. Use today's date.

ASSETS TO SCAN
- Public site: index.html and site/index.html (must be identical), check.html, site/intake-form.html, llms.txt, robots.txt, terms.html, refund.html.
- Deliverable: templates/report-template.html (square-bracket fields here are intended template placeholders, not defects).
- Internal: dashboard.html, dashboard-data.json, glossary.html, internal/ tools.
- State and prompts: COWY_STATE.md, PIVOT_LOG.md, FILING.md, prompts/.

CHECKLIST (flag every hit with file, line, and a one-line fix)
1. True to the business plan. Positioning is accuracy, not visibility (the offer is making AI tell the truth about a brand). Offer ladder is exact: free check, then the $1,500 AI Accuracy Report, then AI Watchdog at $79 a month, then Done For You at $2,500 a month. Niche is baby and kids consumables on Shopify. Nothing contradicts COWY_STATE or PIVOT_LOG. Cannabis content stays on the internal gated dashboard, never the public site.
2. Accurate, hard facts only. No unverified statistics (no orphan percentage without a cited source), no fabricated AI answers or quotes, no invented capability or client result. Flag any number that lacks a source.
3. Consistent. Same offer names, prices, and positioning across every asset. index.html equals site/index.html. Title, meta description, and JSON-LD match the on-page copy. No leftover old framing. Scan case-insensitively for "AI visibility", "get recommended", "get you recommended", "get you named", "who gets named", "who AI names", "AI names you", "names instead", "name my competitors", "not named", "named inside", "show up in", "showing up", "where you stand", "drops you off", "skip others", "losing to", "invisible", "recommendation share", "share of voice", "Visibility Report", "Visibility Score". Treat a hit as a finding unless it sits inside an accuracy sentence such as "what AI says" or "gets the facts right".
4. On brand voice (house style). No em dashes or en dashes (characters or HTML entities), no one or two word sentence fragments, no staccato triads, no mid sentence dramatic colon, no hype words (revolutionary, seamless, unlock, supercharge, elevate, game changer), no AI openers ("in today's world"), no filler (very, really, simply, just). Voice: Cowy is plain, parent aware, accuracy led, anti hype.
5. Launch ready. No unfilled placeholder in a public page (square brackets such as [Brand] or [Date], TODO, lorem); the demo card placeholders like "your brand" are intentional. Pricing and CTAs point somewhere real. Payment links are wired or explicitly flagged as not wired. Legal pages (terms, refund) exist and are filled. Gating is correct (internal pages return 401, public pages 200). No secret in any file. robots.txt and llms.txt are present and current.

OUTPUT: a findings table grouped by severity (Blocker, Should-fix, Nice-to-have), each row with file, issue, and fix. End with a one-line launch verdict (Go or Fix-first) and the blocker count. Do not edit anything until the user approves the fixes.

## House style (non-negotiable, no AI tells)
Any copy you write or update must read like a person wrote it. No em dashes or en dashes (use a period, a comma, or the word "and"). No one or two word fragments and no staccato triads. No mid sentence dramatic colon, no "it is not X, it is Y" filler. No hype words and no AI openers. Hard facts only, cited. Read it aloud before shipping.
