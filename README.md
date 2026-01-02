# Standardized Supply Chains Library

[![CC BY 4.0][cc-by-shield]][cc-by]

## Introduction

The purpose of developing this _"Standardized Supply Chain Library"_ is to
integrate globally recognized standards into the Cardano blockchain. This was
influenced not only by our commitment to fostering robust standards for supply
chain management but also by our strategic aim to directly align these standards
with defined project milestones.

Specifically, we focus on enhancing traceability for

* [agricultural products](#agricultural-products)
* [optimizing transportation and logistics](#transportation-and-logistics)
* and [retail and consumer goods standards](#retail-and-consumer-goods)

This will be done through the integration of **GS1** standards. GS1 is a global
non-profit organization that develops and maintains standards for business
communication, most notably the standards for barcodes used in retail supply
chains. These standards were selected for their global usability,
interoperability, and ability to promote transparent and efficient operations
across the supply chain.

### Specification-First Scope (What this Repository is Today)

This repository is intentionally **specification-first**.

The primary outputs of this work are:

* A CBOR-friendly structural mapping of GS1 identifiers and related fields
* A concrete CDDL schema for validation and interoperability
* Descriptive documentation that explains the mapping approach and design
  choices
* Example scenario documents that demonstrate how these identifiers can be
  applied

While it may be useful in the future to provide optional tooling (encoders,
decoders, validation helpers, reference implementations), this repository is
currently focused on defining and stabilizing the specification and examples so
that independent implementers can build interoperable solutions.

## Interoperability & Integration

This specification is intended to be usable across heterogeneous enterprise and
ecosystem environments. For interoperability guidance and ingestion workflows,
see:

- [INTEROPERABILITY.md](INTEROPERABILITY.md) — actor roles, trust boundaries,
  and interaction models
- [INGESTION-PATTERNS.md](INGESTION-PATTERNS.md) — standard ingestion workflows
  for ERP, IoT/logistics, and oracle/data availability services

## Metadata Compatibility & Publishing

Guidance for integrating GS1 metadata with existing Cardano token, NFT, and
metadata infrastructure, and for publishing GS1 records safely and
interoperably:

- [CARDANO-METADATA-COMPATIBILITY.md](CARDANO-METADATA-COMPATIBILITY.md)
- [PUBLISHING-PRACTICES.md](PUBLISHING-PRACTICES.md)


## Chosen Standards

The GS1 General Specifications Standard forms the backbone of our efforts,
providing the framework for the unique and universal identification of products,
services, and entities across various supply chains.

The complete description of the entire **GS1 General Standards** and their
mapping to CBOR/JSON fields and values can be found at: [GS1.md](GS1.md)

Here's how each component specifically supports our targeted milestones:

### Agricultural Products

#### Global Trade Item Number (GTIN)

Central to our traceability initiatives, **GTIN** facilitates the global
identification of agricultural products. This allows for inventory management,
recall execution, and overall product traceability across **agricultural supply
chains**, enabling stakeholders to trace product history from origin to
consumer.

##### Structure of a GTIN

A GTIN consists of:

* **GS1 Company Prefix:** Allocated by a GS1 Member Organization, identifies the
  company (length depends on the number of items the company needs to number).
* **Item Reference Number:** Assigned by the company to identify a specific
  product.
* **Check Digit:** A single digit used for error detection, calculated using the
  [Modulo 10 algorithm](https://en.wikipedia.org/wiki/Luhn_algorithm).

[Agriculture Product Example](GS1-agriculture.md)

### Transportation and Logistics

#### Global Location Number (GLN)

**GLN** is pivotal in optimizing **transportation and logistics** by identifying
physical locations and legal entities. This standard aids in streamlining
logistics operations and ensuring compliance with regulatory standards, thereby
improving the efficiency and transparency of transportation networks.

#### Structure of a GLN

A GLN consists of:

* **GS1 Company Prefix:** Allocated by a GS1 Member Organization, identifies the
  company (length depends on the number of items the company needs to number).
* **Location Reference:** Assigned by the company to identify a specific
  location within their system (e.g., a warehouse, department, or delivery dock)
* **Check Digit:** A single digit used for error detection, calculated using
  the [Modulo 10 algorithm](https://en.wikipedia.org/wiki/Luhn_algorithm).

[Logistics/Transportation Product Example](GS1-logistics.md)

### Retail and Consumer Goods

#### Global Individual Asset Identifier (GIAI)

For **retail and consumer goods**, **GIAI** supports the management of assets
beyond product tracking. It allows for the ability to track individual assets,
facilitating improved supply chain utilization, and overall asset management
within retail environments.

#### Structure of a GIAI

A GIAI consists of:

* **GS1 Company Prefix:** Allocated by a GS1 Member Organization, identifies the
  company (length depends on the number of items the company needs to number).
* A variable length string (letters or numbers) that is assigned by the company
  to uniquely identify the item in question.

[Retail and Consumer Goods Example](GS1-retail.md)

## Complementary Standards

Following the above standards, we feel it is imperative to create a foundation
to allow developers to create products and facilitate a way for forward-thinking
and future development. To build on these foundational standards, we employ the
following **GS1** standards within our focus areas:

#### GS1 Global Traceability Standard (GTS)

Provides a structured framework that complements GTIN by ensuring end-to-end
traceability of **agricultural products** from origin to the consumer, enhancing
safety, regulatory compliance, and consumer trust.

#### GS1's EPC Tag Data Standard (TDS)

Uses RAIN RFID technology in conjunction with the GLN to enhance the capture of
item-level information, thereby improving inventory management and global
product tracking within transportation and logistics.

## On-chain and Off-chain Considerations (Practical Note)

This specification defines the structure of the data, not the storage policy.

In practice:

* Smaller, identity-centric payloads may be stored directly as on-chain datums.
* Larger payloads (or payloads that evolve frequently) may be stored off-chain,
  with cryptographic references anchored on-chain (e.g., hashes, pointers, or
  other commitment mechanisms).
* Many real-world supply-chain systems will maintain the canonical record
  off-chain while using the blockchain as a shared verification layer.

The intent of standardizing a CBOR representation is that, regardless of storage
strategy, the encoded data remains consistent and interoperable.

## Interoperability and Non-Blockchain Participants

Supply chains are inherently multi-party. In real-world traceability systems,
not every party will use the same technology stack (or use a blockchain at all).

This work is grounded in GS1 identifiers so that:

* Parties who do interact with Cardano can encode and validate the same
  structures on-chain.
* Parties who do not use blockchains can still exchange GS1 identifiers and
  supply-chain metadata in a way that remains consistent with the on-chain
  representation.
* The "shared language" remains GS1, not a bespoke schema that only exists in
  one system.

## Potential Outcomes

### Benefits

1. **Enhanced Traceability and Transparency**: The adoption of GS1 standards,
   such as GTIN and GLN, will significantly improve the traceability and
   transparency of products through the Cardano blockchain. This could lead to
   better inventory management, more efficient recall processes, and enhanced
   consumer safety.
2. **Global Compatibility and Interoperability**: By integrating globally
   recognized standards, applications built on the Cardano blockchain will be
   compatible with existing international supply chain systems. This
   interoperability is crucial for ensuring that the Cardano blockchain can
   interact seamlessly with global partners, thereby increasing its adoption and
   utility.
3. **Regulatory Compliance and Consumer Trust**: Implementing GS1 standards aids
   in meeting various regulatory requirements across countries and industries.
   This compliance helps in building consumer trust, as the systems enable
   transparent verification of supply chain practices, improving the reputation
   of businesses using the Cardano blockchain.

### Challenges

1. **Technical and Operational Integration**: The integration of complex
   standards like those of GS1 into existing systems poses significant technical
   challenges. Ensuring that the Cardano blockchain can effectively communicate
   and operate with these standards without errors or inconsistencies will
   require significant development effort and expertise.
2. **Adoption by Stakeholders**: For the full benefits of GS1 standards
   integration to be realized, widespread adoption by all stakeholders in the
   supply chain is necessary. Convincing stakeholders to adopt new technologies
   and adapt to a blockchain-based system might be challenging due to varying
   levels of technology acceptance and readiness.

## Rationale for Integration

### Why GS1?

* **Neutral and Non-Profit**: GS1 is a neutral, not-for-profit international
  organization dedicated to developing and maintaining supply chain standards.
* **Global Reach and Influence**: It has over 116 member organizations and
  influences over 2 million companies across 25 diverse industries worldwide,
  facilitating operations in 150 countries.
* **Barcode Recognition**: GS1 barcodes are universally recognized, with more
  than one billion products using these barcodes, which are scanned more than 10
  billion times each day.
* **Partnership with ISO**: GS1 collaborates with the International Organization
  for Standardization (ISO) to contribute to the creation of globally recognized
  standards, enhancing interoperability and consistency across international
  borders.

The strategic integration of GS1 standards into the Cardano blockchain is guided
by several critical factors:

### Global Recognition and Adoption

By choosing standards that are widely recognized and adopted globally, we ensure
that applications developed on the Cardano blockchain are compatible with
existing supply chain systems worldwide. This compatibility is essential for
seamless interaction and integration with global supply chain operations, from
agricultural traceability to retail and consumer goods management.

### Increased Traceability and Efficiency

GS1 standards like GTIN and GTS provide robust standards for traceability and
efficiency. For agricultural products, this means being able to track the
journey of products from farm to table, ensuring safety and compliance at every
step. In transportation and logistics, the use of GLN and TDS enables more
efficient and transparent processes, improving logistics operations and delivery
accuracy.

### Regulatory Compliance and Consumer Trust

Implementing these standards not only supports compliance with various
regulatory requirements but also builds consumer trust by enabling transparent
and verifiable supply chain practices. In retail environments, the use of GIAI
for asset management ensures that consumer goods meet the highest standards of
quality and safety.

## Current Status and Next Steps

This repository is under active development and refinement as part of a funded
Project Catalyst initiative.

Near-term refinement work includes:

* Formalizing versioning and compatibility rules for GS1 updates
* Documenting practical sizing constraints for on-chain storage
* Defining interoperability and data ingestion patterns across ecosystems
* Aligning recommended practices with Cardano metadata distribution tooling
* Preparing the specification for stable release and wider adoption

## Closing Thoughts

The integration of GS1 standards into the Cardano blockchain allows for a
proactive and future-oriented approach. Adopting these globally recognized
standards lays a robust foundation that not only supports the current
development of powerful applications but also ensures their continued relevance
and interoperability within the global supply chain ecosystem.

This alignment with GS1 standards promises to elevate the Cardano blockchain's
capabilities in key areas:

* **Traceability for Agricultural Products**: Utilizing standards such as the
  Global Trade Item Number (GTIN), we enhance the traceability of agricultural
  products throughout the supply chain. This enables a more transparent path
  from farm to table, ensuring safety, compliance, and reliability in the
  agricultural sector.

* **Transportation and Logistics Standards**: With the integration of the Global
  Location Number (GLN), our initiatives improve the identification of physical
  locations and legal entities, which is essential for optimizing logistics
  operations. This leads to more streamlined transportation processes and
  enhances the efficiency and transparency of supply networks.

* **Retail and Consumer Goods Standards**: The adoption of the Global Individual
  Asset Identifier (GIAI) and other relevant GS1 standards facilitates better
  asset management and product tracking in retail environments. This improvement
  supports higher standards of quality and safety in consumer goods, meeting
  regulatory requirements and boosting consumer trust.

While these efforts promise significant improvements in operational efficiencies
and regulatory compliance, they also pose challenges, including the technical
integration of these standards and the need for widespread adoption among
stakeholders.

## References

* GS1 General Specifications Standard
  https://www.gs1.org/standards/barcodes-epcrfid-id-keys/gs1-general-specifications
* Global Trade Item Number (GTIN)
  https://www.gs1.org/standards/id-keys/gtin
* Global Location Number (GLN)
  https://www.gs1.org/standards/id-keys/gln
* Global Individual Asset Identifier (GIAI)
  https://www.gs1.org/standards/id-keys/global-individual-asset-identifier-giai
* GS1 Global Traceability Standard (GTS)
  https://www.gs1.org/standards/gs1-global-traceability-standard/current-standard#1-Introduction+1-1-Objective
* GS1's EPC Tag Data Standard (TDS)
  https://ref.gs1.org/standards/tds/
* GS1 ISO Standards
  https://www.gs1.org/docs/GS1-and-ISO-06BD.pdf
  https://www.iso.org/organization/10067.html
* GS1 Global Strategy
  https://www.gs1.org/docs/gs1-strategy-booklet.pdf

## License

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/

[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png

[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
