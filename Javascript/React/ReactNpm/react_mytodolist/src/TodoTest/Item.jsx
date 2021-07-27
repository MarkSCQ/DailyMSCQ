import React, { Component } from 'react'

export default class Item extends Component {
    state = {
        mouseState: false
    }

    mouseOnHandler = (ms) => {
        return () => {
            if (ms) {
                this.setState({ mouseState: true })
            }
            else {
                this.setState({ mouseState: false })
            }
        }
    }
    deleteInfo = (info) => {
        return () => {
            console.log(info)
            this.props.deleteHandle(info)
        }
    }

    checkItem = (info) => {
        return (event) => {
            console.log("@!", info)
            this.props.processCheck(info, event.target.checked)
        }
    }

    render() {
        const { info } = this.props
        const { content, status } = info
        return (
            <div>
                <li onMouseLeave={this.mouseOnHandler(false)}
                    onMouseEnter={this.mouseOnHandler(true)}
                    key={content}> <input type="checkbox" checked={status} onChange={this.checkItem(content)} />{content}
                    <button onClick={this.deleteInfo(content)} style={{ display: this.state.mouseState ? "block" : "none" }}>Delete</button>
                </li>
            </div>
        )
    }
}

