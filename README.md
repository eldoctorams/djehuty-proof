# ClaimLedger

> Evidence-grounded auditing for AI-generated reports.

[![Status: Design](https://img.shields.io/badge/status-design--phase-2563eb)](#project-status)
[![License: MIT](https://img.shields.io/badge/license-MIT-0ea5e9)](LICENSE)
[![Evidence: Auditable](https://img.shields.io/badge/evidence-auditable-22c55e)](SECURITY.md)

ClaimLedger will decompose a report into claims, connect each claim to exact supporting evidence, flag unsupported or contradictory statements, and preserve provenance in a portable ledger.

## Why this matters

A real citation can still fail to support the sentence attached to it. AI-assisted reports need verification at the **claim-to-evidence** level—not just link checking or generic hallucination scores.

## Planned capabilities

- Atomic claim extraction with stable IDs.
- Exact evidence spans, source snapshots, hashes and retrieval timestamps.
- Support, contradiction and insufficient-evidence labels with explanations.
- Citation coverage and evidence-quality scores.
- Human review queues and signed audit decisions.
- JSON/Markdown reports and CI gates for research or intelligence pipelines.

## Differentiator

ClaimLedger will treat verification as a durable data model: **claim → evidence span → source → provenance → review decision**. Scores will remain inspectable, and uncertainty will be explicit.

## Project status

**Design phase.** The repository defines the evidence model and MVP. No claim-verification accuracy is asserted yet.

## First release target

```bash
claimledger audit report.md --sources ./sources
claimledger export audit.json
```

The alpha will support Markdown input, local source files, claim segmentation, manual evidence linking and deterministic coverage metrics before model-assisted judgments are added.

## Documentation

- [Roadmap](ROADMAP.md)
- [Reference projects and gap analysis](docs/REFERENCE_PROJECTS.md)
- [Contributing](CONTRIBUTING.md)
- [Security and provenance policy](SECURITY.md)

## Author

**Dr. Ahmed Mohamed El Sayed** — OSINT, digital forensics, cybercrime investigation and AI-powered investigation systems.

[Website](https://drahmedelsayed.com/) · [LinkedIn](https://www.linkedin.com/in/eldoctorams/) · [GitHub](https://github.com/eldoctorams)

## License

MIT. Audit output is decision support, not an automatic truth verdict.
