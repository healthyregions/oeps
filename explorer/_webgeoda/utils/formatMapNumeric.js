/**
 * Format numeric values for map legend labels and hover tooltips.
 * Very small magnitudes (e.g. some 2SFCA fields) must not round to "0".
 */
export function formatMapNumeric(value) {
  const n = typeof value === "number" ? value : Number(value);
  if (!Number.isFinite(n)) return String(value);
  if (Object.is(n, -0) || n === 0) return "0";
  const abs = Math.abs(n);
  if (abs >= 1) {
    return n.toLocaleString("en-US", { maximumFractionDigits: 2 });
  }
  if (abs >= 0.01) {
    return n.toLocaleString("en-US", {
      maximumFractionDigits: 4,
      minimumFractionDigits: 0,
    });
  }
  if (abs >= 1e-7) {
    return n.toLocaleString("en-US", {
      maximumFractionDigits: 9,
      minimumFractionDigits: 0,
    });
  }
  return n.toExponential(2);
}

/** Legend bins may be numeric breaks or categorical / natural-break labels (strings). */
export function formatLegendLabel(bin) {
  if (bin == null || bin === "") return "";
  if (typeof bin === "number" && Number.isFinite(bin)) {
    return formatMapNumeric(bin);
  }
  if (typeof bin === "string") {
    const t = bin.trim();
    const n = Number(t);
    if (
      t !== "" &&
      Number.isFinite(n) &&
      /^[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?$/.test(t)
    ) {
      return formatMapNumeric(n);
    }
    return bin;
  }
  return String(bin);
}
