# GS1 Agricultural Product Example

A basic example of an agriculture product utilizing the GS1 standards would
include a GTIN (Global Trade Item Number) as well as a Batch or Lot Number,
Expiration date, and a quantity.

The examples below, hypothetically could show the recording of a crate of apples
harvested at a farm.

## GS1 Fields Used

| Field | Label            | Value          |
|-------|------------------|----------------|
| 01    | GTIN             | 12341234567893 |
| 10    | BATCH/LOT        | ABC12345       |
| 17    | USE BY OR EXPIRY | 241122         |
| 30    | VAR. COUNT       | 50             |

## GS1 Data Matrix

```
(01)12341234567893(10)ABC12345(17)241231(30)50
```

## JSON

```json 
{
  "01": "12341234567893",
  "10": "ABC12345",
  "17": "241122",
  "30": "50"
}
```

## CBOR

```cbor 
{
    01: "12341234567893",
    10: "ABC12345",
    17: "241122",
    30: "50"
}
```

## Display

```
GTIN: 12341234567893
BATCH/LOT: ABC12345
USE BY OR EXPIRY: 2024-11-22
VAR. COUNT: 50
```