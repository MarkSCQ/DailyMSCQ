// ! https://randomuser.me/api

import React, { Component } from "react"
import axios from 'axios'


export default class GetData extends Component {

    state = {
        inputContent: "",
        info: ""
    }

    inputRef = React.createRef()
    GetData = (urlValue) => {
        return axios.get(urlValue)
            .then(response => {
                console.log(response.data.results[0])
                let d = response.data.results[0]
                this.setState({ info: JSON.stringify(d) })
            })
    }


    buttonHan = () => {
        const inputs = this.inputRef.current.value
        console.log(inputs)
        this.GetData(inputs)
    }


    eventHandlerMethor = (event) => {
        const { keyCode, target } = event
        console.log(keyCode)
        console.log(target.value)
        this.setState({ inputContent: target.value })
    }


    buttonHan2 = () => {
        return axios.get(this.state.inputContent)
            .then(response => {
                console.log(response.data.results[0])
                let d = response.data.results[0]
                this.setState({ info: JSON.stringify(d) })
            })
    }

    render() {
        return (
            <div>

                {/* <input type="text" ref={this.inputRef}></input> */}
                <input type="text" onKeyUp={this.eventHandlerMethor}></input>
                {/* <button onClick={this.buttonHan}>Submit</button> */}
                <button onClick={this.buttonHan2}>Submit</button>
                <div>value:{this.state.inputContent}</div>
                <div>value:{this.state.info}</div>
            </div>
        )
    }
}