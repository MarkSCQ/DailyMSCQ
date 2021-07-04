import React from 'react'
import { Component } from 'react'

class StateCounter extends Component {

    // constructor() {
    //     super();
    //     this.state = { msg: false };
    //     this.changeState = this.changeState.bind(this)
    // }
    state = { msg: 0, clickable: false };
    changeState() {
        this.setState(prevState => ({ msg: prevState.msg + 1, clickable: false }), console.log
            (this.state.msg));
        if (this.state.msg % 10 === 0 && this.state.msg > 0) {
            alert("you click too many times stop!")
            this.setState({ msg: this.state.msg + 1, clickable: true });

        }
    }
    render() {
        console.log(this)
        return (
            <div>
                <h1>{this.state.msg}</h1>
                <button onClick={() => this.changeState()} disabled={this.state.clickable} >CLICKME </button>
            </div>
        )
    }
}

export default StateCounter