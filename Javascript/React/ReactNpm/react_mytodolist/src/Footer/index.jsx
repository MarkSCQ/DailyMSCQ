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

    checkAll = (event) => {
        this.props.checkAllTodo_App(event.target.checked)
    }

    removeSelected = () => {
        this.props.removeAllSelected_App()
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
                    <input type="checkbox" onChange={this.checkAll} checked={dones === checkeds && dones !== 0 ? true : false} />
                </label>
                <span>
                    <span>Dones {checkeds}</span> / {dones}
                </span>
                <button className="btn btn-danger" onClick={this.removeSelected}>Remove Selected Ones</button>
            </div>
        )
    }
}
