import React, { Component } from 'react'

export class EventBind extends Component {
    constructor(props) {
        super(props)

        this.state = {
            msg: "hello"
        }
        // method 2 
        // this.changeMsg = this.changeMsg.bind(this)
    }

    // mtheod 1-3
    // changeMsg() {
    //     this.setState({
    //         msg: "goodbye"
    //     })
    // }
    
    // method 4 in official tutorial
    clickmsg = ()=>{
        this.setState({msg:"bye"})
    }
    render() {
        return (
            <div>
                <div>---------------</div>

                <div>{this.state.msg}</div>
                {/* method 1 Performance Implication*/}
                {/* <button onClick={this.changeMsg.bind(this)}>click</button> */}
                {/* method 2  it is good to pass paramaters via this method*/}
                {/* <button onClick={this.changeMsg}>click</button> */}
                {/* method 3 Performance Implication*/}
                {/* <button onClick={()=>this.changeMsg()}>click</button> */}
                {/* mehtod 4 in official tutorial*/}
                <button onClick={this.clickmsg}>click</button>
            </div>
        )
    }
}

export default EventBind
