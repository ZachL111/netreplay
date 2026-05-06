# netreplay

`netreplay` is a focused JavaScript codebase around replay connection events through deterministic state-machine transitions. It is meant to be easy to inspect, run, and extend without a hosted service.

## Netreplay Walkthrough

I would read the project from the outside in: command, fixture, model, then roadmap. That keeps the networking idea grounded in files that can be checked locally.

## Reason For The Project

The repository exists to keep a technical idea small enough to reason about. The implementation avoids external dependencies where possible, then uses fixtures to make changes easy to review.

## Capabilities

- Models packet shape with deterministic scoring and explicit review decisions.
- Uses fixture data to keep socket state changes visible in code review.
- Includes extended examples for retry behavior, including `surge` and `degraded`.
- Documents policy decisions tradeoffs in `docs/operations.md`.
- Runs locally with a single verification command and no external credentials.

## How It Is Put Together

The design is intentionally direct: parse or construct a signal, score it, classify it, and verify the expected branch. This makes the repository useful for studying networking behavior without needing a service or database unless the language project itself is SQL. The JavaScript version uses native modules and a small Node test path.

## Where Things Live

- `src`: primary implementation
- `tests`: verification harness
- `fixtures`: compact golden scenarios
- `examples`: expanded scenario set
- `metadata`: project constants and verification metadata
- `docs`: operations and extension notes
- `scripts`: local verification and audit commands
- `package.json`: Node package scripts

## Getting It Running

The only required setup is the local JavaScript toolchain. After cloning, stay in the repo root so fixture paths resolve correctly.

## Command Examples

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/verify.ps1
```

This runs the language-level build or test path against the compact fixture set.

## Check The Work

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/audit.ps1
```

The audit command checks repository structure and README constraints before it delegates to the verifier.

## Data Notes

`baseline` is the first example I would inspect because it lands on the `review` path with a score of 120. The broader file also keeps `degraded` at -5 and `surge` at 225, which gives the model a useful low-to-high spread.

## Tradeoffs

This code is local-first. It makes no claim about deployed usage and avoids credentials, hosted state, and environment-specific setup.

## Possible Extensions

- Add a loader for `examples/extended_cases.csv` and promote selected cases into the language test suite.
- Add a short report command that prints the score breakdown for a single scenario.
- Add malformed input fixtures so the failure path is as visible as the happy path.
- Add one more networking fixture that focuses on a malformed or borderline input.
