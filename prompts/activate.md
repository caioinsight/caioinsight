# /activate — Implement the GO-NOW pivots across all business assets

PURPOSE: Take the pivots marked **GO NOW** in the latest dashboard data (the daily intel dashboard's "Pivot Plan" tab) and update EVERY business asset to reflect and activate them — on-brand, hard-facts, verified live. (Run `/pivot` first for a fresh ranking; this command acts on whatever pivots in `dashboard-data.json` have `timing` starting with "GO NOW".)

HOW TO RUN
1. Read `dashboard-data.json` (repo root). For each vertical (`dtc`, `cannabis`), collect every pivot whose `timing` is "GO NOW". Read `COWY_STATE.md` (positioning + Flagship offer) and `PIVOT_LOG.md` (OVERRIDE AUTHORITY). Use today's date.
2. For each GO-NOW pivot, state in one line what it changes about the offer/positioning and confirm it fits current positioning (accuracy for Cowy/DTC; compliance & accuracy for cannabis). If a pivot contradicts PIVOT_LOG, STOP and flag it.

BUSINESS-ASSET MAP (clone the repo via the GitHub token, edit, push — update every relevant one):
- Public website — `index.html` AND `site/index.html` (kept identical): hero, product-card demo, pricing/offer cards, how-it-works, FAQ, `<title>`/meta/JSON-LD.
- Free-check tool — `check.html`.
- Intake form — `site/intake-form.html`.
- AI-readable summary — `llms.txt` (what ChatGPT/Perplexity/Gemini read about the brand; keep current).
- Report deliverable — `templates/report-template.html`.
- Intel dashboard — `dashboard.html` (pitch + framing); note pivots now in execution.
- Daily generators — `scripts/generate_dashboard_data.py` and the Cowork task `cowy-dashboard-daily-6am`, so future daily output stays aligned.
- Canonical brain — `COWY_STATE.md` ("Flagship offer" + Status sections).
- Decision log — `PIVOT_LOG.md` (add a dated activation entry, newest at top).

EXECUTION RULES
- HARD FACTS ONLY: no invented stats, AI answers, or claims. Validate before publishing. Trusted sources; cite non-obvious facts; mark unknowns as assumptions.
- ON BRAND: plain, parent-aware, accuracy-led, anti-hype. Cannabis = compliance & accuracy liability, NEVER visibility / "get recommended".
- Per file: exact-string edits, print a replacement count to confirm nothing was silently missed, then SWEEP for residual old framing ("AI visibility", "who gets named", "recommend you", "not named", "invisible") — leave only genuine market-fact references and code comments.
- CONFIRM before pushing public-site changes (modifying public content). Push via the repo; the Worker auto-deploys.
- After deploy, VERIFY LIVE: fetch each changed URL and assert the new copy is present and the old framing gone. The public site is browser-cached — tell the user to hard-refresh (Ctrl+Shift+R).

OUTPUT: a per-pivot summary (what changed + which files), commit hashes, live-verification results, and anything held for confirmation.
