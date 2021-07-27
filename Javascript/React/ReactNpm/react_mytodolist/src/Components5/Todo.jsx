import React, { Component } from 'react'
import { Input, Button } from 'antd'

import axios from 'axios'
const isValidUrl = (url) => {
    try {
        new URL(url);
    } catch (e) {
        console.error(e);
        return false;
    }
    return true;
};
export default class Todo extends Component {

    state = {
        urldata: "",
        field: ""
    }


    inputHandler = (stateName) => {
        return (event) => {
            // ! one handler process input with its value , statename needs  []! 
            let val = event.target.value.trim()
            console.log(val.length)
            this.setState({ [stateName]: val })
        }
    }

    getData = () => {
        console.log(this.state.urldata, " ", this.state.field)
        if (this.state.urldata.length > 0) {
            if (isValidUrl(this.state.urldata)) {
                console.log("It is url")
                axios.get(this.state.urldata)
                    .then(response => { return response.data.results[0] })
                    .then(data => {
                        console.log(data)
                    })
            }
            else {
                console.log("Not url")
            }
        }
    }
    render() {
        return (
            <div style={{ width: "300px", marginLeft: "50px", marginTop: "50px" }}>
                <Input placeholder="URL" onKeyUp={this.inputHandler("urldata")} /><br /><br />
                <Input placeholder="Field" onKeyUp={this.inputHandler("field")} /><br /><br />
                <Button type="primary" onClick={this.getData} style={{ borderRadius: "5px" }} >Click Me</Button>
            </div>
        )
    }
}
