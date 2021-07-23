import React, { Component, createRef } from 'react'

// 获取redux中store的状态


export default class Count extends Component {
    selectRef = React.createRef();

    state = { car: "BMW", currentNumber: 0 }


    addHandler = () => {
        console.log("addHandler")
        const userAdder = this.selectRef.current.value
        this.props.addition(userAdder * 1)
        //通知redux加

        // this.setState({ currentNumber: parseInt(this.state.currentNumber) + parseInt(userAdder) })

    }

    minusHandler = () => {
        console.log("minusHandler")
        const userAdder = this.selectRef.current.value
        this.props.minus(userAdder * 1)
    }

    addIfOddHandler = () => {
        console.log("addOddHandler")
        const userAdder = this.selectRef.current.value
        if (this.props.count % 2 !== 0) {
            this.props.addition(userAdder * 1)
        }

    }

    addIfAsyncHandler = () => {
        console.log("addAsyncHandler")
        const userAdder = this.selectRef.current.value
        this.props.additionAsync(userAdder * 1)
        // setTimeout(() => {
        //     store.dispatch(creatorAddition(userAdder*1))
        // }, 500)
    }

    // ! 第一种更新state的写
    render() {
        console.log("@", this.props)

        return (
            <div>

                <h1>Current : {this.props.count}</h1>
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
