// lib/markdown.js
import matter from 'gray-matter';

const org = 'healthyregions';
const repo = 'oeps';
const branch = 'main';

/**
 * Load a news post by slug (filename stem without .md).
 * Returns null if the post cannot be loaded or is missing required frontmatter,
 * so a bad CMS entry cannot crash homepage /posts SSR.
 */
export const getPostBySlug = async (slug) => {
  if (!slug || typeof slug !== 'string') {
    console.error('getPostBySlug: invalid slug', slug);
    return null;
  }

  const url = `https://raw.githubusercontent.com/${org}/${repo}/refs/heads/${branch}/explorer/content/posts/${encodeURIComponent(slug)}.md`;
  let response;
  try {
    response = await fetch(url);
  } catch (err) {
    console.error(`getPostBySlug: fetch failed for ${slug}`, err);
    return null;
  }

  if (!response.ok) {
    console.error(
      `getPostBySlug: ${response.status} for slug "${slug}" (expected explorer/content/posts/${slug}.md on ${branch})`
    );
    return null;
  }

  const fileContents = await response.text();
  const { data, content } = matter(fileContents);

  if (!data?.date) {
    console.error(`getPostBySlug: missing date frontmatter for slug "${slug}"`);
    return null;
  }

  const date =
    data.date instanceof Date ? data.date : new Date(data.date);
  if (Number.isNaN(date.getTime())) {
    console.error(`getPostBySlug: invalid date frontmatter for slug "${slug}"`);
    return null;
  }

  return {
    ...data,
    date: date.toISOString(),
    slug,
    content,
  };
};
