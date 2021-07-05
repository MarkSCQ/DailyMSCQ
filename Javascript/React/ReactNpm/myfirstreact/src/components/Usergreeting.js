import React, { Component } from 'react'

class Usergreeting extends Component {


    constructor() {
        super()
        this.state = { isLoggedIn: false }
    }
    render() {

        return (
            this.state.isLoggedIn ? (<div><h1>welcome guest</h1></div>) : (<div><h1>welcome hhh</h1></div>)
        )
        // if (this.state.isLoggedIn) {
        //     return (
        //         <div>
        //             welcome guest
        //         </div>
        //     ) 
        // }
        // else {
        //     return (
        //         <div>
        //             welcome hhh
        //         </div>
        //     )
        // }
        // return (
        //     <div>
        //         <div>
        //             welcome guest
        //         </div>
        //         <div>
        //             welcome hhh
        //         </div>
        //     </div>
        // )
    }
}

export default Usergreeting
