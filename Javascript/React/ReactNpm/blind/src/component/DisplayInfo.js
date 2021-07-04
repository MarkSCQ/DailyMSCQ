import { Component } from "react"
import React from "react"



class DisplayInfo extends Component {

    state = { name: "XXX", id: "000-000", readable: false }


    viewuser() {
        console.log(this.state.readable)
        if (!this.state.readable) {
            this.setState({ name: this.props.name, id: this.props.id, readable: !this.state.readable })
        } else {
            this.setState({ name: "XXX", id: "000-000", readable: !this.state.readable })
        }
    }
    render() {
        return (
            <div>
                <ul>
                    <li>name: {this.state.name}</li>
                    <li>id: {this.state.id}</li>
                </ul>
                <button onClick={() => this.viewuser()}>View User</button>
            </div>
        )
    }
}

export default DisplayInfo