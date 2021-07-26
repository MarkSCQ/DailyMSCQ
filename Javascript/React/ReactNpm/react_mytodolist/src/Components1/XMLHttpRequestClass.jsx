

import React, { Component } from 'react'

export default class XMLHttpRequestClass extends Component {

    constructor(props) {
        super(props)

        this.state = {
            username: "",
            email: ""
        }
    }

    XMLHttpRequestData = () => {
        return new Promise((resolve, reject) => {
            const xhr = new XMLHttpRequest(); //XMLHttpRequest (XHR) objects are used to interact with servers. 
            xhr.responseType = "json"
            // Initializes a request.
            xhr.open('GET', 'https://randomuser.me/api')
            // Sends the request. If the request is asynchronous (which is the default), this method returns as soon as the request is sent.
            xhr.send()
            // An event handler that is called whenever the readyState attribute changes. 
            xhr.onreadystatechange = () => {
                // The XMLHttpRequest.readyState property returns the state an XMLHttpRequest client is in.
                if (xhr.readyState === 4) {
                    // The read-only XMLHttpRequest.status property returns the numerical HTTP status code of the XMLHttpRequest's response.
                    if (xhr.status >= 200 && xhr.status < 300) {
                        resolve(xhr.response)
                    }
                    else {
                        reject(xhr.status)
                    }
                }
            }
        })
    }

    componentDidMount() {
        this.XMLHttpRequestData()
            .then(
                data => {
                    console.log("@data ", data)
                    this.setState({ username: data.results[0].name.last, email: data.results[0].email })
                },
                err => {
                    console.log("@err ", err)
                })
    }

    render() {
        return (
            <div>
                <div>User name: {this.state.username}</div>
                <div> Email: {this.state.email}</div>
            </div>
        )
    }
}
