"""JSON persistence for biosensor passports."""
from __future__ import annotations

import json
from pathlib import Path

from .models import BiosensorPassport


def load_passports(path: Path) -> list[BiosensorPassport]:
    if not path.exists():
        return []
    payload = json.loads(path.read_text(encoding="utf-8"))
    return [BiosensorPassport.from_dict(item) for item in payload]


def save_passports(path: Path, passports: list[BiosensorPassport]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = [passport.to_dict() for passport in passports]
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
