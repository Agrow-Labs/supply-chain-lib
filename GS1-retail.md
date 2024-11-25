# GS1 Retail and Consumer Goods Example

Building on the earlier examples of our [Logistics Example](./GS1-logistics.md)
and our [Agricultural Product Example](./GS1-agriculture.md), in this example we
demonstrate an example of tracking a reusable shipping crate that is used to
transport our apples.

By packaging our crate of apples in a reusable and uniquely identified shipping
crate we can track the progress of our crate of apples throughout the supply
chain.

* In the warehouse, the crate is scanned to ensure it is the correct asset.
* At the retail store, the crate is scanned to associate it with a specific
  shipment
* After emptying the crate, it is returned to the supplier for reuse

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

## JSON

```json
{
  "01": "12341234567893",
  "10": "ABC12345",
  "414": "9876543210987",
  "8004": "12345678901234567890"
}
```

##CBOR

```cbor
{
  01: "12341234567893",
  10: "ABC12345",
  414: "9876543210987",
  8004: "12345678901234567890"
}
```

## Display

```
GTIN: 12341234567893
BATCH/LOT: ABC12345
LOC No: 9876543210987
GIAI: 12345678901234567890
```