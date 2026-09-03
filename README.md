# DJEHUTY PROOF

> Every claim must face the record.

**DJEHUTY PROOF** is a claim-to-evidence auditing engine for AI-assisted, research and intelligence reports. It converts prose into stable claims, binds each claim to exact local evidence spans and preserves a reviewable proof ledger.

## Working alpha

- Deterministic atomic claim IDs.
- Local evidence-span ranking and explicit support labels.
- Support, partial-support, contradiction and insufficient-evidence states.
- SHA-256 fingerprints for reports and evidence.
- Coverage metrics with mandatory human-review policy.
- Interactive cinematic proof chamber.
- CI tests and GitHub Pages deployment.

```bash
# Works immediately after downloading the source or ZIP:
python run.py samples/report.md --sources samples/sources --output audit.json

# Or install the command globally:
python -m pip install .
djehuty samples/report.md --sources samples/sources --output audit.json
```

Docker users can run `docker compose up --build`. The runtime has no third-party Python dependency and performs no network request.

## Research lineage

The evidence model is informed by FEVER's claim/evidence/verdict structure, OpenFactCheck's modular verification pipeline and ClaimBuster's claim-detection research. No third-party source code is vendored; implementation is original and MIT licensed. See `docs/REFERENCE_PROJECTS.md`.

## Verification policy

Lexical scoring in the alpha is deterministic decision support, not semantic truth. Every consequential decision requires human review and source-quality assessment.

## Author

Designed and led by **Dr. Ahmed Mohamed El Sayed** — OSINT, digital forensics, cybercrime investigation, financial crime intelligence and AI-powered investigation systems.

MIT License.
