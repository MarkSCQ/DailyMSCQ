import React, { Component } from 'react'

class Lifecycle4 extends Component {


    componentWillReceiveProps() {
        console.log("kid --- componentWillReceiveProps")
        console.log(this.props)
        //第一次传递不算 正确理解是 componentWillReceiveNewProps
    }

    shouldComponentUpdate() {
        console.log("kid --- shouldComponentUpdate")
        return true;
    }

    componentWillUpdate() {
        console.log("kid --- componentWillUpdate")
    }

    componentDidUpdate() {
        console.log("kid --- componentDidUpdate")
    }

    render() {
        console.log("kid --- render")

        return (
            <div>
                This is kid Lifecycle4:{this.props.carName}
            </div>
        )
    }
}


export default Lifecycle4
