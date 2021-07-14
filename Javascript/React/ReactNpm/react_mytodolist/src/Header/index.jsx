import { nanoid } from 'nanoid'
import React, { Component } from 'react'
import './index.css'

export default class Header extends Component {


    inputHandler = (event) => {
        const texts = event.target.value
        const keycode = event.keyCode
        if (keycode !== 13)
            return
        if (texts.trim() === "") {
            alert("Invalid Input")
            return;
        }
        this.props.addTodo_App({ id: nanoid(), content: texts, isDone: false })
        event.target.value = ""
    }



    render() {
        return (
            <div className="todo-header">
                <input type="text" onKeyUp={this.inputHandler} placeholder="请输入你的任务名称，按回车键确认" />
            </div>
        )
    }
}
