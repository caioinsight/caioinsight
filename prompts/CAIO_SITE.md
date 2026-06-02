# CAIO_SITE — Site Update Template

## Role
Updating caioinsight.ai - single HTML file served from Cloudflare Workers. All CSS, JS, and content inline. Maintain brand system and tone rules exactly.

## Brand System (never deviate)
Fonts: Barlow Condensed 700 (logo) / IBM Plex Mono (data) / Space Grotesk (body)
Colors: #FF6B2B accent / #070D1A background / #F0F4FA text / #00C8A0 teal
Logo mark: 3x3 dot grid, diagonal TR(0.95) to BL(0.22), rest 0.18

## Copy Rules
- No revolutionary, seamless, cutting-edge, dynamic, empower
- Active engineering verbs
- No first person in brand copy
- Data translation layer is the core metaphor

## Site Pages
page-home / page-dtc / page-audit / page-about / page-newsletter / page-thankyou / page-carousel / page-login / page-dashboard / page-glossary

## Current Prices
$449 audit / $2,000 month retainer / $99 strategy call / $197 toolkit / $147 month index / $9 month newsletter

## Update Protocol
1. State which page ID or section is affected
2. Show current text being changed
3. Show proposed replacement
4. Confirm brand system compliance
5. Output only changed HTML snippet unless full rebuild requested

Deploy: push to GitHub main -> Cloudflare auto-deploys in ~30 seconds
