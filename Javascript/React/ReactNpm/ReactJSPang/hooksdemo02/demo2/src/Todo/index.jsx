import React, { Component } from 'react'

import {
    List, Input, Button,
    DatePicker, Form,
    Table, Tag, Space
} from 'antd'


import 'antd/dist/antd.css'

import { nanoid } from 'nanoid'
import moment from 'moment';

// import Item from '../Item'

import { getAllData } from './Methods/getdata';
import { getByDate } from './Methods/getdata';
import { DateYMD } from './Methods/timeProcess';
import '../table.css'

/**
 * ! Two-way binding for form, please read below for details.
 * ! Two-way binding gives components in your application a way to share data. 
 * ! Use two-way binding to listen for events and update values simultaneously between parent and child components.
 */
// todo https://github.com/xitingvip/EditableTable/blob/master/EditableTable.js


/*
{ id: 1, issues: "Racing car sprays burning fuel into crowd.", price: 1, date: "2021-07-11", isNew: false },
{ id: 2, issues: "Japanese princess to wed commoner.", price: 2, date: "2021-07-15", isNew: false },
{ id: 3, issues: "Australian walks 100km after outback crash.", price: 4, date: "2021-07-12", isNew: false },
{ id: 4, issues: "Yelena Belova, Natasha Romanoff", price: 3, date: "2021-07-14", isNew: false }
*/
export default class Todo extends Component {

    state = {
        infos: [
        ],
        newinfo: { id: undefined, content: "", price: 0, date: "", isNew: true },
        editingKey: ''
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
        this.setState({ newinfo: { id: 0, content: "", date: "", isNew: true } })
    }

    makeData = (data) => {
        return data.map(info => {
            return { key: info.id, Content: info.content, Date: DateYMD(info.date), Price: info.price }
        })
    }

    setRowClassName = (record) => {
        console.log(record)

        const rowID = this.state.infos.find(info => {
            return info.id === record.key
        }).id
        console.log(rowID)
        console.log(record.key)
        console.log(record.key === rowID)
        return record.key === rowID ? 'clickRowStyl1' : '';
    }



    submitForm = () => {
        // check if submission is valid
        const newInfo = this.state.newinfo
        if (newInfo.id === undefined || newInfo.content.length === 0) {
            this.resetNew()
            alert("invalid submission")
            return
        }
        const oldinfos = this.state.infos
        oldinfos.push(newInfo)
        this.setState({ infos: oldinfos })
        this.resetNew()
    }

    componentDidMount() {

        getAllData("getData/api/taskList")
            .then(response => { return response.data })
            .then(data => {
                console.log(JSON.stringify(data))
                console.log(data)
                this.setState({infos:data})
            })
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
                    console.log(a.Date)
                    return new moment(a.Date).format("LL , H:mm") - new moment(b.Date).format("LL , H:mm")
                },
                editable: true,
            },
            {
                title: 'Content',
                dataIndex: 'Content',
                key: 'Content',
                // onFilter: (value, record) => record.name.indexOf(value) === 0,
                editable: true,
            },
            {
                title: 'Price',
                dataIndex: 'Price',
                key: 'Price',
                sorter: (a, b) => a.Price - b.Price,
                editable: true,
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
                            onKeyUp={this.inputInfo("content")} />
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
                    style={{ backgroundColor: "pink" }}
                    columns={columns}
                    dataSource={data}
                    pagination={false}
                    onChange={this.onChangeTb}
                    style={{ width: "800px" }}
                    // rowClassName={this.setRowClassName}
                    onRow={(record) => {
                        return {
                            onMouseEnter: (event) => {
                                let tr = event.target.parentNode;
                                tr.style.color = "blue";
                                // tr.style.fontWeight = 'bold';

                            },
                            onMouseLeave: (event) => {
                                let tr = event.target.parentNode;
                                tr.style.color = "black";
                                // tr.style.fontWeight = '';
                            }

                        }
                    }}
                />
            </div>
        )
    }
}
