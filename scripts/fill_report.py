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


def cta_buttons(cta):
    btns = []
    if cta.get("dfy_url"):
        btns.append('<a href="' + esc(cta["dfy_url"]) + '" style="display:inline-block;background:var(--ink);color:#fff;font-weight:800;font-size:15px;padding:14px 26px;border-radius:10px;text-decoration:none;margin:5px">Start Done For You, $2,500 a month &rarr;</a>')
    if cta.get("watchdog_url"):
        btns.append('<a href="' + esc(cta["watchdog_url"]) + '" style="display:inline-block;background:var(--card);color:var(--ink);border:2px solid var(--mint-deep);font-weight:800;font-size:15px;padding:12px 24px;border-radius:10px;text-decoration:none;margin:5px">Just monitor, AI Watchdog $79 a month</a>')
    if not btns:
        return None
    return ('<div class="cta" style="border:none;background:transparent;padding:0;text-align:center">'
            + "".join(btns)
            + '<div style="font-size:12.5px;color:var(--muted);margin-top:10px;font-weight:600">Secure checkout through Stripe. No call needed.</div></div>')


def stakes_box(st):
    lo = st.get("deter_low", 1); hi = st.get("deter_high", 3)
    def numfmt(x): return "{:,}".format(int(round(x)))
    def pct(x): return ("%g" % x)
    if st.get("products"):
        products = st["products"]
    else:
        products = [{"name": st.get("product", "Your product"), "price": st.get("price", 0),
                     "units": st.get("units_monthly") or st.get("units_example", 0), "gap": True}]
    inp = "border:1px solid var(--border);border-radius:8px;padding:6px 8px;font:inherit;font-weight:700;color:var(--ink);background:#fff"
    rows = ""; meta = []; init_lines = []; tl = 0.0; th = 0.0
    for i, p in enumerate(products):
        gap = p.get("gap", True); name = esc(p["name"])
        meta.append({"i": i, "name": p["name"], "gap": bool(gap)})
        if gap:
            price = p.get("price", 0) or 0; units = p.get("units", 0) or 0
            el = price * units * lo / 100.0; eh = price * units * hi / 100.0
            tl += el; th += eh
            rows += ('<div style="margin:8px 0;line-height:1.7">'
                     '<label style="font-weight:800"><input type="checkbox" id="cowyChk' + str(i) + '" checked style="margin-right:8px;vertical-align:middle">' + name + '</label> '
                     'at $<input id="cowyPrice' + str(i) + '" type="number" min="0" step="1" value="' + esc(price) + '" style="' + inp + ';width:78px"> on '
                     '<input id="cowyUnits' + str(i) + '" type="number" min="0" step="1" value="' + esc(units) + '" style="' + inp + ';width:104px"> units a month '
                     '<span style="font-size:12px;color:var(--muted)">(units illustrative)</span></div>')
            init_lines.append(p["name"] + ": $" + numfmt(price) + " on " + numfmt(units) + " units at " + pct(lo) + " to " + pct(hi) + " percent gives $" + numfmt(min(el, eh)) + " to $" + numfmt(max(el, eh)) + " a month")
        else:
            rows += ('<div style="margin:8px 0;line-height:1.7">'
                     '<label style="font-weight:800"><input type="checkbox" id="cowyChk' + str(i) + '" checked style="margin-right:8px;vertical-align:middle">' + name + '</label> '
                     '<span style="color:var(--muted)">no gaps found on the engines we checked, $0</span></div>')
            init_lines.append(p["name"] + ": no gaps found on the engines we checked, $0")
    init_lines.append("Units are illustrative, replace with your figures. The deterrence rate is a conservative assumption. Exposure is revenue at risk, not a billed loss.")
    init_total = "about $" + numfmt(min(tl, th)) + " to $" + numfmt(max(tl, th)) + " a month"
    init_ul = "".join("<li>" + esc(x) + "</li>" for x in init_lines)
    meta_json = json.dumps(meta)
    box = ('<div class="stakes" style="border:1px solid #e6e6e6;border-radius:14px;padding:20px 22px;margin:24px 0;background:#f6faf9">'
           '<h2 style="margin-top:0">What these gaps are worth</h2>'
           '<p>Here is the revenue exposed across the products we audited, as a model you can check. Pick any product or combination, and edit the numbers. It is exposure, not a billed loss.</p>'
           '<div style="font-weight:700;margin:6px 0 2px">Products included, all audited products selected by default</div>'
           + rows
           + '<div style="margin:12px 0 2px">Buyers misdirected by a wrong answer: '
             '<input id="cowyLo" type="number" min="0" max="100" step="0.5" value="' + esc(lo) + '" style="' + inp + ';width:60px"> to '
             '<input id="cowyHi" type="number" min="0" max="100" step="0.5" value="' + esc(hi) + '" style="' + inp + ';width:60px"> percent, a conservative assumption</div>'
           + '<p style="font-size:1.25rem;font-weight:800;margin:14px 0 4px">Total revenue exposed: <span id="cowyOut">' + init_total + '</span>.</p>'
           + '<div style="font-weight:700;font-size:13.5px;margin-top:10px">Assumptions and calculation</div>'
           + '<ul id="cowyCalc" style="font-size:13px;color:#555;margin:4px 0 0;padding-left:18px">' + init_ul + '</ul>'
           + '</div>'
           + '<script>(function(){var P=' + meta_json + ';'
             'function f(n){return "$"+Math.round(n).toLocaleString("en-US");}'
             'function g(id){var e=document.getElementById(id);return e?parseFloat(e.value)||0:0;}'
             'function calc(){var lo=g("cowyLo"),hi=g("cowyHi"),tl=0,th=0,lines=[];'
             'P.forEach(function(p){var c=document.getElementById("cowyChk"+p.i);if(!c||!c.checked)return;'
             'if(p.gap){var pr=g("cowyPrice"+p.i),u=g("cowyUnits"+p.i),el=pr*u*lo/100,eh=pr*u*hi/100;tl+=el;th+=eh;'
             'lines.push(p.name+": $"+pr.toLocaleString("en-US")+" on "+u.toLocaleString("en-US")+" units at "+lo+" to "+hi+" percent gives "+f(Math.min(el,eh))+" to "+f(Math.max(el,eh))+" a month");}'
             'else{lines.push(p.name+": no gaps found on the engines we checked, $0");}});'
             'var o=document.getElementById("cowyOut");if(o)o.textContent="about "+f(Math.min(tl,th))+" to "+f(Math.max(tl,th))+" a month";'
             'lines.push("Units are illustrative, replace with your figures. The deterrence rate is a conservative assumption. Exposure is revenue at risk, not a billed loss.");'
             'var uu=document.getElementById("cowyCalc");if(uu)uu.innerHTML=lines.map(function(l){return "<li>"+l+"</li>";}).join("");}'
             'document.addEventListener("input",calc);document.addEventListener("change",calc);calc();})();</script>')
    return box


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
    if data.get("stakes") and data.get("mode") != "freecheck":
        s = s.replace("<!--/FILL:findings-->", "<!--/FILL:findings-->\n  " + stakes_box(data["stakes"]), 1)
    if data.get("cta"):
        cb = cta_buttons(data["cta"])
        if cb:
            s = re.sub(r'<div class="cta">.*?</div>', lambda m: cb, s, count=1, flags=re.S)

    out = sys.argv[2] if len(sys.argv) > 2 else os.path.join(
        ROOT, "outputs", re.sub(r"[^a-z0-9]+", "-", brand.lower()).strip("-") + "-accuracy-report.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8").write(s)

    leftover = sorted(set(re.findall(r"\[[A-Za-z0-9 ,.%/'-]+\]", s)))
    print("wrote", out)
    print("STILL UNFILLED:", ", ".join(leftover) if leftover else "(none)")


if __name__ == "__main__":
    main()
