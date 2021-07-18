import React, { Component } from 'react'

import { BrowserRouter, Route, Link } from 'react-router-dom'


import Home from './components/pages/Home'
import About from './components/pages/About'
import Header from './components/Header'
export default class App extends Component {


    render() {
        return (
            <div>
                <div className="row">
                    <div className="col-xs-offset-2 col-xs-8">
                        <div className="page-header"><h2>React Router Demo</h2></div>
                    </div>
                </div>
                <div className="row">
                    <div className="col-xs-2 col-xs-offset-2">
                        <div className="list-group">

                            {/* <a className="list-group-item" href="./about.html">About</a>
                            <a className="list-group-item active" href="./home.html">Home</a> */}

                            {/* react中靠路有链接实现切换组件 */}
                            <Link className="list-group-item" to="/about">About</Link>
                            <Link className="list-group-item" to="/home">Home</Link>

                        </div>
                    </div>
                    <div className="col-xs-6">
                        <div className="panel">
                            <div className="panel-body">
                                {/* 注册路由，编写路有链接 */}
                                <Route path="/about" component={About} />
                                <Route path="/home" component={Home} />f
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}
