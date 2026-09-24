import Head from "next/head";
import Link from "next/link";
import styles from "../../styles/Docs.module.css";
import { Gutter } from "../../components/layout/Gutter";
import MainNav from "../../components/layout/MainNav";
import Footer from "../../components/layout/Footer";
import InteractiveDownloadFilters from "../../components/download/InteractiveDownloadFilters";

export default function InteractiveDownload() {
  return (
    <div className={styles.container}>
      <Head>
        <title>Interactive Download :: OEPS </title>
      </Head>
      <MainNav />
      <main className={styles.main}>
        <p>
          <Link href="/download">&larr; Return to Data Access</Link>
        </p>
        <h1 className={styles.title}>Interactive Download</h1>
        <Gutter em={1} />
        <p>
          Build a filtered OEPS subset by year, spatial scale, and theme or
          variables, then download a CSV via a constrained BigQuery query. For
          full packages and individual CSVs, use{" "}
          <Link href="/download">Data Access</Link>.
        </p>
        <Gutter em={1} />
        <h2>Filter by year, scale, and theme</h2>
        <InteractiveDownloadFilters />
      </main>
      <Footer />
    </div>
  );
}
