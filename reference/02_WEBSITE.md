# Website Reference

## Live Assets
| Asset | Value |
|---|---|
| GitHub repo | github.com/caioinsight/caioinsight |
| GitHub branch | main |
| Hosting | Cloudflare Workers (migrated from Netlify) |
| Workers URL | caioinsight.caiospheric.workers.dev |
| Custom domain | caioinsight.ai |
| Domain registrar | Porkbun |
| Nameservers | Cloudflare (migrated from Netlify nsone.net) |
| Netlify site ID | resilient-caramel-20a59e (no longer primary) |

## Output Files
| File | Description |
|---|---|
| index.html | Current live site (v1) |
| caioinsight_navy.html | V2 Navy+Orange design — ready to push |
| index_v2_fixed.html | V2 with all fixes applied |
| caio_palettes.html | 5-palette interactive showcase |

## GitHub Update Workflow
1. Navigate to: github.com/caioinsight/caioinsight/edit/main/[filename]
2. Inject content via CodeMirror 6 JS: cmContent.cmTile.view.dispatch()
3. Commit to main branch
4. Cloudflare auto-deploys in ~30 seconds

## Design System — Navy + Orange (approved)
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

## Typography
- Headlines: Space Grotesk (400/500/600/700)
- Mono labels: Geist Mono (400/500)
- Body: system-ui fallback

## Visual Language (NI Komplete-inspired)
- Dark field + generative orb + chromatic rings + data particles
- Scanline texture on dark sections
- Chromatic gradient nav line (orange → blue → purple)
- Terminal UI for AI visibility demo
- Orange accent ONLY on CTAs, never as background

## Pages (6 total)
1. Home — hero + channel shift + scorecard + GEO + how it works + testimonials + FAQ + CTA
2. DTC Audit — product detail + 7 sections + pricing
3. Audit form — Tally intake (10 questions)
4. About — trust-reversal story + principles
5. Newsletter — The Owned Channel
6. Thank you — post-purchase next steps

## Pending Site Updates
- [ ] Connect Stripe Payment Link to audit submit button
- [ ] Replace Calendly placeholder URL on thank-you page
- [ ] Push caioinsight_navy.html as new index.html (v2)
- [ ] Install GA4
- [ ] Add Tidio live chat
- [ ] Fix: sample offer moved pre-purchase (not post-purchase)

## Writing Rules (apply to ALL site copy)
- No em-dashes as dramatic pivots
- No mid-sentence colons
- No rhythmic paired phrases
- Active verbs, hard numbers, no filler
- Cannabis = "compliance-constrained verticals" only
- Never use real brand names in sample outputs — [Brand Name] or [Your Brand]
- Never show personal name on public-facing pages
