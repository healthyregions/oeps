const workboxBuild = require("workbox-build");
// NOTE: This should be run *AFTER* all your assets are Physical
const buildSW = () => {
  // This will return a Promise
  return workboxBuild
    .injectManifest({
      swSrc: "./sw.js", // this is your sw template file
      swDest: "out/sw.js", // this will be created in the build step
      globDirectory: "out",
      maximumFileSizeToCacheInBytes: 100000000,
      globPatterns: [
        "**/{csv,pbf,geojson}/{csv,pbf,geojson}",
        "**/static/{js,css}/*.{css,js,map}",
        "**/workers/*.{js}",
      ],
    })
    .then(({ count, size, warnings }) => {
      // Optionally, log any warnings and details.
      // warnings.forEach(console.warn);
      // console.log(`${count} files will be precached, totaling ${size} bytes.`);
    });
};
buildSW();
