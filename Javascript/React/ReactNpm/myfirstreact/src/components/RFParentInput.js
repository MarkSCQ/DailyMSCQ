import React, { Component } from 'react'
import RFinput from './RFinput'
class RFParentInput extends Component {
    constructor(props) {
        super(props)
        this.inputREF = React.createRef()
        this.state = {

        }
    }

    clickhandler = () => {
        this.inputREF.current.focus();
    }
    render() {
        return (
            <div>
                <RFinput ref={this.inputREF} />
                <button onClick={this.clickhandler}>focus input</button>
            </div>
        )
    }
}

export default RFParentInput
