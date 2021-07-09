import React, { Component } from 'react'
import RegComp from './RegComp'
import PureComponents from './PureComponents'
import MemoComp from './MemoComp'

class ParentComp extends Component {
    constructor(props) {
        super(props)

        this.state = {
            name: "123123"
        }
    }

    componentDidMount() {
        setInterval(() => {
            this.setState({ name: "33333333333" })
        }, 2000)
    }
    render() {
        console.log("parent rerender")

        return (
            <div>
                ParentComponent
                <MemoComp name={this.state.name} />
                {/* <RegComp name={this.state.name}></RegComp>
                <PureComponents name={this.state.name}></PureComponents> */}
            </div>
        )
    }
}

export default ParentComp
