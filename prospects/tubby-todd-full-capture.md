# Tubby Todd — AI Accuracy Capture Log (full report basis)
_Captured 2026-06-11. Live browser captures. Honest verbatim only, no fabrication._

## Ground truth (tubbytodd.com, All Over Ointment Eczema Treatment)
- Active ingredient: colloidal oatmeal 1% (FDA OTC skin protectant, eczema). It is an OTC "Eczema Treatment".
- Steroid-free, gluten-free, dairy-free, paraben-free, no SLS/SLES. Hypoallergenic. Pediatrician + dermatologist tested. Gentle enough for newborns.
- National Eczema Association Seal of Acceptance (shown on packaging).
- Two versions: Fragrance-Free AND Lavender Rosemary (scented; contains fragrance + lavender oils).
- Made in USA: not stated on the product page (left unverified, not scored).

## Google AI Overviews (11 queries, captured verbatim)
- Good for baby eczema: YES, correct; cites 1% colloidal oatmeal FDA-approved. BUT a "Cons" line: "Not a Medication: While it is a great emollient for maintenance and mild dryness, it usually does not clear up severe, active flare-ups."
- Fragrance-free: YES, names fragrance-free + Lavender Rosemary versions. Also surfaced an "Original Formula (Fragrance-Free): the classic multipurpose balm without colloidal oatmeal" (outdated; current AOO has colloidal oatmeal).
- Active ingredient: 1% Colloidal Oatmeal, FDA-approved skin protectant for eczema. Correct.
- Steroid-free: YES, correct.
- Safe for newborns: YES, correct, "from day one".
- Best baby eczema cream for newborns: named Aveeno, Mustela Stelatopia+, Eucerin. Tubby Todd NOT named.
- NEA: YES, "officially awarded the National Eczema Association Seal of Acceptance". Correct.
- Gluten-free: YES, also dairy/steroid/paraben-free. Correct.
- Made in USA: "Yes, proudly made in the United States" (unverified by us).
- vs Aveeno: balanced; Tubby Todd "premium, plant-based balm... for stubborn flare-ups". Fair.
- Treatment vs moisturizer: "officially classified and formulated as an eczema treatment rather than just a basic moisturizer... NEA Seal". Correct (contradicts the "Not a Medication" line above).

## Perplexity (captured verbatim)
- Fragrance-free: "Yes, Tubby Todd All Over Ointment is fragrance free... There is also a separate fragrance-free version marketed for sensitive or eczema-prone skin." Never mentions the Lavender Rosemary scented version; implies all variants are fragrance-free.
- Treatment vs moisturizer: "best viewed as supportive care for mild eczema or flare-ups, not a medical treatment in the prescription sense." Undersells the OTC eczema-treatment classification.
- Best fragrance-free baby eczema cream for newborns: gated by sign-in this run. Prior free check (2026-06-10): ranked Aveeno first, Tubby Todd as a "good alternative".

## ChatGPT (logged out, partial)
- Treatment vs moisturizer: "Tubby Todd markets its current All Over Ointment as both a moisturizer and an eczema treatment." Correct. Answer truncated by the logged-out limit before the fragrance part.

## Gemini
- Logged in and answered ("Tubby Todd Ointment: Eczema Treatment?"), but the response sits in shadow DOM and could not be extracted cleanly this run. Not scored.

## Catalog extension (2026-06-11, Google AI Overviews)
Tubby Todd has 20+ products. Beyond the hero All Over Ointment, scanned three more on Google:
- Bye-Bye Cradle Cap: active = Zinc Pyrithione 0.95%. CORRECT (ground truth 0.95% pyrithione zinc, OTC).
- Sweet Cheeks Diaper Paste: 14% non-nano zinc oxide. CORRECT (ground truth 14% zinc oxide, OTC).
- Everyday Lotion: fragrance-free plus Lavender Rosemary and Sweet Peach + Jasmine. CORRECT and verified on the product page (Sweet Peach + Jasmine is a real Meri Meri collab scent, more complete than the brand's own best-sellers copy).

## Two self-corrections (caught during the catalog scan)
1. The earlier "outdated original formula without colloidal oatmeal" finding was WRONG. Tubby Todd genuinely sells an All Over Ointment Original Formula ($22, no oatmeal, non-OTC). Google was correct. Finding removed from the report.
2. The candidate "AI invented a Sweet Peach + Jasmine scent" was also WRONG. The scent is real. Not a finding.

## Honest conclusion
For a well-documented brand like Tubby Todd, Google AI Overviews is accurate across products, including the two OTC drug actives. The verified gaps concentrate on Perplexity (fragrance omission, treatment downplay) and on the recommendation omission, not on hard specs. Score raised to 78 of 100. A full audit would test every individual SKU across all four engines; on this evidence it would mostly confirm accuracy and catch the Perplexity gaps.

## RE-VERIFICATION 2026-06-11 (triggered by client live check) — important
A live re-check of the same queries shows the findings have decayed:
- Perplexity "is the All Over Ointment fragrance-free?": NOW CORRECT. Names both the fragrance-free and Lavender + Rosemary scented versions, and that the scented one has fragrance and lavender oils. Earlier capture (omitting the scented version) does NOT reproduce today.
- Perplexity "eczema treatment or just a moisturizer?": NOW CORRECT. "marketed as an eczema treatment and also as a moisturizer... not just a plain moisturizer." Earlier "not a medical treatment" framing does NOT reproduce.
- Google "best baby eczema cream for newborns": STILL omits Tubby Todd (names Aveeno, Mustela, CeraVe). This is a visibility omission, not an accuracy error.

CONCLUSION: As of 2026-06-11, there is NO material, current accuracy error standing for Tubby Todd on the queries checked. Two of three findings self-corrected within roughly a day. The report built on those findings must NOT be sent as a paid accuracy audit. This is direct evidence that (a) one-time audits decay fast, (b) every audit must be re-verified with screenshots on the day it ships, with a human sign-off, and (c) the durable product is monitoring (Watchdog), not a one-time snapshot. The Tubby Todd report is marked SUPERSEDED pending an honest rewrite or retirement.
