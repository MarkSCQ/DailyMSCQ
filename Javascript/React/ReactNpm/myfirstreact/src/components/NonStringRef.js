import React, { Component } from 'react'

class NonStringRef extends Component {
    clickhandler = () => {
        console.log("@")
        console.log(this)
    }
    showdata1 = () => {
        const { input1 } = this
        alert(input1.value)
    }

    showdata2 = () => {
        const { input2 } = this
        alert(input2.value)
    }
    render() {
        return (
            <div>
                <input ref={currentNode => { this.input1 = currentNode }} type="text" placeholder="focus and display data" />&nbsp;
                <button onClick={this.showdata1}>click</button> &nbsp;
                <input ref={currentNode => { this.input2 = currentNode }} onBlur={this.showdata2} type="text" placeholder="los focus and display data" /> &nbsp;
            </div>
        )
    }
}

export default NonStringRef
