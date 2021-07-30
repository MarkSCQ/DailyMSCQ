import React, { Component } from 'react'

import axios from 'axios'
export default class Userdata extends Component {

    state = { info: "" }

    btnAxio = () => {
        axios.get("api1/api/taskList")
            .then(response => { return response.data })
            .then(data =>{ console.log(JSON.stringify(data))})
    }

    render() {
        return (
            <div>
                <button onClick={this.btnAxio}>click</button>
            </div>
        )
    }
}
