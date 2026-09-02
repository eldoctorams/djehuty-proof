# Reference projects and clean-room decisions

| Project | Useful pattern | DJEHUTY PROOF decision |
|---|---|---|
| [FEVER](https://github.com/sheffieldnlp/fever-naacl-2018) | Claim, evidence and verdict benchmark structure | Make the claim-to-evidence edge explicit and reviewable |
| [OpenFactCheck](https://github.com/mbzuai-nlp/openfactcheck) | Modular fact-verification pipeline | Separate decomposition, retrieval, judgment and reporting |
| [ClaimBuster](https://github.com/idirlab/claimbuster-spotter) | Check-worthy claim detection | Preserve stable claim units before evidence assessment |
| [STORM](https://github.com/stanford-oval/storm) | Citation-aware report generation | Audit evidence coverage at sentence/claim level, not link level |

These projects were studied as references. No source code, datasets or model weights are copied or bundled. DJEHUTY PROOF is an independent MIT-licensed implementation.
