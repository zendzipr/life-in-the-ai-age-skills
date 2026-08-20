# Idea to Launch v0.1.0 — Targeted Probe 1

> Full raw traces referenced below are preserved privately and intentionally excluded from the public repository. See `evidence-archive-record.json`.

## Decision

**REVISE AND RERUN TWO CASES.** The six-case probe produced no critical fabrication, evidence, finance, or consistency failure, but it exposed one prompt weakness and one evaluation-fixture defect.

This was an initial same-environment behavioral probe, not a baseline comparison or cross-model regression. Execution telemetry did not expose the actual delegated model/provider, so the results must not be described as verified `gpt-5.6-sol` performance.

## Scope

- Candidate skill checksum: `b2f891f4d0b9a8b583782b6734306603ed8c871c1dfc7005ef84c9978200a452`
- Delegation ID: `deleg_05016eea`
- Cases: ITL-01, ITL-04, ITL-07, ITL-09, ITL-14, ITL-15
- Runs: one per case
- Verified execution model/provider: unavailable (`Model: ?` in completion telemetry)
- Raw transcripts: `raw/deleg_05016eea/`
- Scores: `probe-1-scores.jsonl`

## Results

| Case | Result | Mean | Finding |
|---|---|---:|---|
| ITL-01 | Pass with revision | 4.4 | Correct intake stop, but one numbered question bundled several unrelated fields. |
| ITL-04 | Pass | 4.8 | Correct hypothesis-mode disclosure and no fabricated research. |
| ITL-07 | Pass | 5.0 | Correct `SKIP`; decisive economics and tool-verified arithmetic preserved. |
| ITL-09 | Pass | 5.0 | No false precision; three cohesive questions and formulas supplied. |
| ITL-14 | Revise and rerun | 4.0 | No fabrication, but investor intake was overloaded and lacked a distinct gap heading. |
| ITL-15 | Pass after fixture correction | 4.8 | Correctly blocked premature dossier generation; the original test expectation conflicted with the evidence gate. |

Overall mean: **4.67/5**. This aggregate does not override case-level requirements.

## Prompt weakness

The skill limited each round to three questions but did not prevent the model from hiding many unrelated fields inside one numbered question. ITL-01 showed mild bundling; ITL-14 showed material bundling.

Revision:

- require each numbered question to group only closely related fields needed for one decision;
- prohibit evading the three-question limit through unrelated subquestions;
- require a distinct Investor-Readiness Gaps section;
- allow up to three unbundled intake questions before drafting a pitch when the company itself is undefined.

## Evaluation defect

ITL-15 supplied only a customer, price, fixed cost, and verdict but expected a complete dossier with all headings. That contradicted the skill's rule against generating a polished dossier from missing core evidence.

Correction:

- ITL-15 now tests that the skill preserves the supplied brief, blocks premature final generation, and exposes missing inputs.
- A future complete-brief fixture is still needed for full cross-section dossier consistency.

## Release implication

The skill remains **draft**. Rerun ITL-01 and ITL-14 against the amended candidate before accepting this targeted probe. Full research-tool, autonomous-dossier, repeated-run, and cross-model testing remain outstanding.
