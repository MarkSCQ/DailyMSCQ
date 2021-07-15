// 1. 引入 express
const express = require('express')
const { stringify } = require('uuid')
// 2. 创建应用对象
const app = express()
// 3. 创建路由规则。 
//      request 对报文请求封装， 
//      response，对响应报文封装
app.get('/server', (request, response) => {
    // 设置响应体，允许跨域
    response.setHeader("Access-Control-Allow-Origin", "*")
    // 设置响应体
    response.send("HELLO EXPRESS -2asdf")
})
app.get('/ie', (request, response) => {
    // 设置响应体，允许跨域
    response.setHeader("Access-Control-Allow-Origin", "*")
    // 设置响应体
    response.send("HELLO EXPRESS - i333aa33e")
})
app.post('/server', (request, response) => {
    // 设置响应体，允许跨域
    response.setHeader("Access-Control-Allow-Origin", "*")
    response.setHeader("Access-Control-Allow-Headers", "*")
    // 设置响应体
    response.send("HELLO EXPRESS POST")
})
// 任意类型的请求
app.all('/server', (request, response) => {
    // 设置响应体，允许跨域
    response.setHeader("Access-Control-Allow-Origin", "*")
    response.setHeader("Access-Control-Allow-Headers", "*")
    // 设置响应体
    response.send("HELLO EXPRESS POST")
})

app.all('/json-server', (request, response) => {
    // 设置响应体，允许跨域
    response.setHeader("Access-Control-Allow-Origin", "*");
    response.setHeader("Access-Control-Allow-Headers", "*");

    const data = { id: 12, name: "333" };
    // 设置响应体

    let str = JSON.stringify(data)
    response.send(str);
})


app.get('/timeout', (request, response) => {
    // 设置响应体，允许跨域
    response.setHeader("Access-Control-Allow-Origin", "*");
    setTimeout(() => {
        response.send("Timeout");

    }, 3000);
    // 设置响应体

})

app.all('/axios-server', (request, response) => {
    // 设置响应体，允许跨域
    response.setHeader("Access-Control-Allow-Origin", "*");
    response.setHeader("Access-Control-Allow-Headers", "*");

    const data = { name: "Axios" };

    response.send(JSON.stringify(data))
    // 设置响应体

})

// 监听端口启动服务
app.listen(8000, () => {
    console.log("Express is running , 8000 is used")
})

