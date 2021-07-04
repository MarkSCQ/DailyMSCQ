import React from 'react'
import { Component } from 'react'

class StateButton extends Component {

    // constructor() {
    //     super();
    //     this.state = { msg: false };
    //     this.changeState = this.changeState.bind(this)
    // }
    state = { msg: false };
    changeState() {
        this.setState({ msg: !this.state.msg });
    }
    render() {
        console.log(this)
        return (
            <div>
                <h1>{this.state.msg ? "follow" : "unfollow"}</h1>
                <button onClick={() => this.changeState()}>CLICKME </button>
            </div>
        )
    }
}

export default StateButton