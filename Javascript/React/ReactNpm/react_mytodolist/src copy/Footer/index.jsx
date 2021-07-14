
import React, { Component } from 'react'


import './index.css'

import Item from '../Item'
import { element } from 'prop-types'

export default class Footer extends Component {


    countAllTodos = () => {
        const { todos } = this.props
        // console.log(todos.length)
        return todos.length
    }
    countCheckedAllTodos = () => {

        const { todos } = this.props
        return todos.filter((td) => {
            return td.isDone === true
        }).length
    }


    // deleteCheckedOnes = () => {
    //     const { todos } = this.props

    //     let idlist = []
    //     for (element in todos) {
    //         if (element.isDone) {
    //             idlist.push(element.id)
    //         }
    //     }
    //     console.log(idlist)
    // }


    selectAll = (event) => {
        this.props.checkAll(event.target.checked)
    }

    removeSelected = () => {
        if (window.confirm("Are you sure?")) {
            this.props.removeSelectedTodos()
        }
    }
    render() {
        const checkedNum = this.countCheckedAllTodos()
        const allNum = this.countAllTodos()
        return (
            <div className="todo-footer">
                <label>
                    <input onChange={this.selectAll} type="checkbox" checked={checkedNum === allNum && allNum !== 0 ? true : false} />
                </label>
                <span>
                    <span>{checkedNum}</span> / {allNum}
                </span>
                <button className="btn btn-danger" onClick={this.removeSelected}>Delete Them All</button>
            </div>
        )
    }
}
