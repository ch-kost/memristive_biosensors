"""Validated biosensor passport data model."""
from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import date
from math import isfinite


@dataclass(frozen=True, slots=True)
class BiosensorPassport:
    """Immutable description of a biosensor and its resistance measurement."""

    identifier: str
    material: str
    resistance_ohm: float
    created_at: str

    def __post_init__(self) -> None:
        if not self.identifier.strip():
            raise ValueError("Identifier must not be empty")
        if not self.material.strip():
            raise ValueError("Material must not be empty")
        if not isfinite(self.resistance_ohm) or self.resistance_ohm <= 0:
            raise ValueError("Resistance must be finite and positive")
        date.fromisoformat(self.created_at)

    def to_dict(self) -> dict[str, str | float]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> BiosensorPassport:
        return cls(
            identifier=str(data["identifier"]),
            material=str(data["material"]),
            resistance_ohm=float(data["resistance_ohm"]),
            created_at=str(data["created_at"]),
        )
