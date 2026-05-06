# Netreplay Walkthrough

The fixture is intentionally compact, so the review starts with the cases that pull farthest apart.

| Case | Focus | Score | Lane |
| --- | --- | ---: | --- |
| baseline | packet span | 206 | ship |
| stress | retry pressure | 170 | ship |
| edge | route drift | 176 | ship |
| recovery | socket risk | 208 | ship |
| stale | packet span | 190 | ship |

Start with `recovery` and `stress`. They create the widest contrast in this repository's fixture set, which makes them better review anchors than the middle cases.

The useful comparison is `socket risk` against `retry pressure`, not the raw score alone.
