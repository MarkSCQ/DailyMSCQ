import React, { Component } from 'react'

class Form2 extends Component {

    constructor(props) {
        super(props)
        this.state = {
            name: "",
            email: "",
            phonenum: ""
        }
    }

    nameChange = event => {
        this.setState({ name: event.target.value })
    }
    emailChange = event => {
        this.setState({ email: event.target.value })
    }
    phonenumChange = event => {
        this.setState({ phonenum: event.target.value })
    }

    submitChange = event => {
        console.log(` name:${this.state.name},\n email:${this.state.email},\n phonenum:${this.state.phonenum}`)
        event.preventDefault()
    }

    render() {
        return (
            <div>
                <form onSubmit={this.submitChange}>
                    <div>
                        <label>NAME: </label>
                        <input type="text" value={this.state.name} onChange={this.nameChange} />
                    </div>
                    <div>
                        <label>EMAIL: </label>
                        <input type="email" value={this.state.email} onChange={this.emailChange} />
                    </div>
                    <div>
                        <label>PHONE: </label>
                        <input type="number" value={this.state.phonenum} onChange={this.phonenumChange} />
                    </div>

                    <div>
                        <button type="submit">
                            23333
                        </button>
                    </div>
                </form>
            </div>
        )
    }
}

export default Form2
