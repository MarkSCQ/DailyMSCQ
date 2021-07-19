import React, { Component } from 'react'

import axios from 'axios'



export default class App extends Component {

    getStudentData = () => {
        axios.get('http://localhost:3000/api1/students').then(
            response => { console.log("success ", response.data) },
            error => { console.log("fail ", error); }

        )
    }



    getCarData = () => {
        axios.get('http://localhost:5001/cars').then(
            response => { console.log("success ", response.data) },
            error => { console.log("fail ", error); }

        )
    }


    render() {
        return (
            <div>
                <button onClick={this.getStudentData}>click me get students</button>
                <button onClick={this.getCarData}>click me get cars</button>
            </div>
        )
    }
}
