#!/usr/bin/env python3
"""Offline structural and integrity checks for the skills repository."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_CASE_FIELDS = {
    "id",
    "objective",
    "input",
    "required_context",
    "expected_behavior",
    "disallowed_behavior",
    "validators",
    "severity",
    "tags",
    "notes",
}
SEVERITIES = {"low", "medium", "high", "critical"}
NAME_RE = re.compile(r"^[a-z0-9][a-z0-9_-]{0,63}$")
VERSION_RE = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")
SHA_RE = re.compile(r"^[a-f0-9]{64}$")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path, errors: list[str]):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
        return None


def load_jsonl(path: Path, errors: list[str]) -> list[dict]:
    rows: list[dict] = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        errors.append(f"{path.relative_to(ROOT)}: cannot read: {exc}")
        return rows
    for line_number, line in enumerate(lines, 1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            errors.append(f"{path.relative_to(ROOT)}:{line_number}: invalid JSON: {exc.msg}")
            continue
        if not isinstance(row, dict):
            errors.append(f"{path.relative_to(ROOT)}:{line_number}: row must be an object")
            continue
        rows.append(row)
    return rows


def frontmatter(path: Path, errors: list[str]) -> dict[str, str]:
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        errors.append(f"{path.relative_to(ROOT)}: cannot read: {exc}")
        return {}
    if not lines or lines[0] != "---":
        errors.append(f"{path.relative_to(ROOT)}: missing opening frontmatter delimiter")
        return {}
    try:
        end = lines.index("---", 1)
    except ValueError:
        errors.append(f"{path.relative_to(ROOT)}: missing closing frontmatter delimiter")
        return {}
    values: dict[str, str] = {}
    for line in lines[1:end]:
        if line.startswith((" ", "\t")) or ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip()
    return values


def contained_path(root: Path, relative: str, errors: list[str]) -> Path | None:
    candidate = root / relative
    try:
        resolved = candidate.resolve()
        resolved.relative_to(root.resolve())
    except (OSError, ValueError):
        errors.append(f"path escapes repository or cannot resolve: {relative}")
        return None
    return candidate


def validate_case(case: dict, source: str, errors: list[str]) -> None:
    missing = sorted(REQUIRED_CASE_FIELDS - set(case))
    if missing:
        errors.append(f"{source}: missing fields {missing}")
    if case.get("severity") not in SEVERITIES:
        errors.append(f"{source}: invalid severity {case.get('severity')!r}")
    for field in ("expected_behavior", "disallowed_behavior", "validators", "tags"):
        value = case.get(field)
        if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
            errors.append(f"{source}: {field} must be a list of strings")


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    for schema in (ROOT / "schemas/registry.schema.json", ROOT / "schemas/test-case.schema.json"):
        load_json(schema, errors)

    registry = load_json(ROOT / "registry.json", errors)
    if not isinstance(registry, dict):
        registry = {}
    expected_top = {"$schema", "project", "repository", "visibility", "canonical_branch", "skills"}
    unknown_top = sorted(set(registry) - expected_top)
    if unknown_top:
        errors.append(f"registry.json: unknown top-level fields {unknown_top}")
    if registry.get("project") != "Life in the AI Age":
        errors.append("registry.json: unexpected project name")
    if registry.get("repository") != "https://github.com/zendzipr/life-in-the-ai-age-skills":
        errors.append("registry.json: unexpected repository URL")
    if registry.get("visibility") != "public":
        errors.append("registry.json: repository visibility must match the public GitHub repository")
    if registry.get("canonical_branch") != "main":
        errors.append("registry.json: canonical branch must be main")

    skills = registry.get("skills")
    if not isinstance(skills, list) or not skills:
        errors.append("registry.json: skills must be a non-empty list")
        skills = []

    seen_names: set[str] = set()
    seen_paths: set[str] = set()
    total_cases = 0
    total_paraphrases = 0

    for index, entry in enumerate(skills):
        source = f"registry.json:skills[{index}]"
        if not isinstance(entry, dict):
            errors.append(f"{source}: entry must be an object")
            continue
        required = {"name", "version", "status", "owner", "path", "description", "evaluation_status", "checksums"}
        missing = sorted(required - set(entry))
        if missing:
            errors.append(f"{source}: missing fields {missing}")
            continue
        name = entry["name"]
        relative_path = entry["path"]
        if not isinstance(name, str) or not NAME_RE.fullmatch(name):
            errors.append(f"{source}: invalid skill name {name!r}")
        if name in seen_names:
            errors.append(f"{source}: duplicate skill name {name!r}")
        seen_names.add(name)
        if not isinstance(relative_path, str) or relative_path in seen_paths:
            errors.append(f"{source}: invalid or duplicate path {relative_path!r}")
        seen_paths.add(relative_path)
        if not VERSION_RE.fullmatch(str(entry["version"])):
            errors.append(f"{source}: invalid semantic version {entry['version']!r}")
        description = entry["description"]
        if not isinstance(description, str) or not description.endswith(".") or len(description) > 60:
            errors.append(f"{source}: description must end with a period and fit 60 characters")

        skill_dir = contained_path(ROOT, relative_path, errors)
        if skill_dir is None:
            continue
        skill_md = skill_dir / "SKILL.md"
        readme_md = skill_dir / "README.md"
        cases_path = skill_dir / "tests/cases.jsonl"
        paras_path = skill_dir / "tests/paraphrases.jsonl"
        for required_path in (skill_md, readme_md, cases_path, paras_path, skill_dir / "CHANGELOG.md"):
            if not required_path.is_file():
                errors.append(f"missing required file: {required_path.relative_to(ROOT)}")

        if skill_md.is_file():
            meta = frontmatter(skill_md, errors)
            for key in ("name", "description", "version", "author", "license"):
                if not meta.get(key):
                    errors.append(f"{skill_md.relative_to(ROOT)}: missing frontmatter {key}")
            if meta.get("name") != name:
                errors.append(f"{skill_md.relative_to(ROOT)}: name does not match registry")
            if meta.get("version") != entry["version"]:
                errors.append(f"{skill_md.relative_to(ROOT)}: version does not match registry")
            if meta.get("description") != description:
                errors.append(f"{skill_md.relative_to(ROOT)}: description does not match registry")
            body = skill_md.read_text(encoding="utf-8")
            if "README.md" not in body:
                errors.append(f"{skill_md.relative_to(ROOT)}: README is not linked")

        checksums = entry.get("checksums")
        if not isinstance(checksums, dict) or not checksums:
            errors.append(f"{source}: checksums must be a non-empty object")
        else:
            for rel_file, expected in checksums.items():
                if not isinstance(expected, str) or not SHA_RE.fullmatch(expected):
                    errors.append(f"{source}: invalid SHA-256 for {rel_file}")
                    continue
                file_path = contained_path(skill_dir, rel_file, errors)
                if file_path is None or not file_path.is_file():
                    errors.append(f"{source}: checksum target missing: {rel_file}")
                elif sha256(file_path) != expected:
                    errors.append(f"{source}: checksum mismatch: {rel_file}")

        cases = load_jsonl(cases_path, errors) if cases_path.is_file() else []
        case_ids: set[str] = set()
        for row_index, case in enumerate(cases, 1):
            validate_case(case, f"{cases_path.relative_to(ROOT)}:{row_index}", errors)
            case_id = case.get("id")
            if not isinstance(case_id, str) or not case_id:
                errors.append(f"{cases_path.relative_to(ROOT)}:{row_index}: invalid id")
            elif case_id in case_ids:
                errors.append(f"{cases_path.relative_to(ROOT)}:{row_index}: duplicate id {case_id}")
            else:
                case_ids.add(case_id)
        total_cases += len(cases)

        paraphrases = load_jsonl(paras_path, errors) if paras_path.is_file() else []
        para_ids: set[str] = set()
        for row_index, para in enumerate(paraphrases, 1):
            para_id = para.get("id")
            source_id = para.get("source_id")
            if not isinstance(para_id, str) or not para_id:
                errors.append(f"{paras_path.relative_to(ROOT)}:{row_index}: invalid id")
            elif para_id in para_ids or para_id in case_ids:
                errors.append(f"{paras_path.relative_to(ROOT)}:{row_index}: duplicate id {para_id}")
            else:
                para_ids.add(para_id)
            if source_id not in case_ids:
                errors.append(f"{paras_path.relative_to(ROOT)}:{row_index}: unknown source_id {source_id!r}")
            if not isinstance(para.get("input"), str):
                errors.append(f"{paras_path.relative_to(ROOT)}:{row_index}: input must be a string")
        total_paraphrases += len(paraphrases)

    forbidden_names = {".env", ".git-credentials", "id_rsa", "id_ed25519"}
    for path in ROOT.rglob("*"):
        if ".git" in path.parts or not path.is_file():
            continue
        if path.name in forbidden_names or path.suffix.lower() in {".pem", ".key"}:
            errors.append(f"forbidden credential-like file: {path.relative_to(ROOT)}")

    if errors:
        print(f"FAIL: {len(errors)} error(s)")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "PASS: "
        f"{len(skills)} skill(s), {total_cases} case(s), "
        f"{total_paraphrases} paraphrase(s), checksums verified"
    )
    for warning in warnings:
        print(f"WARNING: {warning}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
