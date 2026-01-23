# Netlify Access and Deployment

The OEPS Explorer is deployed to production at [oeps.healthyregions.org](https://oeps.healthyregions.org) via Netlify.

## Team Account Structure

The OEPS project uses the **US Covid Atlas Team** as the umbrella Netlify account. All HEROP Netlify sites, including OEPS, are managed under this team account.

### Accessing the Team Account

The main team account may be accessed using:
- `theuscovidatlas@gmail.com`, or
- Marynia's email address

As an Owner, you have full control over all OEPS project resources in Netlify.

### Individual Access Pattern

The recommended pattern for team members is:

1. **Create your own Netlify account** by going to [netlify.com](https://netlify.com) and authenticating with GitHub
2. **Request to be added to the team** - contact a team Owner to add your individual account to the US Covid Atlas Team
3. **Receive project-specific access** - Owners can grant access to specific projects (Developer role) or full team access (Owner role)

This approach:
- Reduces clutter in the dashboard by showing only relevant projects
- Makes it easier to find the projects you need to work on
- Allows for granular permission management

### Current Access Levels

Team members can be assigned different roles:
- **Owner**: Full control over all team resources and projects
- **Developer**: Access to specific projects with deployment capabilities
- **Member**: Limited access (typically not used for OEPS)

Owners can adjust permissions at any time. For example, you could:
- Set one person as Owner (along with Marynia)
- Set others to Developer role with access only to the OEPS project

## Deployment

The OEPS Explorer is automatically deployed to Netlify when changes are pushed to the `main` branch. The deployment configuration is defined in [`netlify.toml`](../../../netlify.toml) at the repository root.

### Automatic Deployment

Netlify automatically detects pushes to the `main` branch and triggers a new deployment. The build process:
1. Checks out the latest code from the `main` branch
2. Runs the build command in the `explorer` directory
3. Publishes the built Next.js application
4. Makes the site live at [oeps.healthyregions.org](https://oeps.healthyregions.org)

### Manual Deployment

If you need to trigger a manual deployment:

1. Log into the Netlify dashboard
2. Navigate to the OEPS site (under the US Covid Atlas Team)
3. Go to the "Deploys" tab
4. Click "Trigger deploy" → "Deploy site"
5. You can choose to:
   - Deploy the latest commit from the connected branch (usually `main`)
   - Deploy a specific branch
   - Deploy a specific commit

### Build Configuration

The build process is configured in [`netlify.toml`](../../../netlify.toml):

```toml
[build]
  base = "explorer"
  publish = ".next/"
  command = "npm run build:netlify"
```

**Configuration Details:**
- **Base directory**: `explorer` - Netlify changes to this directory before running the build
- **Build command**: `npm run build:netlify` - This runs a custom build script that:
  1. Executes `node context` - Generates context files needed for the build
  2. Runs `npm run build` - Builds the Next.js application
- **Publish directory**: `.next/` - The output directory containing the built static files

### Build Script Details

The `build:netlify` script (defined in `explorer/package.json`) performs:
```json
"build:netlify": "node context && npm run build"
```

The `context` script (located at `explorer/context.js`) generates necessary configuration files before the Next.js build process, such as API key configuration files from environment variables. This ensures the application has the correct context and configuration for production deployment.

### URL Redirects

The `netlify.toml` file also configures URL redirects from the old domain:

```toml
[[redirects]]
  from = "https://oeps.ssd.uchicago.edu/"
  to = "https://oeps.healthyregions.org/"
  force = true

[[redirects]]
  from = "https://oeps.ssd.uchicago.edu/*"
  to = "https://oeps.healthyregions.org/:splat"
  force = true
```

These redirects ensure that:
- The root URL of the old domain redirects to the new domain
- All paths under the old domain redirect to the corresponding paths on the new domain
- The `force = true` flag ensures the redirect happens even if the path exists on the new domain

### Build Environment

Netlify builds run in a Linux environment with:
- Node.js (version specified in `.nvmrc` or default Netlify version)
- npm (comes with Node.js)
- Access to environment variables configured in the Netlify dashboard

### Build Logs and Debugging

To troubleshoot build issues:
1. Go to the Netlify dashboard
2. Navigate to the OEPS site
3. Click on a specific deploy
4. View the build logs to see:
   - Build command output
   - npm install logs
   - Next.js build output
   - Any errors or warnings

Common issues:
- **Build timeout**: Large builds may exceed the default timeout (15 minutes for free tier, 30 minutes for paid)
- **Memory limits**: Very large builds may hit memory constraints
- **Missing dependencies**: Ensure all dependencies are listed in `package.json`
- **Environment variables**: Check that required environment variables are set in Netlify dashboard

## Site Configuration

### Production URL
- **Primary domain**: [oeps.healthyregions.org](https://oeps.healthyregions.org)
- **Legacy domain**: [oeps.ssd.uchicago.edu](https://oeps.ssd.uchicago.edu) (redirects to primary)

### Repository Connection

The Netlify site is connected to the GitHub repository:
- **Repository**: `healthyregions/oeps`
- **Branch**: `main` (production deployments)
- **Build hook**: Automatically triggered on pushes to `main`

### Environment Variables

If the OEPS Explorer requires environment variables for the build or runtime, these should be configured in the Netlify dashboard:
1. Go to Site settings → Environment variables
2. Add variables as needed
3. Variables are available during build and can be accessed in Next.js via `process.env.VARIABLE_NAME`

## Deployment Workflow

### Typical Deployment Process

1. **Development**: Make changes to the `explorer` directory
2. **Testing**: Test locally using `npm run dev` or `npm run build && npm start`
3. **Commit**: Commit changes to a branch
4. **Pull Request**: Create a PR to `main` (optional, for review)
5. **Merge**: Merge to `main` branch
6. **Automatic Deployment**: Netlify detects the push and starts building
7. **Deploy Preview**: For PRs, Netlify creates a preview deployment
8. **Production**: Once merged to `main`, the production site is updated

### Deploy Previews

When you create a pull request, Netlify automatically:
- Creates a unique preview URL for that PR
- Builds the site with the PR's changes
- Provides a link in the PR comments
- Updates the preview when new commits are pushed to the PR branch

This allows you to:
- Review changes before merging
- Share previews with team members
- Test changes in a production-like environment

### Rollback

If a deployment causes issues, you can rollback:
1. Go to the Netlify dashboard
2. Navigate to the OEPS site → Deploys
3. Find a previous successful deployment
4. Click the three dots menu → "Publish deploy"

This will restore the site to that previous version.

## Technical Stack

The OEPS Explorer is built with:
- **Framework**: Next.js 14
- **React**: React 18.3.1
- **Mapping**: react-map-gl, deck.gl
- **UI Components**: Material-UI, Grommet
- **State Management**: Redux
- **Build Tool**: Next.js built-in bundler
- **Deployment**: Netlify (static site hosting)

The application is a static Next.js site that can be pre-rendered at build time for optimal performance.

## Monitoring and Analytics

Netlify provides built-in analytics and monitoring:
- **Deploy status**: See success/failure of each deployment
- **Build times**: Monitor how long builds take
- **Site analytics**: View visitor statistics (if enabled)
- **Form submissions**: Handle form submissions (if the site has forms)
- **Functions**: Serverless functions for dynamic functionality (if used)

## Additional Resources

- [Netlify Notion Page](https://www.notion.so/Netlify-4b02a88bbff1420b818a0a495cab997c) - Contains additional Netlify credentials and information
- [Netlify Documentation](https://docs.netlify.com/) - Official Netlify documentation
- [Next.js Deployment Documentation](https://nextjs.org/docs/deployment) - Next.js deployment best practices
- [Netlify Build Configuration](https://docs.netlify.com/configure-builds/file-based-configuration/) - Details about `netlify.toml` configuration
