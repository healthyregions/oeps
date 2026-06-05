

// This gets called on every request
import postsMetadata from "../../content/posts.json";
import {getPostBySlug} from "../../lib/markdown";
import MainNav from "@components/layout/MainNav";
import {useEffect, useState} from "react";
import Footer from "@components/layout/Footer";
import styles from "@styles/Home.module.css";

export async function getServerSideProps() {
  // Fetch data from external API
  const posts = [];

  for (const metadata of postsMetadata) {
    const post = await getPostBySlug(metadata.slug);
    posts.push(post);
  }

  // Pass data to the page via props
  return { props: { posts } }
}

const PostsTable = ({ posts }) => {
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    // Waits for server-side props above before first render
    setMounted(true);
  }, [])

  return(
    mounted ? <div className={styles.container}>
      <MainNav />
      <main className={styles.main} style={{ justifyContent: 'start', alignItems: 'start', width: '100%' }}>
        <a href={'/'}>&larr; Home</a>
        <h2>News</h2>
        <table>
          <tbody>
          <tr>
            <th>Date</th>
            <th>Title</th>
          </tr>
          {posts?.sort((a,b) => b?.date?.localeCompare(a?.date))?.map((p, index) => <tr key={'tablerow-'+index} onClick={(p) => console.log(`/posts/${p?.slug}`)}>
            <td>{new Date(p?.date)?.toLocaleDateString()}</td>
            <td><a href={`/posts/${p?.slug}`}>{p?.title}</a></td>
          </tr>)}
          </tbody>
        </table>
      </main>
      <Footer />
    </div> : <></>
  );
}

export default PostsTable;
