import React, { Component } from 'react'

class NonControlledComponent extends Component {

    handleSubmit = (event) => {
        event.preventDefault() // 阻止表单提交 
        const { username, password } = this
        alert(`${username.value},${password.value}`)
    }

    render() {

        return (
            <form action="http://www.google.com" onSubmit={this.handleSubmit}>
                <label>uname: </label><input ref={(c) => this.username = c} type="text" name="username" />&nbsp;
                <label>passwd: </label><input ref={(c) => this.password = c} type="password" name="password" />&nbsp;
                <button>login</button>&nbsp;
            </form>
        )
    }
}

export default NonControlledComponent
