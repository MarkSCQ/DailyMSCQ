import React, { Component } from 'react'
import './index.css'

export default class Footer extends Component {

    countChecked = (todos) => {
        return todos.filter((td) => {
            return td.isDone === true
        }).length

    }
    countAll = (todos) => {
        return todos.length
    }


    render() {
        const { todos } = this.props
        const checkeds = this.countChecked(todos)
        const dones = this.countAll(todos)
        console.log(checkeds)
        console.log(dones)

        return (
            <div className="todo-footer">
                <label>
                    <input type="checkbox" />
                </label>
                <span>
                    <span>已完成{checkeds}</span> / 全部{dones}
                </span>
                <button className="btn btn-danger">清除已完成任务</button>
            </div>
        )
    }
}
