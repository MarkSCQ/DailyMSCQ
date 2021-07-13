
import React, { Component } from 'react'

import './index.css'

export default class Item extends Component {
    state = {
        mouse_state: false
    }

    handleMouse = (mouse) => {
        return () => {
            if (mouse) {
                this.setState({ mouse_state: true })
                // console.log("Mouse true ", this.state.mouse_state)

            }
            else {
                this.setState({ mouse_state: false })
                // console.log("Mouse true ", this.state.mouse_state)
            }
        }
    }


    checkHandler = (id) => {
        return (event) => {
            this.props.checkTodos(id, event.target.checked)
        }
    }

    deleteHandler = (id) => {

        return () => {
            console.log(id)
            console.log("this is delete fucntion")
            if (window.confirm("Do you really want to delete it?")) {
                this.props.deleteTodos(id)
            }
            else {
                return;

            }
        }
    }

    render() {

        const { id, content, isDone } = this.props
        // console.log("id, content, isDone")
        return (
            <div>
                <li onMouseLeave={this.handleMouse(false)} onMouseEnter={this.handleMouse(true)} style={{ backgroundColor: this.state.mouse_state ? "skyblue" : "white" }} >
                    <label>
                        <input type="checkbox" onClick={this.checkHandler(id)} checked={isDone} />
                        <span>{content}</span>
                    </label>
                    <button className="btn btn-danger" style={{ display: this.state.mouse_state ? "block" : "none" }} onClick={this.deleteHandler(id)}>DELETE</button>
                </li>
            </div>
        )
    }
}
