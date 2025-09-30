import Head from "next/head";
import Link from 'next/link';
import styles from "../styles/Home.module.css";
import { Gutter } from "../components/layout/Gutter";
import MainNav from "../components/layout/MainNav";
import Footer from "../components/layout/Footer";

// const diagram = [
//   {
//     name:'oeps-diagram',
//     photo: 'oeps-diagram.png',
//   }
// ]

export default function Home() {
  return (
    <div className={styles.container}>
      <Head>
        <title>OEPS Explorer</title>
      </Head>
      <MainNav />
      <main className={styles.main}>
        <div className="row">
          <div className="col-xs-12 col-md-5 col-lg-4">
            <img src="images/logo-factors.png" className={styles.titleDiagram} alt={''} />
            <Gutter em={3} />
          </div>
          <div className="col-xs-12 col-md-7 col-lg-8">
          <h1 className={styles.title}>
            Opioid Environment Policy Scan
          </h1>
          <p className={styles.description}>
          An open data warehouse, mapping platform, and data ecosystem that explores the multi-dimensional risk environment, from neighborhoods to states,
          impacting opioid use and health outcomes across the United States.
          </p>
          <br></br>
                    <hr></hr>
          <p>
          <em><strong>Updates:</strong></em> Version 2.2 was released in September 2025 and includes updated and 
          standardized metadata, pre- and post-Pandemic data suites, and extensive data quality updates.</p>

          </div>
        </div>

        <Gutter em={3} />
        <div className="row rules">
          <div className="col-xs-12 col-md-4 col-lg-4">
            <img src="images/data.svg" alt="Data Documentation and download." className={styles.threeUpIcon} />
            <h1 className={styles.subhead}>Data</h1>
            <p>
              Access data by theme or spatial scale and explore our methdology.
            </p>
            <p>
            <Link
                className={styles.docsLink}
                href="/download "
              >
                Data Access & Download &gt;
                </Link>
            </p>
            <p>
            <Link
                className={styles.docsLink}
                href="/docs "
              >
              Documentation &gt;
              </Link>
              </p>
              <p>
            <Link
                className={styles.docsLink}
                href="/methods "
              >
              Methodology &gt;
              </Link>
              </p>

          </div>

          <div className="col-xs-12 col-md-4 col-lg-4">
            <img src="images/map.svg" alt="Map and explore data." className={styles.threeUpIcon} />
            <h1 className={styles.subhead}>Map</h1>
            <p>
            Visualize data with our interactive web map.
            </p>
            <p>
            <Link className={styles.docsLink} href="/map" > Start Mapping &gt;</Link>
            </p>
          </div>

          <div className="col-xs-12 col-md-4 col-lg-4 ">
            <img src="images/insights.svg" alt="Data findings and further information." className={styles.threeUpIcon} />
            <h1 className={styles.subhead}>Insights</h1>
            <p>
              Learn about the OEPS, code resources, and research insights .
            </p>
            <p>
            <Link className={styles.docsLink} href="/about ">About &gt;</Link>
            </p>
            <p>
            <Link className={styles.docsLink} href="/codeResources ">Code Resources &gt;</Link>
            </p>
            <p>
            <Link className={styles.docsLink} href="/insights">Insights &gt;</Link>
            </p>
              <p></p>
          </div>
        </div>
 
        <Gutter em={3} />
        <div className="row rules center-xs">
          <div className="col-xs-12 col-md-12 col-lg-10">
                           <hr></hr>
            <p className={styles.description}>
            The OEPS data ecosystem was designed to support research seeking to study environments impacting and impacted by opioid use and opioid use disorder (OUD),
            inform public policy, and reduce harm in communities nationwide. It provides access 
            to data at multiple spatial scales and time periods, already cleaned, merged, and documented. Read more <Link href="/about">about the project</Link>,
            our <Link href="/methods"> methodology</Link>, and <Link href="/insights">insights</Link>.
            </p>
            <p>
            OEPS is led by the <a href="https://healthyregions.org/">Healthy Regions and Policies Lab</a>, based at the
            Department of Geography & GIScience at the University of Illinois at Urbana-Champaign. It was developed for the <a href="https://heal.nih.gov/research/research-to-practice/jcoin">Justice Community Overdose Innovation Network (JCOIN)</a>,
            a NIH HEAL Initiative, as part of the Methodology and Advanced Analytics Resource Center at the University of Chicago.
            </p>
          </div>
        </div>


      </main>
      <Footer />
    </div>
  );
}
