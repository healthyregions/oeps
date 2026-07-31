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
            <h2> Computational Notebooks & Coding Resources </h2>
          </div>
          <div className="col-xs-12 col-md-8 col-lg-9">
            <h3>Opioid Environment Toolkit in R-Spatial</h3>
              <p> This toolkit provides an <b>introduction to GIS and spatial analysis</b> for opioid environment applications.
              This code toolkit supports researchers, analysts, and practitioners with learning open source spatial analytic and visualization services
              in the R software environment. It includes geocoding MOUD resource locations, linking community contextual data, calculating new spatial variables, and 
              conducting access analyses. All code, data, and workshops are free and open to public participation. </p>
              
              <h4><a href="https://healthyregions.github.io/opioid-environment-toolkit/">Opioid Environment Toolkit 2.0 (2026)</a></h4>
              <p>The latest, refactored toolkit series includes an improved  experience, and will move from beginner to intermediate geocomputational and analytic examples. 
              The first workshop, <a href="https://www.youtube.com/watch?v=SF5UumM1INk">Intro To Spatial Data in R </a>
              was published in 2025, with updated modules to be published and shared in the <a href="https://gccp.healthyregions.org/">
              GCCP workshop series </a> through 2027. </p>
                
            <h4><a href="https://geodacenter.github.io/opioid-environment-toolkit/index.html">Opioid Environment Toolkit 1.0 (2021)</a></h4>
            <p> The original version of the toolkit was developed from 2020 to 2021, and may be used with corresponding series of recorded workshops including: 
             <a href="https://www.youtube.com/watch?v=8JLm_sF7gaA&t=2940s"> (1) Introduction to Spatial Analysis for Opioid Risk Environments</a>, 
             <a href="https://www.youtube.com/watch?v=dHfQAhXXwh0&t=14s"> (2) Geocoding and Linking Community Data</a>, and 
             <a href="https://www.youtube.com/watch?v=SF5UumM1INk"> (3) Developing Custom Spatial Access Metrics</a>  </p>
            
              {/* //<a href="https://colab.research.google.com/drive/1YoX5R6Qeb5gXPVmBSPwyMxw9zza2nFeA?usp=sharing"></a> */}

            <h3>Calculating Spatial Access Metrics in Py</h3>
            <p>
            We developed geocomputational notebooks using Python for calculating, visualizing, merging, and/or writing spatial access measures. This spatial feature engineering
            was also used to generate many of the spatial access metrics available in OEPS. We include pre-computer travel time matrices for the country as key components 
            to each approach, as well as sample data from OEPS for exploration and replication purposes. Both 2010 and 2020 Census vintage is supported. </p>
            <ol>
              <li><a href="https://drive.google.com/file/d/17ChX_4-EcX3XTjcn6RQOAWeGW_IWGfTf/view?usp=drive_link"><b>Calculate travel time to nearest resource: </b></a> 
              This notebook provides an overview of how to calculate two spatial access metrics, travel time to the nearest resource and count of resources within a 
              customizable driving time range. Using this beginner-friendly script
            available as a Google Colab notebook, calculate travel time access metrics for different modes of transit and spatial scales.  </li><br></br>
              <li><a href="https://drive.google.com/file/d/1X3cpz3Xuf73OQ2O1uAGHpMrP_KRhycrt/view?usp=sharing"><b>Calculate gravity model estimates for one state: </b></a>
              Gravity model estimates incorporate both supply (resources) and demand (people), better accounting
              for population distributions in varying service needs. This notebook can be calculated on Colab and most analytic machines.</li><br></br>
              <li><a href=""><b>Calculate gravity model estimates for country: </b></a>To scale things up, this notebook can generate nation-wide estimates of gravity model measures
              with the aid of high performance computing environment.</li>
            </ol>
          
          </div>
        </div>

      <Gutter em={2} />


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
          <h4> SDOH & Place Project </h4>
            <p>
            Looking for even more coding resources and data options to better measure and understand the social determinants of health (SDOH)
            and structural drivers of wellbeing? The <a href="http://sdohplace.org">SDOH & Place project</a> provides multiple resources and a 
            community of practice. Learn how to develop your own spatial web mapping application or dashboard. Uncover dozens of new SDOH datasets
            across multiple spatial scales at the Data Discovery Tool.
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
