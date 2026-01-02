# Versioning and Compatibility

This repository is a specification-first effort. As such, versioning exists to
ensure that independent implementations can reliably encode, decode, and evolve
GS1-compatible payloads without ambiguity or accidental breakage.

This document defines two distinct version concepts:

* **schema_version** — the version of *this* specification (structure plus
  encoding rules)
* **gs1_release** — the referenced GS1 General Specifications release used as
  the baseline

These two concepts are intentionally separated so that this spec can evolve
while remaining grounded in a specific GS1 reference publication.

## schema_version

The **schema_version** represents the version of this standard’s:

* CBOR canonicalization requirements
* field encoding rules
* payload structure expectations (including any spec-level envelopes, if used)
* normative constraints defined within this repository

### Version Format

The `schema_version` SHALL follow semantic versioning:

```
MAJOR.MINOR.PATCH
```

### Compatibility Rules

* **PATCH** updates MUST be non-breaking.
    * clarifications, documentation improvements
    * example corrections
    * editorial fixes
    * additional non-normative guidance
* **MINOR** updates MUST be backward compatible for decoders.
    * additive changes only
    * optional fields or extension capabilities
    * new example patterns
    * additional recommended guidance that does not invalidate existing payloads
* **MAJOR** updates MAY be breaking.
    * structural changes that make previously valid payloads ambiguous or
      invalid
    * changes to canonical encoding rules
    * changes that require encoders/decoders to update logic to remain compliant

## gs1_release

The **gs1_release** identifies the GS1 General Specifications release this work
is referencing as the baseline.

This specification currently references:

* GS1 General Specifications, Release **24.0**

The gs1_release value is not intended to be updated frequently. When GS1 issues
a new release, compatibility must be considered carefully, particularly when GS1
introduces new Application Identifiers or modifies constraints.

## Backward Compatibility Commitment

A core principle of this work is that previously published payloads should
remain interpretable.

Accordingly:

* Implementations SHOULD treat unknown additional fields (or unknown AIs) as
  ignorable unless those fields are explicitly required by the `schema_version`
  in use.
* Encoders SHOULD NOT re-encode historical payloads under a different
  `schema_version` unless the intent is explicitly to migrate and republish.

## Canonical Encoding Stability

Canonical CBOR encoding rules are defined in `GS1.md`.

Because on-chain usage depends on stable binary encoding and reproducible
hashes:

* Changes to canonicalization rules (ordering rules, definite-length
  requirements, integer encoding constraints, or tag usage) MUST only occur in a
  MAJOR schema_version update.

## Where Version Fields Appear

This specification does not require that version fields be embedded inside the
raw GS1 Application Identifier map itself.

Instead, version fields are defined for use in **publishing envelopes** (e.g.,
transaction metadata payloads) so that:

* the GS1 AI map remains GS1-aligned and minimal
* versioning remains explicit and self-describing
* payloads remain portable between metadata and datum-based approaches

A recommended publishing envelope format is defined in
[`METADATA.md`](METADATA.md).