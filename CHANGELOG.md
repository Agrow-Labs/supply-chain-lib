# Changelog

This project follows semantic versioning for the specification.

## [v1.0.0] - 2026-02-05

First stable release of the Standardized Supply Chain Library specification.

### Summary

This release incorporates all feedback from the peer review process (Milestone

3) and represents working group consensus on the finalized standard. Peer reviewers confirmed that all identified
   changes have been resolved and the standards are satisfactory.

### Added — New Documentation (Milestone 3/4 Refinement)

- `INTEROPERABILITY.md` — Actor roles, trust boundaries, and interaction models for multi-party supply chain
  environments (#26, #27)
- `INGESTION-PATTERNS.md` — Standard ingestion workflows for ERP systems, IoT and logistics data sources, and
  oracle/data availability services (#28–#31)
- `CARDANO-METADATA-COMPATIBILITY.md` — Guidance for integrating GS1 metadata with Cardano token, NFT, and metadata
  infrastructure (#32, #33)
- `PUBLISHING-PRACTICES.md` — Recommended practices for publishing GS1 records, aligned with existing metadata delivery
  tooling such as NFTCDN (#34, #35)
- `EXTENSIONS.md` — Framework for optional extension modules, maintaining separation between core standard and optional
  functionality (#36, #39)
- `REGULATORY-AND-SUSTAINABILITY.md` — Optional modules for regulatory compliance and sustainability tracking (#37, #38)
- `UTxO-Sizing.md` — Practical sizing constraints for on-chain storage
- `VERSIONING.md` — Formalized versioning and compatibility rules
- `STANDARD-VERSIONS.md` — Version tracking documentation

### Changed

- Validated CDDL schema (`gs1-general-specification-24.cddl`) against token metadata and NFT distribution systems (#33)
- Aligned metadata delivery practices with existing Cardano ecosystem tooling
  (#34)
- Evaluated and documented GS1-aligned Digital Product Passports (DPPs) as a forward-looking extension (#37)
- Updated `README.md` to reflect stable release status and link all new documentation

### Peer Review

Standards were submitted to a working group of peer reviewers during Milestone

3. Feedback was addressed through 16 tracked issues across three workstreams:

- **Ingestion Patterns** (#28–#31): Defined standard workflows for ERP, IoT, and oracle data sources
- **Metadata & Distribution Alignment** (#32–#35): Validated schemas and aligned publishing practices with Cardano
  tooling
- **Forward-Looking Extensions** (#36–#39): Documented extension framework and evaluated Digital Product Passports

All reviewers who responded confirmed the revised standards are satisfactory. Non-responsive reviewers were given
adequate time (1+ month) to provide input.

See: https://github.com/orgs/Agrow-Labs/projects/6

## v0.9.0-rc1

- Pre-release candidate for peer review.
- Consolidates the core GS1 encoding rules, envelopes, extension framework, interoperability guidance, and
  regulatory/DPP positioning.
