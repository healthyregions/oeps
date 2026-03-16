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

### HTML vs Markdown (use Markdown)

When you drop or paste an image into GitHub’s markdown editor, it may insert an HTML `<img>` tag. That works when viewing the file on GitHub, but **the OEPS docs page will not render it**—the image will not show. Use Markdown syntax instead.

| Don’t use (HTML – won’t show on OEPS docs) | Do use (Markdown – works on OEPS docs) |
|-------------------------------------------|----------------------------------------|
| `<img width="1492" height="657" alt="Screenshot" src="https://github.com/user-attachments/assets/abc123" />` | `![Screenshot](https://github.com/user-attachments/assets/abc123)` |

Same image URL; only the syntax changes. Replace any auto-generated `<img>` with the `![alt](url)` form.

### Option 1: GitHub paste/drop (recommended)

1. Paste or drop the image into a **PR or issue comment** so GitHub hosts it.
2. Right‑click the pasted image → **Copy image address**.
3. In your metadata `.md` file, add:

   ```markdown
   ![Short description of the image](paste-the-copied-url-here)
   ```

4. Do not use the auto-generated HTML when you drop an image into the .md file; use this Markdown line so the image renders on the OEPS docs page.

**Example:**

```markdown
![Travel time to nearest provider](https://github.com/user-attachments/assets/98ccd48e-e3a8-40a7-bd64-f6e9251cca45)
```

### Option 2: Use `metadata/images/`

1. Add your image file to the `metadata/images/` folder in the repo (create the folder if needed).
2. In your metadata `.md` file, reference it with the raw GitHub URL:

   ```markdown
   ![Short description of the image](https://raw.githubusercontent.com/healthyregions/oeps/main/metadata/images/your-filename.png)
   ```

3. The URL above points at `main`. If you add an image on a feature branch, use a branch-specific URL during development (replace `main` with your branch name), then switch to `main` after the PR is merged.
