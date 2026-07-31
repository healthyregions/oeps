import Head from "next/head";
import MainNav from "@components/layout/MainNav";
import styles from "@styles/About.module.css";
import {
  Accordion,
  AccordionDetails,
  AccordionSummary,
  Box,
  Container,
  Typography
} from "@mui/material";
import {useId} from "react";
import {ExpandMore} from "@mui/icons-material";
import Footer from "@components/layout/Footer";
import {Gutter} from "@components/layout/Gutter";

export default function DataInclusion() {
  const id = useId();

  // TODO: Form state
  //const [form, setForm] = useState({ /* ... */ });
  // const handleChange = (e) => {
  //   setForm({ ...form, [e.target.name]: e.target.value });
  // };

  // TODO: Form submission logic
  const handleSubmit = (e) => {
    e.preventDefault();
    alert('Form was not actually submitted!');
    //setForm({ /* ... */ });
  };

  return (
    <div className={styles.container}>
      <Head>
        <title>Data Inclusion</title>
      </Head>
      <MainNav />

      <main className={styles.main}>
        <h1 className={styles.title}>Data Inclusion Criteria</h1>
         
        <p>
          We strive for a transparent, high standard of data in OEPS. Data considered for inclusion in OEPS are evaluated across multiple dimensions rather than through a simple pass-or-fail decision. </p>
        
        <p>Each dataset is assessed based on its overall contribution to the OEPS data ecosystem, recognizing that strengths in one area may offset limitations in another. Because candidate data differ in their purpose, geographic coverage, temporal availability, analytical value, data quality, and technical characteristics, each dataset is evaluated before being incorporated into OEPS. 
          Because we also generate new data for inclusion in OEPS (e.g. spatial access metrics, infrastructure measures by various community levels), we strive for the same goals in our own work. </p>
        <p>
          Rather than relying on a single requirement, OEPS uses a consistent set of data inclusion criteria to ensure that data is scientifically relevant, analytically useful, technically sustainable, and suitable for long-term integration within the platform.
          Data must be incorporate all dimensions of <b>inclusion criteria </b>below, in some manner. In the future, we hope to refine these standards further as 
          a series of metrics that can be used to assess data, variable by variable.
        </p>

        <Container maxWidth="lg">
          <Box component="form" onSubmit={handleSubmit} sx={{ mt: 4, display: 'flex', flexDirection: 'column', gap: 1 }}>
            <Accordion defaultExpanded>
              <AccordionSummary
                expandIcon={<ExpandMore />}
                aria-controls={`${id}-panel1-content`}
                id={`${id}-panel1-header`}
              >
                <Typography component="span">Relevant </Typography>
              </AccordionSummary>
              <AccordionDetails>
                <Typography>
                  OEPS data should have a clear conceptual relationship to opioid risk environments, opioid-related outcomes, or the broader social, economic, environmental, health, and policy conditions represented within the platform. Candidate datasets may directly measure opioid-related outcomes, treatment access, harm reduction, or policy environments, or they may describe upstream factors that influence opioid-related risks.
                </Typography>
              </AccordionDetails>
            </Accordion>

            <Accordion>
              <AccordionSummary
                expandIcon={<ExpandMore />}
                aria-controls={`${id}-panel1-content`}
                id={`${id}-panel1-header`}
              >
                <Typography component="span">Community-level</Typography>
              </AccordionSummary>
              <AccordionDetails>
                <Typography>
                OEPS prioritizes data that support community-level research by describing environmental, social, economic, policy, and health conditions across neighborhoods, census tracts, ZIP Code Tabulation Areas (ZCTAs), counties, states, or other geographic units. Preference is given to datasets that enable meaningful comparisons across communities. Regional or state-specific datasets may also be included when they provide unique information that is not available from national sources.
                </Typography>
              </AccordionDetails>
            </Accordion>

            <Accordion >
              <AccordionSummary
                expandIcon={<ExpandMore />}
                aria-controls={`${id}-panel1-content`}
                id={`${id}-panel1-header`}
              >
                <Typography component="span">Spatial</Typography>
              </AccordionSummary>
              <AccordionDetails>
                <Typography>
                OEPS considers whether data includes geographic information that is compatible with the platform’s spatial framework. Geographic resolution, coverage, and compatibility with existing geographic identifiers and boundary files are important because they support data integration, mapping, visualization, and cross-dataset analyses. Datasets with limited geographic coverage may still be included when they provide valuable information unavailable from broader sources.
                </Typography>
              </AccordionDetails>
            </Accordion>
            <Accordion >
              <AccordionSummary
                expandIcon={<ExpandMore />}
                aria-controls={`${id}-panel1-content`}
                id={`${id}-panel1-header`}
              >
                <Typography component="span">Temporal</Typography>
              </AccordionSummary>
              <AccordionDetails>
                <Typography>
               OEPS prefers data that are current (less than 5 years) and, whenever possible, include multiple years of observations to support longitudinal analyses and policy evaluation. Historical datasets may also be included when they capture important policy changes, historical conditions, or unique information that cannot be obtained elsewhere.
                </Typography>
              </AccordionDetails>
            </Accordion>

            <Accordion>
              <AccordionSummary
                expandIcon={<ExpandMore />}
                aria-controls={`${id}-panel1-content`}
                id={`${id}-panel1-header`}
              >
                <Typography component="span">Analytical</Typography>
              </AccordionSummary>
              <AccordionDetails>
                <Typography>
              Data should provide meaningful analytical value by supporting mapping, visualization, statistical analysis, modeling, index development, or other analytical applications. OEPS also considers whether a dataset complements existing resources and provides information that is sufficiently informative for meaningful comparisons across places, populations, or time.
                </Typography>
              </AccordionDetails>
            </Accordion>

            <Accordion >
              <AccordionSummary
                expandIcon={<ExpandMore />}
                aria-controls={`${id}-panel1-content`}
                id={`${id}-panel1-header`}
              >
                <Typography component="span">Data Quality</Typography>
              </AccordionSummary>
              <AccordionDetails>
                <Typography>
              Data quality is evaluated by considering completeness, reporting consistency, geographic coverage, missing values, and other factors that may influence interpretation. Data limitations do not automatically prevent inclusion, but they should be well understood and appropriately documented before integration into OEPS.
                </Typography>
              </AccordionDetails>
            </Accordion>
            <Accordion >
              <AccordionSummary
                expandIcon={<ExpandMore />}
                aria-controls={`${id}-panel1-content`}
                id={`${id}-panel1-header`}
              >
                <Typography component="span">Findable</Typography>
              </AccordionSummary>
              <AccordionDetails>
                <Typography>
            Data should be accompanied by sufficient identifying information, including clear titles, source organizations, release dates, version information, and supporting documentation. This information supports reliable dataset identification, future maintenance, and long-term management within the OEPS data ecosystem.
                </Typography>
              </AccordionDetails>
            </Accordion>


            <Accordion>
              <AccordionSummary
                expandIcon={<ExpandMore />}
                aria-controls={`${id}-panel1-content`}
                id={`${id}-panel1-header`}
              >
                <Typography component="span">Accessible</Typography>
              </AccordionSummary>
              <AccordionDetails>
                <Typography>
         OEPS considers whether data can be obtained through stable and appropriate access mechanisms that support long-term maintenance. Publicly available resources are generally preferred, although restricted-access datasets may also be included when they provide important information unavailable from other sources.
                </Typography>
              </AccordionDetails>
            </Accordion>

            <Accordion >
              <AccordionSummary
                expandIcon={<ExpandMore />}
                aria-controls={`${id}-panel1-content`}
                id={`${id}-panel1-header`}
              >
                <Typography component="span">Interoperable</Typography>
              </AccordionSummary>
              <AccordionDetails>
                <Typography>
        Data should be compatible with the technical standards used throughout OEPS. File formats, geographic identifiers, coding schemes, and data structures should support efficient integration with existing datasets while minimizing extensive preprocessing or harmonization.
                </Typography>
              </AccordionDetails>
            </Accordion>

            <Accordion >
              <AccordionSummary
                expandIcon={<ExpandMore />}
                aria-controls={`${id}-panel1-content`}
                id={`${id}-panel1-header`}
              >
                <Typography component="span">Reusable</Typography>
              </AccordionSummary>
              <AccordionDetails>
                <Typography>
        Data should include sufficient documentation to support interpretation, future maintenance, and responsible reuse. Information describing variables, processing methods, temporal and spatial coverage, limitations, and licensing improves long-term usability and reproducibility.
                </Typography>
              </AccordionDetails>
            </Accordion>

            <Accordion >
              <AccordionSummary
                expandIcon={<ExpandMore />}
                aria-controls={`${id}-panel1-content`}
                id={`${id}-panel1-header`}
              >
                <Typography component="span">Documentation</Typography>
              </AccordionSummary>
              <AccordionDetails>
                <Typography>
        Data should be accompanied by standardized metadata describing their source, variables, processing methods, geographic and temporal coverage, limitations, and other information necessary to support long-term management and reuse. Detailed documentation requirements are provided in the OEPS Metadata Data Docs.
                </Typography>
              </AccordionDetails>
            </Accordion>

{/* No submit button here (yet?) */}
            {/*<Button type="submit" variant="contained" color="secondary">Submit</Button>*/}
          </Box>
        </Container>
      </main>

      <Gutter rem={8} />

      <Footer position={'fixed'} bottom={0} />
    </div>
  );
}
