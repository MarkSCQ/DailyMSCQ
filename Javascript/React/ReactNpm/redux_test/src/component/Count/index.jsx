import React, { Component } from 'react'


import store from '../../reduxfiles/store'


export default class Count extends Component {

    adderRef = React.createRef()

    additionHandler = () => {
        let stateValue = store.getState()
        store.dispatch({ type: "addition", data: this.adderRef.current.value * 1 })
    }

    substractHandler = () => {
        let stateValue = store.getState()
        store.dispatch({ type: "substract", data: this.adderRef.current.value * 1 })
    }

    multiplicationHandler = () => {
        let stateValue = store.getState()
        store.dispatch({ type: "multiplication", data: this.adderRef.current.value * 1 })
    }

    divisionHandler = () => {
        let stateValue = store.getState()
        store.dispatch({ type: "division", data: this.adderRef.current.value * 1 })
    }

    remainderHandler = () => {
        let stateValue = store.getState()
        store.dispatch({ type: "remainder", data: this.adderRef.current.value * 1 })
    }

    componentDidMount() {
        store.subscribe(() => {
            this.setState({})
        })
    }
    render() {
        return (
            <div>
                <h1>Current Number: {store.getState()}</h1>

                <select ref={this.adderRef}>

                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                    <option value="4">4</option>
                    <option value="5">5</option>
                    <option value="6">6</option>

                </select>

                <button onClick={this.additionHandler}> + </button>
                <button onClick={this.substractHandler}> - </button>
                <button onClick={this.divisionHandler}> / </button>
                <button onClick={this.multiplicationHandler}> * </button>
                <button onClick={this.remainderHandler}> % </button>



            </div>
        )
    }
}
