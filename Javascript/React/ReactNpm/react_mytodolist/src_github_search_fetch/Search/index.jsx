import React, { Component } from 'react'
import axios from 'axios'
import { nanoid } from 'nanoid';
import PubSub from 'pubsub-js'

export default class Search extends Component {

    searchHandler = async () => {


        PubSub.publish('message', { isFirstOpen: false, isLoading: true })
        const { keyWordRef: { value: keyWord } } = this;
        console.log(keyWord)

        // axios.get(`/api1/search/users?q=${keyWord}`).then(
        //     response => {
        //         console.log("success, ", response.data)
        //         PubSub.publish('message', { isLoading: false, users: response.data.items })
        //     },
        //     error => {
        //         PubSub.publish('message', { isLoading: false, err: error.message })
        //     }
        // )
        // .then 链式调用 
        // // .then 成功的回调response 失败的回调 error不能两个都走，只能二选一。如果这两个之中走的返回值是一个非promise值，外部.then返回的实例就为成功的 ，值为返回的非promise值；如果返回的是一个promise实例对象，则作为外部.then的返回值
        // fetch(`/api1/search/users?q=${keyWord}`).then(
        //     response => {
        //         console.log(response)
        //         return response.json() // 返回值为 Promise实例对象。之所以可以链式调用是因为存在有效的promise返回值
        //     },
        //     error => {
        //         console.log(error)
        //     }
        // ).then(
        //     response => { console.log(response) },
        //     error => { console.log(error) }
        // )
        try {
            const response = await fetch(`/api1/search/users?q=${keyWord}`)
            const data = await response.json()
            console.log(data)
            PubSub.publish("message", { isLoading: false, users: data.items })
        }
        catch (error) {
            console.log(error)
            PubSub.publish("message", { isLoading: false, err: error.message })

        }
    }
    render() {
        return (
            <div>
                <section className="jumbotron">
                    <h3 className="jumbotron-heading">Search Github Users</h3>
                    <div>
                        {/* // ! this is using createRef:  <input ref={this.keyWordRef} type="text" placeholder="enter the name you search" /> */}
                        <input ref={c => this.keyWordRef = c} type="text" placeholder="enter the name you search" />
                        &nbsp;
                        <button onClick={this.searchHandler}>Search</button>
                    </div>
                </section>
            </div>
        )
    }
}
