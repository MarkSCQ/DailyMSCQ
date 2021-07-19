import React, { Component } from 'react'
// import qs from 'querystring'
// import QueryString from 'qs'



//  let obj = {name:"tom",age:10}   name=tom&age=10 key1=value1&key2=value2 称为 urlencoded
export default class Detail extends Component {
    render() {
        const msgArray = [
            { id: "1", content: "content 1" },
            { id: "2", content: "content 2" },
            { id: "3", content: "content 3" },
            { id: "4", content: "content 4" }
        ]


        // let obj = { name: "tom", age: 10 }
        // console.log(QueryString.parse('name=tom&age=10'))

        // ! 接收search参数
        // const {search} = this.props.location
        // const {id,title} = qs.parse(search.slice(1))
        // console.log(id)
        // console.log(title)

        // ! 接收params
        // const { id, title } = this.props.match.params

        // const findResult = msgArray.find((msg) => { return msg.id === id })


        // ! 接收 state 参数
        const { id, title } = this.props.location.state || {} // ! 从存在的state中取值，如果state因为清除历史记录为空，则利用空对象，传入空值避免错误
        const findResult = msgArray.find((msg) => { return msg.id === id }) || {} // ! 如果没有找到这个对象，则利用空对象，传入空值避免错误
        const news = "info id: " + findResult.id + " content: " + findResult.content
        // console.log(news)
        return (
            <ul>
                <li>{
                    news
                }</li>
            </ul>
        )
    }
}
