# netreplay

`netreplay` is a compact JavaScript repository for networking, centered on this goal: Replay connection events through deterministic state-machine transitions.

## Reason For The Project

The point is to make a small domain rule concrete enough that a reader can change it and immediately see what broke.

## Netreplay Review Notes

The first comparison I would make is `socket risk` against `retry pressure` because it shows where the rule is most opinionated.

## What It Does

- `fixtures/domain_review.csv` adds cases for packet span and retry pressure.
- `metadata/domain-review.json` records the same cases in structured form.
- `config/review-profile.json` captures the read order and the two review questions.
- `examples/netreplay-walkthrough.md` walks through the case spread.
- The JavaScript code includes a review path for `socket risk` and `retry pressure`.
- `docs/field-notes.md` explains the strongest and weakest cases.

## How It Is Put Together

The repository has two validation layers: the original compact policy fixture and the domain review fixture. They are separate so one can change without hiding failures in the other.

The added JavaScript path is deliberately direct, with fixtures doing most of the explaining.

## Run It

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/verify.ps1
```

## Check It

That command is also the regression path. It verifies the domain cases and catches mismatches between the CSV, metadata, and code.

## Boundaries

No external service is required. A deeper version would add more negative cases and a clearer boundary around invalid input.
