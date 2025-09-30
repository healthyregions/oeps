import Head from "next/head";
import Link from 'next/link';
import styles from "../styles/About.module.css";
import { Gutter } from "../components/layout/Gutter";
import MainNav from "../components/layout/MainNav";
import Footer from "../components/layout/Footer";

const contributors = [
  {
    name:'Adam Cox',
    photo: 'adam.jpg',
    link: 'https://github.com/mradamcox'
  },
  {
    name:'Sara Lambert',
    photo: 'sara.jpg',
    link: 'https://github.com/bodom0015'
  },
  {
    name:'Marynia Kolak',
    photo: 'marynia.jpg',
    link: 'https://github.com/Makosak'
  },
]

export default function About() {
  return (
    <div className={styles.container}>
      <Head>
        <title>About :: OEPS </title>
      </Head>
      <MainNav />
      <main className={styles.main}>
        <h1 className={styles.title}>About OEPS</h1>
        <Gutter em={2} />
        <div className="row">
          <div className="col-xs-12 col-md-4 col-lg-3">
            <h2>About</h2>
          </div>
          <div className="col-xs-12 col-md-8 col-lg-9">
            <p>
            The Opioid Environment Policy Scan (OEPS) is an open-source data warehouse and ecosystem to help characterize
            the multi-dimensional risk environment impacting opioid use and health outcomes across the United States.
            </p>
            <p>
            OEPS provides access to data at multiple spatial scales, from U.S. states down to Census tracts. It is designed
            to support research seeking to study environments impacting and impacted by opioid use and opioid use disorder (OUD),
            inform public policy, and reduce harm in communities nationwide.
            </p>
            <p>
            We developed OEPS as a free, open-source platform to aggregate and share publicly-available data at the Census tract, zip code, county, and state levels.
            Geographic boundary shapefiles are provided for ease of merging datasets (csv files) for exploration, spatial analysis, or visualization.
            </p>
            <p>
            Visit the <Link href="/download"> Data Access</Link> page for download links and introduction to libraries that provide programmatic access to OEPS data, or 
            <Link href="/codeResources"> Code Resources</Link> for tutorials and notebooks.
            Learn more about our methods and approaches, including the risk environment framework, on the <Link href="/methods">Methodology</Link> page.
            </p>
          </div>
        </div>
        <div className="row">
          <div className="col-xs-12 col-md-4 col-lg-3">
            <h2>Releases</h2>
          </div>
          <div className="col-xs-12 col-md-8 col-lg-9">
            <ul>
              <li><strong>v2.3</strong> (planned) January, 2026</li>
              <li><strong>v2.2</strong> (current) September, 2025 [<Link href="https://github.com/healthyregions/oeps/releases/tag/v2.2">release notes</Link>]</li>
              <li><strong>v2.1</strong> June, 2025 [<Link href="https://github.com/healthyregions/oeps/releases/tag/v2.1">release notes</Link>]</li>
              <li><strong>v2.0</strong> December, 2024 [<Link href="https://github.com/GeoDaCenter/opioid-policy-scan/releases/tag/v2.0">release notes</Link>]</li>
              <li><strong>v1.0</strong> January, 2022 [<Link href="https://github.com/GeoDaCenter/opioid-policy-scan/releases/tag/v1.0">release notes</Link>]</li>
            </ul>
          </div>
        </div>
        <Gutter em={2} />
            <div className="row">
          <div className="col-xs-12 col-md-4 col-lg-3">
            <h2>Open Source</h2>
          </div>
          <div className="col-xs-12 col-md-8 col-lg-9">
          <p>
            All data, metadata descriptions, and code is available on our <a href="https://github.com/GeoDaCenter/opioid-policy-scan">GitHub</a>.
            As an open source project, we encourage users to
            <a href="https://docs.github.com/en/issues/organizing-your-work-with-project-boards/tracking-work-with-project-boards/adding-issues-and-pull-requests-to-a-project-board"> add an issue </a>
            on GitHub for questions, bugs, or data requests, or <a href="https://docs.github.com/en/get-started/quickstart/fork-a-repo">fork the repo </a>
            to access locally.
            </p>
          </div>
        </div>

        <Gutter em={2} />
        <div className="row">
          <div className="col-xs-12 col-md-4 col-lg-3">
            <h2>Team</h2> <a id="team"></a>
          </div>
          <div className="col-xs-12 col-md-8 col-lg-9">
            <div className={"row " + styles.contributorsContainer}>
              {contributors.map(entry =>
                <div className="col-xs-12 col-md-3 col-lg-3" key={entry.name}>
                  <img src={`images/team/${entry.photo}`} alt={''}/>
                  <h3><a href={entry.link}>{entry.name}</a></h3>
                  <h4>{entry.title}</h4>
                </div>)}
            </div>
            <p>
            The OEPS Project is led by the <a href="https://www.healthyregions.org">Healthy Regions and Policies Lab</a> (HEROP) at the
            Department of Geography & GIScience at the University of Illinois at Urbana-Champaign. 
            It was developed for the <a href="https://heal.nih.gov/research/research-to-practice/jcoin">Justice Community Opioid Innovation Network (JCOIN)</a>,
            a NIH HEAL Initiative, as part of the Methodology and Advanced Analytics Resource Center (MAARC). The HEROP Lab leads the Geospatial Core of the MAARC, 
            which is otherwise based out of University of Chicago Medicine.
            Data and additional resources are also available to the JCOIN Network through the
            <a href="https://jcoin.datacommons.io/login"> JCOIN Data Commons</a>. OEPS was originally developed at the University of Chicago in 2019
            before moving to UIUC in 2022.
            </p>
            <p>
              Past contributors include Ashlynn Wimer, Susan Paykin, Dylan Halpern, Qinyun Lin, Moksha Menghaney, and Angela Lin, as well as Research Assistants (RAs)
              Margot Bolanos Gamez, Alexa Jin, Ally Muszynski, and Rachel Vigil.
            </p>
            <p>
              <a href="https://www.healthyregions.org/team">Learn more</a> about the current HEROP team.
            </p>
          </div>
        </div>
        <Gutter em={2} />
        <div className="row">
          <div className="col-xs-12 col-md-4 col-lg-3">
            <h2>Contact</h2>
          </div>
          <div className="col-xs-12 col-md-8 col-lg-9">
            <p>
            Submit an issue on <a href="https://github.com/healthyregions/oeps">GitHub</a>,
            or email <a href="mailto:mkolak@illinois.edu">Marynia Kolak</a> with any questions.
            </p>
          </div>
        </div>
        <Gutter em={2} />
        <div className="row">
          <div className="col-xs-12 col-md-4 col-lg-3">
            <h2>Citation</h2>
          </div>
          <div className="col-xs-12 col-md-8 col-lg-9">
          <p>
            Adam Cox, Ashlynn Wimer, Sara Lambert, Susan Paykin, Dylan Halpern, Qinyun Lin, Moksha Menghaney, Angela Li,
            Rachel Vigil, Margot Bolanos Gamez, Alexa Jin, Ally Muszynski, and Marynia Kolak. (2024).
            healthyregions/oeps: Opioid Environment Policy Scan (OEPS) Data Warehouse (v2.0). Zenodo.
            <a href= "https://zenodo.org/record/5842465#.YeHj8H3MKHF"> https://doi.org/10.5281/zenodo.5842465</a>
            </p>
            <p>
            <i>This research was supported by the National Institute on Drug Abuse, National Institutes of Health,
            through the NIH HEAL Initiative under award numbers 5UM1DA050098-03 (MAARC 2.0) and UG3DA123456 (MAARC 1.0).
            The contents of this publication are solely the responsibility of the authors and do not necessarily represent
            the official views of the NIH, the Initiative, or the participating sites.</i>
            </p>
          </div>
        </div>
      </main>
      <Footer />
    </div>
  );
}
