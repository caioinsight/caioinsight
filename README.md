# Cowy

Done-for-you AI search optimization (GEO/AEO) for baby & kids consumables DTC brands.
We make AI name your brand over competitors, and never misquote your product facts.

## Repo structure

- **site/** — the marketing site and async intake form
  - `index.html` — kids-gear marketing site (mint brand, cost calculator, 4-tier offer ladder, AI-gap demo, trust block)
  - `intake-form.html` — async client intake (no calls; wire to a form handler before going live)
- **internal/** — operating tools (for the founder, not customers)
  - `intelligence-dashboard.html` — market research, niche map, competitor landscape, where-we-fit, headlines, strategic moves
  - `action-board.html` — rolling-week task board with "Mooove" buttons that build a context-loaded prompt for Claude
- **templates/**
  - `report-template.html` — the $1,500 client report, fillable + print-to-PDF
- **examples/**
  - `bobbie_outreach_pack.md` — sample cold email + 3-min video script (accuracy-led teardown)

## Offer ladder

Free AI-visibility check → $79/mo Watchdog monitoring → $1,500 audit (credited toward retainer) → $2,500/mo done-for-you.

## Notes

- Site files are static HTML; deploy via the existing GitHub → Cloudflare pipeline.
- The action board and dashboard use browser storage for persistence and (in the board) a live prompt-builder for Claude.
- Honest status: pre-launch. Pricing validated against 2026 market data; niche percentages are best-available estimates, flagged in-app.
