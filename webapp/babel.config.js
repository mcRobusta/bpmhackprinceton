module.exports = {
  presets: [
    '@vue/cli-plugin-babel/preset'
  ],
  configureWebpack: {
    devServer: {
      headers: { "Access-Control-Allow-Origin": "*" }
    }
  }
}