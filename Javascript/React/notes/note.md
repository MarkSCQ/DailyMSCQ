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



Mounting Lifecycle Methods 

1. constructor(props)
   1. A special functiont hat will get called whenever a new component is created
   2. initializing state, binding the event handlers
   3. what you should not do: do not cause side effects like http requests
   4. super(props), directly overwrite this.state
2. static getDerivedStateFromProps(props,state)
   This is a rarely used lifecycle method
   1. this mehtod is used when the state of components depends on the changes in props over time
   2. this method is used to get the props and set the state
   3. this method is static, so you cannot use this to call it 
   4. what you should not do: do not cause side effects like http requests
3. render()
   1. only required method
   2. read props and states and return jsx
   3. what you should not do: do not change the state or interact with DOM or make ajax calls
   4. The childern components lifecycle methods are also executed.
4. componentDidMount()
   
    componentDidMount() is invoked immediately after a component is mounted (inserted into the tree). Initialization that requires DOM nodes should go here. If you need to load data from a remote endpoint, this is a good place to instantiate the network request.

   1. This mehod will be invoked once of a given component and Invoked immediately after a component and all its children components have been rendered to the DOM
   2. this mehthod is a good palce to perform initialization that reqiures DOM nodes and also load data by making network requests. The side effects: ex: interacting with dom and perfrom any ajax calls to load data


Updating lifecyclye methods
1. static getDerivedStateFromProps(props,state)
    * return null or an object to represent the updated state of the component. Method is called every time a component is re-rendered. 
    * this method is used when the states depends on the props of the component
    * you should not cause any side effect and get odd state from props 
    * rarely used
2. shouldComponentUpdate(nextProps, nextState) 
   * Dictates if the component should re-render or not
   * by defalut, all class components will render whenever the propos or their state changes
   * This method can prevent that defalut behavior by return false
   * Performance Optimization
   * Should not cause side effects like http requests
3. render()
   1. only required method
   2. read props and states and return jsx
   3. what you should not do: do not change the state or interact with DOM or make ajax calls
   4. The childern components lifecycle methods are also executed.
4. getSnapshotBeforeUpdate(prevProps,prevState)
   1. called right before the changes from the virtual DOM are to be relected in the DOM
   2. rarely used
   3. used to capture information of DOM
   4. This method will either return null or return a value. Returned value will be passed as the third parameter to the next method.  
5. componentDidUpdate(prevProps,prevSate,snapshot)
   
   componentDidUpdate() is invoked immediately after updating occurs. This method is not called for the initial render.

   1. called after the render is finished in the re-render cycles
   2. this method is garanteed to be called only once in each rerender cycle 
   3. make ajax calles 




shouldComponentUpdate(nextProps, nextState) 
   * Dictates if the component should re-render or not
   * by defalut, all class components will render whenever the propos or their state changes
   * This method can prevent that defalut behavior by return false
   * Performance Optimization
   * Should not cause side effects like http requests

<img src="../imgs/rp.PNG"> 
 

 <img src="../imgs/sc.PNG"> 
 <img src="../imgs/pc1.PNG"> 

always rerender an new object or array when using purecomponent

Summary for the PureComponent
1. We can create a component by extending the PureComponent Class
2. A PureComponent implements the shouldComponentUpdate lifecycle method by performing a shallow comparison on the props and state of the component
3. if there is no difference, the component is not re-rendered - performance boost
4. its a good idea to ensure that all the children components are also pure to avoid unexpected behaviors.
5. Never mutate the state. Always return a new object that reflects the new state



Fragments, wrap the contenst without using <> or \<div\>. 
div cannot hold some special contents like table td contents

PureComponents will only rerender the class components when there is a difference in shallow comparison of props and states. it uses shouldComponentUpdate with shallow prop and state comparison.

Shallow comparion can be understood as value compariosn instead of reference comparison

memo components is the purecomponents for the functional components


Ref forwarding is a technique for automatically passing a ref through a component to one of its children. 


// Ref a method to access dom node


Ref forwarding  用于在父组件中操作子组件中的dom节点


组件内的标签可以定义ref属性来标志自己

the tag inside the component can be tracked by using ref


Three types of writing refs
1. string refs 
   1. ref="xxx"
2. function refs.
   在下图实例中，ref的回调函数输出的值是当前input tag，a就是当前ref所在节点。a作为当前ref所在节点，赋值给了demo实例的input1属性
   <img src="../imgs/functionref.PNG"> 

            class NonStringRef extends Component {
            clickhandler = () => {
                console.log("@")
                console.log(this)
            }
            showdata1 = () => {
                const { input1 } = this
                alert(input1.value)
            }

            showdata2 = () => {
                const { input2 } = this
                alert(input2.value)
            }
            render() {
                return (
                    <div>
                        <input ref={currentNode => { this.input1 = currentNode }} type="text" placeholder="focus and display data" />&nbsp;
                        <button onClick={this.showdata1}>click</button> &nbsp;
                        <input ref={currentNode => { this.input2 = currentNode }} onBlur={this.showdata2} type="text" placeholder="los focus and display data" /> &nbsp;
                    </div>
                )
            }
        }
    
    回调式函数 ref，callback ref。回调式ref会执行两次当更新的时候。

        官方说法：
        If the ref callback is defined as an inline function, it will get called twice during updates, first with null and then again with the DOM element. This is because a new instance of the function is created with each render, so React needs to clear the old ref and set up the new one. You can avoid this by defining the ref callback as a bound method on the class, but note that it shouldn’t matter in most cases.

    解释和例子
    下方的代码例子是点击改变成hot或者cold。第一次页面正常渲染，实例对象被render调用然后渲染到页面。但是第二次使用的时候，会替换掉之前的ref，更新一个新的ref，所以会额外产生一个null。这种不明显的错误绝大部分时间不会产生致命的影响。

        class FuncRef extends Component {

            state = { isHot: true }

            showInfo = () => {
                const { input1 } = this
                alert(input1.value)
            }

            changeWeather = () => {
                this.setState({ isHot: !this.state.isHot })
            }
            render() {
                return (
                    <div>
                        <h1 onClick={this.changeWeather}>Today is {this.state.isHot ? "hot" : "cold"}</h1>
                        <input ref={(currentNode) => { this.input1 = currentNode; console.log("@", currentNode) }} type="text" />&nbsp;
                        <button onClick={this.showInfo} >click</button> &nbsp;
                    </div>
                )
            }
        }

        export default FuncRef

    针对额外产生的null，在使用callback function时，解决办法就是把写在tag中的内联函数写到外头去，以下为示例

        class NonStringRef extends Component {
            clickhandler = () => {
                console.log("@")
                console.log(this)
            }
            showdata1 = () => {
                const { input1 } = this
                alert(input1.value)
            }

            showdata2 = () => {
                const { input2 } = this
                alert(input2.value)
            }
            render() {
                return (
                    <div>
                        <input ref={currentNode => { this.input1 = currentNode }} type="text" placeholder="focus and display data" />&nbsp;
                        <button onClick={this.showdata1}>click</button> &nbsp;
                        <input ref={currentNode => { this.input2 = currentNode }} onBlur={this.showdata2} type="text" placeholder="los focus and display data" /> &nbsp;
                    </div>
                )
            }
        }

        export default NonStringRef


3. create ref

    会用 React.createRef()相对于回调函数 callback的方式略嫌麻烦，需要几个ref就得create几个ref。这是react官方最推荐的 ref书写形式。没有之一。

        class RefCreateRef extends Component {
            // React.createRef() 调用后可以返回一个容器，该容器可以存储被ref表示的节点，该容器“专人专用”。只能存一个。多次反复存储会产生覆盖。
            myRef = React.createRef();
            myRef2 = React.createRef();

            showData = () => {
                // current is fixed current是固定的属性 不能更改
                // console.log(this.myRef.current.value)
                // const { input1 } = this
                alert(this.myRef.current.value)
            }
            showData2 = () => {
                // const { input2 } = this
                // alert(input2.value)
                alert(this.myRef.current.value)
            }

            render() {
                return (
                    <div>
                        {/* input is storeed in myRef */}
                        <input ref={this.myRef} type="text" /> &nbsp;

                        <button onClick={this.showData} >click</button> &nbsp;

                        <input onBlur={this.showData2} ref={this.myRef2} type="text" />

                    </div>
                )
            }
        }

        export default RefCreateRef

Ref summary
1. 字符串ref 尽量避免ref 除非条件不允许
2. 回调式 callback
3. createRef()

Call back 常用 23都是ok的。


事件
1. 通过onXXXX属性指定的事件处理函数
   1. Reack使用的是自定义事件，而不是原生DOM事件，这是为了更好的兼容性
   2. React中的事件是通过事件委托的方式处理（委托了给了最外层元素），这是为了高效。
2. 通过event.target得到发生事件的DOM元素对象 react官方提示，不要过分使用ref



Controlled Component
页面中所有输入类的DOM，随着输入可以把值维护到state中，等需要使用时，将值从state中取出 这就是受控组件。Controlled component


Un-Controlled Componnet
随用随取


官方说法

        Uncontrolled Components

        In most cases, we recommend using controlled components to implement forms. In a controlled component, form data is handled by a React component. The alternative is uncontrolled components, where form data is handled by the DOM itself.


        Controlled Components
        In HTML, form elements such as <input>, <textarea>, and <select> typically maintain their own state and update it based on user input. In React, mutable state is typically kept in the state property of components, and only updated with setState().

        We can combine the two by making the React state be the “single source of truth”. Then the React component that renders a form also controls what happens in that form on subsequent user input. An input form element whose value is controlled by React in this way is called a “controlled component”.



下面一段代码想要达到的目的是 1.输入uname passwd;2. 存入state中
<img src="../imgs/currying1.PNG"> 

分析：
1. 有两种存储input data到state中的方法 一个是每一个input写一个setState，另一个是利用currying
2. 第一种方法 每一个input写一个setState，虽然效果区别不大，但是很麻烦。如下所列，passwd，uname需要个写一个。如果是普通的登录倒还好，如果是注册需要填写大量数据，那这种方法就很笨拙

        saveUname = (event) => {
            this.setState({ username: event.target.value })
        }

        savePasswd = (event) => {
            this.setState({ password: event.target.value })
        }

3. 利用 function currying 可以将多个save setState合为一个。上图的一些细节问题
   1. onChange 需要的是一个函数 而不是函数返回值
   2. 利用currying，返回的将会是一个function而不是一个value，所以通过使用currying的方式写函(return)可以实现目的
   3. 上图中saveData()中的data，这个data在传值的时候扮演的是一个string的角色，也就是说我们如果setState中写的data，不会对应为password或者username，他将会被创建为一个新的字段data。所以这里不能直接写一个data上去，需要在data外头加上[]进行包裹
4. 但是，通过对于onChange的分析，我们可以得出一个结论，即onChange需要的是一个函数而不是一个值。arrow function 箭头函数就可以被纳入考虑。如下面代码块所示，将onChange的函数写成arrow function也可以达到目标。并且此时不需要currying

        saveData2 = (data, value) => {
            this.setState({ [data]: value })
        }

        uname <input type="text" name="username" onChange={(event) => this.saveData2("username", event.target.value)} /> <br />


高阶函数：如果一个函数符合下面两个规范中的任何一个，那么他就是高阶函数
1. 若函数A，接收的参数是一个函数，那么A就可以称之为高阶函数
2. 若函数A，调用的返回值依旧是一个函数，那么A就可以称之为高阶函数
3. 常见的高阶函数 Promise SetTimeout array.map

函数currying 通过函数调用继续返回函数的方式，实现多次接收参数后统一处理的函数编码形式

        一个简单的currying

        function sum(a){
            return (b)=>{
                return (c)=>{
                    return a+b+c
                }
            }
        }

        sum(1)(2)(3)



组件生命周期


Mount: 第一次被render到page上
Unmount: 组件被移除成为unmount



Render 调用的次数1+n。第一次渲染 render到页面，后面没更新一次state就需要render一次



在关键点调用特殊函数完成特殊的任务。生命周期回调（钩子）（函数），react会帮你调。

componentDidMount()

componnetWillUnmount()





关于生命周期
1. 组件从创建到死亡会经历一些特定的阶段
2. React组建中包换一系列钩子函数（生命周期回调函数），会在特定时间点调用
3. 在定义组件时，会在特定的生命周期回调函数中做特定的工作



LifeCyclye



强制更新，forceUpdate()，不受到shouldComponentUpdate()限制



旧生命周期总结
1. 初始化阶段：由ReactDOM.render触发，初次渲染
   1. constructor()
   2. componentWillMount()
   3. render()
   4. componnetDidMount()==>常用 一般在这个钩子中做一些初始化的事儿。例如开启定时器，发送网络请求，订阅请求
2. 更新阶段：由组件内部this.setState或父组件render触发（强制更新，forceUpdate，234）
   1. shouldComponentUpdate()
   2. componentWillUpdate()
   3. render()
   4. componentDidUpdate()
3. 卸载组件:由ReactDOM.unmountComponnetAtNode()触发
   1. componentWillUnmount() ===> 常用。一般在这个钩子中做一些收尾工作，例如 关闭定时器，取消订阅消息


<img src="../imgs/react生命周期(旧).png"> 


新版本lifecycle中名称更新，除了willunmount,其他的will都要加上UNSAFE_
* UNSAFE_componentWillMount()
* UNSAFE_componentWillReceiveProps()
* UNSAFE_componentWillUpdate()

<img src="../imgs/react生命周期(新).png"> 



getDerivedStateFromProps() 从props中得到一个衍生的状态。这个函数有两个参数 一个props一个state
一旦使用这个函数，那么state将无法做出更新。从上图新的生命周期中可以看出，getDerivedStateFromProps在中间截断，也就是说无论是mount亦或者update，如果getDerivedStateFromProps存在且有了赋值效果，那么state都无法被更新。使用场景和概率极低。

适用场景，state的值完全基于props。官网说明：
*This method exists for rare use cases where the state depends on changes in props over time. For example, it might be handy for implementing a <Transition> component that compares its previous and next children to decide which of them to animate in and out.*

这个方法不是必须使用，因为通过constructor也可以得到props



getSnapshotBeforeUpdate() 更新之前获取快照


中文说明 在最近一次渲染输出（提交到DOM节点）之前调用。他使得组件能再发生更改之前从DOM中捕获一些信息。此生命周期的任何返回值将作为参数传递给componentDidUpdate（）

此方法使用场景并不常见  


新生命周期 总结
1. 初始化阶段，由ReactDOM.render触发，初次渲染
   1. constructor()
   2. getDerivedStateFromProps()
   3. render()
   4. componnetDidMount()==>常用 一般在这个钩子中做一些初始化的事儿。例如开启定时器，发送网络请求，订阅请求
2. 更新阶段，由组件内部this.setState()或父组件重新render触发
   1. getDerivedStateFromProps()
   2. shouldComponentUpdate()
   3. render()
   4. getSanpshotBeforeUpdate
   5. componentDidUpdate()
3. 卸载组件，由ReactDOM.unmountComponentAtNode()触发
   1. componentWillUnmount() ===> 常用。一般在这个钩子中做一些收尾工作，例如 关闭定时器，取消订阅消息


经典面试题
1. react/vue 中的key有什么作用？Key的内部原理是什么
2. 为什么遍历列表式，key最好不要用index？

1. 虚拟DOM中Key的作用：
   1. 简单地说就是：key是虚拟DOM对象的标识，在更新显式时key起着极其重要的作用
   2. 详细的说：当状态中的数据发生变化时，react会根据新数据生成新的虚拟DOM，随后react进行新虚拟dom和旧虚拟dom的diffing对比。规则如下：
      1. 旧虚拟dom中找到了与新虚拟dom中相同的key
         1. 若虚拟dom中内容不变，直接使用之前的真实dom
         2. 若虚拟dom中内容改变，则声称新的真实dom，随后替换掉页面中之前的真实dom
      2. 旧虚拟DOM中没有找到与新虚拟DOM中相同的key
         1. 根据数据创见得新的真实dom，然后渲染到页面
2. 用index作为key引发的问题
   1. 若对数据进行：逆序添加，逆序删除等破坏顺序的操作
      1. 会产生没有必要的真实DOM更新 ==> 界面效果没问题，效率低
   2. 如果结构中包含输入类DOM
      1. 会产生错误DOM的更新 ==> 界面有问题
   3. 注意，如果不存在对数据的逆序添加，逆序删除等破坏顺序的操作，仅用于渲染列表用于展示，index作为key是没有问题的
        
3. 开发中如何选择key?:
    1.最好使用每条数据的唯一标识作为key, 比如id、手机号、身份证号、学号等唯一值。
    2.如果确定只是简单的展示数据，用index也是可以的。



## What is State?

The state is an instance of React Component Class can be defined as an object of a set of observable properties that control the behavior of the component. In other words, the State of a component is an object that holds some information that may change over the lifetime of the component. For example, let us think of the clock that we created in this article, we were calling the render() method every second explicitly, but React provides a better way to achieve the same result and that is by using State, storing the value of time as a member of the component’s state. We will look into this more elaborately later in the article.
 

Difference of Props and State.

We have already learned about Props and we got to know that Props are also objects that hold information to control the behavior of that particular component, sounds familiar to State indeed but props and states are nowhere near be same. Let us differentiate the two.
 
Props are immutable i.e. once set the props cannot be changed, while State is an observable object that is to be used to hold data that may change over time and to control the behavior after each change.
States can only be used in Class Components while Props don’t have this limitation.
While Props are set by the parent component, State is generally updated by event handlers. For example, let us consider the toggle the theme of the GeeksforGeeks {IDE} page. It can be implemented using State where the probable values of the State can be either light or dark and upon selection, the IDE changes its color. 


What is Ajax:

Difference NPM and Yarn

Portal:

(from Docs)
Portals provide a way to render children into a DOM node that exists outside the DOM hierarchy of the parent component.

但是前提是你得知道那个目标的id或者能够用一种方式捕捉到那个target

(传送门)

Why need it?










