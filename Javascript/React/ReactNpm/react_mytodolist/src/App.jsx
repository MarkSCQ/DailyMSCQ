import React, { Component } from 'react'


import './App.css'

import Header from './Header'
import List from './List'
import Footer from './Footer'




export default class App extends Component {

    state = {
        todos: [
            { id: "001", content: "sleep", isDone: false },
            { id: "002", content: "work out", isDone: false },
            { id: "003", content: "code", isDone: false },
            { id: "004", content: "eat", isDone: false },
        ]
    }


    // ! ----- Header Input ----- 
    addTodo_App = (todoObj) => {
        const { todos } = this.state
        const newtodo = [todoObj, ...todos]

        this.setState({ todos: newtodo })
    }
    // * ----- Header Input ----- 


    // ! ----- Todo Item Remove ----- 
    removeTodo_App = (id) => {
        const { todos } = this.state
        const newtodos = todos.filter((todoObj) => {
            return todoObj.id !== id
        })
        this.setState({ todos: newtodos })
    }
    // * ----- Todo Item Remove ----- 


    checkTodo_App = (id, isDone) => {
        console.log("object")
        const { todos } = this.state
        const newtodos = todos.map((todoObj) => {
            if (todoObj.id === id) {
                todoObj.isDone = isDone
                return { ...todoObj, isDone }
            }
            else {
                return todoObj
            }
        })
        console.log(newtodos)
        this.setState({ todos: newtodos })
    }

    checkAllTodo_App = (checkState) => {
        console.log("checkAllTodo_App")
        const { todos } = this.state
        const newtodos = todos.map((todoObj) => {
            return { ...todoObj, isDone: checkState }
        })
        this.setState({ todos: newtodos })
    }
    removeAllSelected_App = () => {
        const { todos } = this.state
        const newtodos = todos.filter((todoObj) => {
            return todoObj.isDone === false
        })
        console.log(newtodos)

        this.setState({ todos: newtodos })

    }
    render() {
        const { todos } = this.state
        return (
            <div className="todo-container">
                <div className="todo-wrap">

                    <Header addTodo_App={this.addTodo_App} />

                    <List
                        todos={todos}
                        addTodo_App={this.addTodo_App}
                        removeTodo_App={this.removeTodo_App}
                        checkTodo_App={this.checkTodo_App}
                    />

                    <Footer
                        todos={todos}
                        checkAllTodo_App={this.checkAllTodo_App}
                        removeAllSelected_App={this.removeAllSelected_App}
                    />

                </div>
            </div>
        )
    }
}
