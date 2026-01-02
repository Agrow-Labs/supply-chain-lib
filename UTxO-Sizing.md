# UTxO Storage & Performance Review

This document provides guidance for sizing and storage decisions when using GS1
payloads on Cardano.

This specification defines deterministic CBOR encoding rules, but it does not
mandate where data must live (datum vs. metadata vs. off-chain). Storage
strategy is driven primarily by:

- payload size
- update frequency
- validation requirements
- consumer/indexer requirements
- long-term interoperability

## What We Measure

For practical on-chain use, the important unit is the **encoded byte size** of
the payload that will be stored or hashed.

Accordingly, implementations **SHOULD** measure:

- CBOR byte size of the **GS1 AI map** (canonical/deterministic encoding)
- CBOR byte size of any **publishing envelope** (if used)
- Total byte footprint if:
    - stored as an inline datum
    - stored as transaction metadata
    - stored off-chain with an on-chain anchor

A helper tool is provided in `tools/size_check.py`.

## Practical UTxO Considerations

Inline datums compete for space and budget within real transactions.

As datum size increases:

- transaction construction becomes more constrained
- fees and execution budgets may increase (depending on usage)
- operational reliability declines (especially for multi-output transactions)
- scripts that validate or transform large datums become more complex and costly

This means that the most reliable pattern is often:

- keep the on-chain datum minimal (identity-centric fields)
- store large, evolving data off-chain
- anchor the off-chain record on-chain with a verifiable commitment (hash)

## Optimization Guidance

### 1. Prefer Minimal, Identity-Centric Datums

If the intent is to validate identity and traceability linkage, store only the
minimal fields necessary for correctness.

Example: a compact GS1 AI map containing GTIN + batch/lot + expiry.

Avoid placing long histories, document blobs, or repeated event lists directly
in a datum.

### 2. Prefer Anchors for Large or Evolving Payloads

If the payload is large or expected to evolve, publish:

* a hash of canonical CBOR (deterministic encoding)
* an optional retrieval pointer (e.g., ipfs://, https://)

See [METADATA.md](METADATA.md) for an anchor envelope pattern.

### 3. Avoid Repetition

Supply-chain event models can explode in size when repeatedly embedding:

* duplicated identifiers
* repeated location strings
* repeated timestamps

Prefer to keep the on-chain payload as an anchor to a structured off-chain
record when event histories grow beyond a small footprint.

### 4. Use Domain-Specific Extension Records Off-Chain

When adding fields beyond the core GS1 identifiers (e.g., certificates, lab
reports, temperature logs), treat these as extension records and anchor them
rather than embedding them.

## Optional Compression

This specification does not mandate compression.

Compression **MAY** be used for off-chain storage and transport. However:

* the anchored hash **MUST** be computed over the canonical CBOR payload as
  defined by this spec (prior to compression), unless an implementation
  explicitly publishes the compression algorithm and hashes the compressed form.

If a compressed form is published, the anchor MUST specify:

* compression algorithm
* content type
* whether the hash applies to the compressed or uncompressed form

## **Hybrid Pattern: On-Chain Identity + Off-Chain Events**

In most real-world supply-chain systems, the *identity* of an asset is
relatively stable, while the *history* of that asset grows continuously over
time. Attempting to store both identity and full event history on-chain leads to
unbounded datum growth, higher transaction costs, and unnecessary UTxO churn.

This specification therefore recommends a **hybrid storage pattern**:

> **Store state on-chain. Store history off-chain. Anchor history on-chain.**

### On-Chain: Identity Core (Inline Datum)

The inline datum should contain only the minimal GS1 identity fields required to
establish the asset’s identity and current state, such as:

* GTIN (01)
* Batch/Lot (10)
* Serial (21), when applicable
* Optional: GIAI (8004) for reusable assets
* Optional: current owner/location fields when required for validation

This identity core remains compact, stable, and inexpensive to validate.

### Off-Chain: Event History and Documents

All append-heavy data should be maintained off-chain, including:

* custody transfers
* logistics events
* inspections and certifications
* sensor logs
* regulatory or compliance documents

This data may grow arbitrarily large without affecting on-chain storage costs.

### On-Chain Anchor: Verifiable Link to History

Each off-chain record update is anchored on-chain using an **anchor object**
containing:

* cryptographic hash of the off-chain record
* content type
* retrieval URI
* optional sequencing or version fields

The anchor may be published:

* in transaction metadata (recommended for discoverability and low churn), or
* within the datum itself when the validator must enforce state continuity.

### Storage and Performance Implications

Using the hybrid model:

* the inline datum remains small and stable (typically tens to low hundreds of
  bytes),
* the anchor metadata remains small and constant,
* the off-chain record may grow arbitrarily without increasing UTxO costs.

This approach minimizes transaction fees, avoids unnecessary UTxO bloat, and
preserves a strong cryptographic linkage between on-chain state and off-chain
history.

## Recommended Project Thresholds (Non-Normative)

For reliability and interoperability, implementations SHOULD define
project-level thresholds for when to:

* embed directly
* anchor instead

A reasonable starting guideline is:

* keep inline datum payloads “small” and identity-centric
* anchor payloads once they begin to include event history, documents, or
  multi-party append-only logs

Because network parameters and application constraints vary, this document
intentionally avoids hardcoding protocol limits. Instead, measure the actual
encoded byte sizes and design accordingly.

## Measurement Notes

All size references in this repository should be based on:

* canonical/deterministic CBOR encoding rules defined in [GS1.md](GS1.md)
* minimal integer widths for AI keys
* definite-length CBOR encoding only

The helper tool in [tools/size_check.py](tools/size_check.py) is intended to
support consistent and repeatable measurement across scenarios.

The following measurements reflect the storage implications of the patterns
described above, including the hybrid model.

## Representative Size Measurements (Canonical CBOR)

The following measurements were produced using canonical/deterministic CBOR
encoding and include the transaction metadata label wrapper (`163532014`) when
measuring metadata records.

| Scenario                   | AI Map (CBOR bytes) | Metadata Record (CBOR bytes) |
|----------------------------|---------------------|------------------------------|
| Agriculture                | 40                  | 118                          |
| Logistics                  | 81                  | 160                          |
| Retail                     | 68                  | 146                          |
| Representative GS1 Payload | 136                 | 225                          |

### Anchor Pattern Measurements

| Record Type                         | Size (CBOR bytes) |
|-------------------------------------|-------------------|
| Off-chain trace record (25 events)  | 2333              |
| Off-chain trace record (100 events) | 8649              |
| On-chain anchor metadata record     | 235               |

These measurements demonstrate that the anchor method keeps the on-chain
footprint stable even as the underlying trace record grows.

### Hybrid On-Chain Cost Summary

Using the hybrid model, the total on-chain footprint is the sum of:

- the inline datum containing the GS1 identity core, and
- the anchor metadata record published with each update.

Based on representative measurements:

| Component                               | Size (CBOR bytes)  |
|-----------------------------------------|--------------------|
| Inline identity datum                   | ~40–136            |
| Anchor metadata record                  | 235                |
| **Total on-chain footprint per update** | **~275–371 bytes** |

The associated off-chain trace record may grow into kilobytes or megabytes
without affecting on-chain storage costs.