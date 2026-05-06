# Metadata Writing Guidelines

## Overview 

- When any dataset is updated, edited, or added to OEPS, a corresponding metadata document must be generated or updated.
- When generating a new document from scratch, use the template document to start.
- In addition, you must update the registry file at: https://app.pagescms.org/healthyregions/oeps/main/collection/metadata
    - Learn more about this process here: https://healthyregions.github.io/oeps/guides/adding-data-to-oeps/#create-a-new-metadata-entry

### Tips

- The most recent author goes first in authorship. Please add yourself as an author even if you've only worked in updating the metadata file, not the data file. If there are questions about metadata, we'll need to know who to ask.
- Replace the last person who modified the file with your name. 'Last modified by' is only meant to have one name.
- Be sure to check URLs to ensure they are working. If not, update. 
- In addition to updating the table, also carefully read and update (if necessary) every other section. If the URL where you sourced the data changed this time, add that to the metadata source description. Indicated when you pulled data, when appropriate.
- Add more tips here for your fellow writers in the future.

## Adding images

The OEPS docs page renders metadata markdown with ReactMarkdown, which does **not** render raw HTML. Use **Markdown image syntax** so images show correctly on the OEPS docs page.

### Image URLs and the OEPS docs site

The explorer loads markdown from  
`https://raw.githubusercontent.com/healthyregions/oeps/main/metadata/{slug}.md`  
(the `main` branch). For images:

- **Relative paths** under the metadata folder, e.g. `images/your-file.png`, are rewritten when rendering on [oeps.healthyregions.org/docs/...](https://oeps.healthyregions.org/docs) so they load from the same raw base (`.../metadata/images/your-file.png`). Without that rewrite, the browser would request the wrong host and the image would break.
- **Absolute URLs** (`http://` or `https://`) are used as-is if you must link an external image; prefer repo files under `metadata/images/` for anything shipped with OEPS metadata.
- **Stable assets:** Commit files under `metadata/images/` and link them with a relative `images/...` path or a `raw.githubusercontent.com/.../metadata/images/...` URL so links stay tied to the branch and do not rely on expiring signed URLs.
- **Avoid** `https://github.com/.../blob/...` as the image URL in markdown: that is an HTML page, not a direct image, and may not display reliably in an `<img>` on the docs site. Use `raw.githubusercontent.com/...` or a relative `images/...` path instead.

### HTML vs Markdown (use Markdown)

When you drop or paste an image into GitHub’s markdown editor, it may insert an HTML `<img>` tag. That works when viewing the file on GitHub, but **the OEPS docs page will not render it**—the image will not show. Use Markdown syntax instead.

| Don’t use (HTML – won’t show on OEPS docs) | Do use (Markdown – works on OEPS docs) |
|-------------------------------------------|----------------------------------------|
| `<img width="1492" height="657" alt="Screenshot" src="https://raw.githubusercontent.com/healthyregions/oeps/main/metadata/images/example.png" />` | `![Screenshot](https://raw.githubusercontent.com/healthyregions/oeps/main/metadata/images/example.png)` |

Same image URL; only the syntax changes. Replace any auto-generated `<img>` with the `![alt](url)` form (or a relative `images/...` link if the file lives in `metadata/images/`).

### Use `metadata/images/`

1. Add your image file to the `metadata/images/` folder in the repo (create the folder if needed).
2. In your metadata `.md` file, use **either** form (both work on the OEPS docs site once the file is on `main`):

   **Relative (rewritten on the docs site to raw GitHub):**

   ```markdown
   ![Short description of the image](images/your-filename.png)
   ```

   **Explicit raw URL (same file; also works in GitHub’s UI and other viewers):**

   ```markdown
   ![Short description of the image](https://raw.githubusercontent.com/healthyregions/oeps/main/metadata/images/your-filename.png)
   ```

3. The examples above point at `main`. If you add an image on a feature branch, use a branch-specific raw URL while developing (replace `main` with your branch name). After the PR is merged, use `main` (or keep the relative `images/...` path).
