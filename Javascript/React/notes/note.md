# React
用于构建用户界面的JavaScript裤

React是一个将数据渲染为HTML视图的开源JavaScript裤

组件化/模块化

**特点**
1. 组件化 声明式编码 提升开发效率和组件复用率
2. react native 可以写移动端开发
3. 虚拟DOM+优秀的Diffing算法，尽量减少真是DOM的交互

JSX makes writing virtual dom more easier

关于虚拟dom
1. 本质是Object类型的对象
2. 虚拟DOM比较“轻”，相比如真实DOM，因为虚拟DOM是react内不再用，所以无需使用真实DOM上那么多的属性
3. 虚拟DOM最终会被React转化为真实DOM，呈现在页面上
   

XML 存储数据和传输数据的一种方式<br>
后来发现JSON好像更牛逼<br>


JSON parse和stringfy

关于JSX
1. 全程JSX
2. react定义的一种类似XML的JS拓展与法
3. 本质上是React.createElement(component，props,....)的语法糖
4. 作用 用于创建虚拟DOM
   1. 写法 var ee = \<h1\>hello JSX \</h1\>
   2. 注意事项： 
      1. 他不是字符串也不是HTML/XML标签
      2. 他最终产生的将是一个JS对象
5. 标签名任意：HTML标签或者其他标签


JSX 语法规则：
    1. 定义虚拟DOM时，不要写引号
    2. 标签中混入JS表达式时 使用{}引入
    3. 样式类名不用class 用className. class -> className
    4. 内联样式需要用 style={{key:value}}的形式去写
    5. 虚拟DOM不能有多个根标签，只能有一个根标签
    6. 标签必须必和 \<input type="text" /\>
    7. 标签首字母
        (1) 小写字母开头， 则将标签转换为html中同名元素，若html中无改标签同名元素，则报错
        (2) 若大写开头，react就去渲染该组件，若组件未定义，则报错



JS表达式
JS语句（代码）
<br>

Javascript 模块
1. ***向外提供特定功能的js程序，一般就是一个js文件***
2. 随着业务逻辑增加，代码越来越复杂
3. 复用js，简化js程序编写 提高运行效率
<br>

组件
1. 理解 ***用来实现局部功能效果的代码和资源的集合***
2. 一个界面功能更复杂
3. 复用 编码 简化项目编码 提高运行效率


<br>
模块化： 当应用的js都已模块来编写，这个应用就是一个模块化的应用<br>
组件化：复杂的功能以组建来实现 这个应用就是一个组件化的应用<br>


函数式组件，用函数定义，适用于简单组件的定义。<br>
1. ***函数式组件 函数必须开头大写。***
2. ***组件必须用标签 </>***

类式组件，用类定义，适用于复杂组件的定义<br>



在实验中,使用到了babel。经过Babel翻译的jsx会进入严格模式(ES5 strict mode)
<img src="../imgs/functional_components.PNG">
(ES5 严格模式 strict mode 禁止自定义函数的this指向window)
        

关于 JavaScript class的三点
1. constructor 不是必须写的,需要实例化的时候才写
2. 关于super，如果a类继承b类且a中有构造器，那么a类构造器中super必须被调用
3. 类中定义的方法 都是放在了类的原型对象上




类式组件 
1. 继承父类 react component
2. 必须有render
3. render必须有返回值


render()放在哪里？    MyComponent的原型对象放在类中 供实例使用。
render()中的this是谁? MyComponent的实例对象，MyComponent组件实例对象


执行了ReactDOM.render(....)后发生了什么？
1. React解析足见标签 找到了MyComponent组件
2. 发现组件是使用类定义的，随后new该类的实例，并通过该类的实例调用到圆形render的方法
3. 将render返回的虚拟dom转化为真实dom，随后呈现在页面中


什么事复杂组件？
有状态（State）就是复杂组件

什么是状态（state）？

组件的状态驱动着页面。 => 数据在状态里。状态中的数据驱动叶绵绵的展示



组件实例的三大核心属性 State
1. 理解
    1. state是组件对象最重要的属性，值是对象，可以包含多个key-value
    2. 组件被称为“状态机”，通过更新组建的state来更新页面的显式（重新渲染组件）
2. 注意
   1. 组建中render方法中的this为组建的实例对象
   2. 组件自定义的方法中 this为undefined如何解决？
      1. 强制绑定this，通过函数兑现个的bind()
      2. 箭头函数
3. 状态数据 不能直接修改或者更新


Props 传递参数
1. class中调用 this.props.variablename
2. function中调用 props.variablename


Destructuring the props and state
1. in function, destructuring in function variable <br> 
    <img src="../imgs/des1.PNG"><br>
2. destructuring in body<br>
    <img src="../imgs/des2.PNG"><br>
3.destructuring in class<br>
    <img src="../imgs/des3class.PNG"><br>
    <img src="../imgs/des4class.PNG"><br>
 


click in Functional Components
1. do not put () in {}
   what should is as below

        function FunctionClick() {
            const fun = () => {
                console.log("caonimalegebi")
            }
            return (
                <div>
                    <button onClick={fun}>
                        func
                    </button>
                </div>
            )
        }
2. 这两种写法都ok
   <img src="../imgs/funclick.PNG"> 

3. Class Component中写记得加上this example如下图
    <img src="../imgs/classclick.PNG"> 


Event binding in React

    // write in class
    mtheod 1-3
    changeMsg() {
        this.setState({
            msg: "goodbye"
        })
    }
    
    method 4 in official tutorial
    clickmsg = ()=>{
        this.setState({msg:"bye"})
    }
* method 1

        // write in render()
        <button onClick={this.changeMsg.bind(this)}>click</button> 

* method 2

        // write in render()
        <button onClick={this.changeMsg}>click</button> 

* method 3 

        // write in render()
        <button onClick={()=>this.changeMsg()}>click</button>

* method 4 

        // write in render()
        clickmsg = ()=>{this.setState({msg:"bye"})}       
        

What are the differencs between using binding adn arrow function???


Passing Component to component

setting parameters or props. In the image below, the function is passed as param. The *greetHandler* is functioned as param name, the param content or value is the function *this.greetparent*.

<img src="../imgs/passpara.PNG">

The image below is child component which is called to make a button and call the *greetparent* function. This component takes the parent component's input as event to be triggered and it will also insert *"KID"* to tell it from child component.

<img src="../imgs/passkid.PNG"> 

The flow of how this work can be described as below.

<img src="../imgs/flow.PNG"> 


**Lists and Keys**

When rendering list, remember render the key too. The updates of data is based on the key attribute. Key is a must for react.
1. A "key" is a special string attribute you need to linclude when creating lists of elements.
2. Keys give the elements a stable identity
3. Keys help react identify which items have been changed, added or removed
4. Help in efficient update of user interface


**Index as key**

Problems: when using index as key, there will not have huge difference if we add some elemenmts at the tail. However, there might cause problems when insert at the head.

**Example**

<img src="../imgs/idxkey2.PNG"> 

In the image above, we want to update the data by insert at the head. But when react read the data we want to insert, it compares the origin with current one we have, that is reusing the data. 

As we human being, we might think the data should shift down if we add at the beginning. However, react will just reuse the data.

In another word, the key and the value itself, do not have a strong relationship. This situation is more vivid when making the todo using this link (https://codepen.io/gopinav/pen/gQpepq).


<img src="../imgs/idxkey.PNG"> 
 
Index as key

When to use index as a key?

1. The items in your list do not have a unique id
2. The list is static and will not chage
3. The list will never be reordered or filtered



Stying React Components
1. CSS stylesheets
2. inline stying
3. CSS modules
