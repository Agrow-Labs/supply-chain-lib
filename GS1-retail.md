# GS1 Retail and Consumer Goods Example

Building on the earlier examples of our [Logistics Example](./GS1-logistics.md)
and our [Agricultural Product Example](./GS1-agriculture.md), in this example we
demonstrate the tracking of a reusable shipping crate that is used to transport
our apples.

By packaging our crate of apples in a reusable and uniquely identified shipping
crate, we can track the progress of the shipment throughout the supply chain.

* In the warehouse, the crate is scanned to ensure it is the correct asset.
* At the retail store, the crate is scanned to associate it with a specific
  shipment.
* After emptying the crate, it is returned to the supplier for reuse.

## Scenario Description

This scenario represents asset-level traceability within a retail environment,
where the same physical container (identified by a GIAI) is reused across
multiple shipments while maintaining linkage to the underlying product and its
batch identity.

## Details

* **Product:** Crate of apples
* **GTIN:** 12341234567893
* **Batch/Lot Number:** ABC12345
* **GLN of Store Location:** 9876543210987 (_Springfield Grocery Store_)
* **GIAI:** 12345678901234567890 (_Reusable Crate ID_)

## GS1 Fields Used

| Field | Label     | Value                |
|-------|-----------|----------------------|
| 01    | GTIN      | 12341234567893       |
| 414   | LOC No.   | 9876543210987        |
| 10    | BATCH/LOT | ABC12345             |
| 8004  | GIAI      | 12345678901234567890 |

## GS1 Data Matrix

```
(01)12341234567893(414)9876543210987(10)ABC12345(8004)12345678901234567890
```

## JSON Representation

```json
{
  "01": "12341234567893",
  "10": "ABC12345",
  "414": "9876543210987",
  "8004": "12345678901234567890"
}
```

## CBOR Representation (Conceptual)

```cbor
{
  01: "12341234567893",
  10: "ABC12345",
  414: "9876543210987",
  8004: "12345678901234567890"
}
```

## Canonical CBOR Encoding (Deterministic)

Using the canonical encoding rules defined in GS1.md, the above structure is
encoded using definite-length CBOR, sorted map keys, minimal integer widths, and
no semantic tags.

### Sorted Keys

```
1, 10, 414, 8004
```

### Canonical CBOR Bytes

```cbor
a4
01 6e 3132333431323334353637383933
0a 68 4142433132333435
19 019e 6d 39383736353433323130393837
19 1f44 6a 3132333435363738393031323334353637383930
```

### Hex Encoding (On-Chain Form)

```hex
a4016e31323334313233343536373839330a68414243313233343519019e6d39383736353433323130393837191f446a3132333435363738393031323334353637383930
```

## Human-Readable Display

```
GTIN: 12341234567893
BATCH/LOT: ABC12345
LOC No: 9876543210987
GIAI: 12345678901234567890
```

## Transaction Metadata Envelope (Recommended)

When publishing this example using Cardano transaction metadata, the GS1 payload
may be wrapped in the recommended publishing envelope (see
[METADATA.md](METADATA.md)) and published under the recommended metadata label
`163532014`.

```json
{
  "163532014": {
    "standard": "gs1",
    "schema_version": "1.0.0",
    "gs1_release": "24.0",
    "payload": {
      "01": "12341234567893",
      "10": "ABC12345",
      "414": "9876543210987",
      "8004": "12345678901234567890"
    }
  }
}
```

## Interoperability Notes

This example demonstrates how asset-level traceability can be achieved while
remaining interoperable across independent systems. The same structure may be
exchanged between blockchain-based and non-blockchain participants, with the
blockchain serving as a shared verification layer when appropriate.

As with the other examples, storage strategy (on-chain datum vs. off-chain
record with on-chain reference) is implementation-dependent and driven by
payload size, update frequency, and application requirements.