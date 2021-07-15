发送Http请求（request），没有刷新网页返回结果

Asynchronous Javascript and XML

XML Extensible Markup Language 存储和传输数据

XML中没有预定义标签，自定义标签名

Ajax 特点：
1. 优点
   1. 无刷新与服务器进行通信
   2. 允许你根据用户时间来更新部分网页的内容
2. 缺点
   1. 没有浏览历史，不能回退
   2. 存在跨域问题（通源）
   3. SEO不友好

Http
HyperText transportation Protocol 超文本传输协议。协议规定了浏览器和万维网服务之间相互通信的规则 

请求：客户端发给服务端的信息

发送内容 请求报文

```
请求行 请求类型 get/post/... + URL(s?ie=utf-8) + Http协议版本(HTTP/1.1)
请求头  Host：atguigu.com
        Cookie: name=guigu
        Content-type: aplication/x-www-form-urlencoded
        User_agent: chrome 83
空行
请求体 useranem=admin&password=admin
```

响应：服务端发还给客户端的结果

返回的结果 响应报文
```
响应行  HTTP版本(HTTP/1.1) 响应状态码(404,400...) 响应状态字符串
响应头(相关内容描述)  Host：atguigu.com
        Content-type: text/html;charset=utf-8
        Content-length: 2048
        Content-encoding: gzip
空行
响应体 (主要返回结果) 
        <html>
            <head>
            </head>
            <body>
                content
            </body>
        </html>
```
