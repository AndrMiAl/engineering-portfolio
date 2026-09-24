"""Sanitized portfolio example — not production source."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Article:
    slug: str
    title: str
    text: str


def search_articles(query: str, articles: list[Article]) -> list[Article]:
    needle = query.strip().casefold()
    if not needle:
        return []
    return [
        article
        for article in articles
        if needle in article.title.casefold() or needle in article.text.casefold()
    ]
