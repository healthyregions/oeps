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
        <meta name="description" content="Web explorer for the Opioid Environment Policy Scan data warehouse." />
        <script defer data-domain="oeps.healthyregions.org" src="https://plausible.io/js/script.js"></script>
        <link rel="icon" href="/favicon.ico" />

      </Head>
      <MainNav />
      <main className={styles.main}>
        <div className="row">
          <div className="col-xs-12 col-md-5 col-lg-4">
            <img src="images/oeps_diagram_mk2.png" className={styles.titleDiagram} alt={''} />
            <Gutter em={3} />
          </div>
          <div className="col-xs-12 col-md-7 col-lg-8">
          <h1 className={styles.title}>
            Opioid Environment Policy Scan
          </h1>
          <p className={styles.description}>
          An open data warehouse exploring the multi-dimensional risk environment, from neighborhoods to states,
          impacting opioid use and health outcomes across the United States.
          </p>
          <p className={styles.description}>
          <em><strong>Latest news:</strong></em> In June 2025 we completed an update to data in OEPS, including data from 2020 to 2025.
          You can find all of these data updates right now in the <Link href="/map">map</Link>, and we are in the process of cascading the new data
          to each <Link href="/download">data access</Link> method that we provide. Stay tuned for updates!</p>
          </div>
        </div>

        <Gutter em={2} />
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

          <div className="col-xs-12 col-md-4 col-lg-4 rules-on">
            <img src="images/map.svg" alt="Map and explore data." className={styles.threeUpIcon} />
            <h1 className={styles.subhead}>Map</h1>
            <p>
            Visualize data with our interactive web map.
            </p>
            <p>
            <Link className={styles.docsLink} href="/map" > Start Mapping &gt;</Link>
            </p>
          </div>

          <div className="col-xs-12 col-md-4 col-lg-4">
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
        <Gutter em={2} />
        <div className="row rules center-xs">
          <div className="col-xs-12">
            <h1>What is the OEPS?</h1>
          </div>
          <div className="col-xs-12 col-md-12 col-lg-10">
            <p>
            The Opioid Environment Policy Scan (OEPS) is an open-source data warehouse focused on the
            multi-dimensional risk environment impacting opioid use and health outcomes across the United States.
            </p>
            <p>
            The OEPS provides access to data at multiple spatial scales, from U.S. states down to Census tracts. It is designed
            to support research seeking to study environments impacting and impacted by opioid use and opioid use disorder (OUD),
            inform public policy, and reduce harm in communities nationwide.
            </p>
            <p>
              The OEPS Explorer makes it quick and easy to explore, visualize, and download data. Read more <Link href="/about">about the project</Link>,
              our <Link href="/methods"> methodology</Link>, and our <Link href="/standards">data standards</Link>.
            </p>
            <p>
            The OEPS is led by the <a href="https://healthyregions.org/">Healthy Regions and Policies Lab</a>, based at the
            Department of Geography & GIScience at the University of Illinois at Urbana-Champaign. It was developed for the <a href="https://heal.nih.gov/research/research-to-practice/jcoin">Justice Community Opioid Innovation Network (JCOIN)</a>,
            an NIH HEAL Initiative, as part of the Methodology and Advanced Analytics Resource Center at the University of Chicago.
            </p>
          </div>
        </div>


      </main>
      <Footer />
    </div>
  );
}
