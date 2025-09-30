import Head from "next/head";
import styles from "../styles/About.module.css";
import { Gutter } from "../components/layout/Gutter";
import MainNav from "../components/layout/MainNav";
import Footer from "../components/layout/Footer";

export default function About() {
  return (
    <div className={styles.container}>
      <Head>
        <title>Insights :: OEPS </title>
      </Head>
      <MainNav />
      <main className={styles.main}>
        <h1 className={styles.title}>Insights</h1>
        <p className={styles.description}>
        Research, data tools, and extensions of OEPS data.
        </p>

        <Gutter em={2} />

        <div className="row">
        <div className="col-xs-12 col-md-8 col-lg-12">
        <p>
        Understanding the drivers and impacts of opioid use disorder (OUD) necessitates a nuanced, place-based consideration 
        of communities and varying dimensions of risk. We lead, collaborate, and consult on multiple projects that bring a holistic perspective to OUD social and spatial epidemiology,
        building on a “risk environment” conceptual model with a social determinants of health sensibility. </p>
        <p>Researchers also access and reference OEPS data in their own research. 
        If you have used OEPS and would like to be added to the research list below, please let us know! Submit your addition as <a href="https://github.com/healthyregions/oeps/issues">a new issue</a> in Github.
        </p>
        </div>

        <p className={styles.description}>
        <b>Research Completed Using OEPS</b>
        </p>

        <div className="row">
          <div className="col-xs-12 col-md-4 col-lg-3">
            <h2> 2025</h2>
          </div>
          <div className="col-xs-12 col-md-8 col-lg-9">
           <p>
            Balawajder, E.F., Ducharme, L., Taylor, B.G., Lamuda, P.A., Kolak, M., Friedmann, P.D., Pollack, H.A. and Schneider, J.A., 
            2025. Barriers to Universal Availability of Medications for Opioid Use Disorder in US Jails. <i>JAMA network open</i>, 8(4),
             pp.e255340-e255340.
           </p>
           </div>
        </div>


        <div className="row">
          <div className="col-xs-12 col-md-4 col-lg-3">
            <h2> 2024</h2>
          </div>
          <div className="col-xs-12 col-md-8 col-lg-9">
          <p>
            Aalsma, M.C., Bell, L.A., Schwartz, K., Ouyang, F., Kolak, M., Monahan, P.O., Mermelstein, S.P., Carson, I., Hulvershorn, 
            L.A. and Adams, Z.W., 2024. Clinician willingness to prescribe medications for opioid use disorder to adolescents in Indiana. 
            <i>JAMA network open</i>, 7(9), pp.e2435416-e2435416.
           </p>
           <p>
            Balawajder, E.F., Ducharme, L., Taylor, B.G., Lamuda, P.A., Kolak, M., Friedmann, P.D., Pollack, H.A. and Schneider, J.A., 2024. 
            Factors associated with the availability of medications for opioid use disorder in US jails. <i>JAMA network open</i>, 7(9), 
            pp.e2434704-e2434704.
           </p>
           <p>
            Tatara, E., Lin, Q., Ozik, J., Kolak, M., Collier, N., Halpern, D., Anselin, L., Dahari, H., Boodram, B. and Schneider, J., 2024. 
            Spatial inequities in access to medications for treatment of opioid use disorder highlight scarcity of methadone providers 
            under counterfactual scenarios. <i>PLoS computational biology</i>, 20(7), p.e1012307.
           </p>
          </div>
        </div>

      <div className="row">
          <div className="col-xs-12 col-md-4 col-lg-3">
            <h2> 2023</h2>
          </div>
          <div className="col-xs-12 col-md-8 col-lg-9">
           <p>
            Grella, C.E., Scott, C.K., Dennis, M.L. and LaVallee, R.A., 2023. Access to services for pregnant people with opioid use 
            disorder in jails in the United States. <i>Journal of Correctional Health Care</i>, 29(4), pp.299-307.
          </p>
         </div>
      </div>

      <div className="row">
          <div className="col-xs-12 col-md-4 col-lg-3">
            <h2> 2021</h2>
          </div>
          <div className="col-xs-12 col-md-8 col-lg-9">
           <p>
            Schneider, J.A., Taylor, B.G., Hotton, A.L., Lamuda, P.A., Ozik, J., Lin, Q., Flanagan, E., Tuyet Pho, M., Kolak, M., 
            Brewer, R. and Pagkas-Bather, J., 2021. National variability in Americans’ COVID-19 protective behaviors: 
            Implications for vaccine roll-out. <i>PloS one</i>, 16(11), p.e0259257.
           </p>
         </div>
      </div>

      </div>
      <Gutter em={3} />

      <div className="row">
          <div className="col-xs-12 col-md-4 col-lg-3">
            <p className={styles.description}>
            <b> Additional Resources</b></p>
          </div>
          <div className="col-xs-12 col-md-8 col-lg-9">
          <h3> Geospatial Consortium & Community of Practice (GCCP) </h3>
            <p>
            The GCCP, launched in 2025, is a collaboration of researchers and practitioners that 
            meet regularly to share, discuss, and learn how geospatial methods, tools, and models 
            can be used to build understanding and develop resources for the opioid epidemic. As part 
            of the JCOIN Community, we focus on justice populations, though we’ll also be seeking how 
            to measure and model multiple communities & places across the U.S. To do that, we’ll be 
            linking fields across epidemiology, medicine, geography, GIS, data science, and more. 
            Learn more and sign up at the <a href="http://gccp.healthyregions.org">GCCP Website</a>.
            </p>
          <h3> Opioid Environment Toolkit </h3>
            <p>
            The <a href="https://geodacenter.github.io/opioid-environment-toolkit/index.html">Opioid Environment Toolkit</a> provides an introduction to GIS and spatial analysis in R for opioid environment
            applications that will allow researchers, analysts, and practitioners to support their communities with better
            data analytics and visualization services. Chapters include Introduction to Spatial Data, Geocoding Resource Locations,
            Thematic Mapping, and Nearest Resource Analysis.
            </p>
            <h3> US COVID Atlas </h3>
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

        <Gutter em={2} />

{/* <div className="row">
    <div className="col-xs-12 col-md-4 col-lg-3">
      <h2> Ongoing Research</h2>
    </div>
    <div className="col-xs-12 col-md-8 col-lg-9">
      <p>
      <b> Study (021): Spatially Extended Treatment Effect Analysis of Access to MOUD Resources and Changing Policies </b> | PI: Marynia Kolak
      </p>
      <p>
      The Healthy Regions & Policies Lab is developing a geospatial model to decompose and quantify the impact of access to MOUD and related services into different policy scenarios to inform future policy-making. This project will measure how local policies affect the impact of access to medication and service resources on opioid-related health outcomes, and build a risk environment warehouse to index all policy variables, both by spatial scale (census, tract, zip code, and county) and time (year).
      </p>
      <p>
      <b>Study (020): Finding an Optimal Distance of Success: Measuring Access to Critical Resources in Opioid Use Disorder Justice Settings</b> | PI: Marynia Kolak
      </p>
      <p>
      Accessing evidence-based medications and other critical resources for opioid use disorder (MOUD) is critical to saving lives and healing communities,
      yet little is known on how access to these resources is best measured. The University of Chicago is conducting a geospatial modeling study
      to measure optimal distance and access (e.g., availability, affordability, and acceptability) to MOUD and relevant resources to identify a
      threshold of success that contributes to health outcomes. The study uses spatial analysis data and mapping software to identify what critical
      resources are needed at a community level to support individuals with opioid use disorder (OUD).
      </p>
      <p>
      <b>Study (019): Measuring Social and Spatial Inequities in Access to Opioid Use Disorder Treatment for Reducing HIV and HCV Transmissions </b> | PIs: Marynia Kolak and Jonathan Ozik, Argonne National Lab
      </p>
      <p>
      Access to treatment and medication for opioid use disorder (MOUD) is essential for reducing HIV and HCV transmissions.
      However, the spatial distribution of the resources for treatment and medication is a result of various social factors, which can include potential inequities.
      To demonstrate the utility of a spatial perspective in evaluating access to MOUD resources,
      The University of Chicago and Argonne National Laboratory will use a simulation approach to evaluate how treatment and intervention locations
      affect HIV and HCV transmissions. This study will also evaluate interventions using scenarios of varying levels of spatial inequity in HepCEP,
      a validated agent-based model (ABM) for Hepatitis C Elimination in Persons Who Inject Drugs (PWID). Outcomes from this study may
      provide insight into the complex factors that drive MOUD treatment heterogeneity within communities using more spatialized approaches for evaluation of efficacy.
      </p>

    </div>
  </div> */}

      </main>
      <Footer />
    </div>
  );
}
