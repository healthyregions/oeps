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

### Recommended: store files in `metadata/images/` and link with a relative path

1. Add your image file under **`metadata/images/`** in this repo (for example `metadata/images/My_Map_Title.png`).
2. Use a **short, stable filename**: letters, numbers, and underscores only (no spaces); use underscores instead of spaces.
3. In your metadata `.md` file in `metadata/`, reference it like this:

   ```markdown
   ![Short description of what the figure shows](images/My_Map_Title.png)
   ```

The path `images/...` is relative to the markdown file in `metadata/`, so it resolves to `metadata/images/` when the docs site builds.

### HTML vs Markdown (use Markdown)

When you drop or paste an image into GitHub's markdown editor, it may insert an HTML `<img>` tag. That can look fine on GitHub, but **the OEPS docs page will not render it**—use Markdown instead.

| Don't use (HTML – won't show on OEPS docs) | Do use (Markdown – works on OEPS docs) |
|-------------------------------------------|----------------------------------------|
| `<img width="1492" height="657" alt="Screenshot" src="images/My_Map_Title.png" />` | `![Screenshot](images/My_Map_Title.png)` |

Replace any auto-generated `<img>` with the `![alt](path)` form.

### Optional: absolute URL to `main`

If you need a full URL (for example in external docs), you can point at the file on `main`:

```markdown
![Short description](https://raw.githubusercontent.com/healthyregions/oeps/main/metadata/images/My_Map_Title.png)
```

Prefer the **relative** `images/...` form in metadata markdown so links stay correct on branches and after merge.

### Avoid relying on GitHub-only image hosts

Do **not** depend on pasted **issue/PR** image URLs (`github.com/user-attachments/...`) or temporary **private** image links as the only copy of an asset. Those are easy to lose track of and may not match what lives in the repo. Put the canonical image in **`metadata/images/`** and link it from the `.md` file as above.
