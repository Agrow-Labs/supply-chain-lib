# tools/gs1_codec.py
from __future__ import annotations

from typing import Any, Dict, List
import binascii

try:
    import cbor2  # type: ignore
except Exception:
    cbor2 = None

RECOMMENDED_METADATA_LABEL = 163532014


def require_cbor2() -> None:
    if cbor2 is None:
        raise RuntimeError(
            "Missing dependency 'cbor2'. Install with: pip install cbor2")


def encode_canonical_cbor(obj: Any) -> bytes:
    """
    Canonical/deterministic CBOR encoding (RFC 8949 canonical form).
    """
    require_cbor2()
    return cbor2.dumps(obj, canonical=True)


def to_hex(b: bytes) -> str:
    return binascii.hexlify(b).decode()


def measure(obj: Any) -> tuple[int, bytes]:
    data = encode_canonical_cbor(obj)
    return len(data), data


def ai_map_to_json_keys(payload_ai_map: Dict[int, str]) -> Dict[str, str]:
    """
    JSON readability helper: represent AIs as string keys.
    This does NOT change the CBOR requirement that AI keys must be unsigned integers.
    """

    def ai_key(k: int) -> str:
        # Keep "01" style for <100 to match common GS1 presentation
        return str(k).zfill(2) if k < 100 else str(k)

    return {ai_key(k): v for k, v in payload_ai_map.items()}


def make_envelope(payload_ai_map: Dict[int, str]) -> Dict[str, Any]:
    """
    Recommended publishing envelope (metadata-friendly).
    """
    return {
        "standard": "gs1",
        "schema_version": "1.0.0",
        "gs1_release": "24.0",
        "payload": ai_map_to_json_keys(payload_ai_map),
    }


def make_metadata_record_json(payload_ai_map: Dict[int, str]) -> Dict[str, Any]:
    """
    JSON-friendly representation (keys must be strings).
    Use for documentation and off-chain JSON exchange.
    """
    return {
        str(RECOMMENDED_METADATA_LABEL): make_envelope(payload_ai_map)
    }


def make_metadata_record_cbor(payload_ai_map: Dict[int, str]) -> Dict[int, Any]:
    """
    On-chain accurate representation (label is an unsigned integer).
    This is what must be CBOR-encoded for transaction metadata.
    """
    return {
        RECOMMENDED_METADATA_LABEL: make_envelope(payload_ai_map)
    }


def make_anchor_payload(
        *,
        hash_hex: str,
        uri: str,
        content_type: str = "application/cbor",
        hash_alg: str = "blake2b-256",
) -> Dict[str, Any]:
    """
    Anchor payload object (for envelope.payload).
    """
    return {
        "type": "anchor",
        "hash_alg": hash_alg,
        "hash_hex": hash_hex,
        "uri": uri,
        "content_type": content_type,
    }


def make_anchor_metadata_record_json(
        *,
        hash_hex: str,
        uri: str,
        content_type: str = "application/cbor",
        hash_alg: str = "blake2b-256",
) -> Dict[str, Any]:
    envelope = {
        "standard": "gs1",
        "schema_version": "1.0.0",
        "gs1_release": "24.0",
        "payload": make_anchor_payload(
            hash_hex=hash_hex,
            uri=uri,
            content_type=content_type,
            hash_alg=hash_alg,
        ),
    }
    return {str(RECOMMENDED_METADATA_LABEL): envelope}


def make_anchor_metadata_record_cbor(
        *,
        hash_hex: str,
        uri: str,
        content_type: str = "application/cbor",
        hash_alg: str = "blake2b-256",
) -> Dict[int, Any]:
    envelope = {
        "standard": "gs1",
        "schema_version": "1.0.0",
        "gs1_release": "24.0",
        "payload": make_anchor_payload(
            hash_hex=hash_hex,
            uri=uri,
            content_type=content_type,
            hash_alg=hash_alg,
        ),
    }
    return {RECOMMENDED_METADATA_LABEL: envelope}

def make_offchain_trace_record(
        *,
        base_ai_map: Dict[int, str],
        num_events: int = 25,
) -> Dict[str, Any]:
    """
    Build a sizeable off-chain trace record that still stays "GS1-shaped":
    - includes a GS1 identity block
    - includes an event list that grows with num_events

    This is meant for sizing comparisons (full record vs anchor).
    """
    identity = ai_map_to_json_keys(base_ai_map)

    events: List[Dict[str, Any]] = []
    # Deterministic, repeatable synthetic events (no randomness).
    # Keep text fields realistic but compact.
    for i in range(num_events):
        # Rotate through a small set of event "types"
        evt_type = ["pack", "ship", "receive", "store", "return"][i % 5]
        # Deterministic timestamps (string form; your spec can later recommend formats)
        ts = f"2025-01-{(i % 28) + 1:02d}T{(i % 24):02d}:{(i % 60):02d}:00Z"
        # Deterministic “actor” and “location”
        actor = f"org:{(i % 7) + 1}"
        loc = f"gln:{9876543210987 + (i % 3)}"

        events.append(
            {
                "ts": ts,
                "type": evt_type,
                "actor": actor,
                "loc": loc,
                "note": f"event-{i+1}",
            }
        )

    return {
        "standard": "gs1-trace-record",
        "schema_version": "1.0.0",
        "gs1_release": "24.0",
        "identity": identity,
        "events": events,
    }