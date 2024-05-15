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

### Acceptable Characters (GS1 Encodable Character Set 82)

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

### Date Formats

Dates in GS1 must be specified as 6-character strings in the format of YYMMDD. Each field MUST be
zero-padded. If a particular day of the month is not applicable the date should be specified as `00`
and should be assumed to represent the last day of the month specified including
adjustment for leap years.

```
gs1-date = tstr .regexp "([0-9]{2})([0-9]{2})([0-9]{2})"
```

### Application Identifiers (AI)

**Note:** A GS1 EC82 string shall be defined in the table below
as: `gs1ec82 = tstr .regexp "[A-Za-z0-9)(=!&,\/.;\<\>\"\'\*\-_\?%\+:]+"`

| AI   | Content                                                          | Format `[] = Optional`                 | Title/Label             | 
|------|------------------------------------------------------------------|----------------------------------------|-------------------------|
| 00   | Logistic Unit ID (SSCC)                                          | uint .size 18                          | SSCC                    |
| 01   | Global Trade Item Number (GTIN)                                  | uint .size 14                          | GTIN                    |
| 02   | Trade item inside a logistic unit                                | uint .size 14                          | CONTENT                 |
| 10   | Batch or Lot Number                                              | gs1-ec82 .size (..20)                  | BATCH/LOT               |
| 11   | Production Date                                                  | gs1-date                               | PROD DATE               |
| 12   | Due Date (for payment)                                           | gs1-date                               | DUE DATE                |
| 13   | Packaging Date                                                   | gs1-date                               | PACK DATE               |
| 15   | Best Before Date                                                 | gs1-date                               | BEST BEFORE or BEST BY  |
| 16   | Sell by Date                                                     | gs1-date                               | SELL BY                 |
| 17   | Expiration Date                                                  | gs1-date                               | USE BY or EXPIRY        |
| 20   | Internal Product Variant                                         | uint .size 2                           | VARIANT                 | 
| 21   | Serial Number                                                    | gs1-ec82 .size (..20)                  | SERIAL                  | 
| 22   | Consumer Product Variant                                         | gs1-ec82 .size (..20)                  | CPV                     | 
| 235  | 3rd Party GTIN Extensions                                        | gs1-ec82 .size (..28)                  | TPX                     |
| 240  | Manufacturer Additional ID                                       | gs1-ec82 .size (..30)                  | ADDITIONAL ID           |
| 241  | Customer Part Number                                             | gs1-ec82 .size (..30)                  | CUST. PART No.          |
| 242  | Made-to-Order Variation Number                                   | uint .size (..6)                       | MTO VARIANT             |
| 243  | Packaging Component Number                                       | gs1-ec82 .size (..20)                  | PCN                     |
| 250  | Secondary Serial Number                                          | gs1-ec82 .size (..30)                  | SECONDARY SERIAL        |
| 251  | Reference to Source Entity                                       | gs1-ec82 .size (..30)                  | REF. TO SOURCE          |
| 253  | Global Document Type ID (GDTI)                                   | uint .size 13 [+gs1-ec82 .size (..17)] | GDTI                    |
| 254  | Global Location Number (GLN)                                     | gs1-ec82 .size (..20)                  | GLN EXTENSION COMPONENT |
| 255  | Global Coupon Number (GCN)                                       | uint .size 13 [+uint .size (..12)]     | GCN                     |
| 30   | Variable Count of Items                                          | uint .size (..8)                       | VAR. COUNT              |
| 310n | Net weight, kilograms (variable measure trade item)              | uint .size 6                           | NET WEIGHT (kg)         |
| 311n | Length or first dimensions, metres (variable measure trade item) | uint .size 6                           | LENGTH (m)              |

## License

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/

[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png

[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg