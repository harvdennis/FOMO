const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = app => {
  app.use(
    "/api",
    createProxyMiddleware ({
      target: "http://localhost:8000",
      changeOrigin: true
    })
  );
  app.use(
    "/auth",
    createProxyMiddleware ({
      target: "http://studentnet.cs.manchester.ac.uk",
      changeOrigin: true
    })
  );
};