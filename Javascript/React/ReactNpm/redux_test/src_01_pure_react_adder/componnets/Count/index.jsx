import React, { Component, createRef } from 'react'

export default class Count extends Component {
    selectRef = React.createRef();

    state = { currentNumber: 0 }


    addHandler = () => {
        console.log("addHandler")
        const userAdder = this.selectRef.current.value

        this.setState({ currentNumber: parseInt(this.state.currentNumber) + parseInt(userAdder) })

    }

    minusHandler = () => {
        console.log("minusHandler")
        const userAdder = this.selectRef.current.value
        this.setState({ currentNumber: parseInt(this.state.currentNumber) - parseInt(userAdder) })
    }

    addIfOddHandler = () => {
        console.log("addOddHandler")
        const userAdder = this.selectRef.current.value
        const { currentNumber } = this.state
        if (currentNumber % 2 !== 0) {
            this.setState({ currentNumber: parseInt(this.state.currentNumber) + parseInt(userAdder) })
        }

    }

    addIfAsyncHandler = () => {
        console.log("addAsyncHandler")
        const userAdder = this.selectRef.current.value
        const { currentNumber } = this.state
        setTimeout(() => {
            this.setState({ currentNumber: parseInt(currentNumber) + parseInt(userAdder) })
        }, 500)
    }

    render() {
        return (
            <div>

                <h1>Current : {this.state.currentNumber}</h1>
                <select ref={this.selectRef}>
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                </select>
                <button onClick={this.addHandler}>+</button>
                <button onClick={this.minusHandler}>-</button>
                <button onClick={this.addIfOddHandler}>add when odd</button>
                <button onClick={this.addIfAsyncHandler}>async add</button>
            </div>
        )
    }
}
