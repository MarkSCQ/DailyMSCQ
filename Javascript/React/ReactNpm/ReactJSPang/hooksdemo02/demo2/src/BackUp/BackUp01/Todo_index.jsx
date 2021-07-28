import React, { Component } from 'react'

import { List, Input, Button, DatePicker } from 'antd'
import 'antd/dist/antd.css'

import { nanoid } from 'nanoid'
import moment from 'moment';

import Item from '../Item'

export default class Todo extends Component {

    state = {
        infos: [
            { id: 1, content: "Racing car sprays burning fuel into crowd.", date: "2021-07-13", status: false },
            { id: 2, content: "Japanese princess to wed commoner.", date: "2021-07-13", status: false },
            { id: 3, content: "Australian walks 100km after outback crash.", date: "2021-07-13", status: false },
            { id: 4, content: "Man charged over missing wedding girl.", date: "2021-07-13", status: false },
            { id: 5, content: "Los Angeles battles huge wildfires.", date: "2021-07-13", status: false },
            { id: 6, content: "Yelena Belova, Natasha Romanoff", date: "2021-07-13", status: false }
        ]
    }

    inputRef = React.createRef()

    deleteProcess = (id) => {
        console.log("@ ", id)
        const new_infos = this.state.infos.filter(info => {
            return info.id != id
        })
        this.setState({ infos: new_infos })
    }

    addInfoToState = (info) => {
        if (info.trim().length === 0) {
            alert('Cannot add empty contents')
            return
        }
        this.setState({ infos: [...this.state.infos, { id: nanoid(), content: info, status: false }] })
    }

    inputInfo = (event) => {
        const { target, keyCode } = event

        if (keyCode === 13) {
            this.addInfoToState(target.value)
            this.inputRef.current.setValue("")
        }
    }

    addProcess = () => {
        const inputVal = this.inputRef.current.input.value
        this.addInfoToState(inputVal)
        this.inputRef.current.setValue("")
    }


    dateGetter = (memontObject) => {
        // this.setState()
        console.log(moment(memontObject).format('YYYY-MM-DD'))
        // return (event) => {
        //     console.log([field])
        //     console.log(event.current)
        // }
    }

    render() {
        const { infos } = this.state

        return (
            <div style={{ margin: "50px" }}>
                <table>
                    <tbody>
                        <tr>
                            <td><label><b>Date: &nbsp;</b></label> </td>
                            <td><DatePicker style={{ height: "25px" }} onChange={this.dateGetter} /><br /></td>
                        </tr>
                        <tr>
                            <td><label><b>Content: &nbsp;</b></label></td>
                            <td><Input style={{ width: "330px", height: "25px" }} ref={this.inputRef} onKeyUp={this.inputInfo} /></td>
                        </tr>
                        <tr>
                            <td><label><b>Price: &nbsp;</b></label></td>
                            <td><Input type="number" style={{ width: "330px", height: "25px" }} ref={this.inputRef} onKeyUp={this.inputInfo} /></td>
                        </tr>
                    </tbody>
                </table>

                <Button
                    onClick={this.addProcess}
                    type="primary"
                    style={{ width: "80px", height: "25px", fontSize: "10px" }}
                >
                    <b>Add</b>
                </Button>
                <br />
                <br />
                <List
                    style={{ width: "483px" }}
                    bordered
                    dataSource={infos}
                    renderItem={
                        item => (
                            <div>
                                <Item key={item.id} item={item} deleteProcess={this.deleteProcess} />
                            </div>
                        )
                    }
                />
            </div>
        )
    }
}
