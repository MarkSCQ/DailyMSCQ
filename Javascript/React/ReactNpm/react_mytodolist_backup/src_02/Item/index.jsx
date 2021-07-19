import React, { Component } from 'react'
import './index.css'

export default class Item extends Component {

    state = {
        mouseState: false
    }

    mouseMove = (mouse_state) => {
        return () => {
            if (mouse_state) {
                this.setState({ mouseState: true })
            }
            else {
                this.setState({ mouseState: false })
            }
        }
    }

    removeHandler = (id) => {

        return () => {
            if (window.confirm("Remove?")) {
                this.props.removeTodo_App(id)
            }
        }
    }

    checkHandler = (id) => {
        return (event) => {
            this.props.checkTodo_App(id, event.target.checked)

        }
    }

    render() {

        const { id, content, isDone } = this.props.todo_obj
        console.log(id, content, isDone)
        return (
            <div>
                <li onMouseEnter={this.mouseMove(true)} onMouseLeave={this.mouseMove(false)} style={{ backgroundColor: this.state.mouseState ? "skyblue" : "white" }}  >
                    <label>
                        <input type="checkbox" onChange={this.checkHandler(id)} checked={isDone} />
                        <span id={id}>{content}</span>
                    </label>
                    <button className="btn btn-danger" onClick={this.removeHandler(id)} style={{ display: this.state.mouseState ? "block" : "none" }}>DELETE</button>
                </li>

            </div>
        )
    }
}
