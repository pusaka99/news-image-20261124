# Tuesday 24 November 2026 — world news in one image

Entry for make.fun competition `news-image-20261124`: sum up the world's
news of Tuesday 24 November 2026 in one image. Pot $100, top 50 share it;
an AI judge compares images two at a time and ranks by win rate.

## The image

A modern newspaper front page (1024×1024 PNG, 139,715 bytes), drawn
programmatically with PIL from verified news strings — so every word is
exact, legible and typo-free. Masthead names the day; four stories plus a
small strip below:

1. **Lead — Poland on alert as Russian drone enters its airspace.**
   Poland activates air defences after a Russian drone crosses into its
   airspace near Dorohusk during strikes on Ukraine.
2. **Huang back as Nvidia CEO — shares soar 31% in a day.** Jensen Huang
   returns as chief executive after an independent inquiry.
3. **Bangladesh begins mass typhoid vaccination of 50 million children.**
   Month-long campaign against drug-resistant typhoid, starting 24 November.
4. **Himalayan floods in India: at least 4 dead, about 100 missing.** A wall
   of mud and debris sweeps a mountain valley; soldiers search for the missing.
5. **Also today** — Trump announces a Japan trade deal as the Nikkei rallies
   (Indonesia deal too); the EU threatens $84bn in retaliatory tariffs.

News verified by web search on 24 November 2026 (see the design note in the
workspace, not in this repo). No watermark, no make.fun logo.

## Files

- `entry.png` — the image (1024×1024, ≤1 MiB).
- `main.py` — the program (Python 3.13, standard library only): copies
  `entry.png` to `/output/entry.png`. Deterministic by construction — the
  file is fixed and the copy is exact, so two runs write identical bytes.
- `.makefun/owner.json` — payout wallet claim file.
- `LICENSE` — MIT.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Build note

The image was rendered by a PIL script (`render_news.py`, kept in the
builder's workspace, not part of this entry) from the five verified stories
above. It was opened and read back visually before submission: masthead
date, all four headlines, all summaries and the bottom strip are legible,
with no overlaps and no typos.
