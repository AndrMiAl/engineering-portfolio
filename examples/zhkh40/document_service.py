"""Sanitized portfolio example — not production source."""

from dataclasses import dataclass


@dataclass(frozen=True)
class RecalculationForm:
    full_name: str
    address: str
    reason: str


def build_paragraphs(form: RecalculationForm) -> list[str]:
    return [
        "Заявление на перерасчёт",
        f"Заявитель: {form.full_name}",
        f"Адрес: {form.address}",
        f"Основание: {form.reason}",
    ]
