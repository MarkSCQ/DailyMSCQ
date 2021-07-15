import React, { Component } from 'react'

import axios from 'axios'



export default class App extends Component {

    getStudentData = () => {
        axios.get('http://localhost:3000/students').then(
            response => { console.log("success ", response.data) },
            error => { console.log("fail ", error); }

        )
    }
    render() {
        return (
            <div>
                <button onClick={this.getStudentData}>click me get data</button>
            </div>
        )
    }
}
