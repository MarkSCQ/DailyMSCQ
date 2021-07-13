import React, { Component } from 'react'
import { nanoid } from 'nanoid'
import PropTypes from 'prop-types'

import './index.css'

export default class Header extends Component {

    // 对接收的props state进行限制
    static propTypes = {
        addTodos: PropTypes.func.isRequired
    }

    // ！ 键盘事件的回调
    inputHandler = (event) => {
        let { keyCode, target } = event

        // 如果是 enter
        if (keyCode !== 13)
            return;
        // 如果空input
        if (target.value.trim() === "") {
            alert("Empty input is invalid")
            return;
        }

        // console.log(target.value, keyCode);
        // ！ 创建新 obj
        const TodoObj = { id: nanoid(), content: target.value, isdone: false }
        // ！ 将新的obj传递给app
        this.props.addTodos(TodoObj)
        target.value = ""
    }

    render() {
        return (
            <div className="todo-header">
                <input onKeyUp={this.inputHandler} type="text" placeholder="请输入你的任务名称，按回车键确认" />
            </div>
        )
    }
}
