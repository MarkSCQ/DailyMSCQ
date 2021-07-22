import React, { Component, createRef } from 'react'

// 获取redux中store的状态


export default class Count extends Component {
    selectRef = React.createRef();

    state = { car: "BMW", currentNumber: 0 }


    addHandler = () => {
        console.log("addHandler")
        const userAdder = this.selectRef.current.value

        //通知redux加

        // this.setState({ currentNumber: parseInt(this.state.currentNumber) + parseInt(userAdder) })

    }

    minusHandler = () => {
        console.log("minusHandler")
        const userAdder = this.selectRef.current.value
    }

    addIfOddHandler = () => {
        console.log("addOddHandler")
        const userAdder = this.selectRef.current.value

    }

    addIfAsyncHandler = () => {
        console.log("addAsyncHandler")
        const userAdder = this.selectRef.current.value
        // setTimeout(() => {
        //     store.dispatch(creatorAddition(userAdder*1))
        // }, 500)
    }

    // ! 第一种更新state的写
    render() {
        return (
            <div>

                <h1>Current : { }</h1>
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
