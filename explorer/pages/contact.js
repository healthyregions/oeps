import Head from "next/head";
import MainNav from "@components/layout/MainNav";
import styles from "@styles/About.module.css";
import {Box, Button, Container, InputLabel, Select} from "@mui/material";

import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import {useState} from "react";
import TextField from "@mui/material/TextField";
import Footer from "@components/layout/Footer";
import {Gutter} from "@components/layout/Gutter";
import Snackbar from "@mui/material/Snackbar";

export default function Contact() {

  const googleFormUrl = `${process.env.NEXT_PUBLIC_EMAIL_FORM_URL}`
  const slackFormUrl = `${process.env.NEXT_PUBLIC_SLACK_FORM_SUBMISSION_URL}`

  const messageTypes = [
    'General',
    'Bug Report or Error',
    'Data Question',
    'Feature Request',
    'Technical or Open Source Questions',
    'Press or Media'
  ];

  // Form state
  const [formData, setFormData] = useState({
    Category: 'General',
    Contact_Name: '',
    Contact_Email: '',
    Contact_Phone: '',
    Message: ''
  });
  const handleChange = (e) => {
    const propName = e.target.name;
    const propValue = e.target.value;
    setFormData({ ...formData, [propName]: propValue });
    isValid(formData, propName, propValue);
  };

  // Success confirmation
  const [submitting, setSubmitting] = useState(false);
  const [submitted, setSubmitted] = useState(false);
  const handleClose = () => {
    setSubmitted(false);
    setSubmitting(false);
  }

  // Error state + Validation
  const emailRegexPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
  const phoneRegexPattern = /^(\+\d{1,2}\s?)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$/;
  const [formErrors, setFormErrors] = useState({
    Category: '',
    Contact_Name: '',
    Contact_Email: '',
    Contact_Phone: '',
    Message: ''
  });

  const isValidName = (propValue) => {
    if (!propValue) {
      setFormErrors({ ...formErrors, Contact_Name: 'Name is required' });
      return false;
    }
    setFormErrors({ ...formErrors, Contact_Name: '' });
    return true;
  }

  const isValidEmail = (propValue) => {
    if (!propValue) {
      setFormErrors({...formErrors, Contact_Email: 'Email is required'});
      return false;
    } else if (!emailRegexPattern.test(propValue)) {
      setFormErrors({...formErrors, Contact_Email: 'Must be a valid email address'});
      return false;
    }
    setFormErrors({...formErrors, Contact_Email: ''});
    return true;
  }

  const isValidPhone = (propValue) => {
    if (!propValue) {
      // Empty is a valid case for phone (which is optional)
      setFormErrors({...formErrors, Contact_Phone: ''});
      return true;
    } else if (!phoneRegexPattern.test(propValue)) {
      setFormErrors({...formErrors, Contact_Phone: 'Must be a valid phone number'});
      return false;
    }
    setFormErrors({...formErrors, Contact_Phone: ''});
    return true;
  }

  const isValidMessage = (propValue) => {
    if (!propValue) {
      setFormErrors({...formErrors, Message: 'Please enter your message'});
      return false;
    }
    setFormErrors({...formErrors, Message: ''});
    return true;
  }

  const isValid = (formState, propName, propValue) => {
    switch(propName) {
      // If no propName is provided, then we validate entire form
      default: {
        let valid = true;
        ['Contact_Name', 'Contact_Email', 'Contact_Phone', 'Message'].forEach((propName) => {
            const propValue = formState[propName];
            if (!isValid(formState, propName, propValue)) {
              valid = false;
            }
          }
        );
        return valid;
      }
      case 'Contact_Name': {
        return isValidName(propValue);
      }
      case 'Contact_Email': {
        return isValidEmail(propValue);
      }
      case 'Contact_Phone': {
        return isValidPhone(propValue);
      }
      case 'Message': {
        return isValidMessage(propValue);
      }
    }
  }

  const generateURL = async (data, googleFormUrl) => {
    let returnURL = `${googleFormUrl}?Date=${encodeURIComponent(new Date().toISOString().slice(0,10))}`
    for (const property in data){
      returnURL += `&${encodeURIComponent(property)}=${encodeURIComponent(data[property])}`
    }
    return returnURL
  }
  const handleSubmit = async (e) => {
    e.preventDefault();
    if (isValid(formData)) {
      try {
        setSubmitting(true);

        // Send feedback to Google Sheet
        const gSheetURL = await generateURL(formData, googleFormUrl);
        await fetch(gSheetURL, {method: 'GET'});

        // Send feedback notification to Slack channel
        let slackText = `Submission from ${window.location.href}`
        slackText += `\n*Name:* ${formData.Contact_Name}`
        slackText += `\n*Email:* ${formData.Contact_Email}`
        slackText += `\n*Phone:* ${formData.Contact_Phone}`
        slackText += `\n*Message Category:* ${formData.Category}`
        slackText += `\n---\n${formData.Message}`
        await fetch(slackFormUrl, {
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
          },
          method: 'POST',
          body: JSON.stringify({text: slackText})
        });

        // Clear out the form and notify the user
        setFormData({Category: 'General', Contact_Name: '', Contact_Email: '', Message: '', Contact_Phone: ''});

        // Notify the user of success
        setSubmitted(true);
      } finally {
        setSubmitting(false);
      }
    }
  };

  return (
    <div className={styles.container}>
      <Head>
        <title>Contact Us</title>
      </Head>
      <MainNav />
      <main className={styles.main}>
        <h1 className={styles.title}>Contact Us</h1>
        <p className={styles.description}>
          Hit a problem? Want to share feedback or feature suggestions?
        </p>

        <Container maxWidth="sm">
          <Box component="form" onSubmit={handleSubmit} sx={{ mt: 4, display: 'flex', flexDirection: 'column', gap: 2 }}>
            <FormControl fullWidth>
              <InputLabel color={'secondary'} id="message-type-select-label">Message Type</InputLabel>
              <Select
                variant={'filled'}
                color={'secondary'}
                labelId="message-type-select-label"
                id="message-type-select"
                label="Message Type"
                name="type"
                value={formData.Category}
                error={!!formErrors.Category}
                //helperText={formErrors.type}
                onChange={handleChange}
              >
                {messageTypes?.map((type, index) =>
                  <MenuItem key={`select-option-${index}`} value={type}>{type}</MenuItem>
                )}
              </Select>
            </FormControl>

            <TextField color={'secondary'} label="Name" name="Contact_Name" placeholder="Your Name" error={!!formErrors.Contact_Name} helperText={formErrors.Contact_Name} value={formData.Contact_Name} onChange={handleChange} required fullWidth />
            <TextField color={'secondary'} label="Email" name="Contact_Email" type="email" placeholder="greetings@you.com" error={!!formErrors.Contact_Email} helperText={formErrors.Contact_Email} value={formData.Contact_Email} onChange={handleChange} required fullWidth />
            <TextField color={'secondary'} label="Phone (optional)" name="Contact_Phone" type="phone" placeholder="111-867-5309" error={!!formErrors.Contact_Phone} helperText={formErrors.Contact_Phone} value={formData.Contact_Phone} onChange={handleChange} fullWidth />
            <TextField color={'secondary'} label="Message" name="Message" placeholder="Your message..." error={!!formErrors.Message} helperText={formErrors.Message} value={formData.Message} onChange={handleChange} multiline minRows={5} maxRows={10} required fullWidth />

            <Button type="submit" variant="contained" color="secondary" loading={submitting}>Send</Button>
          </Box>

          <Snackbar
            open={submitted}
            anchorOrigin={{ vertical: 'top', horizontal: 'center' }}
            autoHideDuration={6000}
            onClose={handleClose}
            message="Feedback has been sent"
          />
        </Container>
      </main>

      <Gutter rem={8} />

      <Footer position={'fixed'} bottom={0} />
    </div>
  );
}
