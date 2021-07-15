import React, { Component } from 'react'
import { nanoid } from 'nanoid'

import './index.css'



import Item from '../Item'
export default class List extends Component {
    render() {
        const { todos } = this.props
        return (
            <div>
                <ul className="todo-main">
                    {
                        todos.map((todo_obj) => {
                            return <Item
                                key={nanoid()}
                                todo_obj={todo_obj}
                                removeTodo_App={this.props.removeTodo_App}
                                checkTodo_App={this.props.checkTodo_App}
                            />
                        })
                    }
                </ul>
            </div>
        )
    }
}
