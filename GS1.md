# GS1 General Standards for Cardano Based Blockchains

[![CC BY 4.0][cc-by-shield]][cc-by]

This specification attempts to define a data structure for representing GS1-compatible
data on a Cardano-based blockchain network through either metadata or datums.

This specification is based on
the [GS1 General Specifications, Release 24.0](https://ref.gs1.org/standards/genspecs/) which were
released in January 2024 and are the most recent as of this writing.

## A Tale of Two Datas

When it comes to data availability and interoperability there are two facets to consider:

* Consumer-facing Product Data
* Supply Chain-facing Product Data

### Consumer-Facing Product Data

One of the principle benefits of using blockchain for recording and tracking supply chain data is
the ability to efficiently provide product lifecycle information to end consumers in ways that were
never available before.

While the standards currently being documented in this repository focus primarily on supply-chain
facing information for interoperability, it's important to take a moment to take note of the amazing
and thorough GS1 JSON-LD Schema [Available at [https://www.gs1.org/voc/](https://www.gs1.org/voc/)]
which provides a plethora of consumer-facing information.

Standards and best practices around incorporating and providing this information both on-chain and
to end consumers as part of a supply chain application will be a stretch goal for this repository.

### Supply Chain-Facing Product Data

The reason that GS1 Standards have been the global standard for supply chains for the past ~50 years
is because they are great at breaking down the barriers of international trade through thorough and
useful standards for interoperability between various systems and facets of the supply and logistics
chains for commerce.

The standards defined here will initially focus on the General Specifications and some of the more
specific standards to target unique industries.

## Limitations

There will be, throughout the course of this integration, certain limitations or criteria that are
imposed by one standard or another. The most-restrictive standard shall be used in order to
maximize compatibility with going both on-chain and off-chain and to or from other GS1-compatible
systems.

### Acceptable Characters

#### (GS1 Encodable Character Set 82)

The GS1 Encodable Character Set 82 is defined in **Figure 7.11-1** of the GS1 General Specification
v24.0

GS1 defines a subset of ISO 646 that consists of a total of 82 characters:

* Capital and lowercase alphabetic non-accented characters: `A-Z or a-z`
* Numeric digits: `0 1 2 3 4 5 6 7 8 9`
* Special Characters: `! " % & ' ( ) * + , - . / _ : ; > = < ?`

| Symbol | Name              | Symbol | Name             | Symbol | Name             |
|--------|-------------------|--------|------------------|--------|------------------|
| !      | Exclamation Mark  | "      | Quotation Mark   | %      | Percent Sign     |
| &      | Ampersand         | '      | Apostrophe       | (      | Open Parenthesis |
| )      | Close Parenthesis | *      | Asterisk         | +      | Plus Sign        |
| ,      | Comma             | -      | Dash             | .      | Period           |
| /      | Forward Slash     | _      | Underscore       | :      | Colon            |
| ;      | Semicolon         | \>     | Greater Than     | =      | Equal Sign       |
| <      | Less Than         | ?      | Question Mark    | A      | Capital Letter A |
| B      | Capital Letter B  | C      | Capital Letter C | D      | Capital Letter D |
| E      | Capital Letter E  | F      | Capital Letter F | G      | Capital Letter G |
| H      | Capital Letter H  | I      | Capital Letter I | J      | Capital Letter J |
| K      | Capital Letter K  | L      | Capital Letter L | M      | Capital Letter M |
| N      | Capital Letter N  | O      | Capital Letter O | P      | Capital Letter P |
| Q      | Capital Letter Q  | R      | Capital Letter R | S      | Capital Letter S |
| T      | Capital Letter T  | U      | Capital Letter U | V      | Capital Letter V |
| W      | Capital Letter W  | X      | Capital Letter X | Y      | Capital Letter Y |
| Z      | Capital Letter Z  | 0      | Digit Zero       | 1      | Digit One        |
| 2      | Digit Two         | 3      | Digit Three      | 4      | Digit Four       |
| 5      | Digit Five        | 6      | Digit Six        | 7      | Digit Seven      |
| 8      | Digit Eight       | 9      | Digit Nine       | a      | Small Letter a   |
| b      | Small Letter b    | c      | Small Letter c   | d      | Small Letter d   |
| e      | Small Letter e    | f      | Small Letter f   | g      | Small Letter g   |
| h      | Small Letter h    | i      | Small Letter i   | j      | Small Letter j   |
| k      | Small Letter k    | l      | Small Letter l   | m      | Small Letter m   |
| n      | Small Letter n    | o      | Small Letter o   | p      | Small Letter p   |
| q      | Small Letter q    | r      | Small Letter r   | s      | Small Letter s   |
| t      | Small Letter t    | u      | Small Letter u   | v      | Small Letter v   |
| w      | Small Letter w    | x      | Small Letter x   | y      | Small Letter y   |
| z      | Small Letter z    |        |                  |        |                  |

**Regular Expression Pattern**

```regexp
[A-Za-z0-9)><(=!&,.;\"'*_?%+:\/-]+
```

**CBOR CDDL Definition**

```cddl
gs1-ec82 = tstr .regexp "[A-Za-z0-9)><(=!&,.;\"'*_?%+:\/-]+"
```

#### (GS1 Encodable Character Set 39)

The GS1 Encodable Character Set 39 is define in **Figure 7.11-2** Of the GS1 General Specification
v24.0

GS1 defines a subset of ISO 646 that consists of a total of 39 characters:

* Capital alphabetic non-accented characters: `A-Z`
* Numeric digits: `0 1 2 3 4 5 6 7 8 9`
* Special Characters: `# - /`

| Symbol | Name             | Symbol | Name             | Symbol | Name                  |
|--------|------------------|--------|------------------|--------|-----------------------|
| #      | Number Sign      | -      | Hyphen/Minus     | \/     | Forward Slash/Solidus |
| A      | Capital Letter A | B      | Capital Letter B | C      | Capital Letter C      |
| D      | Capital Letter D | E      | Capital Letter E | F      | Capital Letter F      |
| G      | Capital Letter G | H      | Capital Letter H | I      | Capital Letter I      |
| J      | Capital Letter J | K      | Capital Letter K | L      | Capital Letter L      |
| M      | Capital Letter M | N      | Capital Letter N | O      | Capital Letter O      |
| P      | Capital Letter P | Q      | Capital Letter Q | R      | Capital Letter R      |
| S      | Capital Letter S | T      | Capital Letter T | U      | Capital Letter U      |
| V      | Capital Letter V | W      | Capital Letter W | X      | Capital Letter X      |
| Y      | Capital Letter Y | Z      | Capital Letter Z | 0      | Digit Zero            |
| 1      | Digit One        | 2      | Digit Two        | 3      | Digit Three           |
| 4      | Digit Four       | 5      | Digit Five       | 6      | Digit Six             |
| 7      | Digit Seven      | 8      | Digit Eight      | 9      | Digit Nine            |

** Regular Expression Pattern**

```regexp 
[A-Z0-9#\/-]+
```

**CBOR CDDL Definition**

```cddl
gs1-ec39 = tstr .regexp "[A-Z0-9#\/-]+"
```

### Date Formats

#### Dates

Dates in GS1 must be specified as 6-character strings in the format of YYMMDD. Each field MUST be
zero-padded. If a particular day of the month is not applicable the date should be specified as `00`
and should be assumed to represent the last day of the month specified including
adjustment for leap years.

```
YYMMDD

YY = Tens and units of year (00 - 99, e.g., 2007 = 07)
MM = Zero-padded number of the month (e.g., January = 01)
DD = Number of the day of the month (e.g., second day = 02)
```

#### Date-Times

Fields that represent a date and time (date-time) should follow the same format as that for dates
but also include the hours and minutes as the last four digits (total of 10 digits). The hours and
minutes should be filled using a local 24-hour time (e.g., 2:30 a.m. = 0230, 2:30 p.m. = 1430). If
it is not necessary to specify a time, these fields MUST be filled with nines (e.g. 9999).

```
YYMMDDHHMM

YY = Tens and units of year (00 - 99, e.g., 2007 = 07)
MM = Zero-padded number of the month (e.g., January = 01)
DD = Number of the day of the month (e.g., second day = 02)
HH = Number of the hour on a 24-hour time (e.g. 2 p.m. = 14, 2 a.m. = 02)
MM = Number of the minute of the hour (00 - 59)
```

```
gs1-date = tstr .regexp "([0-9]{2})([0-9]{2})([0-9]{2})" .size 6

gs1-date-time tstr .regexp "([0-9]{2})([0-9]{2})([0-9]{2})([0-9]{2})([0-9]{2})" .size 10
```

### Application Identifiers (AI)

> **LEGEND + NOTES**
> * If an AI Key ends in `n` then `n` should be replaced with an integer from 0-6 implying the
    decimal position
> * If an AI Key ends in `s` then `s` refers to the sequence number and this entry allows for
    multiple occurences of the AI
> * Formats enclosed in square brackets `[]` are optional
> * Number formats with a fixed size (e.g. `uint .size 6`) must use a fixed length integer number
    padded with zeroes to the left of the number. Example: `123` becomes `000123`
> * Temperature entries are always expressed in hundredths of degrees and should have a trailing
    dash if negative. (e.g. `-98.6 F` == `009860-`)

| AI Key  | Content                                                              | Format `[] = Optional`                  | Title/Label                  | 
|---------|----------------------------------------------------------------------|-----------------------------------------|------------------------------|
| 00      | Logistic Unit ID (SSCC)                                              | uint .size 18                           | SSCC                         |
| 01      | Global Trade Item Number (GTIN)                                      | uint .size 14                           | GTIN                         |
| 02      | Trade item inside a logistic unit                                    | uint .size 14                           | CONTENT                      |
| 10      | Batch or Lot Number                                                  | gs1-ec82 .size (..20)                   | BATCH/LOT                    |
| 11      | Production Date                                                      | gs1-date                                | PROD DATE                    |
| 12      | Due Date (for payment)                                               | gs1-date                                | DUE DATE                     |
| 13      | Packaging Date                                                       | gs1-date                                | PACK DATE                    |
| 15      | Best Before Date                                                     | gs1-date                                | BEST BEFORE or BEST BY       |
| 16      | Sell by Date                                                         | gs1-date                                | SELL BY                      |
| 17      | Expiration Date                                                      | gs1-date                                | USE BY or EXPIRY             |
| 20      | Internal Product Variant                                             | uint .size 2                            | VARIANT                      | 
| 21      | Serial Number                                                        | gs1-ec82 .size (..20)                   | SERIAL                       | 
| 22      | Consumer Product Variant                                             | gs1-ec82 .size (..20)                   | CPV                          | 
| 235     | 3rd Party GTIN Extensions                                            | gs1-ec82 .size (..28)                   | TPX                          |
| 240     | Manufacturer Additional ID                                           | gs1-ec82 .size (..30)                   | ADDITIONAL ID                |
| 241     | Customer Part Number                                                 | gs1-ec82 .size (..30)                   | CUST. PART No.               |
| 242     | Made-to-Order Variation Number                                       | uint .size (..6)                        | MTO VARIANT                  |
| 243     | Packaging Component Number                                           | gs1-ec82 .size (..20)                   | PCN                          |
| 250     | Secondary Serial Number                                              | gs1-ec82 .size (..30)                   | SECONDARY SERIAL             |
| 251     | Reference to Source Entity                                           | gs1-ec82 .size (..30)                   | REF. TO SOURCE               |
| 253     | Global Document Type ID (GDTI)                                       | uint .size 13 [gs1-ec82 .size (..17)]   | GDTI                         |
| 254     | Global Location Number (GLN)                                         | gs1-ec82 .size (..20)                   | GLN EXTENSION COMPONENT      |
| 255     | Global Coupon Number (GCN)                                           | uint .size 13 [uint .size (..12)]       | GCN                          |
| 30      | Variable Count of Items                                              | uint .size (..8)                        | VAR. COUNT                   |
| 310n    | Net Weight, kilograms                                                | uint .size 6                            | NET WEIGHT (kg)              |
| 311n    | Length or first dimensions, metres                                   | uint .size 6                            | LENGTH (m)                   |
| 312n    | Width or second dimension, metres                                    | uint .size 6                            | WIDTH (m)                    |
| 313n    | Height or third dimension metres                                     | uint .size 6                            | HEIGHT (m)                   |
| 314n    | Area, square metres                                                  | uint .size 6                            | AREA (m<sup>2</sup>)         |
| 315n    | Net Volume, litres                                                   | uint .size 6                            | NET VOLUME (l)               |
| 316n    | Net Volume, cubic metres                                             | uint .size 6                            | NET VOLUME (m<sup>3</sup>)   |
| 320n    | Net Weight, pounds                                                   | uint .size 6                            | NET WEIGHT (lb)              |
| 321n    | Length or first dimension, inches                                    | uint .size 6                            | LENGTH (in)                  |
| 322n    | Length or first dimension, feet                                      | uint .size 6                            | LENGTH (ft)                  |
| 323n    | Length or first dimension, yards                                     | uint .size 6                            | LENGTH (yd)                  |
| 324n    | Width or second dimension, inches                                    | uint .size 6                            | WIDTH (in)                   |
| 325n    | Width or second dimension, feet                                      | uint .size 6                            | WIDTH (ft)                   |
| 326n    | Width or second dimension, yards                                     | uint .size 6                            | WIDTH (yd)                   |
| 327n    | Height or third dimension, inches                                    | uint .size 6                            | HEIGHT (in)                  |
| 328n    | Height or third dimension, feet                                      | uint .size 6                            | HEIGHT (ft)                  |
| 329n    | Height or third dimension, yards                                     | uint .size 6                            | HEIGHT (yd)                  |
| 330n    | Logistic Weight, kilograms                                           | uint .size 6                            | GROSS WEIGHT (kg)            |
| 331n    | Logistic Length or first dimension, metres                           | uint .size 6                            | LENGTH (m), log              |
| 332n    | Logistic Width or second dimension, metres                           | uint .size 6                            | WIDTH (m), log               |
| 333n    | Logistic Height or third dimension, metres                           | uint .size 6                            | HEIGHT (m), log              |
| 334n    | Logistic Area, square metres                                         | uint .size 6                            | AREA (m<sup>2</sup>), log    |
| 335n    | Logistic Volume, litres                                              | uint .size 6                            | VOLUME (l), log              |
| 336n    | Logistic Volume, cubic metres                                        | uint .size 6                            | VOLUME (m<sup>3</sup>), log  |
| 337n    | Kilograms per square metre                                           | uint .size 6                            | KG PER m<sup>2</sup>         |
| 340n    | Logistic Weight, pounds                                              | uint .size 6                            | GROSS WEIGHT (lb)            |
| 341n    | Logistic Length or first dimension, inches                           | uint .size 6                            | LENGTH (in), log             |
| 342n    | Logistic Length or first dimension, feet                             | uint .size 6                            | LENGTH (ft), log             |
| 343n    | Logistic Length or first dimension, yards                            | uint .size 6                            | LENGTH (yd), log             |
| 344n    | Logistic Width or second dimension, inches                           | uint .size 6                            | WIDTH (in), log              |
| 345n    | Logistic Width or second dimension, feet                             | uint .size 6                            | WIDTH (ft), log              |
| 346n    | Logistic Width or second dimension, yards                            | uint .size 6                            | WIDTH (yd), log              |
| 347n    | Logistic Height or third dimension, inches                           | uint .size 6                            | HEIGHT (in), log             |
| 348n    | Logistic Height or third dimension, feet                             | uint .size 6                            | HEIGHT (ft), log             |
| 349n    | Logistic Height or third dimension, yards                            | uint .size 6                            | HEIGHT (yd), log             |
| 350n    | Area, square inches                                                  | uint .size 6                            | AREA (in<sup>2</sup>)        |
| 351n    | Area, square feet                                                    | uint .size 6                            | AREA (ft<sup>2</sup>)        |
| 352n    | Area, square yards                                                   | uint .size 6                            | AREA (yd<sup>2</sup>)        |
| 353n    | Logistic Area, square inches                                         | uint .size 6                            | AREA (in<sup>2</sup>), log   |
| 354n    | Logistic Area, square feet                                           | uint .size 6                            | AREA (ft<sup>2</sup>), log   |
| 355n    | Logistic Area, square yards                                          | uint .size 6                            | AREA (yd<sup>2</sup>), log   |
| 356n    | Net Weight, troy ounces                                              | uint .size 6                            | NET WEIGHT (t)               |
| 357n    | Net Weight (or volume), ounces                                       | uint .size 6                            | NET VOLUME (oz)              |
| 360n    | Net Voluem, quarts                                                   | uint .size 6                            | NET VOLUME (q)               |
| 361n    | Net Volume, gallons U.S.                                             | uint .size 6                            | NET VOLUME (g)               |
| 362n    | Logistic Volume, quarts                                              | uint .size 6                            | VOLUME (q), log              |
| 363n    | Logistic Volume, gallons U.S.                                        | uint .size 6                            | VOLUME (g), log              |
| 364n    | Net Volume, cubic inches                                             | uint .size 6                            | VOLUME (in<sup>3</sup>)      |
| 365n    | Net Volume, cubic feet                                               | uint .size 6                            | VOLUME (ft<sup>3</sup>)      |
| 366n    | Net Volume, cubic yards                                              | uint .size 6                            | VOLUME (yd<sup>3</sup>)      |
| 367n    | Logistic Volume, cubic inches                                        | uint .size 6                            | VOLUME (in<sup>3</sup>), log |
| 368n    | Logistic Volume, cubic feet                                          | uint .size 6                            | VOLUME (ft<sup>3</sup>), log |
| 369n    | Logistic Volume, cubic yards                                         | uint .size 6                            | VOLUME (yd<sup>3</sup>), log |
| 37      | Count of trade items or trade item pieces                            | uint .size (..8)                        | COUNT                        |
| 390n    | Amount payable or coupon value (single currency)                     | uint .size (..15)                       | AMOUNT                       |
| 391n    | Amount payable and ISO currency code                                 | uint .size 3 + uint .size (..15)        | AMOUNT                       |
| 392n    | Amount payable for item (single currency)                            | uint .size (..15)                       | PRICE                        |
| 393n    | Amount payable for item and ISO currency code                        | uint .size 3 + uint .size (..15)        | PRICE                        |
| 394n    | Percentage discount of a coupon                                      | uint .size 4                            | PRCNT OFF                    |
| 395n    | Amount payable per unit of measure (single currency)                 | uint .size 6                            | PRICE/UoM                    |
| 400     | Customer's Purchase Order (PO) Number                                | gs1-ec82 .size (..30)                   | ORDER NUMBER                 |
| 401     | Global Identification Number for Consignment (GINC)                  | gs1-ec82 .size (..30)                   | GINC                         |
| 402     | Global Shipment Identification Number (GSIN)                         | uint .size 17                           | GSIN                         |
| 403     | Routing Code                                                         | gs1-ec82 .size (..30)                   | ROUTE                        |
| 410     | Ship To - Deliver To Global Location Number (GLN)                    | uint .size 13                           | SHIP TO LOC                  |
| 411     | Bill To - Invoice To Global Location Number (GLN)                    | uint .size 13                           | BILL TO                      |
| 412     | Purchased from Global Location Number (GLN)                          | uint .size 13                           | PURCHASE FROM                |
| 413     | Ship For - Deliver For - Forward To Global Location Number (GLN)     | uint .size 13                           | SHIP FOR LOC                 |
| 414     | Identification of a Physical Location - Global Location Number (GLN) | uint .size 13                           | LOC No.                      |
| 415     | Global Location Number (GLN) of the invoicing party                  | uint .size 13                           | PAY TO                       |
| 416     | Global Location Number (GLN) of the production or service location   | uint .size 13                           | PROD/SERV LOC                |
| 417     | Party Global Location Number (GLN)                                   | uint .size 13                           | PARTY                        |
| 420     | Ship To - Deliver To Postal Code with Single Postal Authority        | gs1-ec82 .size (..20)                   | SHIP TO POST                 |
| 421     | Ship To - Deliver To Postal Code with ISO Country Code               | uint .size 3 + gs1-ec82 .size (..9)     | SHIP TO POST                 |
| 422     | Country of Origin of a Trade Item (ISO)                              | uint .size 3                            | ORIGIN                       |
| 423     | Country of Initial Processing                                        | uint .size 3 + uint .size (..12)        | COUNTRY - INITIAL PROCESS    |
| 424     | Country of Processing                                                | uint .size 3                            | COUNTRY - PROCESS            |
| 425     | Country of Disassembly                                               | uint .size 3 + uint .size (..12)        | COUNTRY - DISASSEMBLY        |
| 426     | Country Covering Full Process Chain                                  | uint .size 3                            | COUNTRY - FULL PROCESS       |
| 427     | Country subdivision of origin code for a trade item                  | gs1-ec82 .size (..3)                    | ORIGIN SUBDIVISION           |
| 4300    | Ship To / Deliver To Company Name                                    | gs1-ec82 .size (..35)                   | SHIP TO COMP                 |
| 4301    | Ship to / Deliver To Contact Name                                    | gs1-ec82 .size (..35)                   | SHIP TO NAME                 |
| 4302    | Ship To / Deliver To Address Line 1                                  | gs1-ec82 .size (..64)                   | SHIP TO ADD1                 |
| 4303    | Ship To / Deliver To Address Line 2                                  | gs1-ec82 .size (..64)                   | SHIP TO ADD2                 |
| 4304    | Ship To / Deliver To Suburb                                          | gs1-ec82 .size (..64)                   | SHIP TO SUB                  |
| 4305    | Ship To / Deliver To Locality                                        | gs1-ec82 .size (..64)                   | SHIP TO LOC                  |
| 4306    | Ship To / Deliver To Region                                          | gs1-ec82 .size (..64)                   | SHIP TO REG                  |
| 4307    | Ship To / Deliver To Country Code                                    | gs1-ec82 .size 2                        | SHIP TO COUNTRY              |
| 4308    | Ship To / Deliver To Telephone Number                                | gs1-ec82 .size (..30)                   | SHIP TO PHONE                |
| 4309    | Ship To / Deliver To GEO Location                                    | uint .size 20                           | SHIP TO GEO                  |
| 4310    | Return To Company Name                                               | gs1-ec82 .size (..35)                   | RTN TO COMP                  |
| 4311    | Return To Contact Name                                               | gs1-ec82 .size (..35)                   | RTN TO NAME                  |
| 4312    | Return To Address Line 1                                             | gs1-ec82 .size (..64)                   | RTN TO ADD1                  |
| 4313    | Return To Address Line 2                                             | gs1-ec82 .size (..64)                   | RTN TO ADD2                  |
| 4314    | Return To Suburb                                                     | gs1-ec82 .size (..64)                   | RTN TO SUB                   |
| 4315    | Return To Locality                                                   | gs1-ec82 .size (..64)                   | RTN TO LOC                   |
| 4316    | Return To Region                                                     | gs1-ec82 .size (..64)                   | RTN TO REG                   |
| 4317    | Return To Country Code                                               | gs1-ec82 .size 2                        | RTN TO COUNTRY               |
| 4318    | Return To Telephone Number                                           | gs1-ec82 .size (..30)                   | RTN TO PHONE                 |
| 4319    | Return To GEO Location                                               | uint .size 20                           | RTN TO GEO                   |
| 4320    | Service Code Description                                             | gs1-ec82 .size (..35)                   | SRV DESCRIPTION              |
| 4321    | Dangerous Goods Flag                                                 | uint .size 1                            | DANGEROUS GOODS              |
| 4322    | Authority to Leave Flag                                              | uint .size 1                            | AUTH LEAVE                   |
| 4323    | Signature Required Flag                                              | uint .size 1                            | SIG REQUIRED                 |
| 4324    | Not Before Delivery Date/Time                                        | uint .size 10                           | NBEF DEL DT                  |
| 4325    | Not After Delivery Date/Time                                         | uint .size 10                           | NAFT DEL DT                  |
| 4326    | Release Date                                                         | gs1-date                                | REL DATE                     |
| 4330    | Maximum Temperature in Fahrenheit                                    | uint .size 6 + [ - ]                    | MAX TEMP F                   |
| 4331    | Maximum Temperature in Celsius                                       | uint .size 6 + [ - ]                    | MAX TEMP C                   |
| 4332    | Minimum Temperature in Fahrenheit                                    | uint .size 6 + [ - ]                    | MIN TEMP F                   |
| 4333    | Minimum Temperature in Celsius                                       | uint .size 6 + [ - ]                    | MIN TEMP C                   |
| 7001    | NATO Stock Number (NSN)                                              | uint .size 13                           | NSN                          |
| 7002    | UNECE Meat Carcasses and Cuts Classification                         | gs1-ec82 .size (..30)                   | MEAT CUT                     |
| 7003    | Expiration Date and Time                                             | gs1-date-time                           | EXPIRY TIME                  |
| 7004    | Active Potency                                                       | uint .size (..4)                        | ACTIVE POTENCY               |
| 7005    | Catch Area                                                           | gs1-ec82 .size (..12)                   | CATCH AREA                   |
| 7006    | First Freeze Date                                                    | gs1-date                                | FIRST FREEZE DATE            |
| 7007    | Harvest Date                                                         | gs1-date + [gs1-date]                   | HARVEST DATE                 |
| 7008    | Species for Fishery Purposes                                         | gs1-ec82 .size (..3)                    | AQUATIC SPECIES              |
| 7009    | Fishing Gear Type                                                    | gs1-ec82 .size (..10)                   | FISHING GEAR TYPE            |
| 7010    | Production Method                                                    | gs1-ec82 .size (..2)                    | PROD METHOD                  |
| 7011    | Test By Date                                                         | gs1-date + [uint .size 4]               | TEST BY DATE                 |
| 7020    | Refurbishment Lot ID                                                 | gs1-ec82 .size (..20)                   | REFURB LOT                   |
| 7021    | Functional Status                                                    | gs1-ec82 .size (..20)                   | FUNC STAT                    |
| 7022    | Revision Status                                                      | gs1-ec82 .size (..20)                   | REV STAT                     |
| 7023    | Global Individual Asset Identifier (GIAI) of an assembly             | gs1-ec82 .size (..30)                   | GIAI - ASSEMBLY              |
| 703s    | Number of Processor with ISO Country Code                            | uint .size 3 + gs1-ec82 .size (..27)    | PROCESSOR # s                |
| 7040    | GS1 UIC with Extension 1 and Importer Index                          | uint .size 1 + gs1-ec82 .size 3         | UIC + EXT                    |
| 723s    | Certification Reference                                              | gs1-ec82 .size (2..30)                  | CERT # s                     |
| 7240    | Protocol ID                                                          | gs1-ec82 .size (..20)                   | PROTOCOL                     |
| 7241    | AIDC Media Type                                                      | uint .size 2                            | AIDC MEDIA TYPE              |
| 7242    | Version Control Number (VCN)                                         | gs1-ec82 .size (..25)                   | VCN                          |
| 8001    | Roll Products: Width, Length, Core Diameter, Direction, Splices      | uint .size 14                           | DIMENSIONS                   |
| 8002    | Cellular Mobile Telephone Identifier                                 | gs1-ec82 .size (..20)                   | CMT No.                      |
| 8003    | Global Returnable Asset Identifier (GRAI)                            | uint .size 14 + [gs1-ec82 .size (..16)] | GRAI                         |
| 8004    | Global Individual Asset Identifier (GIAI)                            | gs1-ec82 .size (..30)                   | GIAI                         |
| 8005    | Price per unit of measure                                            | uint .size 6                            | PRICE PER UNIT               |
| 8006    | Identification of an Individual Trade Item Piece (ITIP)              | uint .size 18                           | ITIP                         |
| 8007    | International Bank Account Number (IBAN)                             | gs1-ec82 .size (..34)                   | IBAN                         |
| 8008    | Date and Time of Production                                          | gs1-date-time                           | PROD TIME                    |
| 8009    | Optically Readable Sensor Indicator                                  | gs1-ec82 .size (..50)                   | OPTSEN                       |
| 8010    | Component/Part Identifier (CPID)                                     | gs1-ec39 .size (..30)                   | CPID                         |
| 8011    | Component/Part Identifier Serial Number                              | uint .size (..12)                       | CPID SERIAL                  |
| 8012    | Software Version                                                     | gs1-ec82 .size (..20)                   | VERSION                      |
| 8013    | Global Model Number (GMN)                                            | gs1-ec82 .size (..25)                   | GMN                          |
| 8017    | Global Service Relation Number (GSRN) - Provider                     | uint .size 18                           | GSRN - PROVIDER              |
| 8018    | Global Service Relation Number (GSRN) - Recipient                    | uint .size 18                           | GSRN - RECIPIENT             |
| 8019    | Service Relation Instance Number (SRIN)                              | uint .size (..10)                       | SRIN                         |
| 8020    | Payment Slip Reference Number                                        | gs1-ec82 .size (..25)                   | REF No.                      |
| 8026    | Identification of a piece of a trade item (ITIP) inside logistics    | uint .size 18                           | ITIP CONTENT                 | 
| 8030    | Digital Signature (DigSig)                                           | **TBD**                                 | DIGSIG                       |
| 8110    | Loyalty Points of a Coupon                                           | uint .size 4                            | POINTS                       |
| 8112    | Positive Offer File Coupon Identification for North America          | gs1-ec82 .size (..64)                   | -                            |
| 8200    | Extended Packaging URL                                               | gs1-ec82 .size (..64)                   | PRODUCT URL                  |
| 90      | Information Mutually Agreed Between Trading Partners                 | gs1-ec82 .size (..30)                   | INTERNAL                     |
| 91 - 99 | Company Internal Information                                         | gs1-ec82 .size (..64)                   | INTERNAL                     |

## License

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/

[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png

[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg