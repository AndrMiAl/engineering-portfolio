"""Sanitized portfolio example — not production source."""

from flask import Blueprint, jsonify, render_template

bp = Blueprint("catalog", __name__)


def get_profession_by_slug(slug: str) -> dict | None:
    """Repository call is intentionally omitted in the public example."""
    return {"slug": slug, "title": "Example profession"}


@bp.get("/profession/<slug>")
def profession_page(slug: str):
    profession = get_profession_by_slug(slug)
    if profession is None:
        return render_template("404.html"), 404
    return render_template("profession.html", profession=profession)


@bp.get("/api/professions")
def professions_api():
    items = [
        {"slug": "data-analyst", "title": "Data Analyst"},
        {"slug": "backend-developer", "title": "Backend Developer"},
    ]
    return jsonify(items)
