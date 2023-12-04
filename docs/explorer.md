# OEPS Explorer

The OEPS Explorer is a NextJS app that uses [WebGeoDa](#about-webgeoda) (built with [jsGeoDa](https://jsgeoda.libgeoda.org/)) for geospatial interactivity.

## Install & Develop

To get started locally with the explorer:

```
git clone https://github.com/healthyregions/oeps
cd oeps/explorer
yarn install
cp .env.example .env
```

Some environment variable values will already be set in `.env`, but you'll need to add a Mapbox token. Then run

```
yarn dev
```

and open `http://localhost:3000`

### More about Mapbox dependencies

Two Mapbox Tilesets must be configured externally and linked within this app, one for Zip Code Tabulation Areas (ZCTAs) and one for Census Tracts. These geometries are joined with local CSV tables to drive map visualizations.

Additionally, a basemap style must be provided, as well as a Mapbox access token. All of these elements are (currently) provided through environment variables, so make sure your `.env` file has the following:

```
NEXT_PUBLIC_MAPBOX_TOKEN=<your token>
NEXT_PUBLIC_MAPBOX_TILESET_ID_ZCTA="<account id>.<tileset id>"
NEXT_PUBLIC_MAPBOX_TILESET_ID_TRACT="<account id>.<tileset id>"
NEXT_PUBLIC_MAPBOX_STYLE="mapbox://styles/<account id>/<style id>'
```


## About WebGeoDa

![A map of population density in texas](https://github.com/nofurtherinformation/webgeoda/blob/main/public/cover.png?raw=true)

WebGeoDa Scaffolding is a set of easy-to-use frontend JavaScript toolkits to get started building and exploring client-side geospatial analytics.

⚠️ Heads up! WebGeoDa is an _unstable_ work in progress. This means a lot will change in future releases. ⚠️

### About Webgeoda Scaffolding

**What is this thing?**

WebGeoDa is a set of tools, templates, and scaffolding to quickly and easily develop geospatial data dashboards. WebGeoDa builds on the GeoDa suite of geospatial software and extends jsGeoDa through accessible and ready-to-go examples. WebGeoDa uses  [jsGeoDa](https://jsgeoda.libgeoda.org/) (Xun Li & Luc Anselin) as the core of it's geospatial engine, alongside a collection of modern and high-performance libraries for mapping, analysis, data handling, and UI matters.

WebGeoDa capabilities have four areas of complexity. It's easy to learn, but with a high ceiling for customization:

‍💻 Add your geospatial data (GeoJSON), join it to your tabular data (CSV) right in the browser. Specify your variables with a simple JSON specification, and your map is ready to be published!

📑 Customize and add static pages to describe your data and the context of your dashboard. WebGeoDa provides some Physical-in styling tools using Plain CSS and a reasonably approachable JSX, similar to HTML.

🗺 Add additional map features using Mapbox and Deck.gl, or explore additional data insights through interactive tooltip and sidebar functions.

🦺 Dive directly into the WebGeoDa scaffolding with full control over custom react hooks, the jsGeoDa WebAssembly + WebWorker geospatial engine, a fast Redux-backed state, and extensible and accessible components. 

### What can WebGeoDa do?

WebGeoDa focuses on enabling exploratory data dashboards with complex data, the need for diverse variables, and high performance in-browser analytics. You can make maps with a variety of color-binning techniques and spatial statistical methods, like Hotspot cluster analysis, through a simple JSON based data and variable configuration.

### See the [full docs](https://dhalpern.gitbook.io/webgeoda-templates/) for more and [get started here](https://dhalpern.gitbook.io/webgeoda-templates/getting-started).
