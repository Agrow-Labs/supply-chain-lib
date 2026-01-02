# Metadata Publishing Practices

This document defines recommended practices for publishing GS1 metadata on
Cardano in a manner that is reliable, interoperable, and compatible with
existing ecosystem tooling.

These practices are intended to guide implementers in making consistent design
decisions across different application domains and deployment models.

## Design Goals

Metadata publishing under this specification **SHOULD**:

- preserve long-term interpretability,
- avoid fragmentation of metadata standards,
- support deterministic verification,
- remain compatible with existing Cardano tooling, and
- enable incremental adoption.

## Choosing a Publishing Strategy

Implementers **SHOULD** select the publishing strategy based on the
characteristics of the data being published.

### Inline Datum

Use inline datums when:

- the payload is small and identity-centric,
- the data is required for on-chain validation, or
- the data represents the current state.

#### Inline Datum & CIP-68 Considerations

When using CIP-68 reference tokens, implementers **MUST** account for the fact
that CIP-68 relies on inline datums for token metadata storage.

Because each UTxO can contain only a single inline datum, designs that attempt
to co-locate GS1 payloads and CIP-68 token metadata within the same UTxO may
become constrained or infeasible.

Implementers **SHOULD** therefore avoid placing GS1 data in inline datums on
UTxOs that are also used for CIP-68 reference tokens unless:

- the combined payload remains minimal and stable, and
- the UTxO layout is explicitly designed to support both data models.

In environments where CIP-68 is used extensively, anchor-based publishing or
transaction metadata is typically the preferred mechanism for GS1 records.

### Transaction Metadata

Use transaction metadata when:

- the payload is moderate in size,
- the data must be publicly discoverable,
- the data does not need to be enforced by scripts.

### Anchor-Based Publishing (Recommended)

Use anchor-based publishing when:

- the payload is large or evolving,
- the data consists primarily of event history or documents,
- the data is updated frequently.

Anchor-based publishing provides constant on-chain footprint while preserving
the verifiable integrity of large off-chain records.

## Publisher Authority & Update Authorization

GS1 records that evolve over time (via anchors or metadata updates) require a
well-defined authority model to determine _who is permitted to publish updates._

This specification defines the concept of a **Publisher Authority**:
the entity or mechanism authorized to publish new anchors, corrections, and
state updates for a GS1 record.

The specific authority mechanism is implementation-dependent. However,
implementations **SHOULD** support at least one of the following patterns.

### Pattern 1 — Key-Based Authority (Simplest)

#### Establishment

The initial GS1 publication includes an `authority` field identifying a
verification key hash (or payment credential).

#### Authorization

An update is authorized if the transaction publishing the update is signed by
the corresponding key.

#### Benefit

This is the simplest and most widely compatible model. It requires no additional
on-chain assets or scripts and integrates directly with existing wallet and
signing infrastructure.

### Pattern 2 — Token-Gated Authority (Most Transferable)

#### Establishment

An Authority Token (NFT or CIP-68 reference token) is minted to represent
control over the GS1 record or record set. The GS1 publication references the
authority token by asset ID or CIP-68 reference.

#### Authorization

An update is authorized if the transaction proves control of the authority
token, for example, by spending the UTxO holding the token or satisfying a
validator condition that enforces its presence.

#### Benefit

This is the most transferable model. Control of the GS1 record can be
transferred by transferring the authority token, enabling clean handoff of
publishing rights between organizations without rotating cryptographic keys.

### Pattern 3 — Script-Based Authority (Recommended for Regulated Environments)

#### Establishment

The GS1 publication includes the hash of a validator script that governs update
authorization.

#### Authorization

An update is authorized if the transaction satisfies the validator’s rules
(multi-signature, quorum, time locks, role tokens, or other governance logic).

#### Benefit

This is the most expressive and auditable model. It supports complex governance,
regulatory compliance, and multi-party approval flows, making it the preferred
choice for high-assurance and regulated deployments.

### Authority Evolution & Attestation (Optional)

Implementations **MAY** support authority rotation, delegation, and external
attestations by anchoring updated authority records or associated certification
documents off-chain and publishing new anchors.

This allows trust models to evolve without breaking historical verifiability.

## Publishing Lifecycle

### Initial Publication

1. Establish GS1 identity core.
2. Publish identity on-chain (datum or metadata).
3. Initialize off-chain record.
4. Publish anchor.

### Updates

1. Append new events to off-chain record.
2. Recompute canonical record.
3. Publish new anchor on-chain.

### Decommissioning / Finalization

Optionally, publish a final anchor indicating record closure.

## Versioning & Upgrades

Publishers **MUST**:

- include `schema_version` in all envelopes,
- follow semantic versioning rules defined in [VERSIONING.md](VERSIONING.md),
- avoid breaking changes outside **MAJOR** version updates.

Consumers **SHOULD**:

- tolerate unknown fields,
- preserve backward compatibility.

## Label Selection & Namespacing

Implementers **SHOULD**:

- use the recommended GS1 metadata label for general publication,
- avoid reusing labels for unrelated domains,
- treat metadata labels as stable namespaces.

When publishing multiple metadata standards in the same transaction, each
**MUST** use a distinct label.

## Publishing with Tokens & NFTs

When publishing GS1 metadata alongside tokens or NFTs:

- preserve separation of concerns by label,
- avoid embedding GS1 data directly into token metadata schemas,
- establish explicit bindings between tokens and GS1 records as defined in
  [CARDANO-METADATA-COMPATIBILITY.md](CARDANO-METADATA-COMPATIBILITY.md).

## Indexer & Delivery Considerations

Publishers **SHOULD**:

- prefer deterministic CBOR encoding,
- avoid unnecessary envelope churn,
- batch updates when possible,
- ensure anchors remain retrievable.

These practices maximize compatibility with indexers, explorers, and metadata
delivery services.

## Security & Integrity

Publishers **MUST**:

- compute anchors over canonical CBOR payloads,
- preserve the immutability of anchored records,
- protect signing and publishing keys.

Consumers **MUST**:

- verify hashes against on-chain anchors,
- validate `schema_version` compatibility.

## Summary

Consistent publishing practices are essential to long-term interoperability and
ecosystem trust. These guidelines enable GS1 metadata to integrate cleanly with
Cardano’s existing infrastructure while remaining flexible enough to support
diverse application requirements.
