# GS1 Logistics Example

Building on the earlier [Agricultural Product Example](./GS1-agriculture.md), in
this example we will ship our crate of apples from one location (the farm)
to another (the cider mill).

This example highlights several key GS1 elements used for tracking and tracing
both the source product and its movements throughout the supply chain.

* the GTIN (01) defines the type of product being moved
* the GLN (413/414) is used to identify both the origin and destination location
* SSCC (00) is the shipment identifier and tracks the shipment container (pallet
  or crate)

---

## Scenario Description

A shipment is prepared at the farm and transferred to the cider mill. The
shipment is tracked as a distinct logistics unit while preserving its linkage to
the underlying agricultural product and its batch identity.

---

## GS1 Fields Used

| Field | Label        | Value              |
|-------|--------------|--------------------|
| 01    | GTIN         | 12341234567893     |
| 414   | LOC No.      | 9876543210987      |
| 413   | SHIP FOR LOC | 1234567890123      |
| 00    | SSCC         | 003456789012345678 |
| 10    | BATCH/LOT    | ABC12345           |

---

## GS1 Data Matrix

```
(01)12341234567893(414)9876543210987(413)1234567890123(00)003456789012345678(10)ABC12345
```

---

## JSON Representation

```json 
{
  "00": "003456789012345678",
  "01": "12341234567893",
  "10": "ABC12345",
  "413": "1234567890123",
  "414": "9876543210987"
}
```

---

## CBOR Representation (Conceptual)

```cbor 
{
  00: "003456789012345678",
  01: "12341234567893",
  10: "ABC12345",
  413: "1234567890123",
  414: "9876543210987"
}
```

---

## Canonical CBOR Encoding (Deterministic)

Using the canonical encoding rules defined in GS1.md, the above structure is
encoded using definite-length CBOR, sorted map keys, minimal integer widths, and
no semantic tags.

### Sorted Keys

``` 
0, 1, 10, 413, 414
```

### Canonical CBOR Bytes

```cbor 
a5
00 72 303033343536373839303132333435363738
01 6e 3132333431323334353637383933
0a 68 4142433132333435
19 019d 6d 31323334353637383930313233
19 019e 6d 39383736353433323130393837
```

### Hex Encoding (On-Chain Form)

```hex 
a50072303033343536373839303132333435363738016e31323334313233343536373839330a68414243313233343519019d6d3132333435363738393031323319019e6d39383736353433323130393837
```

---

## Human-Readable Display

```
SSCC: 003456789012345678
GTIN: 12341234567893
BATCH/LOT: ABC12345
SHIP FOR LOC: 1234567890123
LOC No.: 9876543210987
```

--- 

## Interoperability Notes

This example demonstrates how logistics events can be represented in a
consistent and verifiable form that remains interoperable across independent
systems. The same structure may be exchanged between blockchain-based and
non-blockchain participants, with the blockchain serving as a shared
verification layer when appropriate.

As with the agricultural example, storage strategy (on-chain datum vs. off-chain
record with on-chain reference) is implementation-dependent and driven by
payload size, update frequency, and application requirements.