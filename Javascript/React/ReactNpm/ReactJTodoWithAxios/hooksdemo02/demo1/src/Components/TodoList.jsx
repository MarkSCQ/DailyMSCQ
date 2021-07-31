import React, { Component } from 'react'


import { Input, Button, List } from 'antd'
import 'antd/dist/antd.css'

import store from './Store/index'


export default class TodoList extends Component {

    constructor(props) {
        super(props)
        console.log("@", store.getState())

        this.state = store.getState()
        this.addData = this.addData.bind(this)
        this.storeChange = this.storeChange.bind(this)
        store.subscribe(this.storeChange)
    }

    addData(event) {
        console.log(event.target.value)
        const action = {
            type: "addData",
            value: event.target.value
        }
        store.dispatch(action)
    }
    storeChange() {
        this.setState(store.getState())
    }
    render() {
        const fakedata = [

        ]
        console.log(fakedata)
        return (
            <div>
                <div style={{ margin: '10px' }}>
                    <Input style={{ width: '250px', marginRight: '10px' }} onChange={this.addData} />
                    <Button
                        type="primary"

                    >
                        Add
                    </Button>
                </div>
                <div style={{ margin: '10px', width: "300px" }}>
                    <List
                        bordered
                        dataSource={this.state.infos}
                        renderItem={item => (
                            <List.Item>
                                {item}
                            </List.Item>
                        )
                        }
                    />
                </div>

            </div>
        )
    }
}
