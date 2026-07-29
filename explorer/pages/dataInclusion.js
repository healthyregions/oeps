import Head from "next/head";
import MainNav from "@components/layout/MainNav";
import styles from "@styles/About.module.css";
import {
  Accordion,
  AccordionDetails,
  AccordionSummary,
  Box,
  Checkbox,
  Container,
  FormControlLabel,
  Radio,
  RadioGroup,
  Switch,
  Typography
} from "@mui/material";
import {useId} from "react";
import {ExpandMore} from "@mui/icons-material";
import TextField from "@mui/material/TextField";
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
        <h1 className={styles.title}>Data Inclusion</h1>
        <p className={styles.description}>
          Guidelines for submitting data to the OEPS Data Ecosystem
        </p>

        <Container maxWidth="lg">
          <Box component="form" onSubmit={handleSubmit} sx={{ mt: 4, display: 'flex', flexDirection: 'column', gap: 2 }}>
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
                  This is an Accordion whose sections can be collapsed.
                  <br/>
                  You can copy/paste/modify these sections to lay out the data inclusion page.
                </Typography>
              </AccordionDetails>
            </Accordion>

            <Accordion>
              <AccordionSummary
                expandIcon={<ExpandMore />}
                aria-controls={`${id}-panel2-content`}
                id={`${id}-panel2-header`}
              >
                <Typography component="span">Example Form Controls</Typography>
              </AccordionSummary>
              <AccordionDetails>
                <Typography>
                  Here is a set of simple form controls that can be copy/pasted to help lay out this page.
                  <br/>
                  The behavior to submit the form details can be wired up once we know all the fields and the process for submission.
                </Typography>
                <hr/>

                {/* Example: Checkbox */}
                <FormControlLabel control={<Checkbox defaultChecked color={'secondary'} />} label="Example Checkbox" />

                <hr/>

                {/* Example: RadioGroup (aka radio buttons) */}
                <Typography>Example RadioGroup</Typography>
                <RadioGroup
                  defaultValue="hello"
                >
                  <FormControlLabel value="hello" control={<Radio color={'secondary'} />} label="Hello" />
                  <FormControlLabel value="world" control={<Radio color={'secondary'} />} label="World" />
                  <FormControlLabel value="other" control={<Radio color={'secondary'} />} label="Other" />
                </RadioGroup>


                <hr/>

                {/* Example: Switch (aka toggle) */}
                <FormControlLabel value="hello" control={<Switch color={'secondary'} />} label="Example Switch" />

                <hr/>

                <TextField label="Example TextField" variant="outlined" color={'secondary'} placeholder={'Placeholder text...'}></TextField>

                <hr/>

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
