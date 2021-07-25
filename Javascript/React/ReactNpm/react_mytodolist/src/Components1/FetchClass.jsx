import React, { Component } from 'react'


export default class FetchClass extends Component {
    constructor(props) {
        super(props)

        this.state = {
            username: "",
            email: ""
        }
    }

    fetchGetData = async () => {
        return await fetch("https://randomuser.me/api")
            .then(
                response => response.json()
            )
    }


    componentDidMount() {
        // call the axio to update 
        this.fetchGetData().then(
            data => {
                let realData = data["results"][0]
                this.setState({ username: realData.name.last, email: realData.email })
            }
        ).catch(err => {
            console.log(err)
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
