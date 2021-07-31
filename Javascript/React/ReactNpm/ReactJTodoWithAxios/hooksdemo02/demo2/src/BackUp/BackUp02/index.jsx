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
        newinfo: { id: 0, issues: "", price: 0, date: "", status: false, isNew: true }
    }

    inputRef = React.createRef()


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
        console.log(typeof (moment(memontObject).format('YYYY-MM-DD')))
        console.log(moment(memontObject).format('YYYY-MM-DD'))
        return moment(memontObject).format('YYYY-MM-DD')
    }

    resetNew = () => {
        this.setState({ newinfo: { id: 0, issues: "", date: "", status: false, isNew: true } })
    }

    setWithField = (fieldName) => {
        return () => {
            this.setState({ newinfo: { id: 0, issues: "", date: "", status: false, isNew: true } })
        }
    }

    makeData = (data) => {
        return data.map(info => {
            return { key: info.id, Issues: info.issues, Date: info.date, Price: info.price }
        })
    }

    render() {
        const { infos } = this.state

        //////
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
        //这里是表格内的数据
        // const data = [
        //     {
        //         id: '1',
        //         Date: 'John Brown',
        //         Issues: 32,
        //         Price: 'New York No. 1 Lake Park',
        //     },
        //     {
        //         key: '2',
        //         Date: 'Jim Green',
        //         Issues: 42,
        //         Price: 'London No. 1 Lake Park',
        //     },
        // ];
        const data = this.makeData(this.state.infos)
        return (
            <div style={{ margin: "50px" }}>
                {/* 
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
                <br /> */}
                {/* <List
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
                <br />
 */}

                <Form>
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
                        // 这个button 一方面加载到local 一方面输出到server 或者说 send到sever后重新在返回一下值 重新render
                        // onClick={this.addProcess}
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
