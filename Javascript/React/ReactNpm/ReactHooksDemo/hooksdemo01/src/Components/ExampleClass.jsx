import React, { Component } from 'react'

export default class ExampleClass extends Component {
    constructor(props) {
        super(props)

        this.state = {
            counter: 0
        }
    }

    counterHandler = () => {
        this.setState({ counter: this.state.counter + 1 })
    }
    
    render() {
        return (
            <div>
                <h1>The current num is {this.state.counter}</h1>

                <button onClick={this.counterHandler}>
                    +1s
                </button>
            </div>
        )
    }
}
