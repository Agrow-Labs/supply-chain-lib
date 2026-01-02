# Interoperability & Off-Chain Interaction Model

This document defines the interoperability model and interaction patterns
between on-chain GS1 metadata published under this specification and the
broader ecosystem of off-chain actors and systems.

The goal is to enable consistent, low-friction adoption of the standard across
enterprise systems, logistics infrastructure, oracle providers, and
decentralized applications while preserving strong cryptographic integrity and
long-term data portability.

This document does not prescribe specific vendor tooling or implementation
technologies. Instead, it defines **roles, responsibilities, and data flows**
that implementations SHOULD follow.

---

## Design Principles

This interoperability model is guided by the following principles:

- **Protocol neutrality:** the specification does not privilege any particular
  ERP vendor, cloud provider, oracle network, or storage system.
- **Cryptographic verifiability:** all on-chain commitments must remain
  independently verifiable regardless of off-chain infrastructure choices.
- **Incremental adoption:** participants MAY adopt the standard at different
  layers (identity only, anchoring only, full lifecycle integration).
- **Composable trust:** no single off-chain actor is assumed to be universally
  trusted.

---

## Actor Roles

Implementations typically involve the following roles.

### On-Chain Roles

**Publisher**  
The entity that constructs GS1 payloads and publishes them on-chain.

**Validator / Smart Contract**  
On-chain logic that may validate identity, continuity, or anchoring rules.

**Indexer / Consumer**  
Entities that observe on-chain state and interpret GS1 records for downstream
applications, analytics, compliance, or user interfaces.

### Off-Chain Roles

**Producer**  
Creates or originates physical goods and initial GS1 identity data.

**Logistics / Transporter**  
Generates custody, movement, and condition events.

**Inspector / Certifier**  
Produces attestations, certifications, and audit records.

**ERP System**  
Maintains enterprise master data and business workflows.

**IoT / Telemetry Source**  
Produces high-frequency sensor data (temperature, humidity, GPS, etc.).

**Oracle Provider**  
Aggregates, signs, and publishes verified statements or commitments to on-chain
consumers.

**Data Availability Provider**  
Stores off-chain records and makes them retrievable via stable identifiers.

**Regulator / Auditor**  
Consumes historical data for compliance, reporting, and enforcement.

---

## Trust & Responsibility Boundaries

This specification enforces the following boundaries:

- On-chain state establishes **authoritative commitments**.
- Off-chain systems are responsible for **data production, storage, and
  retrieval**.
- Verification of integrity occurs by comparing off-chain records against
  their on-chain anchors.

No off-chain actor is required to be trusted beyond its ability to provide
records whose hashes match the on-chain commitments.

---

## Lifecycle Overview

A typical GS1 data lifecycle proceeds as follows:

1. **Identity Establishment**  
   GS1 identity core is published on-chain (inline datum or metadata).

2. **Event Generation**  
   Logistics, ERP, IoT, and inspection systems produce off-chain records.

3. **Record Assembly**  
   Events and documents are assembled into a canonical off-chain record.

4. **Anchoring**  
   The canonical off-chain record is hashed and anchored on-chain.

5. **Discovery & Verification**  
   Consumers retrieve the off-chain record and verify integrity using the
   on-chain anchor.

This lifecycle is compatible with both permissioned and permissionless
environments.

---

## Interaction Models

### Minimal Adoption Model

Participants publish only GS1 identity on-chain.

Off-chain systems operate independently.

This model enables early adoption with minimal operational change.

### Anchor-Based Model

Participants publish identity on-chain and anchor evolving off-chain records.

This is the recommended production model.

### Validator-Enforced Model

Smart contracts enforce continuity and anchoring constraints on-chain.

This model is appropriate for high-assurance or regulated environments.

---

## Interoperability Guarantees

Implementations that follow this specification obtain the following guarantees:

- Long-term interpretability of GS1 records
- Vendor-neutral data portability
- Cryptographically verifiable audit trails
- Safe incremental adoption across heterogeneous systems

---

## Summary

This interoperability model allows diverse off-chain systems to cooperate
without central coordination while preserving a single verifiable on-chain
source of truth.

It enables GS1 metadata to function as a durable public coordination layer for
supply-chain systems on Cardano.
