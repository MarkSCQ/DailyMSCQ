import React, { Component } from 'react'

class Form extends Component {

    constructor(props) {
        super(props)
        this.state = { email: "", password: "", identification: "", choice: "" }
    }


    emailChange = event => {
        this.setState({ email: event.target.value })
    }

    passwdChange = event => {
        this.setState({ password: event.target.value })
    }

    identificationChange = event => {
        this.setState({ identification: event.target.value })
    }

    choiceChange = event => {
        this.setState({ choice: event.target.value })
    }

    submitHandler = event => {
        console.log(` email:${this.state.email},\n password:${this.state.password},\n identification:${this.state.identification},\n choice:${this.state.choice}`)
        event.preventDefault()
    }
    render() {
        return (
            <div>
                <form onSubmit={this.submitHandler}>
                    <div>
                        <label>Email: </label>
                        <input type="text" value={this.state.email} onChange={this.emailChange} /></div>
                    <div>
                        <label>Password: </label>
                        <input type="text" value={this.state.password} onChange={this.passwdChange} />
                    </div>
                    <div>
                        <label>Identification: </label>
                        <input type="text" value={this.state.identification} onChange={this.identificationChange} />
                    </div>
                    <div>
                        <label>Choice: </label>
                        <select value={this.state.choice} onChange={this.choiceChange}>
                            <option value="111">
                                111
                            </option>
                            <option value="222">
                                222
                            </option>
                            <option value="333">
                                333
                            </option>
                        </select>
                    </div>
                    <div>
                        <button type="submit">Submit</button>
                    </div>
                </form>
            </div>
        )
    }
}

export default Form
