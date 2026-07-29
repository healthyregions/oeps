import Head from "next/head";
import MainNav from "@components/layout/MainNav";
import styles from "@styles/About.module.css";

export default function Contact() {
  return (
    <>
      <Head>
        <title>Contact Us</title>
      </Head>
      <MainNav />
      <main className={styles.main}>
        <h1 className={styles.title}>Contact Us</h1>
        <p className={styles.description}>
          Ran into a problem? Want to share feedback or suggestions with us?
        </p>
      </main>
    </>
  );
}
