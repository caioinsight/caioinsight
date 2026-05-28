# CAIO Insight — Master Business Context

> Single source of truth for all Claude sessions, AI agents, and automated workflows.
> Read this file completely before acting on any CAIO Insight task.
> Last updated: 2026-05-27

---

## Business Identity

**Name:** CAIO Insight
**URL:** caioinsight.ai
**Location:** Carlsbad, California

**One-line pitch:**
An AI-augmented fractional CMO practice delivering marketing audits to Shopify DTC brands that diagnose underperforming channels and AI visibility gaps. $399, 48-hour delivery.

**Elevator pitch:**
"A marketing audit tool for Shopify brands that tells you not just what is broken in your current channels, but whether AI shopping agents like ChatGPT can find you — delivered in 48 hours for $399."

---

## Business Model

### Entry product — AI-Ready Audit ($399)
- Client fills 10-minute intake form (Tally)
- Store scanned for AI visibility signals
- 7-section Notion workspace delivered in 48 hours
- No discovery calls. No agency. Async by design.

### 7 Report Sections
1. Brand snapshot — proves comprehension before advice
2. Channel scorecard — A-F grade per active channel with specific reason
3. AI Visibility Score — schema markup, llms.txt, review velocity, LLM citations, GEO content (0-100)
4. Root-cause diagnosis — real problem, not symptom
5. 3 quick wins — 30-day implementable, revenue impact estimated
6. Competitor gap analysis — including AI visibility advantage
7. 90-day dual plan — fix existing channels and build AI infrastructure

### Core retainer — $2,000/month (no contract)
Monthly AI visibility report, one GEO initiative per month, channel performance tracking, unlimited async Q&A, quarterly re-audit. Cancel anytime.

### Add-on — Strategy call ($99)
30-minute audit walkthrough, live Q&A, priority booking.

### Secondary revenue
| Product | Price |
|---|---|
| AI Readiness Toolkit | $197 |
| White-label license | $2,000-$5,000 one-time + $297/mo |
| Newsletter paid tier (The Owned Channel) | $9/month |
| Klaviyo affiliate | 20% recurring |
| Shopify affiliate | 20% recurring + $500/referral |

### Revenue path to $160K year one
- 5 audits/week x $399 = ~$103K/year
- 3 retainer clients x $2,000/month by month 6 = $72K additional
- Toolkit + affiliate = ~$15K additional
- Target achieved by month 10

---

## ICP (Ideal Customer Profile)

**Primary:** Shopify DTC brands
- Revenue: $200K-$2M annual
- Stage: 12-36 months old, founder-run
- Ad spend: $2K-$15K/month on Meta + email
- Pain signal: "What do I do now that Meta doesn't work like it used to?"

**Secondary verticals:**
- Franchise systems (multi-location, compliance-aware GEO)
- Compliance-constrained industries — NEVER name cannabis publicly; always say "compliance-constrained verticals"

---

## Positioning

The only fractional CMO who shows you how they think before you spend a dollar on a retainer. The only audit in the $200K-$2M DTC segment that grades both channel performance and AI visibility (GEO score).

**The AI angle:**
- Shopify reported 11x increase in AI-attributed orders in 2025
- 85-92% of Shopify stores are invisible to AI shopping agents
- No competitor serves the $200K-$2M DTC segment with GEO intelligence
- Window: 12-18 months before enterprise tools go downmarket

---

## Brand Voice Rules (apply to ALL outputs)

### Style
- Tight, metric-driven, no filler
- Active verbs, past-tense in bullets
- Hard numbers always included
- Single declarative sentences preferred
- Match LinkedIn profile voice: punchy, specific, no adjective padding

### AI-tell removal (always check before outputting)
Remove these patterns:
- Em-dashes used as dramatic pivots
- Rhythmic paired phrases ("Never assumed, never pressured")
- "Specific inputs produce specific outputs"
- "Your time is the constraint"
- Colon-then-list mid-sentence
- Over-hedged transitional language ("It is worth noting that...")
- Passive dramatic reveals framed as insights

### Absolute rules
- Cannabis = always "compliance-constrained verticals" in public copy
- Never use real brand names in sample audit outputs — use [Brand Name] or [Your Brand]
- Never show personal name (Patrick O'Brien) on public-facing site pages

---

## Design System

### Active palette: Navy + Orange
```
--ink:      #070D1A   deep navy
--ink-2:    #0C1526   card bg
--ink-3:    #132038   borders
--acid:     #FF6B2B   orange CTA (only CTAs + highlights)
--acid-dim: #E55A1A   hover state
--paper:    #F0F4FA   warm cool white
--paper-2:  #E4EBF5   section bg
--teal:     #00C8A0   positive grades
```

### Typography
- Headlines: Space Grotesk (400/500/600/700)
- Mono labels: Geist Mono (400/500)
- Body: system-ui fallback

### Visual language
- NI Komplete-inspired hero: dark field + generative orb + chromatic rings + data particles
- Scanline texture on dark sections
- Chromatic gradient nav line (orange to blue to purple)
- Terminal UI for AI visibility demo

---

## Technical Assets

| Asset | Value |
|---|---|
| GitHub repo | github.com/caioinsight/caioinsight |
| GitHub branch | main |
| Netlify site ID | resilient-caramel-20a59e |
| Netlify URL | resilient-caramel-20a59e.netlify.app |
| Custom domain | caioinsight.ai |
| Domain registrar | Porkbun |
| Nameservers | dns1-dns4.p06.nsone.net |
| LinkedIn | linkedin.com/in/panalyst |
| Current site file | index.html (v1 live) |
| Pending deploy | caioinsight_navy.html (v2 — Navy+Orange design) |

### Tech stack
Netlify (hosting), GitHub (CI/CD), HubSpot (CRM), Brevo (email), Tally (forms), Calendly (scheduling), Zapier (automation), Tidio (chat), GA4 + Clarity (analytics), Stripe (payments), Canva (design via MCP).

### GitHub update workflow
1. Navigate to: github.com/caioinsight/caioinsight/edit/main/[filename]
2. Inject content via CodeMirror 6 JS: cmContent.cmTile.view.dispatch()
3. Commit to main branch
4. Netlify auto-deploys in 30 seconds

---

## Competitive Landscape

### Tier 1 — Direct threats
1. The Lifecycle Labs — diagnostic-first DTC retention, $3K-$8K/mo
2. Zoronto — founder-led DTC retention
3. DTCCOO — DTC marketing audit $299-$499 (no AI visibility)
4. eCommerce Coffee Break — DTC audit $199-$299 (no AI visibility)
5. Hawke Media — a la carte fractional CMO $2.5K-$5K/mo

### GEO tool competitors (check monthly for new launches)
- Semrush — AI Visibility Index, enterprise only, acquired by Adobe $1.9B
- Ahrefs Brand Radar — $828/month min, not ecommerce-specific
- Parcel Perform — top-10 brands only, not mid-market
- Metricus — Shopify app, individual brands only, no benchmark
- Conductor / Evertune / Brandi — Fortune 1000 only, wrong ICP

### Moat
No competitor offers a public weekly AI visibility benchmark for $200K-$2M Shopify DTC brands. No competitor offers a paid diagnostic before the retainer.

### Acquisition thesis
Targets: Shopify, Klaviyo, Semrush/Adobe, Ahrefs
Asset: Proprietary dataset of AI visibility scores across DTC brands by category
Timeline: 3-4 years, $8M-$60M outcome range

---

## Agent Roles

### Orchestrator
Routes requests to specialist agents. Reads this file first. Assembles all outputs.

### Strategy agent
Business model, competitive analysis, pivot evaluation, revenue modeling.
Always loads full context. Always stress-tests before recommending.

### Content agent
All written outputs: LinkedIn posts, site copy, audit reports, newsletter.
Always applies brand voice rules. Always runs AI-tell check before outputting.

### Research agent
Competitive and market research. Live web search.
Always check whether Semrush/Ahrefs/Shopify/Klaviyo launched new GEO products since last scan.
Always include publication dates on all findings.

### Builder agent
Website updates, GitHub commits, Netlify deploys, integrations.
Always read this file for repo URL, site ID, and design tokens before writing code.

### Audit agent
GEO scoring: LLM API queries, schema checks, review velocity scoring.
Output: AI Visibility Score 0-100 across 5 signals in structured JSON.

---

## Pending Actions (2026-05-27)

### Immediate
- [ ] SECURITY: Revoke exposed GitHub token ghp_qFXm6oK4...
- [ ] Connect Stripe Payment Link to audit submit button
- [ ] Replace Calendly placeholder URL on thank-you page
- [ ] Build Tally intake form and connect to HubSpot
- [ ] Register Shopify Partners (partners.shopify.com)
- [ ] Register Klaviyo Partners (klaviyo.com/partners)
- [ ] Push caioinsight_navy.html as new index.html (Navy+Orange v2 design)

### Month 1
- [ ] Set up Notion MCP connection
- [ ] Create 5 agent system prompt files in /agents folder
- [ ] Build beehiiv newsletter (The Owned Channel)
- [ ] Run first manual DTC AI Visibility Index (50 brands, 5 categories)
- [ ] Publish first LinkedIn post (audit-of-own-site angle)
- [ ] Send first 10 warm DMs to DTC founder contacts

### Month 2-3
- [ ] Semi-automate AI Visibility Index (Python + LLM APIs)
- [ ] Approach 5 agencies for white-label licensing at $500/month
- [ ] First fractional CMO conversation from inbound audit
- [ ] Launch AI Readiness Toolkit at $197

---

## Session Startup Instructions

When starting any new Claude session for CAIO Insight work:
1. Read this CLAUDE.md file completely before responding
2. Check the Technical Assets table for current file versions
3. Check Pending Actions for outstanding tasks
4. Identify which agent role applies to the current task
5. Apply all brand voice rules to every output
6. Never ask for context that exists in this file


---

## Quick Start Prompts

Copy and paste these at the start of any new Claude session.
No context-setting required — the file does it automatically.

---

### 1. Session startup (use this every time)

```
Read the CLAUDE.md file at github.com/caioinsight/caioinsight then confirm you have full context and tell me what's in the pending actions list.
```

---

### 2. Update the live website

```
Read CLAUDE.md at github.com/caioinsight/caioinsight. Then [describe the change you want]. Apply all brand voice rules, use the Navy+Orange design system, and push the update to GitHub so Netlify deploys it automatically.
```

---

### 3. Write a LinkedIn post

```
Read CLAUDE.md at github.com/caioinsight/caioinsight. Write a LinkedIn post about [topic]. Apply all brand voice rules and AI-tell removal checks. Format for 1,200-1,500 characters. No links in the post body — first comment only. Use the problem-led format unless specified otherwise.
```

---

### 4. Evaluate a business pivot or idea

```
Read CLAUDE.md at github.com/caioinsight/caioinsight. Evaluate this idea: [describe idea]. Stress-test it against the existing business model, competitive landscape, and acquisition thesis. Score it on market size, defensibility, time to revenue, and fit with the behind-the-scenes operator constraint. Recommend yes, no, or modify.
```

---

### 5. Run a competitive scan

```
Read CLAUDE.md at github.com/caioinsight/caioinsight. Run a current competitive scan for CAIO Insight. Check whether Semrush, Ahrefs, Shopify, Klaviyo, or Metricus have launched new GEO or AI visibility products since the last scan. Check for any new direct competitors in the $200K-$2M DTC audit space. Include publication dates on all findings. Flag anything that changes the moat or acquisition thesis.
```

---

### 6. Generate a marketing audit (for a real client intake)

```
Read CLAUDE.md at github.com/caioinsight/caioinsight. Run the AI-Ready Marketing Audit for the following intake answers: [paste intake form responses]. Follow the 7-section format. Apply all brand voice rules. Use [Brand Name] if referencing competitor examples. Deliver as a structured Notion-ready document.
```

---

### 7. Update CLAUDE.md itself

```
Read CLAUDE.md at github.com/caioinsight/caioinsight. Add or update the following information: [describe the change]. Preserve all existing sections. Commit the updated file to GitHub.
```

---

### 8. Research a specific topic for CAIO Insight

```
Read CLAUDE.md at github.com/caioinsight/caioinsight. Research [topic] specifically for CAIO Insight's context — ICP is Shopify DTC brands $200K-$2M, positioning is GEO + channel audit, acquisition target is Shopify/Klaviyo/Semrush. Include dates on all sources. Flag anything that changes strategy or creates urgency.
```

---

### 9. Create a design asset in Canva

```
Read CLAUDE.md at github.com/caioinsight/caioinsight. Create a [asset type] in Canva for CAIO Insight. Use the Navy+Orange design system: deep navy #070D1A background, orange #FF6B2B accent, Space Grotesk typography. Purpose: [describe purpose and where it will be used].
```

---

### 10. Full business strategy session

```
Read CLAUDE.md at github.com/caioinsight/caioinsight. I want to work through [strategic question or decision]. Load full business context including the competitive landscape, acquisition thesis, revenue model, and pending actions. Think as the strategy agent. Stress-test before recommending.
```

---

## Prompt Writing Guide

When writing new prompts for this system, always include:
1. "Read CLAUDE.md at github.com/caioinsight/caioinsight" as the first line
2. The specific task clearly stated
3. Any constraints not already in CLAUDE.md
4. The desired output format

What NOT to include in prompts (already in CLAUDE.md):
- Brand voice rules
- ICP description
- Pricing details
- Competitor list
- Design system values
- Writing style rules
- Cannabis language rules
- Real brand name prohibition
