#!/usr/bin/env python3
"""Render index.html from _template.html + values.txt.

Every [[KEY]] with a value in values.txt is substituted as plain text.
Every [[KEY]] left blank stays a visibly-unfinished grey placeholder,
so nothing on the live page can silently read as fact when it isn't.
"""
import html, io, re, sys, pathlib

root = pathlib.Path(__file__).parent
vals = {}
for line in io.open(root / "values.txt", encoding="utf-8"):
    line = line.strip()
    if not line or line.startswith("#") or "=" not in line:
        continue
    k, v = line.split("=", 1)
    vals[k.strip()] = v.strip()

src = io.open(root / "_template.html", encoding="utf-8").read()
filled, blank = [], []

for key, value in vals.items():
    token = "[[%s]]" % key
    if value:
        # drop the placeholder styling along with the token
        src = src.replace('<span class="ph">%s</span>' % token, html.escape(value))
        src = src.replace(token, html.escape(value))
        filled.append(key)
    else:
        blank.append(key)

leftover = sorted(set(re.findall(r"\[\[([A-Z_]+)\]\]", src)))
io.open(root / "index.html", "w", encoding="utf-8").write(src)

print("filled : %s" % (", ".join(filled) or "none"))
print("blank  : %s" % (", ".join(sorted(set(blank + leftover))) or "none"))
if leftover:
    print("\n!! index.html still shows placeholders for the fields above.")
    print("   Fill values.txt and re-run before this page names a real closure.")
