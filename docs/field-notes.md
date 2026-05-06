# Field Notes

`netreplay` is easiest to review by starting with the fixture, not the prose.

The domain cases cover `packet span`, `retry pressure`, `route drift`, and `socket risk`. They sit beside the smaller starter fixture so the project has both a compact scoring check and a domain-flavored review check.

`recovery` is the strongest case at 208 on `socket risk`. `stress` is the cautious anchor at 170 on `retry pressure`.

The extra check gives the repository a behavior path that can fail for a domain reason, not only a syntax reason.
