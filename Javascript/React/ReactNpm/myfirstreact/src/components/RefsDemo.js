import React, { Component } from 'react'

class RefsDemo extends Component {
    constructor(props) {
        super(props)
        this.inputRef = React.createRef()

        this.cbRef = null
        this.setCbRef=(element)=>{
            this.cbRef = element
        }

    }

    componentDidMount() {
        // createref 
        // this.inputRef.current.focus()
        // console.log(this.inputRef)

        //cbref
        if(this.cbRef){
            this.cbRef.focus()
        }

    }

    clickHandler = () => {
        alert(this.inputRef.current.value)
    }

    render() {
        return (
            <div>
                <label>
                    text:
                </label>
                <input type="text" ref={this.inputRef} />
                <input type="text" ref={this.setCbRef} />
                <button onClick={this.clickHandler}>CLICK</button>
            </div>
        )
    }
}

export default RefsDemo
