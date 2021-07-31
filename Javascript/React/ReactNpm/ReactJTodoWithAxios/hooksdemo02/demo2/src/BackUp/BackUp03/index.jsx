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
            { id: 1, issues: "Racing car sprays burning fuel into crowd.", price: 1, date: "2021-07-11", status: false, isNew: false },
            { id: 2, issues: "Japanese princess to wed commoner.", price: 2, date: "2021-07-15", status: false, isNew: false },
            { id: 3, issues: "Australian walks 100km after outback crash.", price: 4, date: "2021-07-12", status: false, isNew: false },
            { id: 4, issues: "Yelena Belova, Natasha Romanoff", price: 3, date: "2021-07-14", status: false, isNew: false }
        ],
        newinfo: { id: undefined, issues: "", price: 0, date: "", status: false, isNew: true },
    }

    // inputRef = React.createRef()
    // inputDateRef = React.createRef()
    // inputIssueRef = React.createRef()
    // inputPriceRef = React.createRef()

    formRef = React.createRef()

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
        this.formRef.current.resetFields(["datepicker", "issueinput", "price"]);
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
        // check if submission is valid
        const newInfo = this.state.newinfo
        // newinfo: { id: undefined, issues: "", price: 0, date: "", status: false, isNew: true },
        if (newInfo.id === undefined || newInfo.issues === "") {
            this.resetNew()
            alert("invalid submission")
            return
        }
        const oldinfos = this.state.infos
        oldinfos.push(newInfo)
        this.setState({ infos: oldinfos })
        this.resetNew()
    }

    // formFun = () => {
    //     const form = Form();
    //     const onReset = () => {
    //         form.resetFields();
    //     };}

    onReset = () => {
        console.log("123")
        console.log(this.formRef)
        console.log("321")

    };
    render() {
        const { infos } = this.state
        /* in nodejs
        const Moment = require('moment')
        const array = [{date:"2018-05-11"},{date:"2018-05-12"},{date:"2018-05-10"}]
        const sortedArray  = array.sort((a,b) => new Moment(a.date).format('YYYYMMDD') - new Moment(b.date).format('YYYYMMDD'))
        console.log(sortedArray)
         */
        // ! define the table
        const columns = [
            {
                title: 'Date',
                dataIndex: 'Date',
                key: 'Date',
                //     sorter: (a, b) => a.age - b.age,
                sorter: (a, b) => {

                    return new moment(a.Date).format('YYYYMMDD') - new moment(b.Date).format('YYYYMMDD')
                }
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
                sorter: (a, b) => a.Price - b.Price,
            },
        ];

        const data = this.makeData(this.state.infos)

        return (
            <div style={{ margin: "50px" }}>

                <Form ref={this.formRef}>
                    <table>
                        <tbody>
                            <tr>
                                <td><label><b>Date: &nbsp;</b></label> </td>
                                <td>
                                    <Form.Item name="datepicker" >
                                        <DatePicker
                                            style={{ width: "330px" }}
                                            onChange={this.dateGetter}
                                        />
                                    </Form.Item>
                                </td>
                            </tr>
                            <tr>
                                <td><label><b>Content: &nbsp;</b></label></td>
                                <td>
                                    <Form.Item name="issueinput">
                                        <Input
                                            style={{ width: "330px" }}
                                            onKeyUp={this.inputInfo("issues")} />
                                    </Form.Item>
                                </td>
                            </tr>
                            <tr>
                                <td><label><b>Price: &nbsp;</b></label></td>
                                <td>
                                    <Form.Item name="price" >
                                        <Input
                                            type="number"
                                            style={{ width: "330px" }}
                                            onKeyUp={this.inputInfo("price")} />
                                    </Form.Item>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <Button
                        onClick={this.submitForm}
                        type="primary"
                        style={{ width: "80px", height: "25px", fontSize: "10px", borderRadius: "8px" }}
                    >
                        <b>Add</b>
                    </Button>

                </Form>

                <Table columns={columns} dataSource={data} pagination={false} onChange={this.onChangeTb} />
            </div>
        )
    }
}
