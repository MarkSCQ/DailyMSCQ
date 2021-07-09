import React, { Component } from 'react'
import Input from './Input'

class FocusInput extends Component {
    constructor(props) {
        super(props)
        this.componentRef = React.createRef()
        this.state = {

        }
    }
    inputHandler = () => {
        this.componentRef.current.focusInput()
    }
    render() {
        return (
            <div>
                asc<Input ref={this.componentRef} />
                <button onClick={this.inputHandler}>fffff</button>

            </div>
        )
    }
}

export default FocusInput
