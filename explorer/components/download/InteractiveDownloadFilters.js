import { useEffect, useMemo, useState } from "react";
import styles from "../../styles/Docs.module.css";
import csvDownloads from "../../meta/csvDownloads.json";
import metadataVariables from "../../meta/metadataVariables.json";

const SCALES = ["State", "County", "Tract", "ZCTA"];

const SCALE_CSV_KEY = {
  State: "state",
  County: "county",
  Tract: "tract",
  ZCTA: "zcta",
};

const STATES = [
  ["01", "AL", "Alabama"],
  ["02", "AK", "Alaska"],
  ["04", "AZ", "Arizona"],
  ["05", "AR", "Arkansas"],
  ["06", "CA", "California"],
  ["08", "CO", "Colorado"],
  ["09", "CT", "Connecticut"],
  ["10", "DE", "Delaware"],
  ["11", "DC", "District of Columbia"],
  ["12", "FL", "Florida"],
  ["13", "GA", "Georgia"],
  ["15", "HI", "Hawaii"],
  ["16", "ID", "Idaho"],
  ["17", "IL", "Illinois"],
  ["18", "IN", "Indiana"],
  ["19", "IA", "Iowa"],
  ["20", "KS", "Kansas"],
  ["21", "KY", "Kentucky"],
  ["22", "LA", "Louisiana"],
  ["23", "ME", "Maine"],
  ["24", "MD", "Maryland"],
  ["25", "MA", "Massachusetts"],
  ["26", "MI", "Michigan"],
  ["27", "MN", "Minnesota"],
  ["28", "MS", "Mississippi"],
  ["29", "MO", "Missouri"],
  ["30", "MT", "Montana"],
  ["31", "NE", "Nebraska"],
  ["32", "NV", "Nevada"],
  ["33", "NH", "New Hampshire"],
  ["34", "NJ", "New Jersey"],
  ["35", "NM", "New Mexico"],
  ["36", "NY", "New York"],
  ["37", "NC", "North Carolina"],
  ["38", "ND", "North Dakota"],
  ["39", "OH", "Ohio"],
  ["40", "OK", "Oklahoma"],
  ["41", "OR", "Oregon"],
  ["42", "PA", "Pennsylvania"],
  ["44", "RI", "Rhode Island"],
  ["45", "SC", "South Carolina"],
  ["46", "SD", "South Dakota"],
  ["47", "TN", "Tennessee"],
  ["48", "TX", "Texas"],
  ["49", "UT", "Utah"],
  ["50", "VT", "Vermont"],
  ["51", "VA", "Virginia"],
  ["53", "WA", "Washington"],
  ["54", "WV", "West Virginia"],
  ["55", "WI", "Wisconsin"],
  ["56", "WY", "Wyoming"],
]
  .map(([fips, abbr, name]) => ({ fips, abbr, name }))
  .sort((a, b) => a.name.localeCompare(b.name));

function buildFilterOptions() {
  const themes = [
    ...new Set(
      Object.values(metadataVariables)
        .map((entry) => entry.theme)
        .filter(Boolean)
    ),
  ].sort();

  const variables = [];
  for (const entry of Object.values(metadataVariables)) {
    for (const variable of entry.variables || []) {
      if (!variable?.name) continue;
      variables.push({
        name: variable.name,
        title: variable.title || variable.name,
        theme: entry.theme || "",
        years: (variable.years || []).map(String),
        geographies: variable.geographies || [],
      });
    }
  }
  variables.sort((a, b) => a.title.localeCompare(b.title));

  return { themes, variables };
}

function catalogYearsForScale(scale) {
  const key = SCALE_CSV_KEY[scale];
  const rows = key ? csvDownloads[key] || [] : Object.values(csvDownloads).flat();
  return new Set(rows.map((row) => String(row.year)));
}

function yearsOnVariable(variable, scale) {
  if (Array.isArray(variable.availability) && variable.availability.length) {
    return variable.availability
      .map((item) => {
        const match = /^(\d{4})\s+(.+)$/.exec(String(item));
        return match ? { year: match[1], scale: match[2] } : null;
      })
      .filter((item) => item && (!scale || item.scale === scale))
      .map((item) => item.year);
  }
  if (scale && !(variable.geographies || []).includes(scale)) return [];
  return (variable.years || []).map(String);
}

function toggleValue(list, value) {
  return list.includes(value)
    ? list.filter((item) => item !== value)
    : [...list, value];
}

function formatList(values, emptyLabel) {
  return values.length ? values.join(", ") : emptyLabel;
}

function formatVariableSummary(selectedNames, variablesByName) {
  if (!selectedNames.length) return "none selected";
  if (selectedNames.length <= 5) {
    return selectedNames
      .map((name) => {
        const variable = variablesByName.get(name);
        return variable ? `${variable.title} (${name})` : name;
      })
      .join("; ");
  }
  return `${selectedNames.length} variables selected`;
}

function getQueryMode(activeFilters) {
  if (activeFilters.variable.length > 0) {
    return {
      id: "variables",
      label: "Variables win",
      detail:
        "The download will use only the checked variables. Theme is just helping you browse the list.",
    };
  }
  if (activeFilters.theme.length > 0) {
    return {
      id: "theme",
      label: "Whole theme(s)",
      detail:
        "No individual variables checked — the download would include all variables in the selected theme(s).",
    };
  }
  return {
    id: "all",
    label: "No content filter",
    detail:
      "No theme or variables selected — a future query would use the full warehouse scope (subject to limits).",
  };
}

export default function InteractiveDownloadFilters() {
  const { themes, variables } = useMemo(buildFilterOptions, []);
  const variablesByName = useMemo(
    () => new Map(variables.map((variable) => [variable.name, variable])),
    [variables]
  );

  const [activeFilters, setActiveFilters] = useState({
    year: [],
    scale: [],
    state: [],
    theme: [],
    variable: [],
  });
  const [variableQuery, setVariableQuery] = useState("");
  const [downloadState, setDownloadState] = useState({
    status: "idle", // idle | loading | error | success
    message: "",
  });

  const availableYears = useMemo(() => {
    const scale = activeFilters.scale[0] || "";
    const catalog = catalogYearsForScale(scale);
    const picked = activeFilters.variable
      .map((name) => variablesByName.get(name))
      .filter(Boolean);
    const pool = picked.length
      ? picked
      : activeFilters.theme.length
        ? variables.filter((variable) => activeFilters.theme.includes(variable.theme))
        : [];
    let yearSet = catalog;
    if (pool.length) {
      const contentYears = new Set(
        pool.flatMap((variable) => yearsOnVariable(variable, scale))
      );
      yearSet = new Set([...catalog].filter((year) => contentYears.has(year)));
    }
    return [...yearSet].sort((a, b) => Number(a) - Number(b));
  }, [
    activeFilters.scale,
    activeFilters.theme,
    activeFilters.variable,
    variables,
    variablesByName,
  ]);

  useEffect(() => {
    setActiveFilters((prev) => {
      if (!prev.year.length || availableYears.includes(prev.year[0])) return prev;
      return { ...prev, year: [] };
    });
  }, [availableYears]);

  const handleFilter = (val, type) => {
    setActiveFilters((prev) => {
      const next = {
        ...prev,
        [type]:
          type === "scale" || type === "year"
            ? val
              ? [val]
              : []
            : toggleValue(prev[type], val),
      };

      // Drop variable picks that are impossible for theme / year / scale.
      if (type === "theme" || type === "year" || type === "scale") {
        next.variable = next.variable.filter((name) => {
          const variable = variablesByName.get(name);
          if (!variable) return false;
          if (next.theme.length && !next.theme.includes(variable.theme)) {
            return false;
          }
          if (
            next.year.length &&
            !next.year.some((year) => variable.years.includes(year))
          ) {
            return false;
          }
          if (
            next.scale.length &&
            !next.scale.some((scale) => variable.geographies.includes(scale))
          ) {
            return false;
          }
          return true;
        });
      }

      return next;
    });
    setDownloadState({ status: "idle", message: "" });
  };

  const clearFilters = () => {
    setActiveFilters({ year: [], scale: [], state: [], theme: [], variable: [] });
    setVariableQuery("");
    setDownloadState({ status: "idle", message: "" });
  };

  const visibleVariables = useMemo(() => {
    const query = variableQuery.trim().toLowerCase();

    return variables.filter((variable) => {
      if (
        activeFilters.theme.length &&
        !activeFilters.theme.includes(variable.theme)
      ) {
        return false;
      }

      if (
        activeFilters.year.length &&
        !activeFilters.year.some((year) => variable.years.includes(year))
      ) {
        return false;
      }

      if (
        activeFilters.scale.length &&
        !activeFilters.scale.some((scale) =>
          variable.geographies.includes(scale)
        )
      ) {
        return false;
      }

      if (!query) return true;
      return (
        variable.title.toLowerCase().includes(query) ||
        variable.name.toLowerCase().includes(query) ||
        variable.theme.toLowerCase().includes(query)
      );
    });
  }, [
    variables,
    activeFilters.theme,
    activeFilters.year,
    activeFilters.scale,
    variableQuery,
  ]);

  const hasSelection =
    activeFilters.year.length > 0 ||
    activeFilters.scale.length > 0 ||
    activeFilters.state.length > 0 ||
    activeFilters.theme.length > 0 ||
    activeFilters.variable.length > 0;

  const canDownload =
    activeFilters.year.length === 1 &&
    activeFilters.scale.length === 1 &&
    (activeFilters.variable.length > 0 || activeFilters.theme.length > 0);

  const downloadHint = !canDownload
    ? "To download: select one scale, either a theme or specific variables, and one year."
    : "";

  const queryMode = getQueryMode(activeFilters);
  const variablesWin = queryMode.id === "variables";

  const handleDownload = async () => {
    if (!canDownload || downloadState.status === "loading") return;
    setDownloadState({ status: "loading", message: "Running BigQuery…" });
    try {
      const response = await fetch("/api/interactive-download", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          years: activeFilters.year,
          scales: activeFilters.scale,
          states: activeFilters.state,
          themes: activeFilters.theme,
          variables: activeFilters.variable,
        }),
      });
      const contentType = response.headers.get("content-type") || "";
      if (!response.ok) {
        let message = `Download failed (${response.status})`;
        if (contentType.includes("application/json")) {
          const data = await response.json();
          message = data.error || message;
        } else {
          message = (await response.text()) || message;
        }
        setDownloadState({ status: "error", message });
        return;
      }

      const blob = await response.blob();
      const disposition = response.headers.get("content-disposition") || "";
      const match = /filename="?([^";]+)"?/i.exec(disposition);
      const filename = match?.[1] || "oeps-subset.zip";
      const url = URL.createObjectURL(blob);
      const anchor = document.createElement("a");
      anchor.href = url;
      anchor.download = filename;
      document.body.appendChild(anchor);
      anchor.click();
      anchor.remove();
      URL.revokeObjectURL(url);

      const rows = response.headers.get("x-oeps-row-count");
      setDownloadState({
        status: "success",
        message: rows
          ? `Downloaded ${filename} (${Number(rows).toLocaleString()} rows).`
          : `Downloaded ${filename}.`,
      });
    } catch (err) {
      setDownloadState({
        status: "error",
        message: err?.message || "Unexpected download error.",
      });
    }
  };

  return (
    <div>
      <p>
        Choose a scale and the variables first. The year list then shows only
        years that exist for that selection. Download runs a constrained
        BigQuery query through the OEPS backend (no free-form SQL).
      </p>

      <h3 className={styles.filterSectionTitle}>1. Where</h3>
      <h4 id="download-scale-label">Spatial scale</h4>
      <select
        id="download-scale"
        aria-labelledby="download-scale-label"
        className={styles.filterSelect}
        value={activeFilters.scale[0] || ""}
        onChange={(event) => handleFilter(event.target.value, "scale")}
      >
        <option value="">Select a scale</option>
        {SCALES.map((scale) => (
          <option key={scale} value={scale}>
            {scale}
          </option>
        ))}
      </select>

      <h4>State</h4>
      <p className={styles.selectionHint}>
        Optional. Nothing selected means the whole United States. You can
        select more than one.
      </p>
      <div className={styles.filterRow}>
        {STATES.map((state) => (
          <button
            key={state.fips}
            type="button"
            title={state.name}
            onClick={() => handleFilter(state.fips, "state")}
            className={`${styles.filterButton} ${
              activeFilters.state.includes(state.fips) ? styles.activeDownload : ""
            }`}
            aria-pressed={activeFilters.state.includes(state.fips)}
          >
            {state.abbr}
          </button>
        ))}
      </div>

      <h3 className={styles.filterSectionTitle}>2. Which variables</h3>

      <div className={styles.rulesCallout} role="note">
        <p className={styles.rulesCalloutTitle}>How theme and variables work together</p>
        <ol className={styles.rulesList}>
          <li>
            <strong>Theme</strong> narrows the list below (and can mean “all
            variables in that theme” if you pick no checkboxes).
          </li>
          <li>
            <strong>Variables</strong> are the precise columns. If any are
            checked, <strong>variables win</strong> — theme is only for browsing.
          </li>
        </ol>
      </div>

      <div
        className={`${styles.queryModeBanner} ${
          variablesWin
            ? styles.queryModeVariables
            : queryMode.id === "theme"
              ? styles.queryModeTheme
              : styles.queryModeAll
        }`}
        aria-live="polite"
      >
        <div className={styles.queryModeLabel}>What a download would use</div>
        <div className={styles.queryModeValue}>{queryMode.label}</div>
        <p className={styles.queryModeDetail}>{queryMode.detail}</p>
      </div>

      <section
        className={`${styles.filterPanel} ${styles.filterPanelBrowse}`}
        aria-labelledby="theme-browse-heading"
      >
        <div className={styles.filterPanelHeader}>
          <span className={styles.filterPanelBadge}>Browse</span>
          <h4 id="theme-browse-heading">Theme</h4>
        </div>
        <p className={styles.selectionHint}>
          Optional shortcut to filter the variable list. With no variables
          checked, selecting a theme means “include every variable in that
          theme.”
        </p>
        <div className={styles.filterRow}>
          {themes.map((theme) => (
            <button
              key={theme}
              type="button"
              onClick={() => handleFilter(theme, "theme")}
              className={`${styles.filterButton} ${
                activeFilters.theme.includes(theme) ? styles.activeDownload : ""
              }`}
              aria-pressed={activeFilters.theme.includes(theme)}
            >
              {theme}
            </button>
          ))}
        </div>
      </section>

      <section
        className={`${styles.filterPanel} ${styles.filterPanelSelect} ${
          variablesWin ? styles.filterPanelActive : ""
        }`}
        aria-labelledby="variable-select-heading"
      >
        <div className={styles.filterPanelHeader}>
          <span className={styles.filterPanelBadgeSelect}>Select</span>
          <h4 id="variable-select-heading">Variables</h4>
          {variablesWin ? (
            <span className={styles.winsPill}>Takes priority</span>
          ) : null}
        </div>
        <p className={styles.selectionHint}>
          Optional. Check specific variables to override theme.{" "}
          {visibleVariables.length} shown
          {activeFilters.variable.length
            ? ` · ${activeFilters.variable.length} selected`
            : ""}
          .
        </p>
        <input
          type="search"
          className={styles.variableSearch}
          placeholder="Search by title or Variable ID…"
          value={variableQuery}
          onChange={(event) => setVariableQuery(event.target.value)}
          aria-label="Search variables"
        />
        <div className={styles.variableList} role="listbox" aria-label="Variables">
          {visibleVariables.length === 0 ? (
            <p className={styles.selectionHint}>
              No variables match these filters.
            </p>
          ) : (
            visibleVariables.map((variable) => {
              const checked = activeFilters.variable.includes(variable.name);
              return (
                <label
                  key={variable.name}
                  className={`${styles.variableOption} ${
                    checked ? styles.variableOptionSelected : ""
                  }`}
                >
                  <input
                    type="checkbox"
                    checked={checked}
                    onChange={() => handleFilter(variable.name, "variable")}
                  />
                  <span>
                    <span className={styles.variableTitle}>{variable.title}</span>
                  <span className={styles.variableMeta}>
                    {" "}
                    · <code>{variable.name}</code> · {variable.theme}
                    {" · "}
                    {variable.years.join(", ")}
                  </span>
                  </span>
                </label>
              );
            })
          )}
        </div>
      </section>

      <h3 className={styles.filterSectionTitle}>3. When</h3>
      <h4 id="download-year-label">Year</h4>
      <p className={styles.selectionHint}>
        Only years with data for the current scale and variables are listed.
      </p>
      <select
        id="download-year"
        aria-labelledby="download-year-label"
        className={styles.filterSelect}
        value={activeFilters.year[0] || ""}
        onChange={(event) => handleFilter(event.target.value, "year")}
      >
        <option value="">Select a year</option>
        {availableYears.map((year) => (
          <option key={year} value={year}>
            {year}
          </option>
        ))}
      </select>

      <div className={styles.selectionSummary} aria-live="polite">
        <h4>Current selection</h4>
        <ul>
          <li>
            <strong>Spatial scale:</strong>{" "}
            {formatList(activeFilters.scale, "none selected")}
          </li>
          <li>
            <strong>States:</strong>{" "}
            {activeFilters.state.length
              ? activeFilters.state
                  .map(
                    (fips) =>
                      STATES.find((state) => state.fips === fips)?.name || fips
                  )
                  .join(", ")
              : "Whole United States"}
          </li>
          <li>
            <strong>Theme (browse / whole-theme fallback):</strong>{" "}
            {formatList(activeFilters.theme, "none")}
          </li>
          <li>
            <strong>Variables (precise columns — win if any):</strong>{" "}
            {formatVariableSummary(activeFilters.variable, variablesByName)}
          </li>
          <li>
            <strong>Year:</strong>{" "}
            {formatList(activeFilters.year, "none selected")}
          </li>
        </ul>
        <p className={styles.selectionHint}>
          {hasSelection
            ? `Mode: ${queryMode.label}. ${queryMode.detail}`
            : queryMode.detail}
        </p>
      </div>

      <div className={styles.downloadActions}>
        <button
          type="button"
          className={`${styles.downloadButton} ${
            canDownload && downloadState.status !== "loading"
              ? ""
              : styles.passiveButton
          }`}
          disabled={!canDownload || downloadState.status === "loading"}
          onClick={handleDownload}
        >
          {downloadState.status === "loading"
            ? "Downloading…"
            : "Download CSV"}
        </button>
        <button
          type="button"
          className={styles.filterButton}
          onClick={clearFilters}
          disabled={!hasSelection || downloadState.status === "loading"}
        >
          Clear filters
        </button>
      </div>
      {downloadHint ? (
        <p className={styles.selectionHint}>{downloadHint}</p>
      ) : null}
      {downloadState.message ? (
        <p
          className={
            downloadState.status === "error"
              ? styles.downloadError
              : styles.downloadSuccess
          }
          role="status"
        >
          {downloadState.message}
        </p>
      ) : null}
    </div>
  );
}
