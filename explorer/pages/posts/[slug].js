import {getPostBySlug} from "../../lib/markdown";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import MainNav from "@components/layout/MainNav";
import {useEffect, useState} from "react";
import Footer from "@components/layout/Footer";
import styles from "@styles/Home.module.css";


export async function getServerSideProps(context) {
  const post = await getPostBySlug(context.params.slug);
  if (!post) {
    return { notFound: true };
  }
  return { props: { post } };
}
export const PostLayout = ({ post }) => {
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    // Waits for server-side props above before first render
    setMounted(true);
  }, []);

  return(
    mounted ? <div className={styles.container}>
      <MainNav />
      <main className={styles.main} style={{ alignItems: 'start'}}>
        <a href={'/posts'}>&larr; All News</a>
        <h1>{post?.title} <small>({new Date(post?.date)?.toLocaleDateString()})</small></h1>
        <summary>Summary: {post?.summary}</summary>
        <br />
        <hr style={{ borderTop: '1px dashed' }} />
        <ReactMarkdown plugins={[remarkGfm]}>{post?.content}</ReactMarkdown>
      </main>
      <Footer />
    </div> : <></>
  );
}

export default PostLayout;
