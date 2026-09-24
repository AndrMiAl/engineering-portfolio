"""Sanitized portfolio example for turning processed rows into map points."""

from dataclasses import dataclass


@dataclass(frozen=True)
class MapPoint:
    lat: float
    lon: float
    label: str
    error_class: str


def valid_points(rows: list[dict]) -> list[MapPoint]:
    points: list[MapPoint] = []
    for row in rows:
        if row.get("lat") is None or row.get("lon") is None:
            continue
        points.append(
            MapPoint(
                lat=float(row["lat"]),
                lon=float(row["lon"]),
                label=str(row.get("address", "")),
                error_class=str(row.get("error_class", "unknown")),
            )
        )
    return points
