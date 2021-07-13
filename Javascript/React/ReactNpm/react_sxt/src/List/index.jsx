import React, { Component } from 'react'

import Item from '../Item'
import './index.css'
import PropTypes from 'prop-types'

export default class List extends Component {


    static propTypes = {
        todos: PropTypes.array.isRequired,
        updateTodos: PropTypes.func.isRequired,
        removeTodos: PropTypes.func.isRequired
    }


    render() {
        const { todos, updateTodos, removeTodos } = this.props
        return (
            <div>
                <ul className="todo-main">
                    {
                        todos.map(itm => {
                            return <Item key={itm.id} {...itm} updateTodos={updateTodos} removeTodos={removeTodos} />
                        })
                    }
                </ul>
            </div>
        )
    }
}
