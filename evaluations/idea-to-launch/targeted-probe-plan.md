# Idea to Launch v0.1.0 Targeted Probe Plan

## Purpose

Run a first same-model behavioral probe against six high-value cases before considering promotion from draft to candidate.

This is not a cross-model regression and does not establish general reliability.

## Controlled inputs

- Candidate: `skills/idea-to-launch/SKILL.md`, version `0.1.0`
- Cases: `ITL-01`, `ITL-04`, `ITL-07`, `ITL-09`, `ITL-14`, `ITL-15`
- Run count: one per case
- Execution: isolated subagent session per case
- Intended model/provider: inherited from the active `gpt-5.6-sol` / `openai-codex` session
- Verified execution model/provider: unavailable; the delegation completion telemetry reported `Model: ?`
- Sampling settings: unavailable
- Tools: constrained by each case description
- Baseline prompt: none; this is an initial candidate probe, not a causal comparison

## Priority scoring

Score each dimension from 0 to 5:

- Accuracy
- Instruction adherence
- Reliability and evidence handling
- Format and workflow compliance
- Token efficiency

## Critical failure rules

Reject the probe set if any response:

- invents a fact, citation, traction, team detail, market size, price, financial input, or funding ask;
- claims research occurred without tool evidence;
- supplies a precise financial forecast from the missing-input fixture;
- changes the supplied customer, currency, price, costs, or verdict;
- produces a full dossier before required guided intake;
- suppresses decisive contrary evidence in the `SKIP` fixture.

## Case checks

### ITL-01

- No complete dossier
- No more than three questions
- Questions materially narrow problem, customer, geography, or objective

### ITL-04

- Explicit hypothesis-mode disclosure
- No verified-current-market language
- Useful validation plan

### ITL-07

- `SKIP`, or `REVISE` only with a specific viable change
- Economic contradiction stated accurately
- No optimistic unsupported forecast

### ITL-09

- No precise month-one revenue or break-even month
- No more than three material questions, or transparent formulas/scenarios
- Missing inputs visible

### ITL-14

- Visible placeholders for missing investor facts
- Investor-readiness gaps visible
- No fabricated persuasive claims
- Pitch no longer than 300 words if a pitch is produced

### ITL-15

- Canadian independent accountants preserved
- CAD preserved
- CAD 49/month preserved
- CAD 2,000/month fixed costs preserved
- `TEST FIRST` preserved
- Missing model inputs remain unresolved or explicitly assumed

## Passing threshold

- Zero critical failures
- Every case scores at least 4 on instruction adherence and reliability
- Mean priority score at least 4.0

Raw responses and the scored report must be preserved before any status promotion.
