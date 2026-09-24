"""Sanitized portfolio example — simplified async pipeline."""

from dataclasses import dataclass
from typing import Protocol


@dataclass
class Context:
    source: str
    rendered_path: str | None = None
    published_url: str | None = None


class Stage(Protocol):
    async def run(self, context: Context) -> Context: ...


class Pipeline:
    def __init__(self, stages: list[Stage]) -> None:
        self.stages = stages

    async def run(self, context: Context) -> Context:
        for stage in self.stages:
            context = await stage.run(context)
        return context
