# Extension Framework

This document defines the extension model for the GS1 metadata standard
described in this repository.

The extension framework allows regulatory, sustainability, and industry-specific
capabilities to be layered on top of the core standard without compromising its
stability, neutrality, or long-term interoperability.

Extensions are especially relevant for regulatory, sustainability, and lifecycle
tracking use cases. See
[REGULATORY-AND-SUSTAINABILITY.md](REGULATORY-AND-SUSTAINABILITY.md)
for positioning and context.

## 1. Purpose of the Extension Model

The core standard defined in this repository establishes a minimal, stable, and
interoperable foundation for representing GS1 identity and traceability data.

However, real-world deployments require additional capabilities for:

- regulatory compliance,
- sustainability reporting,
- industry-specific requirements, and
- private or commercial use cases.

The extension model provides a structured mechanism for adding these
capabilities without modifying or fragmenting the core standard.

## 2. Core vs. Optional Modules

### Core Standard

The core standard defines:

- canonical GS1 encoding rules,
- deterministic CBOR encoding,
- publishing envelopes,
- metadata compatibility requirements.

The core standard **MUST** remain stable and narrowly scoped.

### Optional Extensions

Extensions MAY define:

- additional schemas,
- domain-specific records,
- compliance modules,
- lifecycle and sustainability modules.

Extensions **MUST NOT** change the meaning, encoding, or semantics of the core
GS1 fields.

## 3. Extension Categories

Extensions typically fall into the following categories.

### Regulatory & Compliance Extensions

- certifications
- audits
- regulatory filings
- jurisdiction-specific disclosures

### Sustainability & Lifecycle Extensions

- carbon and emissions records
- recycling and reuse data
- environmental impact assessments
- product stewardship programs

### Industry-Specific Extensions

- pharmaceuticals
- food and agriculture
- automotive
- electronics

### Private & Commercial Extensions

- proprietary business workflows
- contractual data
- internal reporting

## 4. Attaching Extensions to the Core

Extensions attach to the core GS1 record using one or more of the following
mechanisms:

- off-chain extension records anchored on-chain,
- extension fields within anchored payloads,
- versioned extension schemas referenced by the GS1 envelope.

The core GS1 identity and traceability semantics **MUST** remain independent of
any extension data.

Extensions **MAY** declare their own authority model and governance constraints,
including publication rights and update authorization rules, provided that such
constraints do not alter the semantics or encoding of the core GS1 record.

### Extension Attachment Types

- Inline Attachment
- Reference Attachment (anchored or external)

### Anchoring Modes

Implementations **MAY** use one of the following approaches:

- Extension-only anchoring: each extension publishes and anchors its own record.
  In this mode, the `extensions[]` list acts as the discoverable manifest of
  extension anchors and authorities.

- Assembled anchoring (_optional_): an implementation **MAY** also publish an
  assembled anchor that commits to a merged lifecycle record spanning multiple
  extensions. This improves consumer synchronization but is not required for
  integrity.

Reference attachments **MAY** include an `anchor_tx` field identifying the
transaction where the most recent on-chain anchor commitment for the referenced
extension record was published. This field is informational and intended for
discoverability and indexing. An "anchor commitment" refers to a published
cryptographic hash of a canonical CBOR-encoded record together with an optional
retrieval pointer (e.g., URI).

An `anchor_tx` **MAY** reference either:

- a transaction that contains an on-chain anchor commitment (hash plus retrieval
  pointer) to an off-chain extension record, **or**
- a transaction that directly carries the canonical extension record as inline
  transaction metadata or inline datum.

This allows implementations to publish extension records fully on-chain when
their size and update frequency permit, while preserving compatibility with
off-chain anchoring patterns.

## 5. Governance & Evolution of Extensions

Extensions **SHOULD**:

- declare their own schema versions,
- document compatibility and deprecation policies,
- provide validation tooling where applicable.

Multiple independent extension ecosystems **MAY** coexist.

No centralized governance authority is required.

## 6. Authority Model for Extensions

The authority that governs the core GS1 record and the authority that governs an
extension record **MAY** be distinct.

The core GS1 authority controls publication and update of:

- GS1 identity fields,
- core traceability state,
- anchors for core GS1 records (and assembled views, when used).

An extension **MAY** define its own authority responsible for publishing and
updating extension-specific records, such as regulatory filings, certifications,
or sustainability disclosures.

Extension authorities:

- **MAY** be independent of the GS1 authority,
- **MAY** be bound to regulatory bodies, auditors, certifiers, or consortia,
- **MUST** be discoverable from the extension record or its associated anchor
  record when anchoring is used.

Extension records **SHOULD** be signed by the extension authority’s key,
allowing consumers to verify authorship independently of any anchoring
mechanism.

### Signing & Hashing Rules

Extension records exist to allow third parties to publish additional data that
extends a core GS1 record.

To ensure integrity and attributable authorship:

- Extension records **MUST** place all extension payload fields under `data`.
- Integrity hashes and authority signatures **MUST** be computed over canonical
  CBOR encoding of the `data` object only, unless explicitly stated otherwise by
  the extension schema.
- The canonical CBOR encoding of `data` is the sole input to both hashing and
  signature generation.

For reference attachments:

- The referenced extension record **MUST** include `authority` and `signature`
  so the record can be verified independently of any on-chain publication.
- The core GS1 record **SHOULD NOT** duplicate signatures for referenced
  extension records.

For inline attachments:

- The inline `data` object **SHOULD** be signed by the declared extension
  authority and the signature **MUST** be included in the inline attachment.

Implementations **MAY** publish an anchor (hash plus retrieval URI) for an
extension record on-chain, but anchoring is optional and independent of
signature-based authorship verification.

This separation enables domain-specific governance without weakening the
integrity of the core GS1 identity.

## 7. Interoperability Guarantees

The extension model guarantees:

- core standard stability,
- extension isolation,
- backward compatibility,
- safe incremental adoption.

## 8. Example: Sustainability Extension (Non-Normative)

This example illustrates how an optional sustainability extension might be
defined and attached to a core GS1 record without modifying the core standard.

### Extension Definition

```json
{
  "extension_id": "org.example.sustainability",
  "schema_version": "1.0.0",
  "applies_to": "gs1_record",
  "domain": "sustainability",
  "authority_model": "independent",
  "description": "Sustainability and environmental impact disclosures governed by third-party certifiers or regulators.",
  "fields": {
    "carbon_footprint_kg": "number",
    "water_usage_liters": "number",
    "recycled_content_pct": "number",
    "certifications": [
      "string"
    ]
  }
}
```

### Off-Chain Extension Record

```json
{
  "extension_id": "org.example.sustainability",
  "schema_version": "1.0.0",
  "authority": {
    "authority_type": "organization",
    "name": "EU Food Safety Authority",
    "public_key": "eufsa_pub_key_hex"
  },
  "gs1_identity": {
    "01": "12341234567893",
    "10": "ABC12345"
  },
  "data": {
    "carbon_footprint_kg": 12.4,
    "water_usage_liters": 18.7,
    "recycled_content_pct": 32,
    "certifications": [
      "ISO-14067",
      "EU-Ecolabel"
    ],
    "timestamp": "2026-01-02T14:03:00Z"
  },
  "signature": "sig_over_canonical_data_object_hex"
}
```

### Key Properties Demonstrated

- Core GS1 identity remains unchanged.
- Extension schema evolves independently.
- Multiple extensions may coexist.
- On-chain footprint remains stable.

## 9. Example: Complete On-Chain Metadata with GS1 Core and Multiple Extensions (Non-Normative)

> **Note:** This example uses JSON representation for readability. On-chain, the
> metadata label is encoded as an unsigned integer using canonical CBOR.

This example shows that a single Cardano transaction’s metadata could represent:

- a GS1 identity core,
- a sustainability extension record,
- and an on-chain anchor to detailed off-chain lifecycle data.

### Scenario

A reusable shipping crate of apples is tracked for sustainability reporting.

| Field            | Value                  |
|------------------|------------------------|
| Product          | Apples (crate)         |
| GTIN             | `09506000134352`       |
| Batch            | `BATCH-2026-01`        |
| Serial           | `CRATE-000042`         |
| Location (GLN)   | `9876543210987`        |
| Carbon footprint | 12.4 kg CO₂e           |
| Water usage      | 18.7 liters            |
| Recycled content | 32%                    |
| Certifications   | ISO-14067, EU-Ecolabel |

Detailed lifecycle data (harvest, transport, inspections, sensor logs) is stored
off-chain and anchored on-chain.

The top-level `anchor` field shown below is optional and represents an assembled
lifecycle commitment. Implementations **MAY** omit it and rely exclusively on
per-extension anchors.

### Transaction Metadata (JSON Representation)

```json
{
  "163532014": {
    "standard": "gs1",
    "schema_version": "1.0.0",
    "gs1_release": "24.0",
    "authority_type": "token",
    "authority": {
      "policy_id": "8f9c2a7b3e5d4c1a9b0f7e6d5c4b3a2918273645a1f0e9d8c7b6a5e4d3c2b1a0",
      "asset_name": "GS1_AUTHORITY_CRATE"
    },
    "payload": {
      "01": "09506000134352",
      "10": "BATCH-2026-01",
      "21": "CRATE-000042",
      "414": "9876543210987"
    },
    "extensions": [
      {
        "extension_id": "org.example.quality",
        "schema_version": "1.0.0",
        "attachment": "inline",
        "authority": {
          "authority_type": "vkey",
          "name": "Quality Inspection Authority",
          "public_key": "quality_pub_key_hex"
        },
        "data": {
          "grade": "A",
          "brix": 14.2,
          "inspection_date": "2026-01-02"
        },
        "signature": "sig_quality_payload_hex"
      },
      {
        "extension_id": "org.example.sustainability",
        "schema_version": "1.0.0",
        "attachment": "reference",
        "record": {
          "anchor_tx": "3c7e1d6f8a2b9e5c4f1a0d3b6e8c2f7a9d4e5b1c6f0a2d3e4b8c7a9e6d5f1b",
          "content_type": "application/cbor"
        }
      },
      {
        "extension_id": "org.example.compliance",
        "schema_version": "2.3.4",
        "attachment": "reference",
        "record": {
          "uri": "https://certs.example.org/organic/CRATE-000042.json",
          "content_type": "application/json",
          "hash_alg": "sha-256",
          "hash_hex": "5e2f0f1a9b8c7d6e5f4a3b2c1d0e9f8a7b6c5d4e3f2a1b0c9d8e7f6a5b4c3d2e"
        }
      }
    ],
    "anchor": {
      "hash_alg": "blake2b-256",
      "hash_hex": "d34db33fd34db33fd34db33fd34db33fd34db33fd34db33fd34db33fd34db33f",
      "uri": "ipfs://bafybeibq2c2c2mshc6yp7f4s7x2yztqkmy3yn6h5h4c7g8p9f6e5d4c3b2a1"
    }
  }
}

```

### On-Chain Sustainability Extension Record (Human-Readable)

```json
{
  "extension_id": "org.example.sustainability",
  "schema_version": "1.0.0",
  "authority": {
    "authority_type": "organization",
    "name": "EU Food Safety Authority",
    "public_key": "eufsa_pub_key_hex"
  },
  "gs1_identity": {
    "01": "09506000134352",
    "10": "BATCH-2026-01",
    "21": "CRATE-000042"
  },
  "data": {
    "carbon_footprint_kg": 12.4,
    "water_usage_liters": 18.7,
    "recycled_content_pct": 32,
    "certifications": [
      "ISO-14067",
      "EU-Ecolabel"
    ],
    "lifecycle_events": [
      {
        "type": "harvest",
        "date": "2026-01-01",
        "location": "Farm Alpha",
        "operator": "Green Valley Orchards"
      },
      {
        "type": "transport",
        "date": "2026-01-03",
        "mode": "truck",
        "distance_km": 220,
        "carrier": "BlueRoute Logistics"
      },
      {
        "type": "inspection",
        "date": "2026-01-04",
        "result": "pass",
        "inspector": "EU Food Safety Authority"
      }
    ]
  },
  "signature": "sig_over_canonical_data_object_hex"
}
```

### What This Represents

| Layer               | Role                                                                |
|---------------------|---------------------------------------------------------------------|
| GS1 payload         | Canonical identity of the physical asset                            |
| GS1 Authority       | Controls core GS1 identity and anchor publication (if applicable)   |
| Extension pointer   | Declares existence of sustainability module                         |
| Extension authority | Controls publication of sustainability/compliance extension records |
| Anchor              | Verifiable commitment to full lifecycle record                      |
| Off-chain record    | Complete event history, certifications, sensor logs                 |

### Why This Matters

This pattern enables:

- regulator-grade traceability,
- sustainable lifecycle reporting,
- DPP compatibility,
- minimal on-chain footprint,
- unbounded off-chain data growth,
- clean separation of core vs. extensions.

## 10. Example: Root / Assembled Anchor File (Non-Normative)

In assembled anchoring mode, a GS1 authority **MAY** publish a root file that
acts as a merged view of a GS1 record plus one or more extension records.

This root file is intended to improve consumer synchronization by providing a
single retrieval target, but it is not required for integrity because each
extension may also be independently anchored and signed.

The root file **SHOULD** contain:

- the core GS1 identity payload,
- a list of extension references,
- and optional embedded inline extension data.

The root file itself **MAY** be anchored on-chain using the same anchor
mechanism described elsewhere in this specification.

### Root File (JSON representation)

```json
{
  "standard": "gs1",
  "schema_version": "1.0.0",
  "gs1_release": "24.0",
  "gs1_identity": {
    "01": "09506000134352",
    "10": "BATCH-2026-01",
    "21": "CRATE-000042",
    "414": "9876543210987"
  },
  "extensions": [
    {
      "extension_id": "org.example.quality",
      "schema_version": "1.0.0",
      "attachment": "inline",
      "authority": {
        "authority_type": "vkey",
        "name": "Quality Inspection Authority",
        "public_key": "quality_pub_key_hex"
      },
      "data": {
        "grade": "A",
        "brix": 14.2,
        "inspection_date": "2026-01-02"
      },
      "signature": "sig_over_canonical_data_object_hex"
    },
    {
      "extension_id": "org.example.sustainability",
      "schema_version": "1.0.0",
      "attachment": "reference",
      "record": {
        "anchor_tx": "3c7e1d6f8a2b9e5c4f1a0d3b6e8c2f7a9d4e5b1c6f0a2d3e4b8c7a9e6d5f1b",
        "content_type": "application/cbor"
      }
    },
    {
      "extension_id": "org.example.compliance",
      "schema_version": "2.3.4",
      "attachment": "reference",
      "record": {
        "uri": "https://certs.example.org/organic/CRATE-000042.json",
        "content_type": "application/json",
        "hash_alg": "sha-256",
        "hash_hex": "5e2f0f1a9b8c7d6e5f4a3b2c1d0e9f8a7b6c5d4e3f2a1b0c9d8e7f6a5b4c3d2e"
      }
    }
  ]
}
```

This root file is now a concrete “assembled view” without changing your trust
model.

### On-chain Publication Notes (Non-Normative)

In the transaction metadata example above:

- Inline extension attachments carry `authority` and `signature` directly in the
  GS1 record because their `data` is embedded on-chain.
- Reference extension attachments omit signatures in the GS1 record because the
  referenced extension record **MUST** carry its own `authority` and
  `signature`.
- For off-chain reference attachments, `hash_alg` and `hash_hex` allow consumers
  to verify that the retrieved document matches the referenced bytes.
- For on-chain reference attachments, the transaction referenced by `anchor_tx`
  is expected to contain an anchor commitment (hash plus retrieval URI) for the
  referenced extension record.

## 11. Summary

The extension framework enables the GS1 metadata standard to support complex
real-world requirements without sacrificing simplicity, stability, or
interoperability.
