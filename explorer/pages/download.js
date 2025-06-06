import Head from "next/head";
import Link from 'next/link';
import { 
  // useState, 
  useMemo } from 'react';
import styles from "../styles/Docs.module.css";
import { Gutter } from "../components/layout/Gutter";
import MainNav from "../components/layout/MainNav";
import Footer from "../components/layout/Footer";
import csvDownloads from '../meta/csvDownloads.json';
// import * as JSZip from 'jszip';
// import { saveAs } from 'file-saver';

// const years = [
//   '1980',
//   '1990',
//   '2000',
//   '2010',
//   'Latest'
// ]

// const uniqueScales = [
//   'State',
//   'County',
//   'Tract',
//   'Zip'
// ]

// const scalesDict = {
//     'S':'State',
//     'C':'County',
//     'T':'Tract',
//     'Z':'Zip'
// }

// const shpParts = ['.dbf','.prj','.shp', '.shx','.cpg']

// const geomsDict = [{
//     agg: 'State',
//     year: "Latest",
//     folder: 'geometryFiles/state/',
//     baseFileName: 'states2018'
//   },{
//     agg: 'County',
//     year: "Latest",
//     folder: 'geometryFiles/county/',
//     baseFileName: 'counties2018'
//   },{
//     agg: 'Tract',
//     year: "Latest",
//     folder: 'geometryFiles/tract/',
//     baseFileName: 'tracts2018'
//   },{
//     agg: 'Zip',
//     year: "Latest",
//     folder: 'geometryFiles/zcta/',
//     baseFileName: 'zctas2018'
//  },{
//   agg: 'State',
//   year: "2010",
//   folder: 'geometryFiles/state/',
//   baseFileName: 'states2010'
// },{
//   agg: 'County',
//   year: "2010",
//   folder: 'geometryFiles/county/',
//   baseFileName: 'counties2010'
// },{
//   agg: 'Tract',
//   year: "2010",
//   folder: 'geometryFiles/tract/',
//   baseFileName: 'tracts2010'
//  }
// ]

// const BASE_CSV_URL = 'https://raw.githubusercontent.com/GeoDaCenter/opioid-policy-scan/main/data_final/'

export default function Download() {
  // const [downloadMessage, setDownloadMessage] = useState('')
  // const [zipPct, setZipPct] = useState(-1)
//   const [activeFilters, setActiveFilters] = useState({
//     scale: [],
//     year: []
//   })

    const MainHead = () => useMemo(() => <Head>
        <title>Download :: OEPS </title>
        <meta name="description" content="Generated by create next app" />
        <script defer data-domain="oeps.healthyregions.org" src="https://plausible.io/js/script.js"></script>
        <link rel="icon" href="/favicon.ico" />

    </Head>,[])

//     const handlefilter = (val, type) => {
//         setActiveFilters(prev => {
//         let previousType = prev[type].length ? [...prev[type]] : [];
//         let parsed = previousType.includes(val)
//             ? [...previousType.slice(0, previousType.indexOf(val)), ...previousType.slice(previousType.indexOf(val)+1, previousType.length)]
//             : [...previousType, val]

//         return {
//             ...prev,
//             [type]: parsed
//         }
//         })
//     }

//     const handleDownload = async () => {
//       setDownloadMessage('Starting download...')
//       let filesToDownload = [...csvFiles]

//       if (activeFilters.scale.length) {
//         filesToDownload = filesToDownload.filter(entry => activeFilters.scale.includes(scalesDict[entry.scale]))
//       }

//       if (activeFilters.year.length) {
//         filesToDownload = filesToDownload.filter(entry => activeFilters.year.includes(entry.year))
//       }

//       let geomsToDownload = [...geomsDict]
// //      if (activeFilters.year.length !== 0 && !activeFilters.year.includes('Geographic Boundaries')){
// //        geomsToDownload = []
// //      }
      
//       if (activeFilters.scale.length){
//         geomsToDownload = geomsToDownload.filter(f => activeFilters.scale.includes(f.agg))
//       }

//       if (activeFilters.year.length){
//         let historic_data_requested = activeFilters.year.some(yr => ['2010', '2000', '1990', '1980'].includes(yr))
//         geomsToDownload = geomsToDownload.filter(f => activeFilters.year.includes(f.year) || (historic_data_requested && f.year === '2010'))
//       }

//       let geomPromises = [];
//       geomsToDownload.forEach(geometry => {
//         shpParts.forEach(shpPart => {
//           geomPromises.push(fetch(BASE_CSV_URL + geometry.folder + geometry.baseFileName + shpPart).then(r=>r.blob()))
//         })
//       })

//       // declare promises
//       const dataPromises = filesToDownload.map(entry => fetch(BASE_CSV_URL + entry.folder + entry.file + '.csv').then(r=>r.blob()))
//       const docsLinks = await fetch('https://api.github.com/repos/geodacenter/opioid-policy-scan/contents/data_final/metadata').then(r=>r.json()).then(items => items.map(d => ({'name':d.name, 'url': d.download_url})).filter(f => f.url !== null))
//       const docsPromises = await docsLinks.map(link => fetch(link.url).then(r=>r.blob()))

//       // fetch data and docs
//       const docs = await Promise.all(docsPromises).then(values => values.map((v,i) => ({'name':docsLinks[i].name, 'data':v})))
//       setDownloadMessage(`Downloaded ${docs.length} documentation files. Downloading ${filesToDownload.length} CSV files...`)
//       const data = await Promise.all(dataPromises).then(values => values.map((v,i) => ({'name':`${filesToDownload[i].file}.csv`, 'data':v})))
//       setDownloadMessage(`Downloaded ${data.length} CSV files. Downloading ${geomsToDownload.length} geometr${geomsToDownload.length > 1 ? 'ies' : 'y'}...`)
//       const geom = await Promise.all(geomPromises).then(values => values.map((v,i) => ({'name':`${geomsToDownload[Math.floor(i/7)].baseFileName}${shpParts[i%5]}`, 'data':v})))

//       var zip = new JSZip();
//       var dataFolder = zip.folder("data");
//       var docsFolder = zip.folder("docs");
//       var geomFolder = zip.folder("geometry");

//       data.forEach(d => dataFolder.file(d.name, d.data))
//       docs.forEach(d => docsFolder.file(d.name, d.data))
//       geom.forEach(d => geomFolder.file(d.name, d.data))
//       setDownloadMessage(`Building your ZIP archive, this may take a minute...`)

//       zip.generateAsync(
//         {
//           type:"blob",
//           compression: "STORE",
//       }, (meta) => setZipPct(meta.percent)).then(content => {
//         saveAs(content, `OEPS_DOWNLOAD_${new Date().toISOString().slice(0,10)}.zip`);
//       }).then(() => {setDownloadMessage(''); setZipPct(-1)})
//     }

  return (
    <div className={styles.container}>
      <MainHead />
      <MainNav />
      <main className={styles.main}>
        <h1 className={styles.title}>Data Access</h1>
        <Gutter em={1} />
        <p>There are many different ways to download or access OEPS data, find the one that works best for you. You may also be interested in our <Link href="/codeResources">code resources</Link> page with notebooks and tutorials.</p>
        <div className={styles.downloadsContainer}>
          <div>
            <Link className={styles.fullDownload} href="#data-dictionaries"><span>CSVs & Data<br/>Dictionaries</span></Link>
          </div>
          <div>
            <Link className={styles.fullDownload} href="#frictionless-data-package"><span>Frictionless Data Package</span></Link>
          </div>
          <div>
            <Link className={styles.fullDownload} href="#oeps-data-package"><span>oepsData<br/>(R data package)</span></Link>
          </div>
          <div>
            <Link className={styles.fullDownload} href="#big-query"><span>Google BigQuery</span></Link>
          </div>
        </div>
        <div className="row" style={{paddingTop:"2em"}}>

          <div className="col-xs-12 col-md-4 col-lg-3">
            <h2 style={{marginTop:0}}>Direct Download</h2>
          </div>
          <div className="col-xs-12 col-md-8 col-lg-9">
            <h3 id="data-dictionaries">CSVs & Data Dictionaries</h3>
              <p>Not sure where to start? These data dictionaries provide a comprehensive overview of what variables are available for each geography&mdash;State (S), County (C), Census Tract (T), and Zip Code Tabulation Area (Z).</p>
              <ul>
                <li><Link href="https://github.com/healthyregions/oeps/raw/refs/heads/main/backend/oeps/data/dictionaries/S_Dict.xlsx">S_Dict.xlsx</Link></li>
                <li><Link href="https://github.com/healthyregions/oeps/raw/refs/heads/main/backend/oeps/data/dictionaries/C_Dict.xlsx">C_Dict.xlsx</Link></li>
                <li><Link href="https://github.com/healthyregions/oeps/raw/refs/heads/main/backend/oeps/data/dictionaries/T_Dict.xlsx">T_Dict.xlsx</Link></li>
                <li><Link href="https://github.com/healthyregions/oeps/raw/refs/heads/main/backend/oeps/data/dictionaries/Z_Dict.xlsx">Z_Dict.xlsx</Link></li>
              </ul>
              <p>OEPS datasets are merged into single CSVs, one per geography (State, County, Tract, ZCTA) per year (1980, 1990, etc.).
                Each CSV can be joined to an appropriate <Link href="#geometry-files">geometry file</Link> using the HEROP_ID field.</p>
                <h4>State</h4>
              <div className={styles.tableContainer}>
                <table className={styles.variableTable}>
                  <tbody>
                    <tr>
                      <th>Year</th>
                      <th>File</th>
                    </tr>
                    {csvDownloads.state.map(row => 
                    <tr key={row.name}>
                        <td>{row.year}</td>
                        <td><Link href={row.url}>{row.name}</Link></td>
                    </tr>)}
                  </tbody>
                </table>
              </div>
              <h4>County</h4>
              <div className={styles.tableContainer}>
                <table className={styles.variableTable}>
                  <tbody>
                    <tr>
                      <th>Year</th>
                      <th>File</th>
                    </tr>
                    {csvDownloads.county.map(row => 
                    <tr key={row.name}>
                        <td>{row.year}</td>
                        <td><Link href={row.url}>{row.name}</Link></td>
                    </tr>)}
                  </tbody>
                </table>
              </div>
              <h4>Tract</h4>
              <div className={styles.tableContainer}>
                <table className={styles.variableTable}>
                  <tbody>
                    <tr>
                      <th>Year</th>
                      <th>File</th>
                    </tr>
                    {csvDownloads.tract.map(row => 
                    <tr key={row.name}>
                        <td>{row.year}</td>
                        <td><Link href={row.url}>{row.name}</Link></td>
                    </tr>)}
                  </tbody>
                </table>
              </div>
              <h4>Zip Code Tabulation Area (ZCTA)</h4>
              <div className={styles.tableContainer}>
                <table className={styles.variableTable}>
                  <tbody>
                    <tr>
                      <th>Year</th>
                      <th>File</th>
                    </tr>
                    {csvDownloads.zcta.map(row => 
                    <tr key={row.name}>
                        <td>{row.year}</td>
                        <td><Link href={row.url}>{row.name}</Link></td>
                    </tr>)}
                  </tbody>
                </table>
              </div>
            <h3 id="geometry-files">Geometry Files</h3>
            <p>For spatial analysis we provide our geographic datasets generated from the US Census Bureau&apos;s Cartographic Boundary files (500k scale). We provide the following formats: Shapefile, GeoJSON, or PMTiles.</p>
            <ul>
                <li><Link href="/docs/GeographicBoundaries">Go to download links and metadata</Link></li>
            </ul>
            <h4>Joining to geometry files:</h4>
            <ul>
                <li>Use 2010 geometry files when joining to any OEPS data from 1980, 1990, 2000, or 2010. Use the 2018 geometry files for any later datasets up to 2020.</li>
                <li>Use 2020 geometry files for all geographies and years 2020 and beyond.</li>
                <li><strong>In Connecticut:</strong> For county and tract data from 2022 or later you must use 2022 geographies because county (and therefore tract) FIPS ids changed between 2021 and 2022. To translate 2022 tracts back to 2020 geometries, you can use <Link href="https://www.ctdata.org/geographic-resources">these crosswalks</Link> from CT Data Collaborative.</li>
            </ul>
            <h3 id="frictionless-data-package">Frictionless Data Package</h3>
            <p>We provide a single data package with all CSV and Shapefile assets which is structured to match the Data Package specification published by <Link href="https://frictionlessdata.io/">Frictionless Data</Link>.</p>
            <ul>
              <li><Link href="https://github.com/GeoDaCenter/opioid-policy-scan/releases/download/untagged-e509eea25fb66a9a1f90/oeps-data-package-v2_2024-12-05.zip">Download package (208mb)</Link></li>
              <li><Link href="https://specs.frictionlessdata.io/">Frictionless Data Package v1 spec</Link></li>
            </ul>
          </div>
        </div>

        <div className="row" style={{paddingTop:"2em"}}>

          <div className="col-xs-12 col-md-4 col-lg-3">
            <h2 style={{marginTop:0}}>Programmatic Access</h2>
          </div>
          <div className="col-xs-12 col-md-8 col-lg-9">
            <h3 id="oeps-data-package"><Link href="https://oepsdata.healthyregions.org">oepsData &mdash; R Package</Link></h3>
              <p>We maintain a small R package called <Link href="https://oepsdata.healthyregions.org">oepsData</Link>. This package is the best way for researchers who use R to load and analyze OEPS data directly, without the need to download CSVs or Shapefiles and worry about joins.</p>
              <ul>
                <li><Link href="https://oepsdata.healthyregions.org">Documentation</Link>: Learn how to install and use the package.</li>
                <li><Link href="https://oepsdata.healthyregions.org/examples.html">Usage examples</Link>: Within the package docs we have a few examples of what it looks like to load and use OEPS data.</li>
                <li><Link href="https://github.com/healthyregions/oepsdata">GitHub</Link>: Use the GitHub repo to report issues you have with the package, or suggest new features or datasets.</li>
              </ul>
              <p><em>Current release: v0.1</em></p>
            <h3 id="big-query">Google BigQuery</h3>
              <p>We have loaded the OEPS data warehouse into Google BigQuery, a data storage platgorm that provides the ability for researchers to run SQL queries (including spatial queries) to retrieve or perform analysis on specific data subsets. Google publishes many <Link href="https://cloud.google.com/bigquery/docs/reference/libraries">different clients</Link> through which you can access a BigQuery database, and for R users there is <Link href="https://bigrquery.r-dbi.org/">bigrquery</Link>. Here&apos;s how to get started:</p>
              <ul>
                <li><Link href="https://oepsdata.healthyregions.org/getting-oeps-data-from-bigquery.html">Introduction to OEPS in Google BigQuery</Link>: The oepsData documentation includes a detailed overview that is relevant no matter what client you use.</li>
                <li><Link href="https://oepsdata.healthyregions.org/getting-oeps-data-from-bigquery.html#setting-up-bigquery">Setting up BigQuery in R</Link>: The oepsData documentation also has a walkthrough guide illustrating how R users can connect directly to our data in BigQuery.</li>
                <li><Link href="https://github.com/healthyregions/oeps/blob/main/docs/reference/big-query-tables.md">Database Table Reference</Link>: Full reference document, provides the project id and the names of all tables and columns.</li>
              </ul>
          </div>
        </div>

        {/* <Gutter em={5} />

        <h2>Filter Data and Download</h2>

        <div className="row">
          <div className="col-xs-12 col-md-8">
            <h3>Filter by Year</h3>
            {years.map(year => <button key={year} onClick={() => handlefilter(year, 'year')} className={`${styles.filterButton} ${activeFilters.year.includes(year) ? styles.activeDownload : ' '}`}>{year}</button>)}
          </div>
          <div className="col-xs-12 col-md-4">
            <h3>Filter by Scale</h3>
            {uniqueScales.map(scale => <button key={scale} onClick={() => handlefilter(scale, 'scale')} className={`${styles.filterButton} ${activeFilters.scale.includes(scale) ? styles.activeDownload : ' '}`}>{scale}</button>)}
          </div>
        </div>
        <Gutter em={4} />
        {downloadMessage.length ? <div>
            <img src='/images/globe_min.svg' className={styles.loader} alt={''} />
            <h4>{downloadMessage}</h4>
            {zipPct > -1 && <div className={styles.progressContainer}>
              <span className={styles.progressBar} style={{width: `${zipPct}%`}}/>
            </div>}
        </div> : null}
        <button className={`${downloadMessage.length !== 0 ? styles.passiveButton : ''} ${styles.downloadButton}`} onClick={handleDownload} disabled={downloadMessage.length !== 0}>Download Selected Data</button> */}
        
      </main>
      <Footer />
    </div>
  );
}
