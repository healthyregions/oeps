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
import styled from "styled-components";


// const diagram = [
//   {
//     name:'oeps-diagram',
//     photo: 'oeps-diagram.png',
//   }
// ]

// This gets called on every request
export async function getServerSideProps() {
  const posts = [];

  for (const metadata of postsMetadata) {
    const post = await getPostBySlug(metadata.slug);
    if (post) {
      posts.push(post);
    }
  }

  return {props: {posts}}
}

const sectionPadding = '0 12.5vw';

const HeroSection = styled.div`
    padding: ${sectionPadding};
    margin-top: 1rem;
`;


const QuickStartSection = styled.div`
    background-color: #d6aed822;
    padding: ${sectionPadding};
    width: 100%;
    margin-top: 1rem;
    padding: ${sectionPadding};
    display: flex;
    justify-content: left;
`;

const NewsSection = styled.div`
    width: 100%;
    margin-top: 1rem;
    padding: ${sectionPadding};
    display: flex;
    justify-content: center;
`;

const DescriptionAndAcknowledgmentsSection = styled.div`
    margin: 1rem 0;
    display: flex;
    justify-content: center;
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
      label: 'About',
      description: 'Learn about our team, curation approach, & standards.',
      img: 'images/map.svg',
      imgAlt: 'Map and explore data.',
      actions: [
        { label: 'About OEPS >', link: '/about' },
        { label: 'Methodology >', link: '/methods' },
        { label: 'Data Standards >', link: '/dataInclusion' },
      ]
    },
      {
      label: 'Data',
      description: 'Explore & access data for your needs.',
      img: 'images/data.svg',
      imgAlt: 'Explore Data',
      actions: [
        { label: 'Data Inventory >', link: '/docs' },
        { label: 'Explore via Map>', link: '/map' },
        { label: 'Data Download >', link: '/download' },
      ]
    },
    {
      label: 'Insights',
      description: 'Dive into code resources & research insights.',
      img: 'images/insights.svg',
      imgAlt: 'Data findings and further information.',
      actions: [
        { label: 'Code Resources >', link: '/codeResources' },
        { label: 'Insights >', link: '/insights' },
        { label: 'For Developers >', link: 'https://healthyregions.github.io/oeps' },
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
          <Grid container style={{padding: '2rem', width:'100%'}}>
            <Grid size={{ xs:12, md:12, lg:4 }} style={{paddingTop:'2rem'}}>
              <img src="images/logo-factors.png" className={styles.titleDiagram} alt={''}/>
            </Grid>
            <Gutter em={2}/>
            <Grid size={{ xs:12, md:12, lg:7 }} style={{paddingTop:'4rem'}} >
              <h1>
                OEPS: the Opioid Environment Policy Scan Data Ecosystem
              </h1>
              <p>
                A free open data warehouse, mapping platform, and data ecosystem that models the multi-dimensional risk
                environment, from neighborhoods to states,
                impacting opioid use and health outcomes across the United States.
              </p>
              {/* <p className={styles.description}> */}
              <p>
                With over three hundred variables spanning four decades, OEPS continues to grow and be improved
                over time. Check back regularly for updates.
              </p>
            </Grid>
          </Grid>
        </HeroSection>

        <Gutter rem={3}/>

        <ActionsSection>
          <Grid container spacing={2}>
            {
              actionSections?.map((s, indexOuter) =>
                <Grid size={{ xs:12, md:12, lg:4 }} key={`actions-section-${indexOuter}`}>
                  <ActionsHeader>
                    <ActionsHeaderIcon src={s?.img} alt={s?.imgAlt}></ActionsHeaderIcon>
                    <h3 className={styles.subhead}>{s?.label}</h3>
                  </ActionsHeader>
                  <ActionsSubheader>
                    {s?.description}
                  </ActionsSubheader>
                  <ActionsButtons>
                    {
                      s?.actions?.map((a, indexInner) =>
                        <ActionsButton key={`actions-${indexInner}`} className={styles.docsLink} href={a?.link}>{a?.label}</ActionsButton>
                      )
                    }
                  </ActionsButtons>
                </Grid>
              )
            }
          </Grid>
        </ActionsSection>


        <QuickStartSection>
          <Grid container style={{padding: '2rem', width:'100%'}}>

            <Grid size={{ xs:12, md:12, lg:8 }} style={{paddingTop:'2rem'}} alignItems={'left'}>
              <h1> Quick Start Guide</h1>
              <img src="images/start.png" className={styles.title1Diagram} alt={''}/>
            </Grid>

            <Grid size={{ xs:12, md:12, lg:4 }} style={{paddingTop:'2rem'}}>
              <h3> Usage Tips</h3>
                <p2>✔ Data packages will include data across five years: stable census measures are often
                    multi-year averages, whereas access metrics may correspond to one year. </p2>
                    <br></br><br></br>
                <p2>✔ We use 5-digit ZCTAs, or Zip Code Tabulation Areas, to represent zips. </p2>
                <br></br><br></br>
                 <p2>✔ Seeking data on Connecticut? Due to changes in their boundaries after 2020, the
                    most recent Census data may not be available in OEPS. </p2>
                    <br></br><br></br>

             <p2>
              Get more tips at the Data Standards Section of our <a href="/methods"> Methods </a>page, or
              learn more about the <a href="/dataInclusion">Data Inclusion</a> criteria we use.
            </p2>

            <h4> Citation </h4>
            <p2>
            Kim, Y. W., Cox, A., Kabir Adrita, M., Lambert, S., Wimer, A., Halpern, D., Paykin, S., Lin, Q. & Kolak, M. (2026). 
            OEPS: Opioid Environment Policy Scan Data Ecosystem (Version 3.0) [Dataset]. Zenodo. 
            https://doi.org/10.5281/zenodo.21909862
            </p2>

            </Grid>

          </Grid>

        </QuickStartSection>

        {/* if there are any Published Posts, display them here */}
        {
          (posts !== '' && Array.isArray(posts) && posts?.length > 0) && <NewsSection>
            <Grid container style={{padding: '2rem', width:'100%'}}>
              <Grid size={{ xs:12, md:12 }} alignItems={'center'}>
                <h1 className={styles.subhead}>Latest Updates</h1>
                <a href={'/posts'}>See All</a>
                {
                  posts?.sort((a, b) => b?.date?.localeCompare(a?.date))?.slice(0, 3)?.map((p, index) => <div
                    key={`post-${index}-${p.slug}`}>
                    <Grid container alignItems={'end'}>
                      <Grid size={{ xs:10 }}><h4 style={{marginBottom: 0}}>{p?.title}</h4></Grid>
                      <Grid size={{ xs:2 }} textAlign={'right'}>{new Date(p?.date)?.toLocaleDateString()}</Grid>
                    </Grid>
                    <Grid container>
                      <Grid size={{ xs:12 }}>
                        <ReactMarkdown plugins={[remarkGfm]}>{p?.summary}</ReactMarkdown>
                        <a href={`/posts/${p?.slug}`}>Read more &rarr;</a>
                      </Grid>
                    </Grid>
                  </div>)
                }
              </Grid>
            </Grid>
          </NewsSection>
        }


        <DescriptionAndAcknowledgmentsSection>
          <Grid size={{ xs:12 }} maxWidth={'85%'} align={'center'}>
            {/* if there are no Published Posts, insert a horizontal line above this section */}
            { (!posts === '' || Array.isArray(posts) || posts?.length === 0) && <hr /> }

            <p2 style={{ textAlign: 'center', maxWidth: '85%', justifyContent: 'center'}}>
              OEPS is led by the <a href="https://healthyregions.org/">Healthy Regions and Policies Lab</a>, based at
              the University of Illinois at Urbana-Champaign. It was developed
              for the <a href="https://heal.nih.gov/research/research-to-practice/jcoin">Justice Community Overdose
              Innovation Network (JCOIN)</a>,
              a NIH HEAL Initiative, as part of the Methodology and Advanced Analytics Resource Center at the University
              of Chicago.
            </p2>
          </Grid>
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
