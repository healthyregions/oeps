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
          Build a filtered OEPS subset by year era (Historic 1980–2000,
          DSuite2018, or DSuite2023), spatial scale, and theme or variables,
          then download a zip containing one CSV from a constrained BigQuery
          query.
          Variable columns are labeled with a 2-digit table-year suffix. For
          full packages and individual CSVs, use{" "}
          <Link href="/download">Data Access</Link>.
        </p>
        <div className={styles.rulesCallout} role="note">
          <p className={styles.rulesCalloutTitle}>Keeping leading zeros in Excel</p>
          <p className={styles.selectionHint}>
            The CSV already keeps leading zeros on geography codes (
            <code>FIPS</code> for state, county, and tract; <code>ZCTA5</code>{" "}
            for ZCTA)—for example <code>01005</code>, not <code>1005</code>.
            Opening the file with Excel&apos;s default CSV open can drop those
            zeros. To keep them: Data → From Text/CSV → set Data Type Detection
            to &quot;Do not detect data types&quot;, then load the file.
          </p>
        </div>
        <Gutter em={1} />
        <h2>Filter by package era, scale, and variables</h2>
        <InteractiveDownloadFilters />
      </main>
      <Footer />
    </div>
  );
}
