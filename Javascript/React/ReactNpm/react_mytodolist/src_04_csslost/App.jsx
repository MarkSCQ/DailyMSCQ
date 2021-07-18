import React, { Component } from 'react'

import { BrowserRouter, Route, NavLink, Link, Switch } from 'react-router-dom'

// NavLink Link的升级版 这里用于高亮
import Home from './components/pages/Home'
import About from './components/pages/About'
import Header from './components/Header'
import MyNavLink from './components/MyNavLink'
import Test from './components/Test'



export default class App extends Component {


    render() {
        return (
            <div>
                <div className="row">
                    <div className="col-xs-offset-2 col-xs-8">
                        <Header />
                    </div>
                </div>
                <div className="row">
                    <div className="col-xs-2 col-xs-offset-2">
                        <div className="list-group">

                            {/* <a className="list-group-item" href="./about.html">About</a>
                            <a className="list-group-item active" href="./home.html">Home</a> */}

                            {/* react中靠路有链接实现切换组件 */}
                            {/* 
                            写法一 props 传递 标签内容
                            <MyNavLink to="/about" content="About" />
                            <MyNavLink to="/home" content="Home" /> */}
                            {/* 写法二 标签体传递标签内容 */}
                            <Switch>
                                <MyNavLink to="/home">Home</MyNavLink>
                                <MyNavLink to="/about">About</MyNavLink>
                            </Switch>
                        </div>
                    </div>
                    <div className="col-xs-6">
                        <div className="panel">
                            <div className="panel-body">
                                {/* 注册路由，编写路有链接 */}
                                <Route path="/about" component={About} />
                                <Route path="/home" component={Home} />
                                <Route path="/home" component={Test} />
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}
