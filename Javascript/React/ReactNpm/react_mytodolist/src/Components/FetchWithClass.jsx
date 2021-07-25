import React, { Component } from 'react'
import axios from 'axios'
export default class PromiseWithClass extends Component {
    constructor(props) {
        super(props)

        this.state = {
            gender: "",
            name: "",
            email: "",

        }
    }

    getAPIDataXMLHttpRequest() {
        return new Promise(resolve => {
            const xhr = new XMLHttpRequest();
            xhr.overrideMimeType("application/json");
            // 2. set request method and url
            xhr.open('GET', 'https://randomuser.me/api')
            // 3. send request
            xhr.send()
            // 4. event binding, processing the resutls sent from server
            xhr.onreadystatechange = () => {
                // value == 4 server send all results
                if (xhr.readyState == 4) {
                    if (xhr.status >= 200 && xhr.status < 300) {
                        // 1.响应航
                        console.log(xhr.status)                 //状态码
                        console.log(xhr.statusText)             //状态字符串
                        console.log(xhr.getAllResponseHeaders())  //所有响应头
                        console.log(xhr.response)               //响应体
                    }
                    else {
                    }
                }
            }
            return xhr.response
        })

    }

    async getAPIDataFetch() {

        var storeVariable;
        return await fetch("https://randomuser.me/api")
            .then(response => response.json())
            .then(result => {
                // console.log(result["results"][0])
                storeVariable = result["results"][0]
                return storeVariable
                // console.log(storeVariable)
            })
            .catch(error => console.log(error))
    }


    async getAPIDataAxios() {
        let res;
        await axios.get("https://randomuser.me/api")
            .then(response => {
                // console.log(response.data.results[0])
                res = response.data.results[0]
            })
        return res

    }

    renderExam() {
        let getit;
        let getit2;

        try {
            getit = this.getAPIDataFetch().then(response => { return response });
         }
        catch (err) { console.log(err) }
        return getit
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
                <h1>this is from fetch</h1>

                <div> data :</div>

                <div>Gender: {this.state.gender}</div>
                <div>Name: {this.state.name}</div>
                <div>Email: {this.state.email}</div>
            </div>


        )
    }
}
