registry = Registry(registry_path)

    outdir = Path("oeps/data/package_rules")

    var_years = {
        "state": {},
        "county": {},
        "tract": {},
        "zcta": {},
    }

    rules_2019 = {
        "state": {},
        "county": {},
        "tract": {},
        "zcta": {},
    }
    rules_2025 = {
        "state": {},
        "county": {},
        "tract": {},
        "zcta": {},
    }
    for k, v in registry.variables.items():
        for ts in v["table_sources"]:
            year = registry.table_sources[ts]["year"]
            lvl = registry.table_sources[ts]["summary_level"]
            if k in var_years[lvl]:
                var_years[lvl][k].append(year)
            else:
                var_years[lvl][k] = [year]
        var_years[lvl][k].sort()

    for lvl, vars in var_years.items():
        for k, years in vars.items():
            rules_2019[lvl][k] = {
                "pick": None,
                "all years": years
            }
            rules_2025[lvl][k] = {
                "pick": None,
                "all years": years
            }
            for year in years:
                if int(year) <= 2019:
                    rules_2019[lvl][k]["pick"] = year
                if int(year) <= 2025:
                    rules_2025[lvl][k]["pick"] = year

    def write_rules_to_csvs(outdir: Path, rules: dict):
        fields = ("theme", "construct", "name", "pick", "all years")
        for lvl, vars in rules.items():
            path = Path(outdir, f"{lvl}.csv")
            with open(path, "w") as o:
                writer = csv.DictWriter(o, fieldnames=fields)
                writer.writeheader()
                rows = []
                for k, years in vars.items():
                    metadata = registry.metadata[registry.variables[k]["metadata"]]
                    row = {
                        "theme": metadata["theme"],
                        "construct": metadata["construct"],
                        "name": k,
                        "pick": years["pick"],
                        "all years": ",".join(years["all years"]),
                    }
                    rows.append(row)

                rows.sort(key=lambda i: (i["theme"], i["construct"], i["name"]))
                writer.writerows(rows)

    write_rules_to_csvs(Path(outdir, "dp-1"), rules_2019)
    write_rules_to_csvs(Path(outdir, "dp-2"), rules_2025)
