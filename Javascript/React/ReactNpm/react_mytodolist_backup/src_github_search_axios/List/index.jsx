import React, { Component } from 'react'
import './index.css'
export default class List extends Component {
    // users: [],
    // isFirstOpen: true,      //是否第一次打开
    // isLoading: false,       //标识是否加载中
    // error: ''               //存储请求错误信息

    render() {
        const { users, isFirstOpen, isLoading, err } = this.props
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
