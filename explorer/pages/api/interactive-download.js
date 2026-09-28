/**
 * Proxies interactive download requests to the Flask backend.
 * Set OEPS_BACKEND_URL (default http://127.0.0.1:5000) where flask is running.
 */
export default async function handler(req, res) {
  if (req.method !== "POST") {
    res.setHeader("Allow", "POST");
    return res.status(405).json({ error: "Method not allowed" });
  }

  const backend = (process.env.OEPS_BACKEND_URL || "http://127.0.0.1:5000").replace(
    /\/$/,
    ""
  );

  let upstream;
  try {
    upstream = await fetch(`${backend}/api/interactive-download`, {
      method: "POST",
      headers: { "Content-Type": "application/json", Accept: "*/*" },
      body: JSON.stringify(req.body || {}),
    });
  } catch (err) {
    return res.status(503).json({
      error:
        "Could not reach the OEPS backend. Start Flask locally (flask run) or set OEPS_BACKEND_URL.",
      detail: String(err?.message || err),
    });
  }

  const contentType = upstream.headers.get("content-type") || "";
  if (contentType.includes("application/json")) {
    const data = await upstream.json();
    return res.status(upstream.status).json(data);
  }

  const text = await upstream.text();
  if (!upstream.ok) {
    return res.status(upstream.status).json({
      error: text || `Backend returned ${upstream.status}`,
    });
  }

  const disposition =
    upstream.headers.get("content-disposition") ||
    'attachment; filename="oeps-subset.csv"';
  res.setHeader("Content-Type", "text/csv; charset=utf-8");
  res.setHeader("Content-Disposition", disposition);
  const rowCount = upstream.headers.get("x-oeps-row-count");
  if (rowCount) res.setHeader("X-OEPS-Row-Count", rowCount);
  return res.status(200).send(text);
}
