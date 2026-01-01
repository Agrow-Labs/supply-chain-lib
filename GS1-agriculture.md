# GS1 Agricultural Product Example

This example demonstrates how GS1 identifiers and application identifiers may be
used to represent agricultural supply-chain data in a form suitable for
interoperable storage and exchange across systems, including Cardano-based
blockchains.

A basic example of an agriculture product using the GS1 standards would include
a GTIN (Global Trade Item Number) as well as a Batch or Lot Number, Expiration
date, and a quantity.

The examples below record a crate of apples harvested at a farm.

---

## Scenario Description

This scenario represents a simple traceability event where a harvested product
is packaged into a container and prepared for downstream distribution. The goal
is to demonstrate how commonly used GS1 fields can be expressed in a consistent,
machine-readable form that can be encoded into CBOR, stored on-chain as a datum
or referenced from off-chain storage, and exchanged between independent
participants.

---

## GS1 Fields Used

| Field | Label            | Value          |
|-------|------------------|----------------|
| 01    | GTIN             | 12341234567893 |
| 10    | BATCH/LOT        | ABC12345       |
| 17    | USE BY OR EXPIRY | 241122         |
| 30    | VAR. COUNT       | 50             |

---

## GS1 Data Matrix

```
(01)12341234567893(10)ABC12345(17)241231(30)50
```

---

## JSON Representation

```json
{
  "01": "12341234567893",
  "10": "ABC12345",
  "17": "241122",
  "30": "50"
}
```

---

## CBOR Representation (Conceptual)

```cbor 
{
  01: "12341234567893",
  10: "ABC12345",
  17: "241122",
  30: "50"
}
```

> Note: The CBOR form shown here is conceptual. The concrete binary encoding
> follows directly from the defined CDDL schema and the chosen CBOR encoder.

--- 

## Canonical CBOR Encoding (Deterministic)

This specification requires deterministic, definite-length CBOR encoding. The
following hex string represents the canonical on-chain encoding of the above
structure:

### Conceptual CBOR

```
{
  01: "12341234567893",
  10: "ABC12345",
  17: "241122",
  30: "50"
}
```

#### Step 1 - Deterministic CBOR Structure

Sorted numeric keys: `1, 10, 17, 30`

Definite map of four entries → major type 5, length 4 → `a4`

Encoding each field:

| Field            | CBOR Encoding                                      |
|------------------|----------------------------------------------------|
| 1                | `01`                                               |
| "12341234567893" | text length 14 → `6e 3132333431323334353637383933` |
| 10               | `0a`                                               |
| "ABC12345"       | length 8 → `68 4142433132333435`                   |
| 17               | `11`                                               |
| "241122"         | length 6 → `66 323431313232`                       |
| 30               | `18 1e`                                            |
| "50"             | length 2 → `62 3530`                               |

#### Step 2 — Final CBOR Bytes

```hex 
a4
01 6e 3132333431323334353637383933
0a 68 4142433132333435
11 66 323431313232
18 1e 62 3530
```

#### Step 3 — Final CBOR Hex String

```
a4016e31323334313233343536373839330a6841424331323334351166323431313232181e623530
```

This encoding uses:

- definite-length map and strings
- sorted integer keys
- minimal-width integer encodings
- no semantic tags

---

## Human-Readable Display

```
GTIN: 12341234567893
BATCH/LOT: ABC12345
USE BY OR EXPIRY: 2024-11-22
VAR. COUNT: 50
```

---

## Interoperability Notes

This example is intentionally minimal and focuses on identifiers that are
already widely used in existing agricultural and logistics systems. The same
structure can be exchanged between blockchain-based and non-blockchain systems
without requiring those systems to adopt any particular platform or protocol, so
long as the GS1 identifiers themselves remain the shared reference model.

Storage strategy (on-chain datum vs. off-chain record with on-chain reference)
is implementation-dependent and driven by payload size, update frequency, and
application requirements.