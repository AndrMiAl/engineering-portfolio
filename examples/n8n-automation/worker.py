"""Sanitized portfolio worker used to demonstrate an n8n -> Python step."""

from dataclasses import dataclass


@dataclass(frozen=True)
class JobResult:
    ok: bool
    message: str


def run_step(payload: dict) -> JobResult:
    action = str(payload.get("action", "")).strip()
    if not action:
        return JobResult(False, "action is required")

    # Real integrations live in private services.
    return JobResult(True, f"accepted action: {action}")
