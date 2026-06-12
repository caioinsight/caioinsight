# /scan — AI accuracy scan (leading products first, no quota)

PURPOSE: Find the real accuracy errors AI makes about a brand by scanning its leading products in priority order, deep enough to be substantial, and never manufacturing a finding to hit a number.

SCOPE BY TIER (rank SKUs by revenue or best-seller order, exclude bundles):
- Free check: top 5 SKUs. AI Watchdog: top 10. AI Accuracy Report and Done For You: top 20.

HOW TO RUN:
1. Establish ground truth from the brand's own product pages for each product in scope: active ingredients, age range, claims, certifications, variants. Cite the source URL for every fact.
2. For each product in priority order, run the buyer-question bank across ChatGPT, Perplexity, Gemini, and Google AI Overviews. Cover: free-from claims, active ingredient, age and newborn safety, certification or seal, the closest competitor comparison, and the buyer's own top question.
3. Capture every answer verbatim with a screenshot and a timestamp. Compare each to ground truth.
4. Continue product by product until you have found 5 genuine, re-verified errors, OR you have covered every product in scope, whichever comes first. Stop early when you hit 5 real errors.
5. Re-verify every error live on the day the report ships. Cut anything that no longer reproduces.

HARD RULES (non-negotiable):
- Never manufacture or stretch a finding to reach 5. Five is a stopping point for the scan, not a count the report must show.
- A visibility omission (AI not naming the brand on a best-of list) is not an accuracy error. Mark it as a watch item, never as a wrong fact.
- If fewer than 5 real errors exist after covering the scope, say so plainly. An accurate result is a true result, and the report leans on monitoring, since answers change.
- Hard facts only. Every claim sourced and screenshotted.

OUTPUT: a client JSON for scripts/fill_report.py with the findings found (status wrong, ok, or note), a coverage line (products and engines scanned), verified_on, and evidence_on_file set. The fill script blocks an unverified report with a draft banner.
