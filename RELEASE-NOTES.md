## v1.0.0 — First Stable Release

**Release Date:** February 2026
**GS1 Compatibility:** GS1 General Specifications Release 24.0

### Overview

The Standardized Supply Chain Library v1.0.0 is the first stable release of an
open-source specification for integrating GS1 supply chain standards into the
Cardano blockchain ecosystem. This specification defines CBOR-friendly
structural mappings for GS1 identifiers and related fields, accompanied by a
concrete CDDL schema for validation and interoperability.

### What's Included

**Core Standards**
- GS1 General Specifications mapped to CBOR/JSON for Cardano
- Sector-specific documentation: Agriculture (GTIN), Logistics (GLN), Retail (GIAI)
- CDDL schema for validation (`gs1-general-specification-24.cddl`)
- Complete JSON representation (`GS1_Complete.json`)

**Integration & Interoperability**
- Interoperability guidance for multi-party supply chains
- Standard ingestion workflows for ERP, IoT, and oracle services
- Cardano metadata compatibility and publishing practices

**Extensions**
- Regulatory and sustainability module framework
- Digital Product Passport (DPP) evaluation
- Clear separation between core standard and optional extensions

**Infrastructure**
- UTxO sizing analysis for on-chain storage
- Semantic versioning and compatibility rules
- Validation tooling and tests

### Peer Review

This release incorporates feedback from a community working group review
process. All tracked issues were resolved and reviewers confirmed the standards
are satisfactory for stable release.

### License

CC BY 4.0 International

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
