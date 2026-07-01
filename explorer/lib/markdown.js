// lib/markdown.ts
//import path from 'path';
import matter from 'gray-matter';

//const contentDirectory = path.join(process.cwd(), 'content');

const org = 'healthyregions';
const repo = 'oeps';
const branch = 'main';

export const getPostBySlug = async (slug) => {
  const url = `https://raw.githubusercontent.com/${org}/${repo}/refs/heads/${branch}/explorer/content/posts/${slug}.md`;
  const response = await fetch(url);
  const fileContents = await response.text();
  //const fullPath = path.join(contentDirectory, `${slug}.md`);
  //const fileContents = fs.readFileSync(fullPath, 'utf8');

  // gray-matter splits the string into data (frontmatter) and content (body)
  const { data, content } = matter(fileContents);

  return {
    ...data,
    date: data.date.toISOString(),
    slug,
    content,
  };
}
