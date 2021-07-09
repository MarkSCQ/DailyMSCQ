import React, { Component } from 'react'

class Input extends Component {
    constructor(props) {
        super(props)
        // 1. create
        this.inputRef = React.createRef()

        this.state = {
        }
    }

    componentDidMount() {
        this.inputRef.current.focus()
        console.log(this.inputRef)
    }
    focusInput() {
        this.inputRef.current.focus()
    }
    render() {
        return (
            <div>
                {/* add attach */}
                <input type="text" ref={this.inputRef} />
            </div>
        )
    }
}

export default Input
