import React, { Component } from 'react'
import { withRouter } from 'react-router-dom'
class Header extends Component {

    forward = () => {
        this.props.history.goForward()
    }
    back = () => {
        this.props.history.goBack()
    }
    go = () => {
        this.props.history.go(2)
    }

    render() {
        return (
            <div>
                <div className="page-header">
                    <h2>
                        React Router Demo
                    </h2>
                </div>

                <button onClick={this.back}>back</button>
                <button onClick={this.forward}>forward</button>
                <button onClick={this.go}>go</button>
            </div>
        )
    }
}

export default withRouter(Header)