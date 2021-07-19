import React, { Component } from 'react'

import PubSub from 'pubsub-js'



import './index.css'
export default class List extends Component {

    state = {
        users: [],
        isFirstOpen: true,      //是否第一次打开
        isLoading: false,       //标识是否加载中
        err: ''               //存储请求错误信息
    }

    componentDidMount() {
        PubSub.subscribe('message', (msg, data) => {
            console.log(data)
            this.setState(data)
        })
    }

    render() {
        const { users, isFirstOpen, isLoading, err } = this.state
        return (
            <div className="row">
                {
                    isFirstOpen ? <h2>Welcome</h2> :
                        isLoading ? <h2>Loading</h2> :
                            err ? <h2 style={{ color: 'red' }}>{err}</h2> :
                                users.map((u) => {
                                    return (<div className="card" key={u.login}>
                                        <a rel="noreferrer" href={u.html_url} target="_blank">
                                            <img alt="profileImage" src={u.avatar_url} style={{ width: '100px' }} />
                                        </a>
                                        <p className="card-text">{u.login}</p>
                                    </div>)
                                })
                }


            </div>
        )
    }
}
