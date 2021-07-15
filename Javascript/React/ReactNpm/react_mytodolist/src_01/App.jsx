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
        console.log(newtodos)
        this.setState({ todos: newtodos })
    }

    deleteTodos = (id) => {
        console.log("this si deleteTodos()")
        const { todos } = this.state
        console.log("todos")
        console.log(todos)

        const newtodos = todos.filter((td) => {
            return td.id !== id
        })
        console.log(newtodos)

        this.setState({
            todos: newtodos
        })
    }

    checkAll = (checkstate) => {
        const { todos } = this.state
        const newtodos = todos.map((td) => {
            return { ...td, isDone: checkstate }
        })
        this.setState({ todos: newtodos })
    }

    removeSelectedTodos = () => {
        const { todos } = this.state
        console.log(todos)

        const newtodos = todos.filter((td) => {
            return td.isDone === false
        })
        console.log(newtodos)

        this.setState({ todos: newtodos })
    }

    render() {
        const { todos } = this.state
        return (
            <div className="todo-container">
                <div className="todo-wrap">
                    <Header addTodos={this.addTodos} />
                    <List todos={todos} checkTodos={this.checkTodos} deleteTodos={this.deleteTodos} />
                    <Footer todos={todos} checkTodos={this.checkTodos} checkAll={this.checkAll} removeSelectedTodos={this.removeSelectedTodos} />
                </div>
            </div>
        )
    }
}

// export default App
