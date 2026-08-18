# Repository Operating Contract

## Mission

Maintain the canonical public database of Life in the AI Age AI skills, documentation, tests, evaluations, and release metadata.

## Authority

- Repository files are canonical.
- Installed Hermes profile copies are distributions.
- Prompt Engineering owns design, debugging, evaluation, and local repository maintenance.
- Default owns authenticated GitHub operations for `zendzipr`.

## Required workflow

1. Inspect the canonical skill, registry entry, tests, and latest accepted evaluation before editing.
2. Preserve the failing case and rollback version.
3. Make the smallest reliable change.
4. Run `python3 scripts/validate_repo.py`.
5. Run targeted model regressions before a full release suite.
6. Update registry checksums and status only from verified files and results.
7. Review the complete diff before requesting a remote write.

## Prohibited behavior

- Do not commit or expose credentials.
- Do not treat profile-local copies as canonical.
- Do not claim a model was tested when telemetry did not verify it.
- Do not hide critical failures behind aggregate scores.
- Do not commit, push, tag, publish, or install into another profile without explicit approval.
- Do not overwrite raw evaluation evidence.
