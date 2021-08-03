import React, { Component } from 'react'

import {
    List, Input, Button,
    DatePicker, Form,
    Table, Tag, Space, Select
} from 'antd'


import 'antd/dist/antd.css'

import { nanoid } from 'nanoid'
import moment from 'moment';

// import Item from '../Item'

import { getAllData } from './Methods/getdata';
import { getByDate } from './Methods/getdata';

import { addRecord } from './Methods/senddata';

import { DateYMD } from './Methods/timeProcess';

// import '../table.css'

/**
 * ! Two-way binding for form, please read below for details.
 * ! Two-way binding gives components in your application a way to share data. 
 * ! Use two-way binding to listen for events and update values simultaneously between parent and child components.
 */
// todo https://github.com/xitingvip/EditableTable/blob/master/EditableTable.js



export default class Todo extends Component {

    state = {
        infos: [
        ],
        newinfo: { taskid: undefined, content: "", price: 0, date: "", tag: "" },
        tags: [],
        editingKey: ''
    }


    formRef = React.createRef()


    deleteRecord = (ct) => {
        return () => {
            const new_infos = this.state.infos.filter(info => {
                return info.taskid !== ct.key
            })
            this.setState({ infos: new_infos })
        }
    }

    editProcess = (taskid) => {

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
            // console.log("@ ", this.state.newinfo)
        }
    }

    dateGetter = (memontObject) => {
        this.setState({
            newinfo: {
                ...this.state.newinfo,
                date: moment(memontObject).format('YYYY-MM-DD'),
                taskid: nanoid()
            }
        })
    }

    resetNew = () => {
        this.formRef.current.resetFields(["datepicker", "issueinput", "price"]);
        this.setState({ newinfo: { taskid: "", content: "", date: "", tag: "" } })
    }

    makeData = (data) => {

        data.sort((a, b) => {
            return new Date(a.date) - new Date(b.date)
        })

        return data.map(info => {

            return { key: info.taskid, Content: info.content, Tag: [info.tag], Date: DateYMD(info.date), Price: info.price }
        })
    }



    submitForm = () => {
        // check if submission is valid
        const newInfo = this.state.newinfo
        if (newInfo.taskid === undefined || newInfo.content.length === 0) {
            this.resetNew()
            alert("invalid submission")
            return
        }
        const oldinfos = this.state.infos
        oldinfos.push(newInfo)
        this.setState({ infos: oldinfos })
        const { taskid, date, content, price, tag } = this.state.newinfo
        // ! addRecord api put here
        addRecord("getData/apicore/addRecord", date, content, price, tag)
            .then(response => {
                console.log(response.data)
                return response.data
            })
            .then(
                data => {
                    this.setState({ infos: data.data, tags: data.tags })
                    console.log(this.state)

                }
            )
        this.resetNew()
    }

    componentDidMount() {

        getAllData("getData/apicore/taskList")
            .then(response => { return response.data })
            .then(data => {
                // console.log(JSON.stringify(data))
                console.log(data)
                this.setState({ infos: data.data, tags: data.tags })
            })
    }

    render() {
        const { infos } = this.state

        const tagColor = {
            'Food': "green",
            'Entertainment': "yellow",
            'Water fee': "blue",
            'Electricity fee': "red",
            'Gas fee': "blue",
            'Rental fee': "red",
            'Phone fee': "blue",
            'Network fee': "blue"
        }
        // ! define the table
        const columns = [
            {
                title: <div><b>Date</b></div>,
                dataIndex: 'Date',
                key: 'Date',
                sorter: (a, b) => {
                    return new moment(a.Date).format("YYYYMMDD") - new moment(b.Date).format("YYYYMMDD")
                },
                editable: true,

                // ! make filters and onFilter tomorrow
                filters: [

                ],
                onFilter: (value, record) => {

                    record.name.indexOf(value)
                    console.log(value)
                    console.log(record)
                },

            },
            {
                title: <div><b>Content</b></div>,
                dataIndex: 'Content',
                key: 'Content',
                editable: true,
            },
            {
                title: <div><b>Tag</b></div>,
                dataIndex: 'Tag',
                key: 'Tag',
                render: tags => (
                    <>
                        {tags.map(tag => {
                            return (
                                <Tag color={tagColor[tag]} key={tag}>
                                    {tag.toUpperCase()}
                                </Tag>
                            );
                        })}
                    </>
                ),
                editable: true,
            },
            {
                title: <div><b>Price</b></div>,
                dataIndex: 'Price',
                key: 'Price',
                sorter: (a, b) => a.Price - b.Price,
                editable: true,
            },
            {
                title: <div><b>Actions</b></div>,
                render: (text, record) => (
                    <Space size="middle">
                        <Button
                            type="primary"
                            style={{ width: "60px", height: "25px", fontSize: "10px", borderRadius: "8px", background: "white", borderColor: "#95de64" }}
                        >
                            <b style={{ color: "#95de64" }}>Edit</b>
                        </Button>
                        <Button
                            onClick={this.deleteRecord(record)}
                            dtype="primary"
                            style={{ width: "60px", height: "25px", fontSize: "10px", borderRadius: "8px", background: "white", borderColor: "plum" }}>
                            <b style={{ color: "plum" }}>Delete</b>
                        </Button>
                    </Space>

                ),
            }
        ];

        const data = this.makeData(infos)
        const { Option } = Select;

        return (
            <div style={{ margin: "50px" }}>

                <Form
                    ref={this.formRef}
                    labelCol={{ span: 3 }}
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

                    <Form.Item name="tag" label={<b>Tags</b>} >

                        <Select style={{ width: "200px" }} onKeyUp={this.inputInfo("tag")}   >
                            {
                                this.state.tags.map((item) => {
                                    return <Option value={item} key={item}>{item}</Option>

                                })
                            }
                        </Select>
                    </Form.Item>



                    <Form.Item wrapperCol={{ offset: 3, span: 16 }}>

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
                    bordered

                    columns={columns}
                    dataSource={data}
                    pagination={false}
                    onChange={this.onChangeTb}
                    style={{ width: "800px" }}
                    onRow={(record) => {
                        return {
                            onMouseEnter: (event) => {
                                let tr = event.target.parentNode;
                                for (var i = 0; i < tr.childNodes.length; i++) {
                                    // changing the background color of each row, this need to be applied over specific tr nodes of each rows
                                    tr.childNodes[i].style.backgroundColor = "LightSkyBlue"

                                }
                            },
                            onMouseLeave: (event) => {
                                let tr = event.target.parentNode;
                                for (var i = 0; i < tr.childNodes.length; i++) {
                                    tr.childNodes[i].style.backgroundColor = "white"
                                }
                            }
                        }
                    }}
                />
            </div >
        )
    }
}
