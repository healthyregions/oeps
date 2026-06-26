import Head from "next/head";
import Link from 'next/link';
import styles from "../styles/Home.module.css";
import {Gutter} from "@components/layout/Gutter";
import MainNav from "@components/layout/MainNav";
import Footer from "@components/layout/Footer";
import {Button, Grid} from "@mui/material";
import postsMetadata from '../content/posts.json';
import {getPostBySlug} from "../lib/markdown";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import {useEffect, useState} from "react";
import styled from "styled-components";


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

const sectionPadding = '0 12.5vw';

const HeroSection = styled.div`
    padding: ${sectionPadding};
`;


const NewsSection = styled.div`
    background-color: #d6aed822;
    width: 100%;
    margin-top: 1rem;
    padding: ${sectionPadding};
    display: flex;
    justify-content: center;
`;

const DescriptionAndAcknowledgmentsSection = styled.div`
    margin: 1rem 0;
    display: flex;
    padding: ${sectionPadding};
    align-items: center;
`;

const ActionsSection = styled.div`
    display: flex;
    padding: ${sectionPadding};
    align-items: center;
`;

const ActionsHeader = styled.div`
    display: flex;
    align-items: center;
    justify-content: start;
`;

const ActionsHeaderIcon = styled.img`
    margin: 0 1.25rem;
    width: 40px;
`;

const ActionsSubheader = styled.div`
    margin: 0 5.75rem;
`;

const ActionsButtons = styled.div`
    display: flex;
    margin: 0.5rem 5.75rem;
    flex-direction: column;
    align-items: flex-start;
`;

const ActionsButton = styled(Link)`
  
`;

export default function Home({posts}) {
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    // Waits for server-side props above before first render
    setMounted(true);
  }, []);

  const actionSections = [
    {
      label: 'Data',
      description: 'Access data by theme or spatial scale and explore our methodology.',
      img: 'images/data.svg',
      imgAlt: 'Data Documentation and download.',
      actions: [
        { label: 'Data Access & Download >', link: '/download' },
        { label: 'Documentation >', link: '/docs' },
        { label: 'Methodology >', link: '/methods' },
      ]
    },
    {
      label: 'Map',
      description: 'Visualize data with our interactive web map.',
      img: 'images/map.svg',
      imgAlt: 'Map and explore data.',
      actions: [
        { label: 'Start Mapping >', link: '/map' },
      ]
    },
    {
      label: 'Insights',
      description: 'Learn about the OEPS, code resources, and research insights.',
      img: 'images/insights.svg',
      imgAlt: 'Data findings and further information.',
      actions: [
        { label: 'About >', link: '/about' },
        { label: 'Code Resources >', link: '/codeResources' },
        { label: 'Insights >', link: '/insights' },
      ]
    },
  ];

  return (
    mounted ? <>
      <Head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
        <title>OEPS Explorer</title>
      </Head>
      <MainNav/>
      <main>
        <HeroSection>
          <Grid container alignItems={'center'}>
            <Grid item padding={'2rem'} xs={12} md={5} lg={4}>
              <img src="images/logo-factors.png" className={styles.titleDiagram} alt={''}/>
            </Grid>
            <Gutter em={3}/>
              <Grid item xs={12} md={7} lg={8}>
                <h1 className={styles.title}>
                  Opioid Environment Policy Scan
                </h1>
                <p className={styles.description}>
                  An open data warehouse, mapping platform, and data ecosystem that explores the multi-dimensional risk
                  environment, from neighborhoods to states,
                  impacting opioid use and health outcomes across the United States.
                </p>
              </Grid>
          </Grid>
        </HeroSection>

        <Gutter rem={3}/>

        <ActionsSection>
          <Grid container spacing={2}>
            {
              actionSections?.map(s =>
                <Grid item xs={12} md={12} lg={4}>
                  <ActionsHeader>
                    <ActionsHeaderIcon src={s?.img} alt={s?.imgAlt}></ActionsHeaderIcon>
                    <h1 className={styles.subhead}>{s?.label}</h1>
                  </ActionsHeader>
                  <ActionsSubheader>
                    {s?.description}
                  </ActionsSubheader>
                  <ActionsButtons>
                    {
                      s?.actions?.map(a =>
                        <ActionsButton className={styles.docsLink} href={a?.link}>{a?.label}</ActionsButton>
                      )
                    }
                  </ActionsButtons>
                </Grid>
              )
            }
          </Grid>
        </ActionsSection>

        <NewsSection>
          <Grid container padding={'2rem'}>
            <Grid xs={12} md={12} item alignItems={'center'}>
              <h2 style={{ marginBottom: '0.75rem' }}>Recent News</h2>
              <a href={'/posts'}>See All</a>
              {
                posts?.sort((a, b) => b?.date?.localeCompare(a?.date))?.slice(0, 3)?.map(p => <div
                  key={'post-' + p.slug}>
                  <Grid container alignItems={'end'}>
                    <Grid xs={10} item><h4 style={{marginBottom: 0}}>{p?.title}</h4></Grid>
                    <Grid xs={2} item textAlign={'right'}>{new Date(p?.date)?.toLocaleDateString()}</Grid>
                  </Grid>
                  <Grid container>
                    <Grid xs={12} item>
                      <ReactMarkdown plugins={[remarkGfm]}>{p?.summary}</ReactMarkdown>
                      <a href={`/posts/${p?.slug}`}>Read more &rarr;</a>
                    </Grid>
                  </Grid>
                </div>)
              }
            </Grid>
          </Grid>
        </NewsSection>

        <DescriptionAndAcknowledgmentsSection>
          <div className="col-xs-12 col-md-12 col-lg-12">
            <p className={styles.description}>
              The OEPS data ecosystem was designed to support research seeking to study environments impacting and
              impacted by opioid use and opioid use disorder (OUD),
              inform public policy, and reduce harm in communities nationwide. It provides access
              to data at multiple spatial scales and time periods, already cleaned, merged, and documented. Read
              more <Link href="/about">about the project</Link>,
              our <Link href="/methods"> methodology</Link>, and <Link href="/insights">insights</Link>.
            </p>
            <p style={{ textAlign: 'center'}}>
              OEPS is led by the <a href="https://healthyregions.org/">Healthy Regions and Policies Lab</a>, based at
              the
              Department of Geography & GIScience at the University of Illinois at Urbana-Champaign. It was developed
              for the <a href="https://heal.nih.gov/research/research-to-practice/jcoin">Justice Community Overdose
              Innovation Network (JCOIN)</a>,
              a NIH HEAL Initiative, as part of the Methodology and Advanced Analytics Resource Center at the University
              of Chicago.
            </p>
          </div>
        </DescriptionAndAcknowledgmentsSection>


      </main>
      <Footer/>
    </> : <></>
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
