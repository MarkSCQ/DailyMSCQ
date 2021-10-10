import React, { Component } from 'react'

export default class ClassCounterOne extends Component {
    constructor(props) {
        super(props)

        this.state = { counter: 0 }
    }
    componentDidUpdate(prevProps, prevState) {
        document.title = `${this.state.counter} times`
    }

    componentDidMount() {
        document.title = `${this.state.counter} times`

    }
    render() {
        return (
            <div>

                <button
                    onClick={() => { this.setState({ counter: this.state.counter + 1 }) }}
                >
                    click {this.state.counter} times
                </button>

            </div>
        )
    }
}
