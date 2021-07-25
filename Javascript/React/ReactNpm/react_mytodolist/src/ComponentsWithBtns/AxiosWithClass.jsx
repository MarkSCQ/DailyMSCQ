import React, { Component } from 'react'
import axios from 'axios'
import { Button } from 'antd'





export default class FetchWithClass extends Component {
    constructor(props) {
        super(props)

        this.state = {
            gender: "111",
            name: "222",
            email: "333",

        }
    }

    btnHandler = () => {
        let res;
        axios.get("https://randomuser.me/api")
            .then(response => {
                // console.log(response.data.results[0])
                res = response.data.results[0]
                this.setState({ gender: res.gender, name: res.name.first, email: res.email })
            })
        return res
    }

    // renderExam() {
    //     let getit2;

    //     try {
    //         getit2 = this.getAPIDataAxios();
    //     }
    //     catch (err) { console.log(err) }
    //     return getit2
    // }

    // btnHandler = () => {
    //     this.renderExam().then(data => {
    //         console.log(data)
    //         this.setState({ gender: data.gender, name: data.name.first, email: data.email })
    //     })
    // }

    // componentDidMount() {
    //     this.renderExam().then(response => {
    //         console.log("@ ", response)
    //         this.setState({ gender: response.gender, name: response.name.first, email: response.email })
    //     })
    // }

    render() {
        return (
            <div style={{
                margin: "auto"
            }
            }>
                <br /><br />
                <Button type="primary" onClick={this.btnHandler}>Primary Button</Button> <br />

                <h1>this is from axios</h1><br />
                <div> data :</div><br />

                <div>Gender: {this.state.gender}</div><br />
                <div>Name: {this.state.name}</div><br />
                <div>Email: {this.state.email}</div><br />
            </div>
        )
    }
}
