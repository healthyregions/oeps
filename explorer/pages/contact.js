import Head from "next/head";
import MainNav from "@components/layout/MainNav";
import styles from "@styles/About.module.css";
import {Box, Button, Container, Grid, InputLabel, Select, Typography} from "@mui/material";

import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import {useState} from "react";
import TextField from "@mui/material/TextField";
import Footer from "@components/layout/Footer";
import {Gutter} from "@components/layout/Gutter";

export default function Contact() {
  const messageTypes = [
    'General',
    'Bug Report or Error',
    'Data Question',
    'Feature Request',
    'Technical or Open Source Questions',
    'Press or Media'
  ];

  // Form state
  const [form, setForm] = useState({ type: 'General', name: '', email: '', phone: '', message: '' });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    alert('Form was not actually submitted!');
    setForm({ type: 'General', name: '', email: '', message: '', phone: '' });
  };

  // Validation patterns:
  const emailRegexPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
  const phoneRegexPattern = /^(\+\d{1,2}\s?)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$/;
  const phoneRegexPatternUsaOnly = /^(\+0?1\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$/;

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
              <InputLabel id="message-type-select-label">Message Type</InputLabel>
              <Select
                variant={'filled'}
                labelId="message-type-select-label"
                id="message-type-select"
                value={form.type}
                label="Message Type"
                onChange={handleChange}
              >
                {messageTypes?.map((type, index) =>
                  <MenuItem key={`select-option-${index}`} value={type}>{type}</MenuItem>
                )}
              </Select>
            </FormControl>

            <TextField label="Name" name="name" placeholder="Your Name" value={form.name} onChange={handleChange} required fullWidth />
            <TextField label="Email" name="email" type="email" placeholder="greetings@you.com" value={form.email} onChange={handleChange} required fullWidth />
            <TextField label="Phone" name="phone" type="phone" placeholder="111-876-5309" value={form.phone} onChange={handleChange} fullWidth />
            <TextField label="Message" name="message" value={form.message} placeholder="Your message..." onChange={handleChange} multiline minRows={5} maxRows={10} required fullWidth />

            <Button type="submit" variant="contained" color="secondary">Send</Button>
          </Box>
        </Container>
      </main>

      <Gutter rem={8} />

      <Footer position={'fixed'} bottom={0} />
    </div>
  );
}
