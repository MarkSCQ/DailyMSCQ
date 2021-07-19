import React, { Component } from 'react'




export default class Detail extends Component {
    render() {
        const msgArray = [
            { id: "1", content: "content 1" },
            { id: "2", content: "content 2" },
            { id: "3", content: "content 3" },
            { id: "4", content: "content 4" }
        ]
        console.log(this.props)
        const { id, title } = this.props.match.params
        const newsObj = msgArray.filter((msg) => {
            return msg.id === id
        })
        const findResult = msgArray.find((msg) => { return msg.id === id })
        const news = "info id: " + findResult.id + " content: " + findResult.content
        console.log(news)
        return (
            <ul>
                <li>{
                    news
                }</li>
            </ul>
        )
    }
}
