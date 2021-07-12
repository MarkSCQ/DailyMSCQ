import React, { Component } from 'react'
import './App.css'
export default class App extends Component {
    render() {
        return (
            <div>
                <div classname="todo-container">
                    <div classname="todo-wrap">
                        <div classname="todo-header">
                            <input type="text" placeholder="请输入你的任务名称，按回车键确认" />
                        </div>
                        <ul classname="todo-main">
                            <li>
                                <label>
                                    <input type="checkbox" />
                                    <span>xxxxx</span>
                                </label>
                                <button classname="btn btn-danger" style={{ display: 'none' }}>删除</button>
                            </li>
                            <li>
                                <label>
                                    <input type="checkbox" />
                                    <span>yyyy</span>
                                </label>
                                <button classname="btn btn-danger" style={{ display: 'none' }}>删除</button>
                            </li>
                        </ul>
                        <div classname="todo-footer">
                            <label>
                                <input type="checkbox" />
                            </label>
                            <span>
                                <span>已完成0</span> / 全部2
                            </span>
                            <button classname="btn btn-danger">清除已完成任务</button>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}
