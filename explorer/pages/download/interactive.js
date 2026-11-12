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
          Build a filtered OEPS subset by spatial scale, theme or variables,
          and optional years, then download a zip containing one CSV from a
          constrained BigQuery query. Variable columns are labeled with a
          2-digit table-year suffix. For full packages and individual CSVs, use{" "}
          <Link href="/download">Data Access</Link>.
        </p>
        <Gutter em={1} />
        <h2>Filter by scale, variables, and year</h2>
        <InteractiveDownloadFilters />
      </main>
      <Footer />
    </div>
  );
}
