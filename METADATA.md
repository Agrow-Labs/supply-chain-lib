# Transaction Metadata Publishing Guidance

This document defines a recommended approach for publishing GS1-compatible data
on Cardano using transaction metadata.

This is not the only way to publish GS1 data on-chain. However, publishing
conventions are useful because they reduce fragmentation and make it easier for
indexers and consumers to discover and interpret payloads consistently.

## Recommended Metadata Label

For publishing generic GS1 payloads via transaction metadata, this specification
recommends a default metadata label:

**Recommended Label:** `163532014`

This value is derived deterministically from:

``` 
SHA-256("cardano-gs1-metadata-spec")
```

and then converting the first seven hex characters to a decimal integer.

Implementations **SHOULD** use this label when publishing “generic GS1 payloads”
that are not already namespaced under an application-specific label.

Implementations **MAY** use a different label when required by existing system
conventions or application constraints.

## Publishing Envelope

When publishing GS1 data via metadata, the payload SHOULD be wrapped in a small,
self-describing envelope to ensure portability and compatibility across systems.

### Envelope Fields

* **standard**: identifies the payload family (e.g., `"gs1"`)
* **schema_version**: version of this specification (see `VERSIONING.md`)
* **gs1_release**: GS1 General Specs release reference (e.g., `"24.0"`)
* **payload**: either:
    * a full GS1 AI map (small payload), OR
    * an anchored reference object (large payload)

The envelope format is intentionally simple and designed to be stable over time.

## Datum Encoding Considerations (Inline Datums)

When GS1 payloads are stored as inline datums, implementations MAY omit the
publishing envelope and store only the canonical GS1 AI map.

This is typically safe because the interpretation of a datum is already
constrained by the validator and script context in which it appears. In other
words, the script address and validator logic implicitly defines how the datum
is interpreted and validated.

In contrast, transaction metadata is globally visible and context-free, and
therefore SHOULD include the publishing envelope to remain self-describing and
interoperable across independent consumers and indexers.

Implementations MAY choose to use the same envelope format inside a datum when a
self-describing datum is desirable, but this is not required by this
specification.

## Example A: Full Payload Published as Metadata

This pattern is used when the GS1 payload is small enough to publish directly.

### JSON-like Representation (for clarity)

```json
{
  "163532014": {
    "standard": "gs1",
    "schema_version": "1.0.0",
    "gs1_release": "24.0",
    "payload": {
      "01": "12341234567893",
      "10": "ABC12345",
      "17": "241122",
      "30": "50"
    }
  }
}
```

### Notes

In CBOR encodings produced under this specification, the GS1 AI map keys MUST be
encoded as unsigned integers (see GS1.md).

The envelope keys are not GS1 AIs and may be encoded as text keys.

## Example B: Anchor Format Published as Metadata

This pattern is used when the GS1 payload (or associated traceability data) is
too large to publish directly in transaction metadata.

The “anchor” format publishes a verifiable commitment (hash) plus a pointer to
where the full record can be retrieved.

### JSON-like Representation (for clarity)

```json 
{
  "163532014": {
    "standard": "gs1",
    "schema_version": "1.0.0",
    "gs1_release": "24.0",
    "payload": {
      "type": "anchor",
      "hash_alg": "blake2b-256",
      "hash_hex": "d34db33fd34db33fd34db33fd34db33fd34db33fd34db33fd34db33fd34db33f",
      "uri": "ipfs://CID_GOES_HERE",
      "content_type": "application/cbor"
    }
  }
}
```

### Notes

The hash MUST be computed over the canonical/deterministic CBOR encoding of the
anchored payload (see [GS1.md](GS1.md) canonical encoding rules).

The URI field is intentionally flexible. Implementations may use IPFS, HTTP(S),
Arweave, or any other retrieval layer, so long as the hash remains verifiable.

## Guidance on Choosing Full vs Anchor Publishing

As a general rule:

- Use **Full Payload** when:
    - the payload is small and identity-centric
    - the intent is to publish a compact, self-contained record
- Use Anchor when:
    - the payload is large (event histories, documents, certificates, DPP data)
    - the payload evolves frequently
    - the publisher wants a predictable on-chain footprint

This specification standardizes the structure and encoding rules so that either
approach remains interoperable.

## Compatibility Considerations

Version fields exist to ensure payloads remain interpretable over time.

Consumers SHOULD:

- read and interpret `schema_version` to determine decoding expectations
- read and interpret `gs1_release` as the GS1 reference baseline
- treat unknown additional envelope fields as ignorable unless required by a
  particular `schema_version`