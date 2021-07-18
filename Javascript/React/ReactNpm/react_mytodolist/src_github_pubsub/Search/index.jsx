import React, { Component } from 'react'
import axios from 'axios'
import { nanoid } from 'nanoid';
import PubSub from 'pubsub-js'

export default class Search extends Component {

    searchHandler = () => {


        PubSub.publish('message', { isFirstOpen: false, isLoading: true })
        const { keyWordRef: { value: keyWord } } = this;


        axios.get(`/api1/search/users?q=${keyWord}`).then(
            response => {
                console.log("success, ", response.data)
                PubSub.publish('message', { isLoading: false, users: response.data.items })
            },
            error => {
                PubSub.publish('message', { isLoading: false, err: error.message })
            }
        )
        // send request
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
