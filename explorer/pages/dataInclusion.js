import Head from "next/head";
import MainNav from "@components/layout/MainNav";
import styles from "@styles/About.module.css";
import {Accordion, AccordionDetails, AccordionSummary, Checkbox, RadioGroup, Switch, Typography} from "@mui/material";
import {useId} from "react";
import {ExpandMore} from "@mui/icons-material";
import {Form} from "@base-ui/react";
import {RadioButton} from "grommet";
import TextField from "@mui/material/TextField";

export default function DataInclusion() {
  const id = useId();
  return (
    <>
      <Head>
        <title>Data Inclusion</title>
      </Head>
      <MainNav />
      <main className={styles.main}>
        <h1 className={styles.title}>Data Inclusion</h1>
        <p className={styles.description}>
          Guidelines for submitting data to the OEPS Data Ecosystem
        </p>

        <Accordion defaultExpanded>
          <AccordionSummary
            expandIcon={<ExpandMore />}
            aria-controls={`${id}-panel1-content`}
            id={`${id}-panel1-header`}
          >
            <Typography component="span">Expanded by default</Typography>
          </AccordionSummary>
          <AccordionDetails>
            <Typography>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse
              malesuada lacus ex, sit amet blandit leo lobortis eget.
            </Typography>
          </AccordionDetails>
        </Accordion>

        <Accordion>
          <AccordionSummary
            expandIcon={<ExpandMore />}
            aria-controls={`${id}-panel2-content`}
            id={`${id}-panel2-header`}
          >
            <Typography component="span">Header</Typography>
          </AccordionSummary>
          <AccordionDetails>
            <Typography>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse
              malesuada lacus ex, sit amet blandit leo lobortis eget.
            </Typography>
            <Form>
              <Checkbox />
              <RadioGroup>
                <RadioButton name={'hello'} />
                <RadioButton name={'world'} />
              </RadioGroup>
              <Switch></Switch>
              <TextField></TextField>
            </Form>
          </AccordionDetails>
        </Accordion>
      </main>
    </>
  );
}
