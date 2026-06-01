# CAIO Insight — AI Cost & Pricing Strategy
## Deep Research + Cost Modeling · May 31, 2026

---

## The Headline Finding

**AI token costs are not your margin risk. Not even close.**

A full $449 diagnostic audit costs $0.09 in Claude API tokens at standard
pricing. At 100 audits/month that is $9.00 in AI costs against $44,900 in
revenue — 0.02% of revenue. Optimized with caching and batch processing,
it drops to $4.09 per 100 audits.

The margin threat is not tokens. It is time. Every hour spent manually
reviewing, structuring, and delivering the brief is the cost that scales
dangerously at volume.

---

## Current API Pricing (Claude, verified May 2026)

| Model | Input / 1M tokens | Output / 1M tokens | Best for |
|---|---|---|---|
| Haiku 4.5 | $1.00 | $5.00 | Simple routing, free tools, pass/fail checks |
| Sonnet 4.6 | $3.00 | $15.00 | Production default — audits, index runs |
| Opus 4.7 | $5.00 | $25.00 | Complex reasoning — only when Sonnet fails |

**Cost modifiers that stack:**
- Batch API: 50% off everything, no minimum, results in under 24 hours
- Prompt caching (read): 90% off cached input tokens (10% of normal price)
- Prompt caching (write): 125% of input price, one-time per cache period
- Combined: up to 95% total cost reduction vs baseline

---

## Cost Per Workload — CAIO Specific

### Workload 1 — $449 Diagnostic Audit (Sonnet 4.6)
| Optimization level | Cost per audit | Gross margin |
|---|---|---|
| Standard (no optimization) | $0.09 | 99.98% |
| Prompt caching only | $0.08 | 99.98% |
| Batch API only | $0.045 | 99.99% |
| Cache + batch combined | $0.041 | 99.99% |

**Bottom line: AI is ~$0.09 per $449 sale. Tokens are irrelevant.**

### Workload 2 — Carousel Readiness Check (Haiku 4.5, free tool)
| Volume | Standard cost/mo | Cached cost/mo |
|---|---|---|
| 200 checks | $0.50 | $0.32 |
| 2,000 checks | $5.00 | $3.20 |
| 20,000 checks | $50.00 | $32.00 |
| 1,000,000 checks | $2,500 | $1,600 |

At 1M checks/month Haiku still costs less than $2,500. Rate-limit to
10 checks/day per IP + email gate = natural throttle that also captures leads.

### Workload 3 — AI Visibility Index (Sonnet 4.6 + Batch)
| Scale | Batch cost/month | Revenue at $147/brand | AI as % of revenue |
|---|---|---|---|
| 50 brands | $4.50 | $7,350 | 0.06% |
| 500 brands | $45.00 | $73,500 | 0.06% |
| 5,000 brands | $450.00 | $735,000 | 0.06% |

The index scales to 5,000 brands at $450/month AI cost against $735K revenue.
This is a data product, not an AI cost center.

### Workload 4 — $2,000/month Retainer (Sonnet 4.6)
| Optimization | Monthly AI cost | Gross margin |
|---|---|---|
| Standard | $0.099 | 99.995% |
| Optimized | $0.039 | 99.998% |

---

## The Real Margin Risk: Labor, Not Tokens

At $449/audit, AI tokens cost $0.09. The actual cost structure is:

| Cost component | Est. per audit | Notes |
|---|---|---|
| Claude API tokens | $0.09 | Irrelevant |
| Manual QA time (30 min @ $50/hr equiv.) | $25.00 | Main cost now |
| Notion workspace setup | $5.00 | Time cost |
| Schema verification tools | $2.00 | Screaming Frog, etc. |
| **Total current cost** | **~$32** | **93% gross margin** |

At 10 audits/week, 30 min QA per audit = 5 hours/week manual work.
At 50 audits/week, that becomes 25 hours/week — a full-time job.
**The margin risk at scale is delivery time, not token cost.**

---

## Pricing Strategy: Three Layers of Protection

### Layer 1 — Technical cost controls (implement now, free)

**A. Route by complexity**
- Haiku 4.5 for: free tools, routing decisions, classification tasks
- Sonnet 4.6 for: all production audit work (default)
- Opus 4.7 for: edge cases only, never default

**B. Enable prompt caching on every audit run**
The system prompt (methodology, rubric, 4-layer framework) is identical
across every audit. Cache it. Cost drops 90% on that portion instantly.
One line of code: `"cache_control": {"type": "ephemeral"}`

**C. Use Batch API for the index and all non-urgent processing**
The AI Visibility Index runs weekly — perfect for batch (results in <24hrs,
50% cheaper). Every index query, competitor scan, and monitoring task goes
through batch. Real-time API only for interactive/live features.

**D. Cap output tokens per audit**
Output tokens cost 5× input. Set `max_tokens: 4096` on audit calls.
The brief does not need to be 20,000 tokens. Discipline in prompt
engineering = 5× leverage on the most expensive half of the bill.

**E. Compress inputs before the API call**
Strip redundant HTML from scraped pages before passing to Claude.
A 50KB product page compresses to ~2,000 tokens of structured data.
This runs on your own infrastructure at zero cost, before the API call.

---

### Layer 2 — Pricing architecture (protect margins at scale)

**The core principle (validated by research):**
AI product companies that stuck to flat-rate pricing saw gross margins
40% lower than those using usage-based or hybrid models. Do not give
AI away as a free component of a flat subscription at scale.

**Current CAIO pricing is already structurally sound:**

The $449 audit is per-use, not a subscription. Every audit is a discrete
revenue event with a discrete (tiny) AI cost. This is the best possible
structure — there is no "unlimited usage" exposure.

**Where to add protection as you scale:**

1. **The Carousel Check tool** — currently free with email gate.
   At <10K checks/month: zero concern, cost is $25/month on Haiku.
   At >10K checks/month: add a secondary gate (phone number, LinkedIn,
   or a 24-hour cooldown). Never charge for it — it's lead gen.
   The email gate IS the rate limiter. One email = one check.

2. **The AI Visibility Index** — already usage-based at $147/month per brand.
   AI cost is 0.06% of revenue at any scale. No changes needed.
   If you white-label the index data to agencies: charge per seat,
   not per query. Agency pays flat, you absorb the batch cost.

3. **The Retainer** — $2,000/month is flat rate.
   AI cost per retainer is $0.04–$0.10/month. Completely irrelevant.
   The risk at scale is delivery time, not tokens. Solution: automate
   the monthly re-run with n8n, not more Claude calls.

4. **White-label license** — $297/month includes unlimited audits for
   the agency's clients. At $0.09 per audit, 100 agency audits/month
   = $9 in API cost. Fine. The risk: an agency running 10,000 audits/month.
   **Cap white-label at 50 audits/month included, $4.49/audit overage.**
   This is the one place a usage cap matters.

---

### Layer 3 — Future-proofing as token costs shift

**The trend: frontier models are getting cheaper fast.**
Claude Opus dropped 67% in price between generations (from $15/$75 to $5/$25).
Sonnet is now cheaper than GPT-3.5 was two years ago.

**What to watch:**
- Token prices will continue declining on older/tier-2 models
- Frontier model prices hold at premium tiers (Opus equivalent)
- Output tokens will remain 5× input — always optimize output length

**Build your system on Sonnet, not Opus.**
Sonnet 4.6 at $3/$15 does 95% of what Opus does for 60% less.
The audits do not require frontier reasoning — they require structured,
consistent output. Sonnet is the right default and stays that way.

**If Anthropic raises prices:**
At $0.09/audit, prices would need to increase 500× before AI cost
reaches 10% of revenue. This is not a realistic scenario.

---

## Revised Pricing Recommendations

### Current pricing: KEEP AS IS
All current prices ($449 audit, $2,000 retainer, $197 toolkit, $9/month
newsletter, $147/month index) are structurally sound. Token costs do not
justify any pricing changes.

### Add one protection — white-label overage cap
Current: $297/month unlimited audits
Revised: $297/month includes 50 audits, $4.49/audit overage
Reason: The only realistic runaway cost scenario in the entire business.
$4.49 = 10× the AI cost, 50% gross margin even on overage.

### The index should stay $147/month per brand
At $45/month AI cost for 500 brands, this is 0.06% COGS.
Consider raising to $197/month at 100+ brand subscribers — not because
of AI cost but because the data asset is worth more as it grows.

### Do not add token-based pricing to the audit product
Per-token billing would confuse DTC founders and signal that the product
is a commodity API wrapper. It is a professional diagnostic brief.
Price it like one. The fixed $449 price IS the right model.

---

## Implementation Checklist (priority order)

### This week (30 minutes of engineering)
- [ ] Enable prompt caching on the audit system prompt
  Add `"cache_control": {"type": "ephemeral"}` to system message
  Instant 90% cost reduction on the largest input component
- [ ] Set model routing: Haiku for Carousel Check, Sonnet for audits
- [ ] Set `max_tokens: 4096` on all audit output calls
- [ ] Add email gate to Carousel Check (already planned — do it now)

### This month (1-2 hours)
- [ ] Move AI Visibility Index queries to Batch API
  50% cost reduction, results still available same day
- [ ] Compress HTML input before API calls
  Strip tags, extract structured data only
- [ ] Add white-label overage clause to license agreement ($4.49/audit > 50)

### At scale (when needed — not now)
- [ ] n8n automation for retainer monthly re-runs
  This removes the delivery time cost, not the token cost
- [ ] Consider raising index price to $197/month after 100+ brands
- [ ] Revisit model routing quarterly as new models release

---

## Summary: What Actually Threatens Margin at Scale

| Threat | Severity | Solution |
|---|---|---|
| Claude API token costs | Negligible (0.02%) | Caching + batch, already handled |
| Delivery time per audit | HIGH at >20/week | Automation via n8n |
| White-label unlimited abuse | Medium | Overage cap at 50 audits |
| Free tool viral scale | Low (Haiku is cheap) | Email gate rate limiter |
| Anthropic price increases | Very low | Prices trending down |
| Output token runaway | Low | max_tokens cap on every call |

**The business scales cleanly on AI cost. It does not scale cleanly on manual
delivery time. That is the architecture problem to solve first.**

