"""Sanitized portfolio example — not production source."""

from flask import Blueprint, jsonify

from provider_adapter import Provider, collect_overviews

bp = Blueprint("health", __name__)


def provider_registry() -> list[Provider]:
    return []  # Real provider instances are wired from private configuration.


@bp.get("/api/servers/overview")
def servers_overview():
    rows = collect_overviews(provider_registry())
    return jsonify(
        [
            {
                "provider": row.provider,
                "online": row.online,
                "users": row.users,
                "services": list(row.services),
            }
            for row in rows
        ]
    )
