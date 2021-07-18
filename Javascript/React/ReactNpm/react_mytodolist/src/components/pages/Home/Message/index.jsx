import React, { Component } from 'react'
import { Link, Route, Switch } from 'react-router-dom'
import Detail from './Detail'
export default class Message extends Component {
    state = {
        msgArray: [
            { id: 1, title: "info 1" },
            { id: 2, title: "info 2" },
            { id: 3, title: "info 3" },
            { id: 4, title: "info 4" }
        ]
    }
    render() {
        const { msgArray } = this.state
        return (
            <div>
                <ul>
                    {
                        msgArray.map((msg) => {
                            return (
                                <li key={msg.id}>
                                    {/* 向路由组件传递params参数 */}
                                    <Link to={`/home/message/detail/${msg.id}/${msg.title}`}>{msg.title}</Link>
                                </li>
                            )
                        })
                    }
                </ul>
                <hr />

                <Switch>
                    {/* 声明接收params参数 */}
                    <Route path="/home/message/detail/:id/:title" component={Detail} />
                </Switch>
                {/* <Detail /> */}
            </div>
        )
    }
}
