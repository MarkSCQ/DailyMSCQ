import React, { Component } from 'react'

export default class ClassCounter extends Component {

    constructor(props) {
        super(props)

        this.state = {
            counter: 0
        }
    }
    incrementCounter = () => {
        this.setState({
            counter: this.state.counter + 1
        })
    }
    render() {
        return (
            <div>
                <button onClick={this.incrementCounter}>Class Counter {this.state.counter}</button>
            </div>
        )
    }
}