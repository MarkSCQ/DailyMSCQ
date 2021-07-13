import React, { Component } from 'react'
import './index.css'

export default class Item extends Component {

    state = {
        mouse: false
    }

    // 鼠标移入移出
    handleMouse = (mousemove) => {
        return () => {
            if (mousemove) {
                // console.log("enter")
                this.setState({ mouse: mousemove })
            }
            else {
                // console.log("leave")
                this.setState({ mouse: mousemove })
            }
        }
    }
    // 勾选todo
    handleCheck = (id) => {
        return (event) => {
            console.log("current is ", id, " event ", event.target.checked)

            // 传递勾选给App
            this.props.updateTodos(id, event.target.checked)
        }
    }

    handleRemove = (id) => {

        return () => {
            console.log("REMOVE ", id)
            if (window.confirm("Do you really want to delete?")) {
                this.props.removeTodos(id)
            }
            else {
                return;
            }
        }
    }

    render() {
        const { id, content, isdone } = this.props
        return (
            <div>
                <li onMouseEnter={this.handleMouse(true)} onMouseLeave={this.handleMouse(false)} style={{ backgroundColor: this.state.mouse ? '#ddd' : 'white' }}>
                    <label>
                        <input type="checkbox" onChange={this.handleCheck(id)} defaultChecked={isdone} />
                        <span>{content}</span>
                    </label>
                    <button className="btn btn-danger" onClick={this.handleRemove(id)} style={{ display: this.state.mouse ? 'block' : 'none' }}>DELETE</button>
                </li>
            </div>
        )
    }
}
