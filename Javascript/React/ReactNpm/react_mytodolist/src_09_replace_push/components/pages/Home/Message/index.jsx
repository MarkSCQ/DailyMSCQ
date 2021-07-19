import React, { Component } from 'react'
import { Link, Route, Switch } from 'react-router-dom'
import Detail from './Detail'
export default class Message extends Component {
    state = {
        msgArray: [
            { id: "1", title: "info 1" },
            { id: "2", title: "info 2" },
            { id: "3", title: "info 3" },
            { id: "4", title: "info 4" }
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
                                    {/* <Link to={`/home/message/detail/${msg.id}/${msg.title}`}>{msg.title}</Link> */}

                                    {/* search 参数 传递 */}
                                    {/* <Link to={`/home/message/detail/?id=${msg.id}&title=${msg.title}`}>{msg.title}</Link> */}

                                    {/* state参数 */}
                                    <Link replace to={{ pathname: '/home/message/detail', state: { id: msg.id, title: msg.title } }}>{msg.title}</Link>
                                </li>
                            )
                        })
                    }
                </ul>
                <hr />

                <Switch>
                    {/* 声明接收params参数 */}
                    {/* <Route path="/home/message/detail/:id/:title" component={Detail} /> */}

                    {/* search参数无需声明接收 正常路由即可 */}
                    {/* <Route path="/home/message/detail" component={Detail} /> */}

                    {/* state参数无需声明接收 正常路由即可 */}
                    <Route path="/home/message/detail" component={Detail} />

                </Switch>
                {/* <Detail /> */}
            </div>
        )
    }
}
