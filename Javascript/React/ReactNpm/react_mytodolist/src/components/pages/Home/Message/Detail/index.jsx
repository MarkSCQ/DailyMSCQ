import React, { Component } from 'react'




export default class Detail extends Component {
    render() {
        const msgArray = [
            { id: 1, content: "content 1" },
            { id: 2, content: "content 2" },
            { id: 3, content: "content 3" },
            { id: 4, content: "content 4" }
        ]
        console.log(this.props)

        return (
            <ul>
                <li>detail</li>
            </ul>
        )
    }
}
