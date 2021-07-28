import React, { Component } from 'react'

import {
    List, Input, Button,
    DatePicker, Form,
    Table, Tag, Space
} from 'antd'


import 'antd/dist/antd.css'

import { nanoid } from 'nanoid'
import moment from 'moment';

import Item from '../Item'

export default class Todo extends Component {

    state = {
        infos: [
            { id: 1, issues: "Racing car sprays burning fuel into crowd.", price: 0, date: "2021-07-13", status: false, isNew: false },
            { id: 2, issues: "Japanese princess to wed commoner.", price: 0, date: "2021-07-13", status: false, isNew: false },
            { id: 3, issues: "Australian walks 100km after outback crash.", price: 0, date: "2021-07-13", status: false, isNew: false },
            { id: 4, issues: "Yelena Belova, Natasha Romanoff", price: 0, date: "2021-07-13", status: false, isNew: false }
        ],
        newinfo: { id: 0, issues: "", price: 0, date: "", status: false, isNew: true },
    }

    inputRef = React.createRef()
    inputDateRef = React.createRef()
    inputIssueRef = React.createRef()
    inputPriceRef = React.createRef()
    deleteProcess = (id) => {
        console.log("@ ", id)
        const new_infos = this.state.infos.filter(info => {
            return info.id !== id
        })
        this.setState({ infos: new_infos })
    }

    addInfoToState = (info) => {
        if (info.trim().length === 0) {
            alert('Cannot add empty contents')
            return
        }
        this.setState({ infos: [...this.state.infos, { id: nanoid(), issues: info, status: false }] })
    }

    inputInfo = (field) => {
        return (event) => {
            const { target, keyCode } = event

            this.setState({
                newinfo: {
                    ...this.state.newinfo,
                    [field]: target.value
                }
            })
            console.log("@ ", this.state.newinfo)
        }
    }

    addProcess = () => {
        const inputVal = this.inputRef.current.input.value
        this.addInfoToState(inputVal)
        this.inputRef.current.setValue("")
    }


    dateGetter = (memontObject) => {
        this.setState({
            newinfo: {
                ...this.state.newinfo,
                date: moment(memontObject).format('YYYY-MM-DD'),
                id: nanoid()
            }
        })
    }

    resetNew = () => {
        this.inputDateRef.current.value = ""
        this.setState({ newinfo: { id: 0, issues: "", date: "", status: false, isNew: true } })
    }

    setWithField = (fieldName) => {
        return (event) => {
            this.setState({ newinfo: { ...this.state.newinfo, [fieldName]: event.target.value } })
        }
    }

    makeData = (data) => {
        console.log("data is ", data)
        return data.map(info => {
            return { key: info.id, Issues: info.issues, Date: info.date, Price: info.price }
        })
    }

    submitForm = () => {
        const oldinfos = this.state.infos
        oldinfos.push(this.state.newinfo)
        console.log(this.state.oldinfos)
        this.setState({ infos: oldinfos })
        this.resetNew()
        console.log(this.state.infos)

    }
    render() {
        const { infos } = this.state

        // ! define the table
        const columns = [
            {
                title: 'Date',
                dataIndex: 'Date',
                key: 'Date',
            },
            {
                title: 'Issues',
                dataIndex: 'Issues',
                key: 'Issues',
            },
            {
                title: 'Price',
                dataIndex: 'Price',
                key: 'Price',
            },
        ];
        console.log('infos@!', this.state.infos)

        const data = this.makeData(this.state.infos)
        console.log(this.state.newinfo)
        return (
            <div style={{ margin: "50px" }}>

                <Form>
                    <table>
                        <tbody>
                            <tr>
                                <td><label><b>Date: &nbsp;</b></label> </td>
                                <td><DatePicker
                                    style={{ height: "25px" }}
                                    onChange={this.dateGetter}
                                    ref={this.inputDateRef}
                                /><br /></td>
                            </tr>
                            <tr>
                                <td><label><b>Content: &nbsp;</b></label></td>
                                <td><Input
                                    style={{ width: "330px", height: "25px" }}
                                    ref={this.inputIssueRef}
                                    onKeyUp={this.inputInfo("issues")} /></td>
                            </tr>
                            <tr>
                                <td><label><b>Price: &nbsp;</b></label></td>
                                <td><Input
                                    type="number"
                                    style={{ width: "330px", height: "25px" }}
                                    ref={this.inputPriceRef}
                                    onKeyUp={this.inputInfo("price")} /></td>
                            </tr>
                        </tbody>
                    </table>

                    <Button
                        onClick={this.submitForm}
                        type="primary"
                        style={{ width: "80px", height: "25px", fontSize: "10px" }}
                    >
                        <b>Add</b>
                    </Button>
                </Form>

                <Table columns={columns} dataSource={data} pagination={false} />
            </div>
        )
    }
}
