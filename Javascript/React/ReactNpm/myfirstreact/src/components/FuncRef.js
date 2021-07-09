import React, { Component } from 'react'

class FuncRef extends Component {

    state = { isHot: true }

    showInfo = () => {
        const { input1 } = this
        alert(input1.value)
    }

    changeWeather = () => {
        this.setState({ isHot: !this.state.isHot })
    }

    saveInput = (c) => {
        this.input = c;
        console.log("@", c)

    }
    render() {
        return (
            <div>
                <h1 onClick={this.changeWeather}>Today is {this.state.isHot ? "hot" : "cold"}</h1>

                {/* <input ref={(currentNode) => { this.input1 = currentNode; console.log("@", currentNode) }} />*/}
                <input ref={this.saveInput} type="text" />

                <button onClick={this.showInfo} >click</button> &nbsp;
            </div>
        )
    }
}

export default FuncRef


// clickhandler = () => {
//     console.log("@")
//     console.log(this)
// }
// showdata1 = () => {
//     const { input1 } = this
//     alert(input1.value)
// }

// showdata2 = () => {
//     const { input2 } = this
//     alert(input2.value)
// }