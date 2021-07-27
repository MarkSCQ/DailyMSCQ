import React, { Component } from 'react'

export default class Item extends Component {

    state = {
        mouseOn: false
    }

    removeItem = (id) => {
        return () => {
            this.props.removeProcess(id)
        }
    }

    mouseState = (ms) => {
        return () => {
            if (ms) {
                this.setState({ mouseOn: true })
            }
            else {
                this.setState({ mouseOn: false })
            }
        }

    }

    render() {

        const { content, id, status } = this.props.info
        console.log(content, id, status)
        return (
            <div>
                <li
                    onMouseEnter={this.mouseState(true)}
                    onMouseLeave={this.mouseState(false)}
                >
                    {content} <button onClick={this.removeItem(id)}
                        style={{ display: this.state.mouseOn ? "block" : "none" }}>Remove</button>
                </li>
            </div>
        )
    }
}
