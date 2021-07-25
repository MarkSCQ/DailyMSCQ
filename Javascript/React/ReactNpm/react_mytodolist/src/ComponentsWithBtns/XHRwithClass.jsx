import React, { Component } from 'react'

export default class XHRwithClass extends Component {

    constructor(props) {
        super(props)

        this.state = {
            gender: "111",
            name: "222",
            email: "333v",

        }
    }

    getAPIDataXHR() {

        return new Promise(
            (resolve, reject) => {
                const xhr = new XMLHttpRequest();
                xhr.responseType = "json"
                xhr.open('GET', 'https://randomuser.me/api')
                // 3. send request
                xhr.send()
                xhr.onreadystatechange = () => {
                    // value == 4 server send all results
                    if (xhr.readyState == 4) {
                        if (xhr.status >= 200 && xhr.status < 300) {
                            resolve(xhr.response)               //响应体
                        }
                        else {
                            reject(xhr.status)
                        }
                    }
                }
            }
        )
    }

    renderExam() {
        let getit;

        try {
            getit = this.getAPIDataXHR();
            getit.then(
                value => {
                    console.log("value: ", value)
                },
                reason => {
                    console.log("reason: ", reason)
                })
        }
        catch (err) { console.log(err) }
        return getit
    }

    componentDidMount() {
        this.renderExam().then(response => {
            this.setState({ gender: response.results[0].gender, name: response.results[0].name.first, email: response.results[0].email })
        })
    }

    render() {
        const res = this.getAPIDataXHR()
        return (
            <div>
                <h1>this is from XML</h1>

                <div> data :</div>

                <div>Gender: {this.state.gender}</div>
                <div>Name: {this.state.name}</div>
                <div>Email: {this.state.email}</div>
            </div>
        )
    }
}
