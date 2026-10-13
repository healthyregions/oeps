"""HTTP API for constrained interactive BigQuery downloads."""

from flask import Blueprint, Response, jsonify, request

from oeps.clients.interactive_download import (
    InteractiveDownloadError,
    build_download_plan,
    csv_text_as_zip,
    run_download_query,
)

bp = Blueprint("interactive_download", __name__)


def _parse_body():
    data = request.get_json(silent=True) or {}
    return {
        "years": data.get("years") or [],
        "scales": data.get("scales") or [],
        "themes": data.get("themes") or [],
        "variables": data.get("variables") or [],
        "dry_run": bool(data.get("dry_run")),
    }


@bp.post("/api/interactive-download")
def interactive_download():
    """POST JSON filters → zip attachment with one CSV (or dry-run plan JSON)."""
    try:
        body = _parse_body()
        plan = build_download_plan(
            years=body["years"],
            scales=body["scales"],
            themes=body["themes"],
            variables=body["variables"],
        )
        if body["dry_run"]:
            return jsonify(
                {
                    "years": plan.years,
                    "scales": plan.scales,
                    "variables": plan.variable_names,
                    "tables": plan.tables,
                    "sql": plan.sql,
                    "notes": plan.notes,
                }
            )

        csv_text, row_count = run_download_query(plan)
        year = plan.years[0]
        scale = plan.scales[0].lower()
        csv_name = f"oeps-{scale}-{year}-subset.csv"
        zip_name = f"oeps-{scale}-{year}-subset.zip"
        return Response(
            csv_text_as_zip(csv_text, csv_name),
            mimetype="application/zip",
            headers={
                "Content-Disposition": f'attachment; filename="{zip_name}"',
                "X-OEPS-Row-Count": str(row_count),
                "X-OEPS-Table-Count": str(len(plan.tables)),
            },
        )
    except InteractiveDownloadError as exc:
        return jsonify({"error": exc.message}), exc.status_code
    except Exception as exc:  # noqa: BLE001
        return jsonify({"error": f"Unexpected server error: {exc}"}), 500
