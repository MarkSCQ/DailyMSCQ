import React, { Component } from 'react'

import './App.css'

import Header from './Header/index'
import List from './List/index'
import Footer from './Footer/index'

export default class App extends Component {

    state = {
        todos: [
            { id: "001", content: "sleep", isDone: false },
            { id: "002", content: "eat", isDone: false },
            { id: "003", content: "code", isDone: false },
            { id: "004", content: "files", isDone: false },
        ]
    }


    addTodos = (todoObj) => {
        const { todos } = this.state
        const newTodos = [todoObj, ...todos]
        this.setState({ todos: newTodos })
    }

    checkTodos = (id, isDone) => {
        console.log("this is checkTodos()")
        console.log(id, isDone)
        const { todos } = this.state
        console.log(todos)
        const newtodos = todos.map((todo) => {
            if (todo.id === id) {
                todo.isDone = isDone
                return { ...todo, isDone }
            }
            else {
                return todo
            }
        })
        this.setState({ todos: newtodos })

    }

    deleteTodos = () => {
        console.log("this si deleteTodos()")
    }

    render() {
        const { todos } = this.state
        return (
            <div className="todo-container">
                <div className="todo-wrap">
                    <Header addTodos={this.addTodos} />
                    <List todos={todos} checkTodos={this.checkTodos} deleteTodos={this.deleteTodos} />
                    <Footer />
                </div>
            </div>
        )
    }
}

// export default App
