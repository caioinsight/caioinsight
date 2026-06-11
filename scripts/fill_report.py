#!/usr/bin/env python3
"""
Fill the AI Accuracy Report template for one client, in one command.

    python scripts/fill_report.py clients/<brand>.json [output.html]

Reads templates/report-template.html, fills the header fields, regenerates the
score table and the findings list from the client JSON, and writes a finished
report. Honest data only: every finding must be a real captured answer. Leave a
field out and the script tells you what is still unfilled.
"""
import json, re, sys, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "templates", "report-template.html")


def esc(t):
    return str(t).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def score_rows(areas):
    return "\n".join(
        '    <tr><td>%s</td><td>%s</td><td>%s</td></tr>'
        % (esc(a["area"]), esc(a.get("score", "")), esc(a.get("note", "")))
        for a in areas)


def finding_blocks(findings):
    out = []
    for fd in findings:
        ok = fd.get("status", "wrong") == "ok"
        cls = "q" if ok else "q bad"
        tag = ('<span class="tag good">Correct</span>' if ok
               else '<span class="tag out">Fact to fix</span>')
        if ok:
            body = "AI answered %s, which is right. %s %s" % (
                esc(fd["wrong"]), esc(fd.get("truth", "")), esc(fd.get("impact", "")))
        else:
            body = "AI answered %s. %s %s %s" % (
                esc(fd["wrong"]), esc(fd.get("verdict", "That is incorrect.")),
                esc(fd.get("truth", "")), esc(fd.get("impact", "")))
        body = re.sub(r"\s+", " ", body).strip()
        out.append(
            '  <div class="%s">\n'
            '    <div class="qq">"%s"</div>\n'
            '    <div class="qa">%s %s</div>\n'
            '  </div>' % (cls, esc(fd["query"]), body, tag))
    return "\n".join(out)


def between(s, start, end, new):
    a = s.index(start) + len(start)
    b = s.index(end)
    return s[:a] + "\n" + new + "\n  " + s[b:]


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: python scripts/fill_report.py clients/<brand>.json [out.html]")
    data = json.load(open(sys.argv[1], encoding="utf-8"))
    brand = data["brand"]
    s = open(TEMPLATE, encoding="utf-8").read()

    for ph in ("[Brand Name]", "[Brand]"):
        s = s.replace(ph, esc(brand))
    if data.get("category"):
        s = s.replace("[Baby formula]", esc(data["category"]))
    if data.get("date"):
        s = s.replace("[Date]", esc(data["date"]))
    if data.get("facts_wrong"):
        s = s.replace("[4 of 12]", esc(data["facts_wrong"]))
    if data.get("engines"):
        s = s.replace("on ChatGPT and Perplexity.", "on %s." % esc(data["engines"]))

    done = data.get("done", {})
    for ph, key in (("[3]", "pages"), ("[5]", "labels"), ("[6]", "faqs")):
        if done.get(key) is not None:
            s = s.replace(ph, esc(done[key]))

    if data.get("mode") == "freecheck":
        eng = esc(data.get("engines", "Perplexity"))
        price = esc(data.get("report_price", "$1,500"))
        s = s.replace('<div class="rtype">AI Accuracy Report</div>',
                      '<div class="rtype">AI Accuracy Free Check</div>')
        s = re.sub(r'<div class="lead">.*?</div>',
            '<div class="lead">This is a free check for %s. We asked %s the questions a parent '
            'asks before buying, and we recorded what it said. Below are the answers that need '
            'fixing. The full AI Accuracy Report checks twelve questions across ChatGPT, Perplexity, '
            'Gemini, and Google AI Overviews, scores your accuracy, and traces every error to its '
            'source.</div>' % (esc(brand), eng), s, count=1, flags=re.S)
        s = re.sub(r'<h2>Your AI Accuracy Score</h2>.*?</table>',
            '<h2>What this free check covers</h2>\n  <p>This sample looked at %s. We did not score '
            'your full accuracy here. Your AI Accuracy Score across ChatGPT, Perplexity, Gemini, and '
            'Google AI Overviews comes with the full report.</p>' % eng, s, count=1, flags=re.S)
        s = re.sub(r'<h2>Already done for you</h2>.*?</ul>',
            '<h2>What the full report adds</h2>\n  <ul class="done">\n'
            '    <li>Runs all twelve buyer questions across ChatGPT, Perplexity, Gemini, and Google AI Overviews</li>\n'
            '    <li>Scores your accuracy and traces every wrong answer to the source AI reads</li>\n'
            '    <li>Gives you a ranked 90-day fix plan with the exact changes</li>\n  </ul>', s, count=1, flags=re.S)
        s = re.sub(r'<h2>What happens next</h2>.*?they can act on it\.</p>',
            '<h2>What happens next</h2>\n    <p>This free check is yours to keep. The full AI Accuracy '
            'Report is %s. It covers all four engines, scores your accuracy, and gives you the exact '
            'fixes. If you continue with a monthly plan, the report fee credits toward your first '
            'month.</p>\n    <div class="cta">Reply to the email this came from and we will run the '
            'full report. No call needed.</div>\n  </div>\n\n  <p class="devnote">Every fix in the '
            'full report includes the exact change and how to verify it, so you or your developer can '
            'act on it directly.</p>' % price, s, count=1, flags=re.S)

    if data.get("mode") != "freecheck":
        if data.get("lead"):
            lead = esc(data["lead"])
            s = re.sub(r'<div class="lead">.*?</div>',
                       lambda m: '<div class="lead">' + lead + '</div>', s, count=1, flags=re.S)
        if data.get("stage") == "diagnostic":
            done_new = ('<h2>What we fix first</h2>\n  <ul class="done">\n'
                '    <li>Correct the facts AI is getting wrong on the pages and listings it reads</li>\n'
                '    <li>Add the missing product details so AI stops filling gaps with guesses</li>\n'
                '    <li>Strengthen the third-party sources AI trusts so the right answer sticks</li>\n  </ul>')
            s = re.sub(r'<h2>Already done for you</h2>.*?</ul>', lambda m: done_new, s, count=1, flags=re.S)
            next_new = ('<h2>What happens next</h2>\n    <p>This report is the diagnosis. If you want us to make '
                'the fixes, watch the engines each month, and prove each correction, that is the Done For You '
                'plan at $2,500 a month, or AI Watchdog at $79 a month for monitoring alone. The $1,500 for '
                'this report credits toward your first month if you continue.</p>\n    <div class="cta">Reply '
                'to the email this came from and we will start. No call needed.</div>\n  </div>\n\n  '
                '<p class="devnote">Every fix in this report includes the exact change and how to verify it, '
                'so you or your developer can act on it directly.</p>')
            s = re.sub(r'<h2>What happens next</h2>.*?they can act on it\.</p>', lambda m: next_new, s, count=1, flags=re.S)

    sc = {} if data.get("mode") == "freecheck" else data.get("score", {})
    if sc.get("overall") is not None:
        s = re.sub(r'<span class="big">\d+</span>',
                   '<span class="big">%s</span>' % esc(sc["overall"]), s, count=1)
    if sc.get("note"):
        s = re.sub(r'(<div class="sl">).*?(</div>)',
                   lambda m: m.group(1) + esc(sc["note"]) + m.group(2), s, count=1, flags=re.S)
    if sc.get("areas"):
        s = between(s, "<!--FILL:scores-->", "<!--/FILL:scores-->", score_rows(sc["areas"]))
    if data.get("findings"):
        s = between(s, "<!--FILL:findings-->", "<!--/FILL:findings-->", finding_blocks(data["findings"]))

    out = sys.argv[2] if len(sys.argv) > 2 else os.path.join(
        ROOT, "outputs", re.sub(r"[^a-z0-9]+", "-", brand.lower()).strip("-") + "-accuracy-report.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8").write(s)

    leftover = sorted(set(re.findall(r"\[[A-Za-z0-9 ,.%/'-]+\]", s)))
    print("wrote", out)
    print("STILL UNFILLED:", ", ".join(leftover) if leftover else "(none)")


if __name__ == "__main__":
    main()
