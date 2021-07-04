import React, { Component } from 'react'

class Follow extends Component {

    state = { msg: false }


    changeFollow() {
        this.setState({ msg: !this.state.msg })
    }

    render() {
        return (
            <div>
                <h1>
                    {this.state.msg ? "Follow" : "Unfollow"}
                </h1>
                <button onClick={() => this.changeFollow()}>
                    Click
                </button>
            </div>
        )
    }

}

export default Follow