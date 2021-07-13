
import React, { Component } from 'react'


import './index.css'

import Item from '../Item'
import { element } from 'prop-types'

export default class Footer extends Component {


    checkAllTodos = () => {

    }

    countAllTodos = () => {
        const { todos } = this.props
        console.log(todos.length)
        return todos.length
    }
    countCheckedAllTodos = () => {

        const { todos } = this.props
        return todos.filter((td) => {
            return td.isDone === true
        }).length
    }

    selectAll = (event) => {
        const { todos } = this.props
        console.log(todos)
        const idlist = []
        for (var i = 0; i < todos.length; i++) {

            idlist.push(todos[i].id)
            this.props.checkTodos(todos[i].id, !event.target.checked)
        }
    }

    deleteCheckedOnes = () => {
        const { todos } = this.props

        let idlist = []
        for (element in todos) {
            if (element.isDone) {
                idlist.push(element.id)
            }
        }
        console.log(idlist)
    }


    render() {
        return (
            <div className="todo-footer">
                <label>
                    <input onClick={this.selectAll} type="checkbox" defaultChecked={false} />
                </label>
                <span>
                    <span>{this.countCheckedAllTodos()}</span> / {this.countAllTodos()}
                </span>
                <button className="btn btn-danger">Delete Them All</button>
            </div>
        )
    }
}
