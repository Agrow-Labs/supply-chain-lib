#!/usr/bin/env python3
from __future__ import annotations

from typing import Dict

from tools.gs1_codec import (
    RECOMMENDED_METADATA_LABEL,
    encode_canonical_cbor,
    make_anchor_metadata_record_cbor,
    make_anchor_metadata_record_json,
    make_metadata_record_cbor,
    make_metadata_record_json,
    make_offchain_trace_record,
    measure,
    to_hex,
)

SAMPLE_AGRICULTURE_AI_MAP: Dict[int, str] = {
    1: "12341234567893",
    10: "ABC12345",
    17: "241122",
    30: "50"
}

SAMPLE_LOGISTICS_AI_MAP: Dict[int, str] = {
    0: "003456789012345678",
    1: "12341234567893",
    10: "ABC12345",
    413: "1234567890123",
    414: "9876543210987"
}

SAMPLE_RETAIL_AI_MAP: Dict[int, str] = {
    1: "12341234567893",
    10: "ABC12345",
    414: "9876543210987",
    8004: "12345678901234567890"
}

SAMPLE_REPRESENTATIVE_AI_MAP: Dict[int, str] = {
    1: "09506000134352",            # (01) GTIN (example-format)
    10: "BATCH-ABC12345",           # (10) Batch/Lot
    11: "241201",                   # (11) Production date (YYMMDD)
    15: "250101",                   # (15) Best before (YYMMDD)
    17: "250131",                   # (17) Expiry date (YYMMDD)
    21: "SERIAL-000000000001",      # (21) Serial number
    30: "50",                       # (30) Variable count
    37: "12",                       # (37) Quantity
    414: "9876543210987",           # (414) GLN (location)
    422: "840",                     # (422) Country of origin (ISO numeric)
    8004: "12345678901234567890",   # (8004) GIAI (asset id)
}

def print_block(title: str) -> None:
    print(title)
    print("-" * len(title))

def report_ai_and_metadata(name: str, ai_map: Dict[int, str]) -> None:
    ai_size, ai_bytes = measure(ai_map)
    meta_json = make_metadata_record_json(ai_map)
    meta_cbor = make_metadata_record_cbor(ai_map)

    json_size, json_bytes = measure(meta_json)
    cbor_size, cbor_bytes = measure(meta_cbor)

    print_block(f"== {name} ==")
    print(f"AI map (CBOR bytes):            {ai_size}")
    print(f"AI map hex:                     {to_hex(ai_bytes)}")
    print(f"Metadata (JSON-style) bytes:    {json_size}")
    print(f"Metadata (JSON-style) hex:      {to_hex(json_bytes)}")
    print(f"Metadata (CBOR on-chain) bytes: {cbor_size}")
    print(f"Metadata (CBOR on-chain) hex:   {to_hex(cbor_bytes)}")
    print(f"Recommended label:              {RECOMMENDED_METADATA_LABEL}")
    print("")

def report_anchor(name: str, base_ai_map: Dict[int, str], num_events: int) -> None:
    """
    Measure:
    - Off-chain record size (canonical CBOR)
    - Anchor metadata record size (canonical CBOR)
    """
    offchain = make_offchain_trace_record(base_ai_map=base_ai_map, num_events=num_events)
    offchain_bytes = encode_canonical_cbor(offchain)
    offchain_size = len(offchain_bytes)

    # Hash bytes are dummy here; in a real flow you would compute hash(offchain_bytes)
    # and use that value. For sizing, a 32-byte hex string is representative.
    dummy_hash_hex = "d34db33f" * 8  # 64 hex chars (32 bytes)
    dummy_uri = "ipfs://CID_GOES_HERE"

    anchor_json = make_anchor_metadata_record_json(hash_hex=dummy_hash_hex, uri=dummy_uri)
    anchor_cbor = make_anchor_metadata_record_cbor(hash_hex=dummy_hash_hex, uri=dummy_uri)

    json_size, json_bytes = measure(anchor_json)
    cbor_size, cbor_bytes = measure(anchor_cbor)

    print_block(f"== {name} (Anchor sizing) ==")
    print(f"Off-chain record events:       {num_events}")
    print(f"Off-chain record bytes:        {offchain_size}")
    print(f"Anchor (JSON-style) bytes:     {json_size}")
    print(f"Anchor (JSON-style) hex:       {to_hex(json_bytes)}")
    print(f"Anchor (CBOR on-chain) bytes:  {cbor_size}")
    print(f"Anchor (CBOR on-chain) hex:    {to_hex(cbor_bytes)}")
    print(f"Recommended label:             {RECOMMENDED_METADATA_LABEL}")
    print("")


def main() -> None:
    # Original small examples
    report_ai_and_metadata("Agriculture", SAMPLE_AGRICULTURE_AI_MAP)
    report_ai_and_metadata("Logistics", SAMPLE_LOGISTICS_AI_MAP)
    report_ai_and_metadata("Retail", SAMPLE_RETAIL_AI_MAP)

    # Representative bigger (still GS1) example
    report_ai_and_metadata("Representative GS1 Payload", SAMPLE_REPRESENTATIVE_AI_MAP)

    # Anchor sizing example (show how on-chain stays stable as off-chain grows)
    report_anchor("Trace Record", SAMPLE_REPRESENTATIVE_AI_MAP, num_events=25)
    report_anchor("Trace Record", SAMPLE_REPRESENTATIVE_AI_MAP, num_events=100)


if __name__ == "__main__":
    main()