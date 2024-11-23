# GS1 Logistics Product Example

Building on the earlier [Agricultural Product Example](./GS1-agriculture.md), in
this example we will ship our crate of apples from one location (the farm)
to another (the cider mill).

This example highlights several key GS1 components used for the purposes of
tracking and tracing both the source product but also its movements throughout
the supply chain.

* the GTIN (01) defines the type of product being moved
* the GLN (413/414) is used to identify both the origin and destination location
* SSCC (00) is the shipment identifier and tracks the shipment container (pallet
  or crate)

## GS1 Fields Used

| Field | Label        | Value              |
|-------|--------------|--------------------|
| 01    | GTIN         | 12341234567893     |
| 414   | LOC No.      | 9876543210987      |
| 413   | SHIP FOR LOC | 1234567890123      |
| 00    | SSCC         | 003456789012345678 |
| 10    | BATCH/LOT    | ABC12345           |

## GS1 Data Matrix

```
(01)12341234567893(414)9876543210987(413)1234567890123(00)003456789012345678(10)ABC12345
```

## JSON

```json 
{
  "00": "003456789012345678",
  "01": "12341234567893",
  "10": "ABC12345",
  "413": "1234567890123",
  "414": "9876543210987"
}
```

## CBOR

```cbor 
{
  00: "003456789012345678",
  01: "12341234567893",
  10: "ABC12345",
  413: "1234567890123",
  414: "9876543210987"
}
```

## Display

```
SSCC: 003456789012345678
GTIN: 12341234567893
BATCH/LOT: ABC12345
SHIP FOR LOC: 1234567890123
LOC No.: 9876543210987
```