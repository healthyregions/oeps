import { useDispatch, useSelector } from "react-redux";
import { useState, useRef, useEffect } from "react";
import styles from "./VariablePanel.module.css";

import TextField from "@mui/material/TextField";
import Autocomplete from "@mui/material/Autocomplete";

import { Gutter } from "../layout/Gutter";
import RemoteMarkdownModal from "../../components/markdown/RemoteMarkdownModal";
import { Box, Button, Grid, Modal, Typography } from "@mui/material";
import variables from "meta/variables.json";
const variableMeta = Object.values(variables).flat();

const modalStyle = {
  position: "fixed",
  top: "20%",
  left: "50%",
  transform: "translate(-50%,-50%)",
  width: "clamp(300px, 600px, 100%)",
  background: "white",
  padding: "1em",
  fontFamily: "'Lato', Verdana, sans-serif !important",
  // width:'clamp(300px, 600px, 100%)',
};
const modalInner = {
  position: "relative",
  width: "100%",
  height: "100%",
  // width:'clamp(300px, 600px, 100%)',
};

export default function VariablePanel(props) {
  const dataParams = useSelector((state) => state.dataParams);
  const currentData = useSelector((state) => state.currentData);
  const dataPresets = useSelector((state) => state.dataPresets);
  const [activeThemes, setActiveThemes] = useState([]);
  // const [activeYear, setActiveYear] = useState();
  const autocompleteRef = useRef(null);
  const [variableOptions, setVariableOptions] = useState(dataPresets.variables);

  const themeCategories = [...new Set(dataPresets.variables.map(f => f.theme))];
  themeCategories.sort((a, b) => a.localeCompare(b));
  const yearFilters = [...new Set(dataPresets.variables.map(f => f.year))];
  yearFilters.sort((a, b) => a.localeCompare(b));

  const toggleTheme = (theme) => {
    setActiveThemes((activeThemes) => {
      if (activeThemes.includes(theme)) {
        return activeThemes.filter((t) => t !== theme);
      } else {
        return [...activeThemes, theme];
      }
    });
  };

  // const toggleYear = (year) => {
  //   if (activeYear == year) {
  //     setActiveYear(null)
  //   } else {
  //     setActiveYear(year)
  //   }
  // };

  useEffect(() => {
    const filt1 = activeThemes.length ? dataPresets.variables.filter((f) => activeThemes.includes(f.theme)) : dataPresets.variables;
    // const filt2 = activeYear != null ? filt1.filter((f) => activeYear == f.year) : filt1;
    setVariableOptions(filt1)
  },[
    // activeYear,
    activeThemes
  ])

  const [activeDocs, setActiveDocs] = useState("");
  const [modalOpen, setModalOpen] = useState(false);
  const toggleModal = () => {
    setModalOpen((prev) => !prev);
  };
  const dispatch = useDispatch();
  return (
    <>
      <div
        className={
          styles.panelContainer +
          " " +
          (props.open ? styles.open : styles.hidden)
        }
      >
        <Grid container spacing={1}>
          <Grid item xs={6} sm={6} md={12} lg={12}>
            <Typography variant="h5" sx={{ py: 0, my: 0, mb:1 }} fontFamily="'Lato', Verdana, sans-serif;" fontWeight="bold">
              {dataParams.variable}
            </Typography>
            {/* <Typography sx={{ py: 0, my: 0, mb:1 }} fontFamily="'Lato', Verdana, sans-serif;">
              <em>Year: {dataParams.year}</em>
            </Typography> */}
            <Button
              onClick={toggleModal}
              variant="contained"
              sx={{
                textTransform: "none",
                minWidth: "2em",
                backgroundColor: "var(--selected-color)",
                fontFamily: "'Lato', Verdana, sans-serif",
                letterSpacing: 0,
              }}
            >
              <img
                style={{ maxHeight: "1.25em", marginRight: ".5em" }}
                alt="Search for variables"
                src="/images/search.svg"
              />{" "}
              Search for variables
            </Button>
          </Grid>
          <Grid item xs={6} sm={6} md={12} lg={12}>
            {dataPresets.data.length > 1 && (
              <>
                <p>Available Geographies</p>
                {dataPresets.data.map((entry) => (
                  <button
                    onClick={() =>
                      dispatch({
                        type: "CHANGE_DATASET",
                        payload: entry.geodata,
                      })
                    }
                    key={`geography-list-${entry.geodata}`}
                    disabled={
                      !(
                        dataParams.numerator in entry.tables ||
                        dataParams.numerator === "properties"
                      ) || currentData === entry.geodata
                    }
                    className={`${styles.pillButton} ${
                      currentData === entry.geodata && styles.activeButton
                    }`}
                  >
                    {entry.name.split("US ")[1]}
                  </button>
                ))}
              </>
            )}
            <br />
            {dataParams.numerator ? (
              <button
                className={styles.readMoreButton}
                onClick={() => {
                  setActiveDocs(dataParams.metadataUrl.replace("github.com", "raw.githubusercontent.com").replace("/blob", ""))}
                }
              >
                Read more about this data
                <span className={styles.desktop}>
                  Dataset: <code>{dataParams.numerator}</code> |
                  Column: <code>{dataParams.nProperty}</code>
                </span>
              </button>
            ) : null}
            {dataParams.denominator ? (
              <button
                className={styles.readMoreButton}
                onClick={() =>
                  setActiveDocs(dataParams.metadataUrl.replace("github.com", "raw.githubusercontent.com").replace("/blob", ""))
                }
              >
                Read more about this data
                <br />
                Dataset: <code>{dataParams.denominator.split("_")[0]}</code>
                <br />
                Column: <code>{dataParams.dProperty}</code>
              </button>
            ) : null}
          </Grid>
        </Grid>
      </div>
      {activeDocs.length ? (
        <RemoteMarkdownModal
          url={activeDocs}
          reset={() => setActiveDocs(false)}
        />
      ) : null}
      <Modal open={modalOpen} onClose={toggleModal}>
        <Box sx={modalStyle}>
          <Box sx={modalInner}>
            <Typography variant="h5">Search for variables</Typography>
            <Button
              sx={{ position: "absolute", top: "0", right: "0" }}
              onClick={toggleModal}
            >
              &times;
            </Button>
            <Gutter em={0.5} />

            <Typography variant="h6">Toggle Themes</Typography>
            {themeCategories.map((cat, i) => (
              <Button
                key={i}
                variant={activeThemes.includes(cat) ? "contained" : "outlined"}
                onClick={() => toggleTheme(cat)}
                sx={{ margin: ".25em", textTransform: "none" }}
              >
                {cat}
              </Button>
            ))}
            {/* <Typography variant="h6">Filter by Year</Typography>
            {yearFilters.map((yr, i) => (
              <Button
                key={i}
                variant={activeYear == yr ? "contained" : "outlined"}
                onClick={() => toggleYear(yr)}
                sx={{ margin: ".25em", textTransform: "none" }}
              >
                {yr}
              </Button>
            ))} */}
            <Gutter em={0.5} />
            <Autocomplete
              disablePortal
              open={true}
              ref={autocompleteRef}
              id="combo-box-demo"
              options={variableOptions}
              getOptionLabel={(option) => option.variable}
              groupBy={(option) => option.theme}
              fullWidth
              renderInput={(params) => (
                <TextField {...params} label="Type to search" />
              )}
              // use renderOption to add a custom key so it is not duplicated for
              // variables that have the same titles (but different years)
              // when we upgrade to MUI 6x we can use getOptionKey instead:
              // getOptionKey={(option) => `${option.variable}-${option.year}`}
              renderOption={(props, option) => {
                return (
                  <li {...props} key={`${option.nProperty}`}>
                    {option.variable}
                  </li>
                );
              }}
              onChange={(_event, option) => {
                if (option != undefined && option.variable != undefined) {
                  dispatch({
                    type: "CHANGE_VARIABLE",
                    payload: {
                      nProperty: option.nProperty,
                      numerator: option.numerator,
                    },
                  });
                  toggleModal();
                }
              }}
            />
          </Box>
        </Box>
      </Modal>
    </>
  );
}
