import React, { Component } from 'react'
import { unmountComponentAtNode } from 'react-dom'


class NewLifeCycleB extends Component {

    componentWillReceiveProps(props) {
        console.log("B --- componentWillReceiveProps ", props)
    }

    render() {
        console.log("B --- render")
        return (
            <div>

            </div>
        )
    }
}

export default NewLifeCycleB
