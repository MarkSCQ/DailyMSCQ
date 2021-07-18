import React, { Component } from 'react'





import List from './List'
import Search from './Search'

export default class App extends Component {
    state = {
        users: [],
        isFirstOpen: true,      //是否第一次打开
        isLoading: false,       //标识是否加载中
        err: ''               //存储请求错误信息
    }

    // saveUsers = (acquiredUsers) => {
    //     this.setState({ users: acquiredUsers })
    // }


    updateAppState = (stateObj) => {
        this.setState(stateObj)
    }

    render() {
        const { users } = this.state
        return (
            <div className="container">
                <Search
                    saveUsers={this.saveUsers}
                    updateAppState={this.updateAppState}
                />

                <List
                    {...this.state}
                />

            </div>
        )
    }
}
