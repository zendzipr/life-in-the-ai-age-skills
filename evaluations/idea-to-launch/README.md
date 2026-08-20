# Idea to Launch Evaluations

## Current status

Version `0.1.0` is a **candidate**. Peter approved candidate promotion on `2026-08-19T20:32:54Z`.

Completed:

- 19 behavioral test cases and 7 paraphrase cases drafted;
- all 13 critical cases executed on telemetry-verified `gpt-5.6-sol` through `openai-codex`;
- three repetitions completed for every nondeterministic critical case and one calculation-tool execution for deterministic ITL-10;
- 37/37 final executions completed with valid model/provider telemetry and redacted session traces;
- 37/37 final deterministic behavioral checks passed;
- 37/37 final semantic adjudications passed or passed with noncritical limitations;
- zero unresolved critical failures on the amended candidate;
- candidate promotion approved by Peter and recorded on `2026-08-19T20:32:54Z`;
- original failures, superseded candidates, validator defects, raw responses, and tool traces preserved in a private evidence archive;
- current repository validation passed: `PASS: 2 skill(s), 33 case(s), 21 paraphrase(s), checksums verified`.

Not yet completed:

- controlled cross-model comparison;
- independent second-evaluator re-fetch of all current-source claims;
- blinded human strategy adjudication;
- release decision;
- commit, push, publication, tagging, or profile installation.

## Current candidate evidence

- Candidate checksum: `9a243e28f7f2c810abef0f1592f2971ef0411566d7cb4ba8ae9462a3223e2f34`
- Primary model: `gpt-5.6-sol`
- Provider: `openai-codex`
- Final run ID: `primary-gpt-5.6-sol-20260819T135656Z`
- Final scores: `primary-gpt-5.6-sol-final-scores.jsonl`
- Final report: `primary-gpt-5.6-sol-final-report.md`
- Private evidence record: `evidence-archive-record.json`
- Decision: **PASS — promoted to candidate with Peter's approval**

## Evidence history

- `probe-1-report.md` / `probe-1-scores.jsonl` — initial six-case probe and preserved failures.
- `probe-2-report.md` / `probe-2-scores.jsonl` — bounded reruns for ITL-01 and ITL-14.
- `probe-3-report.md` / `probe-3-scores.jsonl` — extended probe and preserved original ITL-13 process failure.
- `probe-3-rerun-report.md` / `probe-3-rerun-scores.jsonl` — jurisdiction-gate correction acceptance.
- `primary-gpt-5.6-sol-report.md` / `primary-gpt-5.6-sol-scores.jsonl` — first telemetry-verified critical suite; rejected after one ITL-16 critical failure.
- `primary-gpt-5.6-sol-correction-rerun-report.md` — 12-execution verdict and change-control correction rerun.
- `primary-gpt-5.6-sol-final-report.md` / `primary-gpt-5.6-sol-final-scores.jsonl` — complete amended primary-model suite; passed.
- `evidence-archive-record.json` — checksum and preservation record for the private full-evidence archive.

## Evidence storage

The public repository includes the test cases, scores, reports, and archive checksum. Full session exports are kept in the private profile archive because they include profile instructions, local paths, and other operational details that should not be published. The archive can be verified using the SHA-256 checksum in `evidence-archive-record.json`.

## Promotion gates

Promotion from draft to candidate requires:

- repository validator passes — **passed**;
- all critical cases execute on the telemetry-verified primary model — **passed**;
- raw outputs and tool traces are preserved in the private archive — **passed**;
- deterministic arithmetic and format checks pass — **passed**;
- zero unresolved critical fabrication, research, checkpoint, change-control, or consistency failures — **passed**;
- explicit candidate-promotion approval — **passed on 2026-08-19**.

Promotion from candidate to released requires a separately approved cross-model regression plan, review of recorded noncritical limitations, and no unresolved critical failures.
