import Head from "next/head";
import styles from "../styles/About.module.css";
import { Gutter } from "../components/layout/Gutter";
import MainNav from "../components/layout/MainNav";
import Footer from "../components/layout/Footer";

export default function About() {
  return (
    <div className={styles.container}>
      <Head>
        <title>Code and Analysis Resources :: OEPS </title>
      </Head>
      <MainNav />
      <main className={styles.main}>
        <h1 className={styles.title}>Code and Analysis Resources</h1>
        <p className={styles.description}>
        Code notebooks and spatial analysis tutorials for research applications
        </p>

        <Gutter em={3} />

        <div className="row">

          <div className="col-xs-12 col-md-4 col-lg-3">
            <h2> Notebooks and Sample Code </h2>
          </div>
          <div className="col-xs-12 col-md-8 col-lg-9">
            <h3><a href="https://healthyregions.github.io/oeps">OEPS Documentation</a></h3>
            <p>The full documentation site includes details about how OEPS is put together, and how the backend application can be used to manage data. This
                documentation site is especially useful for developers who will be working on OEPS, or adding more data into the system.
            </p>
            <h3><a href="https://geodacenter.github.io/opioid-environment-toolkit/index.html">Opioid Environment Toolkit</a></h3>
              <p>
              The Opioid Environment Toolkit provides an <b>introduction to GIS and spatial analysis</b> for opioid environment applications.
              This code toolkit supports researchers, analysts, and practitioners with learning open source spatial analytic and visualization services
              in the R software environment. It includes geocoding MOUD resource locations, linking community contextual data,
              conducting a nearest distance analysis calculating <b>straight line (Euclidean) distance metrics</b>, and more.
            </p>
            <h3><a href="https://colab.research.google.com/drive/1YoX5R6Qeb5gXPVmBSPwyMxw9zza2nFeA?usp=sharing">Calculating Advanced Spatial Access Metrics</a></h3>
            <p>
            This Python notebook provides an overview of how to calculate two spatial access metrics, <b>travel time to the nearest resource </b>
            (i.e. MOUD provider location), and <b>count of resources</b> within a customizable driving time range. Using this beginner-friendly script
            available as a Google Colab notebook, calculate travel time access metrics for different modes of transit and spatial scales. We provide <a href="https://uchicago.box.com/s/ae2mtsw7f5tb4rhciczufdxd0owc23as">pre-computed travel time matrices </a>
            for driving, walking, and biking travel networks, for all 2010 Census tracts and zip codes (ZCTA). <i>Note</i>: The code was revised in 2025 to update and clarify several parameters. Updated vintage files of 2020 boundaries and expanded metrics will be available over the summer of 2025.
            </p>
            <h3><a href="https://access.readthedocs.io/en/latest/index.html">Spatial Access for PySAL</a></h3>
            <p>
            Developed by CSDS researchers and colleagues, this Python Spatial Analysis Library (PySAL) package
            implements a new spatial access measure, Rational Agent Access Model (RAAM), that simultaneously <b>accounts for travel time and congestion at the destination</b>.
            This package also calculates <b>five classic spatial access models</b> for easy comparison, including Floating Catchment Areas (FCA), Two-Step FCAs, and Access Score.
            </p>
          </div>
        </div>

      <Gutter em={2} />

      <div className="row">
          <div className="col-xs-12 col-md-4 col-lg-3">
          <h2> Workshops and Trainings</h2>
          </div>
          <div className="col-xs-12 col-md-8 col-lg-9">
          <h3>Spatial Dimensions of Opioid Risk Environments: Virtual Workshops (2021)</h3>
            <p>
            This <a href= "https://www.jcoinctc.org/maarc-virtual-workshop-series-summer-2021/">three-part workshop series </a> hosted by the MAARC is designed to help researchers, analysts, and practitioners develop stronger spatial
            data analytic and visualization skills. Led by the Healthy Regions/CSDS MAARC team, these workshops introduce basic spatial
            analytic functionalities using open source tools, mainly in R and GeoDa, using applied examples. The workshops were
            originally hosted live and recorded in Summer 2021 for JCOIN partners. The complete recordings are available below.
            </p>
            <h4> Workshop 1: Introduction to Spatial Analysis for Opioid Risk Environments <a href="https://www.youtube.com/watch?v=8JLm_sF7gaA&t=2940s">[Recording]</a></h4>
            <p>
              This workshop introduces participants to the Opioid Environment Policy Scan (OEPS data warehouse, key concepts in spatial data analysis, and generating simple maps using the free spatial software
              <a href="https://geodacenter.github.io/"> GeoDa</a>.
            </p>
            <h4> Workshop 2: Geocoding and Linking Community Data <a href="https://www.youtube.com/watch?v=dHfQAhXXwh0&t=14s">[Recording]</a></h4>
            <p>
            This workshop introduces open source methods for geocoding Medication for Opioid Use Disorder (MOUD) resource locations
            and other address data, integrating community characteristics data using geographic identifiers, and generating maps for exploratory analysis.
            </p>
            <h4> Workshop 3: Developing Custom Spatial Access Metrics <a href="https://www.youtube.com/watch?v=SF5UumM1INk">[Recording]</a></h4>
            <p>
            This workshop instructs how to conduct a nearest resource analysis for MOUD resources at the community level,
            calculate minimum distance access metrics, and generate maps overlaying resource locations and access metrics for further analysis.
            </p>

          </div>
        </div>

        <Gutter em={2} />


      <div className="row">
          <div className="col-xs-12 col-md-4 col-lg-3">
            <h2> Additional Resources</h2>
          </div>
          <div className="col-xs-12 col-md-8 col-lg-9">
          <h4> Geospatial Consortium & Community of Practice (GCCP) </h4>
            <p>
            The GCCP, launched in 2025, is a collaboration of researchers and practitioners that 
            meet regularly to share, discuss, and learn how geospatial methods, tools, and models 
            can be used to build understanding and develop resources for the opioid epidemic. As part 
            of the JCOIN Community, we focus on justice populations, though we’ll also be seeking how 
            to measure and model multiple communities & places across the U.S. To do that, we’ll be 
            linking fields across epidemiology, medicine, geography, GIS, data science, and more. 
            Learn more and sign up at the <a href="http://gccp.healthyregions.org">GCCP Website</a>.
          </p>
          <h4> Opioid Environment Toolkit </h4>
            <p>
            The <a href="https://geodacenter.github.io/opioid-environment-toolkit/index.html">Opioid Environment Toolkit</a> provides an introduction to GIS and spatial analysis in R for opioid environment
            applications that will allow researchers, analysts, and practitioners to support their communities with better
            data analytics and visualization services. Chapters include Introduction to Spatial Data, Geocoding Resource Locations,
            Thematic Mapping, and Nearest Resource Analysis.
            </p>
            <h4> US COVID Atlas </h4>
            <p>
            For historical Pandemic data, resources have been moved to the <a href="https://www.uscovidatlas.org">US COVID Atlas</a>,
            a historic, interactive data visualization platform and archive. The Atlas worked to understand,
            represent, and share stories of the often unequal impact of the COVID-19 pandemic in the United States, 
            from January 2020 through the end of 2023.
            Data includes daily and weekly case counts, vaccination rates, and community health contexts.
            Read more and explore at <a href="https://www.uscovidatlas.org">USCovidAtlas.org</a>.
            </p>

          </div>
        </div>

{/* <div className="row">
    <div className="col-xs-12 col-md-4 col-lg-3">
      <h2> Talks </h2>
    </div>
    <div className="col-xs-12 col-md-8 col-lg-9">
      <h3> Opioid Environment Policy Scan: Open data for analyzing and visualizing the opioid risk environment </h3>
      <p>
      This talk was presented at the American Association of Geographers (AAG) Annual Conference in February 2022 by Susan Paykin.
      It contextualizes the risk environment framework and outlines the data and structure of the OEPS.
      Slides are available on <a href="https://github.com/spaykin/aag2022">GitHub</a>.
      </p>

    </div>
  </div> */}

  <Gutter em={2} />


      </main>
      <Footer />
    </div>
  );
}
