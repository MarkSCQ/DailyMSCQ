import React, { Component } from 'react'
import { nanoid } from 'nanoid'

import './index.css'

export default class Header extends Component {


    inputHandler = (event) => {

        // console.log(event.target.value);

        let { keyCode, target } = event
        if (keyCode !== 13) {
            return;
        }
        if (target.value.trim() === "") {
            alert("Invalid Input")
        }
        const newTodo = { id: nanoid(), content: target.value, isDone: false }
        console.log(newTodo)
        console.log(this.props.addTodos)
        // 
        // update state
        this.props.addTodos(newTodo)
        target.value = ""
    }




    render() {
        return (
            <div className="todo-header">
                <input type="text" onKeyUp={this.inputHandler} placeholder="请输入你的任务名称，按回车键确认" />
            </div>
        )
    }
}
