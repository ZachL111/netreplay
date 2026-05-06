# Review Journal

The review surface for `netreplay` is deliberately narrow: one fixture, one scoring rule, and one local check.

The local checks classify each case as `ship`, `watch`, or `hold`. That gives the project a small review vocabulary that matches its networking focus without claiming live deployment or external usage.

## Cases

- `baseline`: `packet span`, score 206, lane `ship`
- `stress`: `retry pressure`, score 170, lane `ship`
- `edge`: `route drift`, score 176, lane `ship`
- `recovery`: `socket risk`, score 208, lane `ship`
- `stale`: `packet span`, score 190, lane `ship`

## Note

This file is intentionally plain so the fixture remains the source of truth.
