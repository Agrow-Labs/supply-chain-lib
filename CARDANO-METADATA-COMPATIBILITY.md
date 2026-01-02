# Cardano Metadata Compatibility

This document defines how the GS1 metadata standard specified in this repository
integrates with Cardano’s existing transaction metadata ecosystem, token and NFT
metadata standards, and common metadata delivery tooling.

The goal is to ensure that GS1 records can be published, discovered, and
validated within the Cardano ecosystem without disrupting or fragmenting
existing standards or tooling.

This document is informational and normative where stated.

## 1. Purpose & Scope

This specification is designed to coexist with Cardano’s established metadata
infrastructure while providing a standardized representation of GS1 supply-chain
data.

This document defines:

- how GS1 records fit within Cardano transaction metadata,
- how they coexist with token and NFT metadata standards,
- how metadata delivery tooling can ingest and serve GS1 records, and
- the compatibility guarantees this specification provides to implementers.

## 2. Cardano Metadata Model Overview

Cardano transaction metadata is represented as a CBOR map keyed by unsigned
integer labels.

Each label identifies a logically independent metadata namespace.

Metadata is immutable once published and may be indexed and served by off-chain
infrastructure such as explorers, indexers, and metadata delivery services.

This specification conforms to the existing Cardano metadata model and does not
introduce any changes to how metadata is encoded or submitted to the ledger.

## 3. GS1 Envelope Compatibility

GS1 records defined by this specification are published within a single metadata
label using the GS1 publishing envelope described in [METADATA.md](METADATA.md).

### Example (JSON representation)

```json
{
  "163532014": {
    "standard": "gs1",
    "schema_version": "1.0.0",
    "gs1_release": "24.0",
    "payload": {
      "01": "12341234567893",
      "10": "ABC12345"
    }
  }
}
```

### On-Chain Representation (Conceptual)

When submitted on-chain, the metadata label is encoded as an unsigned integer in
CBOR. The envelope and payload follow canonical CBOR encoding rules.

This representation is fully compatible with existing indexers and metadata
consumers.

## 4. Coexistence with Existing Metadata Standards

This specification is designed to coexist with all existing Cardano metadata
standards.

### CIP-25 (NFT Metadata)

GS1 metadata **MAY** be published in the same transaction as CIP-25 NFT metadata
using a separate metadata label.

No field-level coupling is required between GS1 records and CIP-25 records.

### CIP-68 (Reference Metadata)

GS1 metadata **MAY** coexist with CIP-68 reference metadata.

Implementations **MAY** use CIP-68 reference scripts for tokenized
representations of GS1-identified assets while publishing GS1 records under the
GS1 metadata label.

### Token Registries & Asset Metadata

GS1 metadata does not replace existing token registry or asset metadata
standards. Instead, it provides a complementary, domain-specific supply-chain
layer.

### Multiple Standards in a Single Transaction

Multiple metadata standards **MAY** coexist within the same transaction provided
each uses its own label.

This specification **RECOMMENDS** strict separation of metadata domains by label
to avoid collisions and preserve independent evolution of standards.

### Binding GS1 Records to Tokens

GS1 records often describe physical or digital assets that are also represented
on-chain as fungible tokens (FTs) or non-fungible tokens (NFTs). This
specification does not mandate a single binding mechanism, but it defines
recommended patterns for establishing an unambiguous association.

#### Pattern A — Token References GS1

The token’s metadata includes a reference to the GS1 record, such as:

- the GS1 metadata label,
- the transaction ID of the GS1 publication,
- or a hash of the GS1 identity core.

This pattern is useful when tokens are minted after GS1 identity is established.

#### Pattern B — GS1 References Token

The GS1 envelope payload includes a reference to the associated token, such as:

- asset ID (policy ID plus asset name),
- NFT fingerprint,
- or CIP-68 reference pointer.

This pattern is useful when GS1 records are authoritative and tokens are derived
representations.

#### Pattern C — Bidirectional Binding (Recommended)

Both the token metadata and the GS1 record reference each other.

This creates a durable, verifiable linkage that:

- survives independent data delivery systems,
- remains robust under partial data loss,
- and supports strong auditability.

#### Why This Matters

Explicit binding prevents ambiguity when multiple tokens, batches, or
representations exist for the same underlying asset and enables:

- regulator-grade traceability,
- marketplace interoperability,
- reliable indexer correlation.

### Publisher Authority & Update Control

GS1 records that evolve over time require a well-defined authorization model for
publishing updates and anchors.

This specification defines a _Publisher Authority_ model with multiple supported
patterns (key-based, token-gated, and script-based), enabling implementations to
choose an authorization mechanism appropriate to their operational and
regulatory environment.

Detailed guidance is provided in
[PUBLISHING-PRACTICES.md](PUBLISHING-PRACTICES.md).

## 5. Alignment with Metadata Delivery Tooling

Metadata delivery services, indexers, and explorers can ingest GS1 records using
existing metadata pipelines without protocol changes.

GS1 envelopes are:

- self-describing,
- versioned,
- schema-stable, and
- deterministically encoded.

These properties enable reliable long-term indexing, caching, and distribution.

Services such as NFTCDN and similar metadata providers can expose GS1 records
alongside token and NFT metadata without requiring GS1-specific extensions to
their ingestion infrastructure.

## 6. Schema Validation & Distribution Systems

GS1 records may participate in token distribution and NFT minting workflows
without modification.

Validation of GS1 records consists of:

- validating canonical CBOR encoding,
- validating `schema_version` compatibility,
- verifying the integrity of any anchored records, and
- applying domain-specific validation rules where required.

Because GS1 records are decoupled from token and NFT metadata schemas, they may
evolve independently without breaking existing distribution systems.

## 7. Compatibility Guarantees

Implementations conforming to this specification get the following guarantees:

- Non-interference with existing Cardano metadata standards
- Compatibility with existing token and NFT distribution systems
- Safe coexistence with multiple metadata standards in a single transaction
- Long-term indexer and tooling compatibility
- Incremental adoption without ecosystem fragmentation

## 8. Summary & Adoption Guidance

This specification integrates GS1 supply-chain metadata into the Cardano
ecosystem using existing metadata primitives and delivery infrastructure.

Implementers may adopt GS1 metadata alongside existing token and NFT standards
with no changes to underlying blockchain protocols or tooling, enabling rapid
ecosystem integration and long-term stability.