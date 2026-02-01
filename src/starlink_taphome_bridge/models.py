from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any


@dataclass(slots=True)
class Telemetry:
    power_w: float | None = None
    latency_ms: float | None = None
    heater_mode: str | None = None
    uptime_s: int | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class AppliedResult:
    requested: str
    applied: str | None
    success: bool
    message: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
