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
import '../table.css'

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


    formRef = React.createRef()

    deleteProcess = (id) => {
        console.log("@ ", id)
        const new_infos = this.state.infos.filter(info => {
            return info.id !== id
        })
        this.setState({ infos: new_infos })
    }
    deleteIssues = (ct) => {
        return () => {
            console.log("@!!!", ct)
            console.log("@ ", ct.key)
            const new_infos = this.state.infos.filter(info => {
                return info.id !== ct.key
            })
            this.setState({ infos: new_infos })
        }
    }
    editProcess = (id) => {

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

    makeData = (data) => {
        return data.map(info => {
            return { key: info.id, Issues: info.issues, Date: info.date, Price: info.price }
        })
    }

    onClickRow = (record) => {
        return {
            onClick: () => {
                this.setState({
                    rowId: record.id,
                });
            },
        };
    }


    setRowClassName = (record) => {
        console.log(this.state.rowId)
        console.log(record)
        // console.log("@@",record)
        // let issues = this.state.infos.filter(info=>{
        //     return info.issues===record.Issues
        // })[0].issues
        // console.log("#F",issues)
        // return record.Issues === issues? 'clickRowStyl' : 'clickRowStylBT';
        const rowID = this.state.infos.find(info => {
            return info.id === record.key
        }).id
        console.log(rowID)
        console.log(record.key)
        console.log(record.key === rowID)
        return record.key === rowID ? 'clickRowStyl1' : 'clickRowStyl';

    }
    submitForm = () => {
        // check if submission is valid
        const newInfo = this.state.newinfo
        // newinfo: { id: undefined, issues: "", price: 0, date: "", status: false, isNew: true },
        if (newInfo.id === undefined || newInfo.issues.length === 0) {
            this.resetNew()
            alert("invalid submission")
            return
        }
        const oldinfos = this.state.infos
        oldinfos.push(newInfo)
        this.setState({ infos: oldinfos })
        this.resetNew()
    }

    render() {
        const { infos } = this.state
        // ! define the table
        const columns = [
            {
                title: 'Date',
                dataIndex: 'Date',
                key: 'Date',
                //     sorter: (a, b) => a.age - b.age,
                sorter: (a, b) => {
                    return new moment(a.Date).format('YYYYMMDD') - new moment(b.Date).format('YYYYMMDD')
                },

            },
            {
                title: 'Issues',
                dataIndex: 'Issues',
                key: 'Issues',
                // onFilter: (value, record) => record.name.indexOf(value) === 0,
            },
            {
                title: 'Price',
                dataIndex: 'Price',
                key: 'Price',
                sorter: (a, b) => a.Price - b.Price,
            },
            {
                title: "Actions",
                render: (text, record) => (
                    <Space size="middle">
                        <Button
                            type="primary"
                            style={{ width: "60px", height: "25px", fontSize: "10px", borderRadius: "8px", background: "white", borderColor: "#95de64" }}
                        >
                            <b style={{ color: "#95de64" }}>Edit</b>
                        </Button>
                        <Button
                            onClick={this.deleteIssues(record)}
                            danger
                            style={{ width: "60px", height: "25px", fontSize: "10px", borderRadius: "8px" }}>
                            <b>Delete</b>
                        </Button>
                    </Space>

                ),
            }
        ];

        const data = this.makeData(infos)

        return (
            <div style={{ margin: "50px" }}>

                <Form
                    ref={this.formRef}
                    labelCol={{ span: 1 }}
                    wrapperCol={{ span: 10 }}>

                    {/* <label><b>Date: &nbsp;&nbsp;</b></label> */}
                    <Form.Item
                        name="datepicker"
                        label={<b>Date</b>}
                    >
                        <DatePicker
                            style={{ width: "330px" }}
                            onChange={this.dateGetter}
                        />
                    </Form.Item>

                    <Form.Item name="issueinput" label={<b>Issue</b>}>
                        <Input
                            style={{ width: "330px" }}
                            onKeyUp={this.inputInfo("issues")} />
                    </Form.Item>


                    <Form.Item name="price" label={<b>Price</b>}>
                        <Input
                            type="number"
                            style={{ width: "330px" }}
                            onKeyUp={this.inputInfo("price")} />
                    </Form.Item>
                    <Form.Item wrapperCol={{ offset: 1, span: 16 }}>

                        <Button
                            onClick={this.submitForm}
                            type="primary"
                            style={{ width: "80px", height: "25px", fontSize: "10px", borderRadius: "8px" }}
                        >
                            <b>Add</b>
                        </Button>
                    </Form.Item>

                </Form>

                <Table
                    columns={columns}
                    dataSource={data}
                    pagination={false}
                    onChange={this.onChangeTb}
                    style={{ width: "700px" }}
                    // rowClassName={this.setRowClassName}
                    onRow={(record) => {
                        return {
                            onMouseEnter: event=>{
                                console.log(event)
                            }
                        }
                    }}
                />
            </div>
        )
    }
}
