# Answer First Evaluations

This directory stores immutable evaluation manifests, raw model outputs, scores, and release reports for repository-managed versions of `answer-first`.

Version `0.4.1` is currently a candidate. Historical exploratory and controlled tests exist outside this repository, but the repository version has not yet completed its release suite. Import historical evidence only with provenance, model-verification limits, and checksums preserved.

A release evaluation should contain:

```text
<version>/<run-id>/
├── manifest.json
├── cases.jsonl
├── raw/
├── scores.jsonl
└── report.md
```

Do not overwrite prior runs. Mark superseded or invalid runs in the report while preserving their raw evidence.
