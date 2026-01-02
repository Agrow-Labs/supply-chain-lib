# Release Notes — v0.9.0-rc1

This is a pre-release candidate for the GS1 supply-chain metadata standard for
Cardano.

It is intended to be feature-complete and audit-ready, pending peer review.

## Highlights

- Deterministic CBOR encoding rules for GS1 AI maps
- Metadata publishing envelopes and compatibility guidance
- UTxO sizing and performance guidance (inline vs metadata vs anchors)
- Interoperability and ingestion patterns
- Extension framework with authority separation and signing/hashing rules
- Regulatory and sustainability positioning, including DPP alignment

## Review Focus

Peer reviewers are requested to evaluate:

- clarity and completeness of normative requirements,
- determinism and compatibility guarantees,
- extension attachment modes and authority model,
- suitability for a `v1.0.0` production release.

## Scope of Changes Allowed Before v1.0.0

Before `v1.0.0`, refinements may include:

- clarification of wording,
- additional examples,
- tightening of validation guidance,
- minor structural reorganization.

Changes to canonical encoding rules or envelope compatibility guarantees should
be avoided unless required for correctness.
