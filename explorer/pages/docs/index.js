import Head from "next/head";
import { useState, useMemo } from 'react';
import styles from "../../styles/Docs.module.css";
import { Gutter } from "../../components/layout/Gutter";
import MainNav from "../../components/layout/MainNav";
import Footer from "../../components/layout/Footer";
import variables from '../../meta/variables.json';

const VariableTable = ({table, filters}) =>
<div className={styles.tableContainer}>
  <table className={styles.variableTable}>
    <tbody>
    <tr>
      <th>Variable Construct</th>
      <th>Variable Proxy</th>
      <th>Source</th>
      <th>Metadata</th>
      <th>Spatial Scale</th>
      <th>Years</th>
    </tr>
    {table.map(row => (!filters.scale.length || filters.scale.some(scale => row['Spatial Scale'].includes(scale))) ? <tr key={row['Variable Construct']}>
      <td width="15%">{row['Variable Construct']}</td>
      <td width="25%">{row['Variable Proxy']}</td>
      <td width="15%">{row['Source']}</td>
      <td width="15%"><ul>{row['Metadata'].map((docTitle, index) => <li key={`${docTitle}-${index}`}><a href={`docs/${docTitle}`}>{docTitle}</a></li>)}</ul></td>
      <td width="15%">{row['Spatial Scale']}</td>
      <td width="15%">{row['Years']}</td>
    </tr> : null)}
    </tbody>
  </table>
</div>

const tableNames = Object.keys(variables);

const uniqueScales = [
  'State',
  'County',
  'Tract',
  'Zip'
]

const ResourceSection=() => {
  return <div>
    <div className={styles.rowContainer}>
              <div className="row">
              <div className="col-xs-12 col-lg-3">
                <h2>Geocoded Data Resources</h2>
              </div>
              <div className="col-xs-12 col-lg-9">
                <ul>
                  <li> <a href="https://github.com/GeoDaCenter/opioid-policy-scan/tree/v1.0/data_final/moud">MOUD Provider Locations (SAMHSA, 2019)</a></li>
                  <li> <a href="https://github.com/GeoDaCenter/opioid-policy-scan/tree/fc3d94053dd1941a96a5945d73cc6f4845453484/data_final/Health%20Resources">Opioid Treatment Program (OTP) Locations (SAMHSA, 2020)</a> </li>
                  <li> <a href="https://github.com/GeoDaCenter/opioid-policy-scan/tree/fc3d94053dd1941a96a5945d73cc6f4845453484/data_final/Health%20Resources">FQHC Locations (HRSA, 2020)</a></li>
                  <li> <a href="https://github.com/GeoDaCenter/opioid-policy-scan/tree/fc3d94053dd1941a96a5945d73cc6f4845453484/data_final/Health%20Resources">Hospital Locations (CovidCareMap, 2020)</a></li>
                  <li> <a href="https://github.com/GeoDaCenter/opioid-policy-scan/tree/fc3d94053dd1941a96a5945d73cc6f4845453484/data_final/Health%20Resources">Mental Health Provider Locations (SAMHSA, 2020)</a></li>
                </ul>
              </div>
              </div>
              <Gutter em={2} />
            </div>
            <div className={styles.rowContainer}>
              <div className="row">
              <div className="col-xs-12 col-lg-3">
                <h2>Travel Time Matrices</h2>
              </div>
              <div className="col-xs-12 col-lg-9">
                <p>National travel time matrices calculated for origin-destination (O:D) pairs of Census tract and ZCTA centroids for
                  multiple modes of transit: driving, biking, and walking. Matrices calculated using Open Source Routing Machine (<a href= "http://project-osrm.org/">OSRM</a>) in 2020. Download matrices at the links below. </p>
              </div>
              <div className="col-xs-12 col-lg-3">
                <h4>Census Tract </h4>
              </div>
              <div className="col-xs-12 col-lg-9">
                <ul>
                  <li> <a href="https://uchicago.box.com/s/t5h8l5efq4sjixnfj213tmrwdl3c53wu">Tract Driving</a></li>
                  <li> <a href="https://uchicago.box.com/s/tizxrph0t35khzqzzd6tkzbxtumu0qaa">Tract Biking</a> </li>
                  <li> <a href="https://uchicago.box.com/s/1ago3se2zjqul8ip59whg7x1z7fcfoui">Tract Walking</a> </li>
                </ul>
              </div>
              <div className="col-xs-12 col-lg-3">
                <h4>Zip Code Tract Areas (ZCTA) </h4>
              </div>
              <div className="col-xs-12 col-lg-9">
                <ul>
                  <li> <a href="https://uchicago.box.com/s/03yxfypbou26vpb47ktwetd6cb6kmm3h">ZCTA Driving</a></li>
                  <li> <a href="https://uchicago.box.com/s/f5nwqts2bjl6ks9ljdvss0yhdfwqrzqd">ZCTA Biking</a> </li>
                  <li> <a href="https://uchicago.box.com/s/coig0oyjz7py532nhzkt8cp3jkd2xx8n">ZCTA Walking</a> </li>
                </ul>
              </div>
              <Gutter em={2} />
              </div>
            </div>
  </div>
}

export default function DataDocs() {
  const [activeMd, setActiveMd] = useState(false)
  const [activeFilters, setActiveFilters] = useState({
    scale: [],
    topic: []
  })

  const MainHead = () => useMemo(() => <Head>
    <title>About :: OEPS Dashboard</title>
    <meta name="description" content="Generated by create next app" />
    <script defer data-domain="oeps.healthyregions.org" src="https://plausible.io/js/script.js"></script>
    <link rel="icon" href="/favicon.ico" />
  </Head>,[])

  const handlefilter = (val, type) => {
    setActiveFilters(prev => {
      let previousType = prev[type].length ? [...prev[type]] : [];
      let parsed = previousType.includes(val)
        ? [...previousType.slice(0, previousType.indexOf(val)), ...previousType.slice(previousType.indexOf(val)+1, previousType.length)]
        : [...previousType, val]

      return {
        ...prev,
        [type]: parsed
      }
    })
  }

  return (
    <div className={`${styles.container} ${activeMd ? styles.fixed : ''}`} tabIndex={activeMd ? -1 : 0}>
      <MainHead />
      <MainNav />
      <main className={styles.main}>
        <h1 className={styles.title}>Data Docs</h1>
        <Gutter em={1} />
        <p>Variable constructs are grouped thematically below to highlight the multi-dimensional risk environment of opioid use in justice populations. In the <b>Metadata</b> column, linked pages provide more detail about the data source, descriptions of data cleaning or processing, and individual variables included.</p>
        <Gutter em={1} />
        <div className="row">
          <div className="col-xs-12 col-md-8">
            <h3>Filter by Topic</h3>
            {tableNames.map(topic => <button key={topic} onClick={() => handlefilter(topic, 'topic')} className={`${styles.filterButton} ${activeFilters.topic.includes(topic) ? styles.active : ' '}`}>{topic}</button>)}
          </div>
          <div className="col-xs-12 col-md-4">
            <h3>Filter by Scale</h3>
            {uniqueScales.map(scale => <button key={scale} onClick={() => handlefilter(scale, 'scale')} className={`${styles.filterButton} ${activeFilters.scale.includes(scale) ? styles.active : ' '}`}>{scale}</button>)}
          </div>
        </div>
        <Gutter em={2} />

        {tableNames.map(header =>
          (
            (!activeFilters.topic.length || activeFilters.topic.includes(header))
            &&
            (!activeFilters.scale.length || variables[header].some(row => activeFilters.scale.some(scale => row['Spatial Scale'].includes(scale))))
          )
          &&
          <>
          <div className={styles.rowContainer} key={header}>
              <div className="row">
                <div className="col-xs-12 col-lg-2">
                  <h3>{header}</h3>
                </div>
                <div className="col-xs-12 col-lg-10">
                  <VariableTable table={variables[header]} setActive={setActiveMd} filters={activeFilters} />
                </div>
                <Gutter em={2} />
              </div>
          </div>
          </>
        )}
        <Gutter em={2} />
      <ResourceSection />
      </main>
      <Footer />
    </div>
  );
}
