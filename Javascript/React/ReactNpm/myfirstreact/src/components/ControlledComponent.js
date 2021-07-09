import React, { Component } from 'react'

class ControlledComponent extends Component {

    state = {
        username: "",
        password: ""
    }

    saveUname = (event) => {
        this.setState({ username: event.target.value })
    }

    savePasswd = (event) => {
        this.setState({ password: event.target.value })
    }

    handleSubmit = (event) => {
        event.preventDefault() // 阻止表单提交 
        const { username, password } = this.state
        alert(`${username},${password}`)
    }

    render() {
        return (
            <div>
                <form onSubmit={this.handleSubmit}>
                    uname <input type="text" name="username" onChange={this.saveUname} /> <br />
                    passwd <input type="password" name="password" onChange={this.savePasswd} /> <br />
                    <button>submit</button>
                </form>
            </div>
        )
    }
}

export default ControlledComponent
