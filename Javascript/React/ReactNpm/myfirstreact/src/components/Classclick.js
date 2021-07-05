import React, { Component } from 'react'

class Classclick extends Component {

    clickME(){
        console.log("CLICKME")
    }
    render() {
        return (
            <div>
                <button onClick={this.clickME}>clickme</button>
            </div>
        )
    }
}

export default Classclick
