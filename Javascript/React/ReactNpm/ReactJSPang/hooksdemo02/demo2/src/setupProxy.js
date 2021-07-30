const {createProxyMiddleware } = require("http-proxy-middleware")
// 更改该文件必须重启 react

module.exports = function (app) {
    app.use(
        createProxyMiddleware ('/api1', {                        // 遇见/api1 前缀的请求，就会触发该代理配置 
            target: "http://localhost:8000",    // 请求转发给谁
            changeOrigin: true,                 // 控制服务期收到的响应头中Host字段的值
            pathRewrite: { '^/api1': '' }       // 重写请求路径
        }),
        createProxyMiddleware ('/api2', {
            target: "http://localhost:5001",
            changeOrigin: true,
            pathRewrite: { '^/api1': '' }
        })
    )
}

