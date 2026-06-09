#!/usr/bin/env python3
"""Daily research -> dashboard-data.json for cowy.ai/dashboard.html.
Runs in GitHub Actions. Calls the Anthropic API (web search enabled) to gather
real DTC + Cannabis CPG AI-commerce intel, then writes dashboard-data.json.
Fails WITHOUT overwriting if the model output is invalid, so a bad run never
breaks the live dashboard."""
import os, sys, json, re, datetime

try:
    import anthropic
except ImportError:
    sys.exit("anthropic SDK not installed")

API_KEY = os.environ.get("ANTHROPIC_API_KEY")
if not API_KEY:
    sys.exit("ANTHROPIC_API_KEY not set (add it as a repo secret)")

OUT = os.environ.get("OUT_PATH", "dashboard-data.json")
MODEL = os.environ.get("MODEL", "claude-sonnet-4-6")

today = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-7)))  # PT-ish
date_str = today.strftime("%B %-d, %Y") + " · 6:00 AM PT"

SCHEMA = """{
  "date": "<set by caller>",
  "generatedNote": "<ISO datetime>",
  "dtc":      { "priority": str, "metrics": [{"n":str,"l":str} x5], "landscape": [{"level":"high|medium|low","source":str,"headline":str,"body":str} x3-4], "topIdea": {"label":str,"title":str,"body":str,"chips":[str,str,str]}, "competitors": [{"name":str,"threat":"high|medium|low","changed":str,"howToWin":str} x2-3] },
  "cannabis": { same shape as dtc }
}"""

PROMPT = f"""You are the research engine for an internal (gated, private) intelligence dashboard.
Today is {date_str}. Use web search to find REAL, recent (last ~1-3 days) developments. Hard facts only — never invent. If you cannot verify something, leave it out. Cite the real source name in each item's "source" field.

Produce intel for TWO verticals:
1. dtc — DTC / Shopify founders ($200K-$2M revenue) and AI/agentic commerce: ChatGPT shopping & Instant Checkout, Perplexity, Google AI Overviews, Shopify AI features, GEO/AEO tooling, competitor/agency moves.
2. cannabis — Cannabis CPG marketing for compliance-constrained brands: state regulatory/compliance changes (CA DCC, TCPA/SMS, advertising rules), AI-visibility/GEO developments, platform moves (Springbig, Alpine IQ, Leafly, Weedmaps).

For each vertical assemble: one `priority` (single most important action today), 3-4 `landscape` shifts, a `topIdea` (a validated business idea with profitability/ease scores and a $ range in chips), and 2-3 `competitors` (name, threat level, what changed, how to win).

Update the metric numbers to reflect what you actually found. Keep the dtc metrics labels: ["Landscape shifts","Y1 forecast","High threats","Pivots","Validated ideas"] (Y1 forecast stays "$186K"). Keep cannabis metric labels: ["Compliance updates","High threats","Pivots","Validated ideas"].

Output ONLY a single JSON object, no prose, no markdown fences, matching exactly this schema:
{SCHEMA}
Set "date" to "{date_str}" and "generatedNote" to "auto-generated {today.isoformat()}"."""

client = anthropic.Anthropic(api_key=API_KEY)
resp = client.messages.create(
    model=MODEL,
    max_tokens=8000,
    tools=[{"type": "web_search_20250305", "name": "web_search", "max_uses": 8}],
    messages=[{"role": "user", "content": PROMPT}],
)

# collect text from the final assistant message
text = "".join(b.text for b in resp.content if getattr(b, "type", "") == "text")
m = re.search(r"\{.*\}", text, re.S)
if not m:
    sys.exit("No JSON object found in model output:\n" + text[:1000])

try:
    data = json.loads(m.group(0))
except json.JSONDecodeError as e:
    sys.exit(f"Model output is not valid JSON: {e}\n{m.group(0)[:1000]}")

# validate shape — refuse to write a broken file
def ok_vert(v):
    return all(k in v for k in ("priority", "metrics", "landscape", "topIdea", "competitors")) \
        and isinstance(v["landscape"], list) and len(v["landscape"]) >= 1 \
        and isinstance(v["competitors"], list) and len(v["competitors"]) >= 1
if not (isinstance(data, dict) and "dtc" in data and "cannabis" in data
        and ok_vert(data["dtc"]) and ok_vert(data["cannabis"])):
    sys.exit("Validation failed — not overwriting dashboard-data.json. Got keys: " + str(list(data.keys())))

data.setdefault("date", date_str)
data["generatedNote"] = f"auto-generated {today.isoformat()}"

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"Wrote {OUT}: dtc={len(data['dtc']['landscape'])} shifts, cannabis={len(data['cannabis']['landscape'])} shifts")
