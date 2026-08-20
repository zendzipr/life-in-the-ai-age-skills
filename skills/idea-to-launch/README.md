# Idea to Launch

`idea-to-launch` guides an AI through the complete journey from a business idea to an evidence-aware launch plan.

It does not simply produce an impressive-looking business plan. It first establishes what is known, researches what can be verified, tests whether the idea deserves further investment, and then builds one consistent business package.

## What it produces

The final **Business Launch Dossier** can include:

1. Executive decision
2. One-page business plan
3. Market validation report
4. Competitor teardown
5. Revenue-model recommendation
6. Twelve-month financial projections
7. Go-to-market blueprint
8. Risk assessment
9. KPIs and a 90-day action plan
10. Investor pitch summary
11. Evidence register
12. Assumptions and unresolved questions

## How it works

The default guided workflow is:

```text
Understand → Research → Validate → Decide → Model → Plan → Deliver
```

The AI maintains one Working Business Brief so the customer, pricing, costs, strategy, and projections remain consistent.

The skill normally pauses at three checkpoints:

1. **Research framing** — confirm the customer, geography, market category, and competitor scope.
2. **Viability decision** — choose whether to continue, research more, revise, or stop.
3. **Material economics** — confirm or expose pricing, sales, cost, capacity, and funding assumptions.

It asks no more than three material questions in one round and does not hide unrelated intake fields inside bundled questions. In guided mode, it also confirms the relevant jurisdiction before location-dependent legal or regulatory research.

## Evidence labels

The skill distinguishes:

- **USER FACT** — supplied by the user
- **SOURCED FACT** — supported by an external source
- **ASSUMPTION** — temporarily adopted for analysis
- **INFERENCE** — reasoned but not directly established
- **UNKNOWN** — unresolved
- **DECISION** — explicitly chosen by the user

This makes it harder for an unsupported assumption to turn into a polished but misleading business claim.

## Verdicts

The viability stage uses four possible verdicts:

- **BUILD** — evidence supports a bounded launch
- **TEST FIRST** — promising, but material assumptions remain
- **REVISE** — a specific change could make the concept more viable
- **SKIP** — the evidence does not justify further investment in the current concept

Every verdict includes a confidence level, supporting and contrary evidence, critical unknowns, and the cheapest useful next test.

Use **REVISE** when safe, lawful, or economically viable continuation requires a material change to the concept; use **TEST FIRST** when the concept can remain materially the same while evidence is gathered. If a foundational assumption changes, dependent calculations, recommendations, and verdicts remain stale until the affected analysis is regenerated—the skill does not issue a new verdict merely by labelling it “pending regeneration.”

## Research requirements

For current competitors, prices, market conditions, regulations, and demand evidence, use the skill with an AI that has suitable web or research tools.

If those tools are unavailable, the skill switches to **hypothesis mode**. It can still organize the idea, identify assumptions, and create a research plan, but it must not pretend that current market claims were verified.

## Financial safeguards

The skill uses conservative, base, and upside scenarios. It exposes formulas and assumptions and must not invent precise revenue or break-even projections from missing inputs.

This skill does not replace professional legal, tax, accounting, investment, or regulated-industry advice.

## Start a guided session

A useful first request is:

> Use Idea to Launch to help me evaluate and develop this business idea: [describe the idea]. Walk me through the process and research what can be verified.

For a faster first draft:

> Use Idea to Launch in autonomous draft mode. Research this idea, make reversible assumptions where needed, and clearly label every assumption and unresolved decision: [describe the idea].

For one bounded output:

> Use Idea to Launch to produce only a competitor teardown for this idea: [describe the idea]. Complete the research and evidence steps needed for that deliverable.

## Files in this skill

- `SKILL.md` — complete workflow and safeguards
- `HOW-TO.md` — plain-language setup and usage guide
- `README.md` — setup and usage instructions
- `CHANGELOG.md` — version history
- `templates/working-business-brief.md` — shared source-of-truth template
- `templates/business-launch-dossier.md` — final package template
- `tests/` — behavioral evaluation cases

## Use with Hermes

Ask in a conversation:

> Load the `idea-to-launch` skill and help me evaluate my business idea.

Or start a session with the skill loaded:

```bash
hermes chat -s idea-to-launch
```

For a one-time request:

```bash
hermes chat -s idea-to-launch -q "Evaluate this business idea: [description]"
```

Hermes must have the skill installed in the active profile before it can load it. Research quality also depends on the tools available to that profile.

## Use with Claude Code

Copy the complete folder to one of the documented skill locations, for example:

```text
your-project/.claude/skills/idea-to-launch/
```

or:

```text
~/.claude/skills/idea-to-launch/
```

Then invoke it directly with `/idea-to-launch` or ask Claude to use it for the business-planning task.

## Use with Claude.ai

Add `SKILL.md` and the templates to a Claude Project, then add this project instruction:

> Follow the complete `idea-to-launch` instructions in `SKILL.md` when evaluating or planning a business idea. Use the supplied templates for the working brief and final dossier.

For current market research, enable and authorize suitable research capabilities where available.

## Use with ChatGPT

In a regular chat or Project, upload `SKILL.md` and the templates and say:

> Follow the complete Idea to Launch workflow. Walk me through the required checkpoints and distinguish sourced facts from assumptions.

For a custom GPT, place the behavioral instructions in the GPT's Instructions field and provide the templates as supporting files. Enable suitable research capabilities if current market research is expected.

## Use with other AI tools

If the tool supports the Agent Skills format, install the complete folder in its documented skills location.

Otherwise:

1. Add the contents of `SKILL.md` to the tool's system, project, or custom instructions.
2. Add the two templates as supporting files when possible.
3. Ensure current-information tools are available before requesting researched market claims.

## Status

Version `0.1.0` is a draft. Its package structure and test fixtures can be validated offline, but model-backed behavioral and cross-model regressions are still required before candidate or released status.
