import React, { Component } from 'react'

export class Curring extends Component {

    state = { username: "", password: "" }


    saveData = (data) => {
        return (event) => {
            console.log(data, event.target.value);
            this.setState({ [data]: event.target.value })
        }
    }

    saveData2 = (data, value) => {
        this.setState({ [data]: value })

    }

    submitHandler = () => {

    }

    render() {
        return (
            <div>
                <form onSubmit={this.submitHandler}>
                    {/* uname <input type="text" name="username" onChange={this.saveData('username')} /> <br /> */}
                    uname <input type="text" name="username" onChange={(event) => this.saveData2("username", event.target.value)} /> <br />


                    passwd <input type="password" name="password" onChange={this.saveData('password')} /> <br />
                    <button>submit</button>

                </form>

            </div>
        )
    }
}

export default Curring
