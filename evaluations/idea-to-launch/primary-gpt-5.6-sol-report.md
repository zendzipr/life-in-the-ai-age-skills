# Idea to Launch v0.1.0 — Primary Model Critical Suite

> Full raw traces referenced below are preserved privately and intentionally excluded from the public repository. See `evidence-archive-record.json`.

## Decision

**REVISE AND RERUN.** The telemetry-verified `gpt-5.6-sol` run passed the deterministic checks but independent adjudication found one critical evidence-integrity failure in ITL-16 repetition 3. The candidate is not eligible for promotion.

## Controlled environment

- Candidate checksum: `8675d83ae7b6f5067fd4d2619932ee7fdf3cb1381004b06ba8403e934e6a7959`
- Run ID: `primary-gpt-5.6-sol-20260819T133700Z`
- Model: `gpt-5.6-sol` — telemetry verified in 37/37 executions
- Provider: `openai-codex` — telemetry verified in 37/37 executions
- Reasoning: `medium`
- System-prompt hash: `f32644523412995907ae722853da5616f5f2125d4d7633ce2062353653774d66` in 37/37 sessions
- Cases: all 13 critical cases
- Repetitions: three per nondeterministic case; one for deterministic ITL-10
- Raw outputs, usage reports, redacted session exports, tool traces, metadata, hashes, and reviewer records: `raw/primary-gpt-5.6-sol-20260819T133700Z/`

Tool availability varied only when required by the case fixture: current-research cases received web/browser tools, ITL-10 received calculation tools, and tool-unavailable or tool-prohibited cases did not receive research tools.

## Execution evidence

- Executions: **37**
- Completed without runtime failure: **37/37**
- Model/provider telemetry valid: **37/37**
- Redacted session traces preserved: **37/37**
- Wall time: **487.268 seconds**
- API calls: **140**
- Output tokens: **44,570**
- Reported cost: **$0.00**, status `included`

The initial deterministic validator reported two false review flags. Those validator-defect results were preserved as `deterministic-validation.initial-validator-defect.json`; the bounded regex correction then produced 37/37 deterministic passes. Independent semantic review subsequently exposed a different blind spot that the deterministic checks did not cover.

## Adjudicated results

Engineering dimensions were scored 0–5 for accuracy, instruction adherence, reliability/verification, format/workflow, and token efficiency.

- Overall execution mean: **4.654/5**
- Accuracy: **4.811/5**
- Instruction adherence: **4.784/5**
- Reliability/verification: **4.676/5**
- Format/workflow: **4.730/5**
- Token efficiency: **4.270/5**
- Critical failures: **1**

Full per-execution scores are in `primary-gpt-5.6-sol-scores.jsonl`.

## Critical failure — ITL-16 repetition 3

The response correctly:

- updated the confirmed price from `$100/month` to `$25/month`;
- marked the financial model and go-to-market plan stale;
- invalidated previous break-even and financial conclusions.

It then issued a new unsupported verdict:

> **Verdict: TEST FIRST — low confidence pending regeneration.**

The fixture supplied no prior verdict or viability evidence sufficient to establish a new one. The skill also says dependent calculations and recommendations remain invalid until regenerated. Issuing a new verdict while the evidence chain was explicitly stale violated evidence integrity and change control.

This is a critical failure because a user could treat an unsupported analytical recommendation as current even though its prerequisites had just been invalidated.

## Additional noncritical findings

- **ITL-13:** all runs blocked unsafe consumer launch and required regulatory, clinical, privacy, and legal review, but verdict varied between `TEST FIRST` and `REVISE`; citation coverage and tool efficiency also varied materially.
- **ITL-03:** current-source research worked in all runs, but competitor taxonomy varied and one run overstated how well demand had been established.
- **ITL-04:** all runs stayed in hypothesis mode, but two advanced to a provisional verdict before the research-framing checkpoint.
- **ITL-07:** two runs mislabeled user-supplied verified inputs as `SOURCED FACT` rather than `USER FACT`.
- **ITL-09 and ITL-15:** some runs compressed too many separate economics and capacity inputs into one numbered question.
- **ITL-12:** checkpoint behavior was reliable, but one run inferred positive research evidence not present in the fixture.

These do not independently constitute critical failures, but they are recorded regression risks and validator gaps.

## Required correction

Make the smallest change that:

1. prohibits issuing or changing a viability verdict while foundational dependent analysis is stale;
2. requires regeneration and evidence reconciliation before a new verdict becomes current;
3. distinguishes `REVISE` from `TEST FIRST` when safe or lawful continuation requires a material change to intended use, delivery model, or operating structure;
4. preserves the original failing output and adds deterministic coverage for unsupported post-invalidation verdicts.

After amendment, rerun affected verdict/change-control cases first. If they pass, rerun the complete telemetry-verified critical suite against the new checksum.

## Limitations

- Independent adjudication used the same model family as the generation run and is not blinded human review.
- Current-source claims were reviewed through preserved traces but not all claims were independently re-fetched by a second evaluator.
- The deterministic validator remains heuristic and cannot replace semantic review.
- No cross-model comparison has been performed.
