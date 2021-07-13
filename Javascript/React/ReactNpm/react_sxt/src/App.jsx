import React, { Component } from 'react'

import List from './List'
import Footer from './Footer'
import Header from './Header'

import './App.css'

export default class App extends Component {

    // !  initial state
    state = {
        todos: [
            {
                id: '001',
                content: 'sleep',
                isdone: false
            },
            {
                id: '002',
                content: 'eat',
                isdone: false,
            },
            {
                id: '003',
                content: 'code',
                isdone: true
            },
            {
                id: '004',
                content: 'shopping',
                isdone: true
            }
        ]
    }

    addTodos = (TodoObj) => {
        const { todos } = this.state

        const newTodo = [TodoObj, ...todos]

        this.setState({ todos: newTodo })
    }

    updateTodos = (id, isdone) => {

        const { todos } = this.state

        // ! 匹配处理数据
        const newtodos = todos.map((todoObj) => {
            if (todoObj.id === id) {
                return { ...todoObj, isdone }
            }
            else {
                return todoObj
            }
        })
        this.setState({ todos: newtodos })
    }


    removeTodos = (id) => {
        const { todos } = this.state
        const newtodos = todos.filter((todoObj) => {
            return todoObj.id !== id
        })
        this.setState({ todos: newtodos })

    }


    render() {
        const { todos } = this.state
        return (
            <div>
                <div className="todo-container">
                    <div className="todo-wrap">
                        <Header addTodos={this.addTodos} />
                        <List todos={todos} updateTodos={this.updateTodos} removeTodos={this.removeTodos} />
                        <Footer />
                    </div>
                </div>
            </div>
        )
    }
}
