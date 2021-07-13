
import React, { Component } from 'react'

import './index.css'

import Item from '../Item'
export default class List extends Component {



    render() {
        const { todos, checkTodos, deleteTodos } = this.props
        return (
            <div>
                <ul className="todo-main">
                    {
                        todos.map((todo_obj) => {
                            return <Item key={todo_obj.id} {...todo_obj} checkTodos={checkTodos} deleteTodos={deleteTodos} />
                        })
                    }
                </ul>
            </div>

        )
    }
}
