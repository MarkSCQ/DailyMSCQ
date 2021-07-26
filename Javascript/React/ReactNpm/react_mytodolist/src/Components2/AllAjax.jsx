import axios from "axios";
import React, { Component } from "react";

export default class AllAjax extends Component {
    constructor(props) {
        super(props)
        this.state = {
            name: "",
            email: ""
        }
    }
    XMLGetData = () => {
        return new Promise((resolve, reject) => {
            const xhr = new XMLHttpRequest();
            xhr.responseType = "json"
            xhr.open("GET", "https://randomuser.me/api")
            xhr.send()
            xhr.onreadystatechange = () => {
                if (xhr.readyState === 4) {
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

    axiosGetData = async () => {
        return await axios.get("https://randomuser.me/ap2i")
    }

    fetchGetData = async () => {
        return await fetch("https://randomuser.me/api", {
            method: "GET"
        }).then(response => {
            return response.json()
        })
    }


    componentDidMount() {
        // this.XMLGetData()
        //     .then(
        //         response => {
        //             console.log(response)
        //             return response.results[0]
        //         }
        //     ).then(data => {
        //         console.log(data)
        //         // setState
        //     }, responseCode => {
        //         console.warn(responseCode)
        //     }
        //     )

        // this.axiosGetData()
        //     .then(response => {
        //         let curr_data = response.data.results[0]
        //         console.log(curr_data)
        //         return curr_data
        //     })
        //     .then(
        //         (data) => {
        //             console.log(data)
        //             // setState
        //         }
        //     )
        //     .catch(err => {
        //         console.warn(err)
        //     })

        this.fetchGetData()

            .then(data => console.log("@ ", data.results[0]))
            .catch(err => {
                console.log(err)
            })
    }

    render() {
        return (
            <div>
                2333
            </div>
        )
    }

}