# Contributing

This repository is the main copy of the Life in the AI Age skills library.

## Improving a skill

1. Explain what should work differently.
2. Save an example that shows the problem.
3. Make the smallest useful change.
4. Test the changed example.
5. Run the wider test set to look for regressions.
6. Update the version, changelog, status, and checksums.
7. Run:

   ```bash
   python3 scripts/validate_repo.py
   ```

8. Review the complete change before publishing it.

## Skill versions

- **Patch** — documentation or wording correction with no intended behavior change
- **Minor** — new behavior or a new supported use
- **Major** — a change that is incompatible with the previous version

## Status labels

- **Draft** — early work
- **Candidate** — ready for structured testing
- **Released** — passed the required checks
- **Deprecated** — still present but should not be used for new work
- **Archived** — retained for history only

## Before release

A release should have:

- a clear purpose;
- current usage instructions;
- tests for important and risky behavior;
- no unresolved critical failures;
- a rollback version; and
- no credentials or private source material.

## GitHub access

Prompt Engineering maintains and tests the local files. Default performs authenticated GitHub writes for the `zendzipr` account. Credentials must not be copied into this repository.
