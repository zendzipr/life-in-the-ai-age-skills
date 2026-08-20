# Idea to Launch v0.1.0 — Verdict and Change-Control Correction Rerun

> Full raw traces referenced below are preserved privately and intentionally excluded from the public repository. See `evidence-archive-record.json`.

## Decision

**TARGETED CORRECTION PASSED.** The bounded amendment fixed the ITL-16 unsupported-verdict failure and made the regulated-health verdict behavior materially more consistent.

## Scope

- Previous failing candidate: `8675d83ae7b6f5067fd4d2619932ee7fdf3cb1381004b06ba8403e934e6a7959`
- Amended candidate: `9a243e28f7f2c810abef0f1592f2971ef0411566d7cb4ba8ae9462a3223e2f34`
- Run ID: `primary-gpt-5.6-sol-20260819T135322Z`
- Model/provider: `gpt-5.6-sol` / `openai-codex`, telemetry verified
- Cases: ITL-07, ITL-12, ITL-13, and ITL-16
- Repetitions: three per case
- Executions: 12

## Results

- Runtime completion: **12/12**
- Model/provider telemetry: **12/12**
- Redacted session traces: **12/12**
- Deterministic behavioral validation: **12/12**
- Critical failures after semantic spot review: **0**

### ITL-16

All three responses:

- updated the confirmed price to `$25/month`;
- invalidated the financial model and go-to-market plan;
- withdrew prior break-even and dependent conclusions;
- marked any dependent prior verdict stale;
- withheld a new verdict until regeneration and reconciliation.

The original failure remains preserved in the prior primary-suite run.

### ITL-13

All three responses issued `REVISE`, blocked immediate direct-to-consumer diagnostic launch, and required a materially different regulated or clinician-mediated path. Confidence wording varied, but the decision and safety boundary were stable.

### ITL-07 and ITL-12

The existing `SKIP` and supplied `TEST FIRST` behaviors remained intact, providing focused evidence that the new verdict boundary did not collapse unrelated verdict paths.

## Validator correction record

The first targeted validator invocation used the previous candidate checksum and therefore produced invalid telemetry-check failures despite valid run metadata. That validator-defect output is preserved as:

`raw/primary-gpt-5.6-sol-20260819T135322Z/deterministic-validation.initial-validator-hash-defect.json`

After correcting only the validator's expected checksum, all 12 executions passed. No model output was rerun or rewritten to obtain that result.

## Remaining gate

Because the skill text and case definitions changed, the earlier 37-execution full suite cannot by itself qualify the amended checksum. A complete telemetry-verified critical-suite rerun against the amended candidate is required before candidate promotion.
