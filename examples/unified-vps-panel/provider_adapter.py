"""Sanitized portfolio example — no real hosts, users or credentials."""

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class ServerOverview:
    provider: str
    online: bool
    users: int
    services: tuple[str, ...]


class Provider(Protocol):
    name: str

    def overview(self) -> ServerOverview: ...


def collect_overviews(providers: list[Provider]) -> list[ServerOverview]:
    return [provider.overview() for provider in providers]
