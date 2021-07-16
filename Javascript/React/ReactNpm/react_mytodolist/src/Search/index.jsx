import React, { Component } from 'react'
import axios from 'axios'
import { nanoid } from 'nanoid';
export default class Search extends Component {
    // ! When a ref is passed to an element in render, a reference to the node becomes accessible at the current attribute of the ref.
    // ! this is using createRef: keyWordRef = React.createRef();


    searchHandler = () => {
        // get user input
        // ! this is using createRef: console.log(this.keyWordRef.current.value)
        // this is callback function as ref
        // const { value } = this.keyWordRef
        // 连续解构赋值
        const { keyWordRef: { value: keyWord } } = this;

        // ！连续解构赋值并不能解构key值
        // ！console.log(keyWordRef)
        console.log(keyWord);
        // 连续解构赋值+重命名
        // let obj = {a:{b:1}}
        // const {a:{b:data}} = obj
        // 



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
