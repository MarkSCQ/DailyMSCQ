Spring MVC 简化的web开发框架

Spring MVC 是什么

相关度高的归为一层 

代码架构与MVC

经典三层 系统划分
<img src="imgs/jd3_1.PNG">


MVC 设计模式(代码的组织形式)

M   model 模型 (数据模型[pojo, vo, po] + 业务模型[业务逻辑])

V   view 视图 （jsp html）

C   controller 控制器 （servlet）


Spring MVC 应用于表现层的框架


SpringMVC 全名Springweb MVC 是一种基于java的实现MVC设计模型的请求驱动类型轻量级web框架 属于springframework的后续产品

SpringMVC本质可以认为是对servlet的封装 简化了servlet的开发
作用
1) 接受请求
2) 返回响应 跳转页面阿斯蒂芬



SpringMVC spring的一个模块 专用于web开发，基于Spring

web开发地曾是Servlet框架是在servlet上加入了一些功能 让web开放更方便

SpringMVC是一个Spring， Spring是一个容器，ioc能够管理对象，可以使用<bean> @component @Repository @Service，@Controller

SpringMVC能够创建对象米放入到容器中（SpringMVC） SpringMVC容器中放的是控制器对象

我们要做的是使用@Controller创建控制器对象，把对象放到SpringMVC容器中把创建的对象作为控制其使用，这个控制器对象能够接受用户的请求显示处理结果，就当做一个servlet使用

使用@controller朱姐创建的是一个普通类的对象，不是servlert，springmmvc赋予了控制器对象一些额外的功能

web开发地曾是Servlet，SpringMVC中有一个对象是Servlet：DispatcherServlert。

DispatchersServlet:负责接收用户的所有请求，用户把请求给了DispatcherServlet，之后DIspatcherServlet把请求转发给Controller对象，最后是Controller对象处理请求

DispatcherServlet：中央调度器

Index.jsp -> DispatcherServlert -> （转发分配给）Controller对象控制对象（@Controller注解创建的对象）

Controller可以有多个


Spring IOC AOP

IOC: Inversion of Controller<br>
AOP: Aspect-Oriented Programming<br>


SpringMVC请求处理过程

1. 发起some.do
2. tomcat (web.xml 根据 url.pattern中间的规则 知道 *.do 的请求发送给 DispatcherServlet中央调度器)
3. DispatcherServlet，根据MVC配置文件知道some.do是对应的doSome的方法
4. DispatcherServlet吧some.do转发给MyController.doSome()方法
5. 框架根据doSome() 把得到的 ModelAndView 进行处理转发到show。jsp


上面过程简化方式

some.do -> DispatcherServlet -> MyController

SpringMVC执行过程的分析：

1. Tomcat启动 创建容器的过程
   通过load-on-start标签指定的 
   1，创建DispatcherServelet 对象
   DispatcherServlet的父类世纪城HttpServlet的，他是一个Servlet，被创建时会执行init()方法

        //servlet的初始化会执行init()方法，DispatcherServlet在init()中
        
        //创建容器 读取配置文件
        WebApplicationContext ctx = new ClassPathXmlApplicationContext("springmvc.xml");
        //把对象容器放入到ServletContext中
        getServletContext().SetAttribute(key,ctx);

        上面创建容器的作用：创建@Controller注解所在的类的对象，创捷MyController对象，将这个对象放入springmvc容器中，容器是map，类似map.put("MyController",MyController对象)

2. 请求的额处理过程

    执行servlert的service() =》 doService() => DispatcherServlet.doDispatch(){调用MyController的 doSome方法}



1. 配置中央调度器 DispatcherServlet，指定自定义文件路径
2. 自定义文件中添加组件扫描器 视图解析器
3. jsp文件编写
4. Controller中填写转发
   1. RequestMapping可以写多个请求，多个请求对应一个controller 也是可以的