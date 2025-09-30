import Head from "next/head";
import Link from 'next/link';
import styles from "../styles/Docs.module.css";
import { Gutter } from "../components/layout/Gutter";
import MainNav from "../components/layout/MainNav";
import Footer from "../components/layout/Footer";

export default function About() {
  return (
    <div className={styles.container}>
      <Head>
        <title>Methods :: OEPS</title>
      </Head>
      <MainNav />
      <main className={styles.main}>
        <h1 className={styles.title}>Methodology</h1>

      <Gutter em={5} />

        <div className="row">
          <div className="col-xs-12 col-md-4 col-lg-3">
            <h2> Risk Environment Framework</h2>
          </div>
          <div className="col-xs-12 col-md-8 col-lg-9">
            <p>
                Organization and data selection for the OEPS is guided by a risk environment framework (<a href= "https://www.sciencedirect.com/science/article/pii/S0955395902000075">Rhodes 2002</a>).
                The “risk environment” as a framework for understanding and reducing drug-related harms emphasizes the broader contextual domains
                in which opioid use occurs.
            </p>
            <p>
                Our approach is further rooted in the socioecological model of substance use,
                which includes multiple levels of the physical and social environments that interact and overlap to impact health.
                We apply this socio-ecological model of health and use it to further build on previous research on risk environments
                (Cooper et al 2016, Ciccarone 2017).
            </p>
            <p>
                Data and research models must reflect this transdisciplinary and multi-level approach. The risk environment framework
                shifts the focus of drug-related harm research away from individuals,
                and toward environmental factors driving or enabling trends at the community level.
                We see this approach encouraging greater understanding of the spatial and community contexts in which opioid use harm occurs.
            </p>
          </div>
        </div>

      <Gutter em={2} />

      <div className="row">
          <div className="col-xs-12 col-md-4 col-lg-3">
            <h2>Multiple Spatial Scales</h2>
          </div>
          <div className="col-xs-12 col-md-8 col-lg-9">
            <p>
                Most datasets are available at multiple spatial scales, including Census tract,
                ZIP Code or ZIP Code Tract Area (ZCTA), county, and state. You can filter and explore available datasets by spatial scale <Link href="/docs">here</Link>.
            </p>


          </div>
        </div>

        <Gutter em={2} />

    <div className="row">
        <div className="col-xs-12 col-md-4 col-lg-3">
        <h2>Data Themes</h2>
        </div>
        <div className="col-xs-12 col-md-8 col-lg-9">
        <p>
        Data included in the OEPS is grouped thematically for ease of exploration, indices development, and model integration.
        Data is stratfied across six themes:
        </p>
        <ul>
        <li> <b>Social:</b> Household Characteristics, Demographic measures, Race and Ethnicity, Disability measures, Incarceration rates, Veteran population, Educational Characteristics, Residential Segregation Measures, and Community Overlay Variables </li>
        <li> <b>Economic:</b> Employment Trends, Poverty Measures, and Income Inequality</li>
        <li> <b>Environment:</b> Access to Healthcare Providers, Housing Characteristics, Internet Access, Greenspace Measures, Urbanicity/Rurality, and Alchohol Outlet Density </li>
        <li> <b>Policy:</b> State, county, and local policies that may influence access to treatment and/or criminal justice </li>
        <li> <b>Outcomes:</b> Opioid Indicators and Hepatitis C Rate measures</li>

        </ul>
        <p> <i>Note: Historic Covid-19 data was moved to the <a href="https://www.USCovidAtlas.org">US COVID Atlas</a> --
        a free and open source pandemic data archive and visualization tool, also led by the Healthy Regions and Policies Lab.</i>  </p>

        <p> The OEPS also includes <Link href="/download#geography-files">geography boundary shapefiles</Link> from the US Census Bureau’s TIGER/Line (multiple years) for Census tracts, ZCTAs, counties, and states.</p>

    </div>
  </div>

  <Gutter em={2} />

        <div className="row">
          <div className="col-xs-12 col-md-4 col-lg-3">
            <h2>Census Vintages</h2>
          </div>
          <div className="col-xs-12 col-md-8 col-lg-9">
            <p>
                The OEPS data warehouse holds values for variables that span many different decades. Depending on the data year, different Census vintages must be used for the spatial analysis. In general, for any data from 2010 or older, use 2010 Census data. For 2011-2022 data, use the 2018 vintage, and for datasets from 2023 and later, use 2020 vintage. In our prepared <Link href="/download#data-packages">data packages</Link>, a single set of geography files will be included (easy!). If you are directly downloading individual CSVs, you can use the <Link href="/download#csv-downloads">CSV download tables</Link> to determine which geography vintage the data should be joined to.
            </p>


          </div>
        </div>

        <Gutter em={2} />

    <div className="row">
        <div className="col-xs-12 col-md-4 col-lg-3">
        <h2>Data Standards</h2>
        </div>
        <div className="col-xs-12 col-md-8 col-lg-9">
        <p><strong>"No data" values</strong> our CSVs will simply have a blank entry. This means that for a given variable and geographic unit there is no value in the source dataset. Keep in mind that "0" is a valid value for many different measures and should not be treated as "no data".</p>
        <p><b>Most variable names are no more than 10 characters (with some exceptions)</b> for ease of data wrangling with
        shapefiles and GIS software. Some variable names are therefore shortened or abbreviated from the source data.
        </p>
        <p><b>Numbers are either integers or rounded to two decimal places.</b> In our <Link href="https://github.com/healthyregions/oeps/blob/main/docs/src/reference/registry/variables.csv">data registry</Link> you can find a full list of every variable and its data type.
        </p>
        <p>We use a <b>HEROP_ID</b> field in all geography files and CSVs to serve as a <strong>unified geographic identifier for joins</strong>. Other common identifiers, like GEOID, ZIP5, and FIPS may also be included, depending on the file. The HEROP_ID is similar to what the American FactFinder used (now data.census.gov), and it consists of three parts:</p>
        <ol>
          <li>The 3-digit <Link href="https://www.census.gov/programs-surveys/geography/technical-documentation/naming-convention/cartographic-boundary-file/carto-boundary-summary-level.html">Summary Level Code</Link> for this geography. Common summary level codes are:
            <ul>
              <li><code>040</code> -- <strong>State</strong></li>
              <li><code>050</code> -- <strong>County</strong></li>
              <li><code>140</code> -- <strong>Census Tract</strong></li>
              <li><code>860</code> -- <strong>Zip Code Tabulation Area (ZCTA)</strong></li>
            </ul>
          </li>
          <li>
            The 2-letter string <code>US</code>
          </li>
          <li>The standard <Link href="https://www.census.gov/programs-surveys/geography/guidance/geo-identifiers.html">GEOID</Link> for the given unit (length depends on what type of unit)
          <ul>
            <li>GEOIDs are, in turn, hierarchical aggregations of FIPS codes</li>
          </ul>
          </li>
        </ol>
    <p>Expanding out the FIPS codes for the five summary levels shown above, the full IDs would look like:</p>
    <div className={styles.tableContainer}>
    <table className={styles.variableTable}>
    <thead>
        <tr>
            <th>Summary Level</th>
            <th>Format</th>
            <th>HEROP_ID Length</th>
            <th>Example</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>State</td>
            <td><code>040US</code> + <code>STATE</code></td>
            <td>7</td>
            <td><code>040US17</code> (Illinois)</td>
        </tr>
        <tr>
            <td>County</td>
            <td><code>050US</code> + <code>STATE</code> + <code>COUNTY</code></td>
            <td>10</td>
            <td><code>050US17019</code> (Champaign County)</td>
        </tr>
        <tr>
            <td>Tract</td>
            <td><code>140US</code> + <code>STATE</code> + <code>COUNTY</code> + <code>TRACT</code></td>
            <td>16</td>
            <td><code>140US17019005900</code></td>
        </tr>
        <tr>
            <td>ZCTA</td>
            <td><code>860US</code> + <code>ZIP CODE</code></td>
            <td>10</td>
            <td><code>860US61801</code></td>
        </tr>
    </tbody>
</table>
    </div>
<p>
  The advantages of this composite ID are:</p>
  <ol>
    <li>Unique across all geographic areas in the US</li>
    <li>Will always be forced to string formatting</li>
    <li>Easy to programmatically change back into the more standard GEOIDs</li>
  </ol>

  <h5>Converting HEROP_IDs to GEOIDs (integers)</h5>
    <p>
HEROP_IDs can be converted back to standard GEOIDs by removing the first 5 characters, or by taking everything after the substring "US". Here are some examples of what this looks like in different environments:
  </p>
  <div className={styles.tableContainer}>
    <table className={styles.variableTable}>
    <thead>
        <tr>
            <th>Environment</th>
            <th>Example</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Excel</td>
            <td><code>REPLACE(A1, 1, 5, "")</code></td>
        </tr>
        <tr>
            <td>R</td>
            <td><code>geoid &lt;- str_split_i(HEROP_ID, "US", -1)</code></td>
        </tr>
        <tr>
            <td>Python</td>
            <td><code>geoid = HEROP_ID.split("US")[1]</code></td>
        </tr>
        <tr>
            <td>JavaScript</td>
            <td><code>const geoid = HEROP_ID.split("US")[1]</code></td>
        </tr>
    </tbody>
</table>
    </div>

    </div>
  </div>

  <Gutter em={2} />

    <div className="row">
        <div className="col-xs-12 col-md-4 col-lg-3">
        <h2>Documentation</h2>
        </div>
        <div className="col-xs-12 col-md-8 col-lg-9">
        <p>
        Please refer to the <Link href= "/docs">Metadata Docs</Link>{" "}
        {/* or the complete <a href= "https://docs.google.com/document/d/18NPWpuUfFTrKll9_ERHzVDmpNCETTzwjJt_FsIvmSrc/edit?usp=sharing">Data Documentation </a> */}
         for more information about individual datasets and variables.
        </p>

    </div>
  </div>


      </main>
      <Footer />
    </div>
  );
}
