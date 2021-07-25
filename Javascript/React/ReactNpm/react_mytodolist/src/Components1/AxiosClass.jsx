import React, { Component } from 'react'
import axios from 'axios'

export default class AxiosClass extends Component {

    constructor(props) {
        super(props)

        this.state = {
            username: "",
            email: ""
        }
    }

    axiosGetData = async () => {
        return await axios.get("https://randomuser.me/api")
            .then(response => response.data.results[0])
    }

    componentDidMount() {
        this.axiosGetData()
            .then(data => {
                console.log(data)
                this.setState({ username: data.name.last, email: data.email })
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
