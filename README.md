# Old Town Terrace — closure notice

A single static page replacing the restaurant site with a closure notice, **English first, then Turkish**.
No build step, no JavaScript, no external requests. `index.html` is the whole site.

## Editing the facts

Do not hand-edit `index.html` — it is generated.

1. Fill in `values.txt`
2. Run `python3 fill.py`
3. Commit and push

| Field | Goes in |
|---|---|
| `VIOLATIONS` | The specific violations cited in the decision (e.g. "hygiene and storage temperature violations"). The page already states the grounds are food safety and hygiene violations; this line adds the specifics. |
| `ADDRESS` | Street address of the premises |
| `CLOSURE_DATE` | Date the closure order took effect |
| `AUTHORITY` | The body that issued the order, by its real name |
| `DECISION_NO` | The decision/notification reference, **only if you hold the paperwork** |
| `CONTACT` | Where guests chase existing reservations and refunds |
| `NOTICE_DATE` | When this notice was last updated |

Any field left blank renders as a grey dotted placeholder — visibly unfinished rather than silently wrong.

## What this page deliberately does not do

- It carries **no ministry logo, seal, or letterhead**. It is the operator's notice about the closure, not a reproduction of the order.
- It invents **no decision number and no inspection findings**.
- The footer states on the page, in both languages, that this is not an official government publication and that the order itself is held by the issuing authority.

Those three are what keep the page a closure notice rather than something that reads as a forged official document.

## Deploying

Static host, root directory, no build command. Publish directory is the repo root.
