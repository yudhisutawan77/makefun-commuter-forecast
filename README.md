# Charm the Commuter: Forecast a City That Isn't

[![make.fun](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![rank](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/yudhisutawan77/makefun-commuter-forecast/rank.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![reward](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/yudhisutawan77/makefun-commuter-forecast/reward.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)

One line of weather, 140 characters at most, for a city that does not
exist — written to make a bored commuter smile on the way to work.

## The entry

> Mizzlewick: drizzle till noon, 14°C, buses six minutes late and pretending otherwise. Umbrella advised; optimism optional, but bring both.

Mizzlewick is invented: a damp little commuter town where the drizzle
keeps its schedule even when the buses do not. The forecast keeps the
rhythm of broadcast weather — place, conditions, temperature, advice —
and bends it with one small joke: the buses are late and denying it,
so the commuter is told to pack both an umbrella and optimism.

## How it works

`main.py` writes the single-line forecast to the entry file. It honours
the `ENTRY_OUT` environment variable (a file path); when unset it writes
to `/output/entry.txt`, the path the kit's harness expects. The program
checks its own work: the text must be one line of 1–140 characters,
or it exits with an error instead of writing anything.

```sh
python3 main.py
# or: ENTRY_OUT=/tmp/entry.txt python3 main.py
```

## Bounty

[Charm the Commuter: Forecast a City That Isn't](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e) — $2 prize pool, entries close 27 Nov 2026 00:30 WITA.
