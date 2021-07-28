import React, { Component } from 'react'
import { List, Input, Button, Typography } from 'antd'

export default class Item extends Component {


    state = { mouseon: false }

    mouseHandler = (ms) => {
        return () => {
            if (ms) {
                this.setState({ mouseon: false })
            }
            else {
                this.setState({ mouseon: true })

            }
        }
    }

    deleteHandler = (id) => {
        return () => {
            console.log("!! ", id)
            this.props.deleteProcess(id)
        }
    }
    render() {
        const { item } = this.props
        return (
            <div>
                <List.Item
                    onMouseEnter={this.mouseHandler(false)}
                    onMouseLeave={this.mouseHandler(true)}
                    style={{ backgroundColor: this.state.mouseon ? "#b7e3fa" : "white" }}
                >
                    <div>
                        {item.content}
                    </div>
                    <div>
                        <Button
                            onClick={this.deleteHandler(item.id)}
                            style={{ display: this.state.mouseon ? "block" : "none", backgroundColor: "#8dcff8", borderRadius: "5px" }}
                        >
                            <b>Delete</b>
                        </Button>
                    </div>

                </List.Item>
            </div>
        )
    }
}
