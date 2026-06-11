# Client report data

One JSON file per client, named clients/<brand-slug>.json. Fill it from a real
free check, then run:

    python scripts/fill_report.py clients/<brand-slug>.json

The finished report lands in outputs/<brand-slug>-accuracy-report.html.

Rules: honest captures only. Every finding must be a real answer you recorded
from a named engine. Do not invent a score, a quote, or an AI answer. If you
only sampled one engine, say so in "engines" and keep the score partial.
sample-brand.json is an illustrative example with invented data, not a real brand.
