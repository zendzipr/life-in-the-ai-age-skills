# Life in the AI Age Skills

A private library of reusable instructions that help AI tools perform specific tasks or follow a consistent way of working.

Each skill includes:

- the instructions the AI follows;
- a plain-language README;
- examples and tests; and
- a version history.

## Available skills

| Skill | What it does | Status |
|---|---|---|
| [`answer-first`](skills/answer-first/README.md) | Puts the answer, result, or next action first | Candidate |

## Using a skill

Open the skill's README for instructions for Hermes, Claude, ChatGPT, and other AI tools.

The main instruction file is always named `SKILL.md`. Some AI tools can load that file as a native skill. For tools that cannot, you can add its contents to the tool's custom or project instructions.

## How this library is managed

This GitHub repository is the main copy of every skill. Copies installed in individual AI profiles are working installations.

Changes follow a simple process:

1. improve the skill;
2. test the changed behavior;
3. check that unrelated behavior still works;
4. review the results; and
5. publish the approved version.

A skill marked **candidate** is still being tested. A skill marked **released** has passed its required checks.

## Repository folders

```text
skills/          The skill packages
evaluations/     Test results and release reports
registry.json    List of managed skills
scripts/         Repository checks
schemas/         File-format definitions
```

## Validate the library

```bash
python3 scripts/validate_repo.py
```

## Privacy

This is a private repository. Do not add passwords, API keys, private keys, `.env` files, confidential source material, or unreviewed conversation exports.
