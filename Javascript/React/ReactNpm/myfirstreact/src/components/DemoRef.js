import React, { Component } from 'react'

class DemoRef extends Component {
    // ！ String Ref
    // constructor(props) {
    //     super(props)

    //     this.input1 = React.createRef()
    //     this.button100 = React.createRef()


    //     this.state = {

    //     }
    // }

    clickhandler = () => {
        console.log("@")
        console.log(this)
    }
    showdata1 = () => {
        const { input1 } = this.refs
        alert(input1.value)
    }

    showdata2 = () => {
        const { input2 } = this.refs
        alert(input2.value)

    }


    render() {
        return (
            <div>
                <input ref="input1" type="text" placeholder="focus and display data" />&nbsp;
                <button onClick={this.showdata1}>click</button> &nbsp;
                <input ref="input2" onBlur={this.showdata2} type="text" placeholder="los focus and display data" /> &nbsp;

            </div>
        )
    }
}

export default DemoRef