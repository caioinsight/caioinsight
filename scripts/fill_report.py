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

    sc = data.get("score", {})
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
