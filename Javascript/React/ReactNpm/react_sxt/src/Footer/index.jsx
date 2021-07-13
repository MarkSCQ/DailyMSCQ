import React, { Component } from 'react'

import './index.css'
export default class index extends Component {

    countAllTodos = (todos) => {
        // const { todos } = this.props
        console.log(todos.length)
        return todos.length
    }
    countCheckedAllTodos = (todos) => {

        // const { todos } = this.props
        const arr = todos.filter((td) => {
            return td.isdone === true
        }).length
        console.log('ar ', arr)
        return arr
    }


    removeAllHandler = () => {
        if (window.confirm("Remove selected?")) {
            this.props.removeDoneTodos()
        }
        else {
            return;
        }
    }

    changeAllHandler = (event) => {
        this.props.checkAllTodos(event.target.checked)
    }
    render() {
        const { todos } = this.props
        const donecount = this.countCheckedAllTodos(todos)
        const checkcount = this.countAllTodos(todos)
        return (
            <div className="todo-footer">
                <label>
                    {/* defaultchecked只在第一次产生效果 使用checked必须使用onchange handler*/}
                    {/* <input type="checkbox" checked={donecount === checkcount ? true : false} onChange={donecount === checkcount ? this.changeAllHandler(true) : this.changeAllHandler(false)} /> */}
                    <input type="checkbox" checked={donecount === checkcount && checkcount !== 0 ? true : false} onChange={this.changeAllHandler} />
                </label>
                <span>
                    <span>已完成 {donecount} </span> / 全部 {checkcount}
                </span>
                <button className="btn btn-danger" onClick={this.removeAllHandler}>清除已完成任务</button>
            </div>
        )
    }
}
