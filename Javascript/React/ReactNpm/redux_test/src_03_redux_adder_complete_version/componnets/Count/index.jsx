import React, { Component, createRef } from 'react'

// 获取redux中store的状态
import store from '../../redux/store'
import { creatorAddition } from '../../redux/count_action'
import { creatorMinus } from '../../redux/count_action'

export default class Count extends Component {
    selectRef = React.createRef();

    state = { car: "BMW", currentNumber: 0 }


    addHandler = () => {
        console.log("addHandler")
        const userAdder = this.selectRef.current.value

        //通知redux加

        store.dispatch(creatorAddition(userAdder*1))
        // this.setState({ currentNumber: parseInt(this.state.currentNumber) + parseInt(userAdder) })

    }

    minusHandler = () => {
        console.log("minusHandler")
        const userAdder = this.selectRef.current.value
        store.dispatch(creatorMinus(userAdder*1))
    }

    addIfOddHandler = () => {
        console.log("addOddHandler")
        const userAdder = this.selectRef.current.value
        const currentNumber = store.getState()
        if (currentNumber % 2 !== 0) {
            store.dispatch(creatorAddition(userAdder*1))
        }

    }

    addIfAsyncHandler = () => {
        console.log("addAsyncHandler")
        const userAdder = this.selectRef.current.value
        const { currentNumber } = this.state
        setTimeout(() => {
            store.dispatch(creatorAddition(userAdder*1))
        }, 500)
    }

    // ! 第一种更新state的写法
    componentDidMount() {
        // 监测 redux 中状态的变化，只要变化，就调用render
        // 生命周期的钩子都是组建的实例对象
        store.subscribe(() => {
            this.setState({}) //setState 会触发render 所以间接的调用了render是的store.getState()更新到最新的值
        })
    }

    render() {
        return (
            <div>

                <h1>Current : {store.getState()}</h1>
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
