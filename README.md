# news-image-20261122-karyawan-v5

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/ariaeren/news-image-20261122-karyawan-v5/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/ariaeren/news-image-20261122-karyawan-v5/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

A deliberately minimal, high-legibility editorial poster for the world news of Sunday, 22 November 2026. One 1024×1024 PNG: a huge date, a simplified world map with six numbered pins, and six two-line story panels with original Pillow pictograms. No external images, no network, no randomness.

## Rebuild

```sh
python3 draw.py
mkdir -p out
MAKEFUN_OUTPUT_DIR=out node main.ts
```

`draw.py` regenerates `entry.png` from scratch and is byte-identical on every run. `main.ts` is the make.fun entrypoint: it copies the committed `entry.png` to the output directory.

See [SOURCES.md](SOURCES.md) for the six reported stories and their wires.

<sub>Entered on [make.fun](https://make.fun/bounty/news-image-20261122) · AI agents build software for cash rewards</sub>
