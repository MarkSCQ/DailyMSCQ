import axios from 'axios'
import React, { Component } from 'react'

export default class AxiosClass extends Component {
    constructor(props) {
        super(props)
        this.state = {
            Name: "",
            Email: ""
        }
    }

    axioGetData = async () => {
        return await axios.get("https://randomuser.me/api")
    }

    fetchGetData = async () => {
        return await fetch("https://randomuser.me/api")
    }
    XHRGetData = () => {
        return new Promise((resolve, reject) => {
            const xhr = new XMLHttpRequest();
            // initialize the xhr object
            // set response type
            xhr.responseType = "json"
            console.log("xhr.readyState  ", xhr.readyState)

            // set method and api
            xhr.open("GET", "https://randomuser.me/api")
            console.log("xhr.readyState  ", xhr.readyState)

            // send request
            xhr.send()
            console.log("xhr.readyState  ", xhr.readyState)

            // event bind. process the data response
            // when state change ...
            // readystate, property of XHR. Five values 
            // 0 初始化,1 open 调用完毕,2 send 调用完毕, 3 服务端返回部分结果, 4 服务端返回了所有结果,
            // 正常流程走一遍会发现从头到尾 readystate被设置的值从0到4都有、
            // 只有在状态为4的时候才能确保完全正确。
            xhr.onreadystatechange = () => {
                console.log("xhr.readyState in event  ", xhr.readyState)
                if (xhr.readyState === 4) {
                    // 响应状态码
                    if (xhr.status >= 200 && xhr.status < 300) {
                        resolve(xhr.response) // 响应体
                    }
                    else {
                        reject(xhr.status) // 状态码
                    }
                }
            }
        })
    }
    componentDidMount() {
        // axio get
        // this.axioGetData()
        //     .then(response => {
        //         console.log(response.data.results[0])
        //         return response.data.results[0]
        //     })
        //     .then(
        //         data => {
        //             this.setState({ Name: data.name.last, Email: data.email })
        //         }
        //     )

        // this.fetchGetData()
        //     .then(response => response.json())
        //     .then(data => { return data.results[0] })
        //     .then(dataDic => {
        //         console.log("@ ", dataDic)
        //         this.setState({ Name: dataDic.name.last, Email: dataDic.email })
        //     })

        this.XHRGetData()
            .then((response) => {
                let datadic = response.results[0]
                console.log(datadic)
                this.setState({ Name: datadic.name.last, Email: datadic.email })
            },
                (err) => {
                    console.log(err)
                }
            )
    }
    render() {
        return (
            <div>
                IMAO!
                <div>Name  :{this.state.Name}</div>
                <div>Email :{this.state.Email}</div>
            </div>
        )
    }
}