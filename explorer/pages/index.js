import Head from "next/head";
import Link from 'next/link';
import styles from "../styles/Home.module.css";
import {Gutter} from "@components/layout/Gutter";
import MainNav from "@components/layout/MainNav";
import Footer from "@components/layout/Footer";
import {Grid} from "@mui/material";
import postsMetadata from '../content/posts.json';
import {getPostBySlug} from "../lib/markdown";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import {useEffect, useState} from "react";


// const diagram = [
//   {
//     name:'oeps-diagram',
//     photo: 'oeps-diagram.png',
//   }
// ]

// This gets called on every request
export async function getServerSideProps() {
  // Fetch data from external API
  const posts = [];

  for (const metadata of postsMetadata) {
    const post = await getPostBySlug(metadata.slug);
    posts.push(post);
  }

  // Pass data to the page via props
  return {props: {posts}}
}

export default function Home({posts}) {
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    // Waits for server-side props above before first render
    setMounted(true);
  }, []);

  const sections = [{
    name: 'Data',

  }];


  return (
    mounted ? <div className={styles.container}>
      <Head>
        <title>OEPS Explorer</title>
      </Head>
      <MainNav/>
      <main className={styles.main}>
        <div className="row" style={{display: 'flex', alignItems: 'center'}}>
          <div className="col-xs-12 col-md-5 col-lg-4">
            <img src="images/logo-factors.png" className={styles.titleDiagram} alt={''}/>
            <Gutter em={3}/>
          </div>
          <div className="col-xs-12 col-md-7 col-lg-8">
            <h1 className={styles.title}>
              Opioid Environment Policy Scan
            </h1>
            <p className={styles.description}>
              An open data warehouse, mapping platform, and data ecosystem that explores the multi-dimensional risk
              environment, from neighborhoods to states,
              impacting opioid use and health outcomes across the United States.
            </p>

          </div>
        </div>


        <Gutter em={3}/>
        <div className="row rules" style={{ paddingBottom: '1rem' }}>
          <div className="col-xs-12 col-md-12 col-lg-4">



            <Grid container style={{ alignItems: 'center'}}>
              <Grid item xs={1} style={{ marginRight: '16px' }}>
                <img src="images/data.svg" alt="Data Documentation and download." width={40}
                     />
              </Grid>

              <Grid item xs={10}>
                <h1 className={styles.subhead}>Data</h1>
              </Grid>
              <Grid container>
                <Grid item xs={1} style={{ marginRight: '16px' }}></Grid>
                <Grid item xs={10}>
                  Access data by theme or spatial scale and explore our methodology.
                  <div className={'pt-1'}>
                    <Link
                      className={styles.docsLink}
                      href="/download"
                    >
                      Data Access & Download &gt;
                    </Link>
                  </div>
                  <div className={'pt-1'}>
                    <Link className={styles.docsLink} href="/docs">
                      Documentation &gt;
                    </Link>
                  </div>
                  <div className={'pt-1'}>
                    <Link className={styles.docsLink} href="/methods">
                      Methodology &gt;
                    </Link>
                  </div>
                </Grid>
              </Grid>
            </Grid>


          </div>

          <div className="col-xs-12 col-md-12 col-lg-4">

            <Grid container style={{ alignItems: 'center'}}>
              <Grid item xs={1} style={{ marginRight: '16px' }}>
                <img src="images/map.svg" alt="Map and explore data." width={40} style={{marginRight: '1rem'}}/>
              </Grid>
              <Grid item xs={10}>
                <h1 className={styles.subhead}>Map</h1>
              </Grid>
            </Grid>
            <Grid container>
              <Grid item xs={1} style={{ marginRight: '16px' }}></Grid>
              <Grid item xs={10}>
                Visualize data with our interactive web map.

                <div className={'pt-1'}>
                  <Link className={styles.docsLink} href="/map"> Start Mapping &gt;</Link>
                </div>
              </Grid>
            </Grid>
          </div>

          <div className="col-xs-12 col-md-12 col-lg-4 ">
            <Grid container style={{ alignItems: 'center'}}>
              <Grid item xs={1} style={{ marginRight: '16px' }}>
              <img src="images/insights.svg" alt="Data findings and further information." width={40}
                   style={{marginRight: '1rem'}}/>
              </Grid>
              <Grid item xs={10}>
              <h1 className={styles.subhead}>Insights</h1>
              </Grid>
            </Grid>
            <Grid container>
              <Grid item xs={1} style={{ marginRight: '16px' }}></Grid>
              <Grid item xs={10}>
                Learn about the OEPS, code resources, and research insights.
                <div className={'pt-1'}>
                  <Link className={styles.docsLink} href="/about ">About &gt;</Link>
                </div>
                <div className={'pt-1'}>
                  <Link className={styles.docsLink} href="/codeResources ">Code Resources &gt;</Link>
                </div>
                <div className={'pt-1'}>
                  <Link className={styles.docsLink} href="/insights">Insights &gt;</Link>
                </div>
              </Grid>
            </Grid>
          </div>
        </div>

        <div className="row rules">
          <div className="col-xs-12 col-md-12 col-lg-12">
            <br></br>
            <hr></hr>
            <br></br>
            <Grid container spacing={2} className={'row rules'}>
              <Grid xs={12} md={12} item alignItems={'center'}>
                <em><strong>News:</strong></em> <a href={'/posts'}>See All</a>
                {
                  posts?.sort((a, b) => b?.date?.localeCompare(a?.date))?.slice(0, 3)?.map(p => <div
                    key={'post-' + p.slug}>
                    <Grid container spacing={0} alignItems={'end'}>
                      <Grid xs={10} item><h4 style={{marginBottom: 0}}>{p?.title}</h4></Grid>
                      <Grid xs={2} item>{new Date(p?.date)?.toLocaleDateString()}</Grid>
                    </Grid>
                    <Grid container spacing={0}>
                      <Grid xs={12} item>
                        <ReactMarkdown plugins={[remarkGfm]}>{p?.summary}</ReactMarkdown>
                        <a href={`/posts/${p?.slug}`}>Read more &rarr;</a>
                      </Grid>
                    </Grid>
                  </div>)
                }
              </Grid>
            </Grid>
          </div>
        </div>


        <Gutter em={3}/>
        <div className="row rules center-xs">
          <div className="col-xs-12 col-md-12 col-lg-12">
            <hr></hr>
            <p className={styles.description}>
              The OEPS data ecosystem was designed to support research seeking to study environments impacting and
              impacted by opioid use and opioid use disorder (OUD),
              inform public policy, and reduce harm in communities nationwide. It provides access
              to data at multiple spatial scales and time periods, already cleaned, merged, and documented. Read
              more <Link href="/about">about the project</Link>,
              our <Link href="/methods"> methodology</Link>, and <Link href="/insights">insights</Link>.
            </p>
            <p>
              OEPS is led by the <a href="https://healthyregions.org/">Healthy Regions and Policies Lab</a>, based at
              the
              Department of Geography & GIScience at the University of Illinois at Urbana-Champaign. It was developed
              for the <a href="https://heal.nih.gov/research/research-to-practice/jcoin">Justice Community Overdose
              Innovation Network (JCOIN)</a>,
              a NIH HEAL Initiative, as part of the Methodology and Advanced Analytics Resource Center at the University
              of Chicago.
            </p>
          </div>
        </div>


      </main>
      <Footer/>
    </div> : <></>
  );
}

// const postsPerPage = 10;
// export const getStaticProps = async ({ params }) => {
//   const page = parseInt(params?.page);
//   const posts = listPostContent(page, postsPerPage);
//   //const tags = listNewsTags();
//
//   return {
//     props: {
//       page,
//       posts,
//       tags: [],   // TODO: support tags?
//       pagination: {
//         current: page,
//         pages: Math.ceil(countPosts() / postsPerPage),
//       },
//     },
//   };
// };
