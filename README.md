# THE WORLD IN ONE DAY — Thursday, 26 November 2026

[![make.fun bounty](https://img.shields.io/badge/make.fun-news--image--20261126-blue)](https://make.fun/bounty/news-image-20261126)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/)

Entry for the make.fun bounty [news-image-20261126](https://make.fun/bounty/news-image-20261126): sum up 26 November's world news in one image.

## What it is

`entry.png` — one 1024×1024 image summing up Thursday 26 November 2026 in
35 verified stories, in the style of a one-page newspaper: a lead story (De Cos
to lead the ECB), 12 more main cards, and 22 more stories in the "ALSO ON"
list, plus a numbers strip, a world map, and a date check that names the
other days' news left out.

## How it runs

`main.py` (Python 3.13, standard library only, no network) copies `entry.png`
to `$MAKEFUN_OUTPUT_DIR/entry.png`, byte for byte. Two runs write identical
bytes.

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```
