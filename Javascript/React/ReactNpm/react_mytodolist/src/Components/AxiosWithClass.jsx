import React, { Component } from 'react'
import axios from 'axios'
export default class FetchWithClass extends Component {
    constructor(props) {
        super(props)
        this.state = {
            gender: "",
            name: "",
            email: "",

        }
    }



    async getAPIDataAxios() {
        let res;
        await axios.get("https://randomuser.me/api")
            .then(response => {
                res = response.data.results[0]
            })
        console.log("this is res   ", res)
        return res

    }
    renderExam() {
        let getit2;

        try {
            getit2 = this.getAPIDataAxios();
            console.log("getit2 ", getit2)
        }
        catch (err) { console.log(err) }
        return getit2
    }

    componentDidMount() {
        this.renderExam().then(response => {
            console.log("@ ", response)
            this.setState({ gender: response.gender, name: response.name.first, email: response.email })
        })
    }

    render() {
        return (
            <div>
                <h1>this is from axios</h1>
                <div> data :</div>

                <div>Gender: {this.state.gender}</div>
                <div>Name: {this.state.name}</div>
                <div>Email: {this.state.email}</div>
            </div>
        )
    }
}
