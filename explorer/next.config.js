module.exports = {
  // Supported targets are "serverless" and "experimental-serverless-trace"
  target: "serverless",
  generateBuildId: () => "build",
  i18n: {
    locales: ["en"],
    defaultLocale: "en",
  }
}