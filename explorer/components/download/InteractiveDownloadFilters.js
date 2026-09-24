import { useMemo, useState } from "react";
import styles from "../../styles/Docs.module.css";
import csvDownloads from "../../meta/csvDownloads.json";
import metadataVariables from "../../meta/metadataVariables.json";

const SCALES = ["State", "County", "Tract", "ZCTA"];

function buildFilterOptions() {
  const years = [
    ...new Set(
      Object.values(csvDownloads)
        .flat()
        .map((row) => String(row.year))
    ),
  ].sort((a, b) => Number(a) - Number(b));

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

  return { years, themes, variables };
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
  const { years, themes, variables } = useMemo(buildFilterOptions, []);
  const variablesByName = useMemo(
    () => new Map(variables.map((variable) => [variable.name, variable])),
    [variables]
  );

  const [activeFilters, setActiveFilters] = useState({
    year: [],
    scale: [],
    theme: [],
    variable: [],
  });
  const [variableQuery, setVariableQuery] = useState("");
  const [downloadState, setDownloadState] = useState({
    status: "idle", // idle | loading | error | success
    message: "",
  });

  const handleFilter = (val, type) => {
    setActiveFilters((prev) => {
      const next = {
        ...prev,
        [type]: toggleValue(prev[type], val),
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
    setActiveFilters({ year: [], scale: [], theme: [], variable: [] });
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
    activeFilters.theme.length > 0 ||
    activeFilters.variable.length > 0;

  const canDownload =
    activeFilters.year.length === 1 &&
    activeFilters.scale.length === 1 &&
    (activeFilters.variable.length > 0 || activeFilters.theme.length > 0);

  const downloadHint = !canDownload
    ? "To download: select exactly one year, one scale, and either a theme or specific variables."
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
      const filename = match?.[1] || "oeps-subset.csv";
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
        Choose when and where first, then decide <em>which</em> variables.
        Download runs a constrained BigQuery query through the OEPS backend
        (no free-form SQL).
      </p>

      <h3 className={styles.filterSectionTitle}>1. When &amp; where</h3>
      <h4>Year</h4>
      <div className={styles.filterRow}>
        {years.map((year) => (
          <button
            key={year}
            type="button"
            onClick={() => handleFilter(year, "year")}
            className={`${styles.filterButton} ${
              activeFilters.year.includes(year) ? styles.activeDownload : ""
            }`}
            aria-pressed={activeFilters.year.includes(year)}
          >
            {year}
          </button>
        ))}
      </div>

      <h4>Spatial scale</h4>
      <div className={styles.filterRow}>
        {SCALES.map((scale) => (
          <button
            key={scale}
            type="button"
            onClick={() => handleFilter(scale, "scale")}
            className={`${styles.filterButton} ${
              activeFilters.scale.includes(scale) ? styles.activeDownload : ""
            }`}
            aria-pressed={activeFilters.scale.includes(scale)}
          >
            {scale}
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

      <div className={styles.selectionSummary} aria-live="polite">
        <h4>Current selection</h4>
        <ul>
          <li>
            <strong>Years:</strong>{" "}
            {formatList(activeFilters.year, "any (not limited)")}
          </li>
          <li>
            <strong>Scales:</strong>{" "}
            {formatList(activeFilters.scale, "any (not limited)")}
          </li>
          <li>
            <strong>Theme (browse / whole-theme fallback):</strong>{" "}
            {formatList(activeFilters.theme, "none")}
          </li>
          <li>
            <strong>Variables (precise columns — win if any):</strong>{" "}
            {formatVariableSummary(activeFilters.variable, variablesByName)}
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
