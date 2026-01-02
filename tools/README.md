# Tooling: Sizing + Deterministic CBOR Test Helpers

This repository includes lightweight tooling to support:

- measuring representative CBOR sizes for GS1 payloads (datum plus metadata
  patterns)
- generating deterministic (canonical) CBOR hex for reproducible comparisons
- producing “golden vectors” for regression tests

These tools are intended to help implementers validate that their encoders
produce stable, canonical CBOR and to make informed storage decisions (inline
datum vs. metadata vs. anchor).

---

## Requirements

- Python 3.10+ (3.12 tested)
- `pip` for installing dependencies

Install the required dependency:

```bash
pip install cbor2
```

If you want to run tests:

```bash
pip install pytest cbor2
```

## Directory Layout

Typical structure:

```stylus
tools/
  __init__.py
  gs1_codec.py
  size_check.py
tests/
  conftest.py
  test_golden_vectors.py
```

## `tools/gs1_codec.py`

Shared helper functions used by both the CLI tooling and tests. This keeps the
logic in one place so that example generation, sizing checks, and golden-vector
tests all behave consistently.

Common helpers include:

- **Canonical encoding**
    - `encode_canonical_cbor(obj) -> bytes`
    - `to_hex(bytes) -> str`
    - `measure(obj) -> (size_bytes, encoded_bytes)`
- **Publishing envelope builders**
    - `make_envelope(payload_ai_map)`
      Returns an envelope that includes:
        - `standard`
        - `schema_version`
        - `gs1_release`
        - `payload` (GS1 AI map expressed as JSON-friendly keys)
- **Transaction metadata record builders**
    - `make_metadata_record_json(payload_ai_map)`
      JSON-friendly representation. Label key is a string (because JSON keys
      must be strings).
    - `make_metadata_record_cbor(payload_ai_map)`
      On-chain accurate representation. Label key is an integer, which is how
      Cardano transaction metadata labels are encoded in CBOR.
- **Anchor publishing helpers**
    - `make_anchor_metadata_record_json(...)`
    - `make_anchor_metadata_record_cbor(...)`

> Note: When submitting transaction metadata to Cardano, the metadata label is
> an unsigned integer in CBOR. JSON examples show it as a string only because
> JSON requires string keys.

## Running Size Checks

From the repository root:

```bash
python3 -m tools.size_check
```

This prints:

- canonical CBOR byte sizes for the GS1 AI map (datum-friendly)
- canonical CBOR byte sizes for the full metadata record (label plus envelope)
- canonical CBOR byte sizes for anchor metadata records
- canonical CBOR-hex for each object (useful for deterministic comparisons)

### Why `-m`?

Running as a module ensures Python imports resolve correctly (e.g.,
`tools.gs1_codec`)
without requiring local path hacks.

## Deterministic / Canonical Encoding Notes

The tooling uses canonical CBOR encoding (RFC 8949 canonical mode via `cbor2`).

This ensures:

- stable map ordering
- minimal integer widths
- definite-length encoding
- reproducible CBOR-hex across runs

If your implementation produces different CBOR hex for the same logical object,
it is likely not canonical/deterministic.

## Golden Vector Tests (Optional)

Golden vectors are simple regression tests that assert the CBOR-hex output for a
given structure is exactly what we expect.

Run:

```bash 
pytest -q
```

### Common setup issue: `tools` import errors

If `pytest` cannot import `tools.*`, ensure you have:

- `tools/__init__.py`
- `tests/conftest.py` that adds the repo root to `sys.path`

A minimal `tests/conftest.py` looks like:

```python 
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))
```

## Practical Usage Guidance

### If you’re building an on-chain datum

Prefer storing only the canonical GS1 AI map (small, identity-centric). Use the
size tool to confirm the encoded bytes remain compact.

### If you’re publishing via transaction metadata

Use the metadata record builder that encodes the label as an integer for CBOR
(`make_metadata_record_cbor`). JSON examples may wrap the label as a string for
readability, but on-chain labels are integers.

### If your trace record grows over time

Use the anchor pattern. The on-chain anchor metadata stays relatively constant,
even as the off-chain record becomes large.

## Extending the Tooling

These scripts are intentionally small and easy to modify.

Common extensions:

- load AI maps from JSON files rather than embedded samples
- generate multiple record sizes (e.g., 10 / 25 / 100 / 500 events)
- add additional scenarios that reflect your application domain
- output CSV for inclusion in reports

When extending, prefer adding reusable logic to `tools/gs1_codec.py` and keeping
`tools/size_check.py` as a thin runner.