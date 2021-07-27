import React, { Component } from 'react'
import Item from './Item'

export default class FunTest extends Component {

    state = {
        infos: [
            { content: "info 1", status: false },
            { content: "info 2", status: false },
            { content: "info 3", status: false },
            { content: "info 4", status: false },
        ]
    }

    inputRef = React.createRef()

    addInfo = () => {
        const info = { content: this.inputRef.current.value, status: false }
        console.log(info)
        this.setState({ infos: [...this.state.infos, info] })
        this.inputRef.current.value = ""
    }

    deleteHandler = (id) => {
        console.log("@", id)
        const newInfos = this.state.infos.filter(info => {
            return info.content !== id
        })
        this.setState({ infos: newInfos })
    }


    processCheck = (id, checked) => {
        console.log(id, checked)

        const { infos } = this.state
        const newtodos = infos.map((todo) => {
            if (todo.content === id) {
                todo.status = checked
                return { ...todo, checked }
            }
            else {
                return todo
            }
        })
        console.log(newtodos)
        this.setState({ todos: newtodos })

    }

    checkedCount = () => {
        return this.state.infos.filter(
            info => {
                return info.status === true
            }
        ).length
    }
    
    allCheckedCount = () => {
        return this.state.infos.length
    }
    removeChecked = () => {
        const newInfos = this.state.infos.filter(info => {
            return info.status !== true
        })
        console.log(newInfos)
        this.setState({ infos: newInfos })
    }


    checkAllHandler = (event) => {
        const { infos } = this.state
        const newtodos = infos.map((td) => {
            return { ...td, status: event.target.checked }
        })
        this.setState({ infos: newtodos })
    }


    render() {
        console.log("infos ! ", this.state.infos)
        const checkeds = this.checkedCount()
        const checkedsall = this.allCheckedCount()
        return (
            <div>
                <input type="text" placeholder="input info" ref={this.inputRef} />
                <button onClick={this.addInfo}>Add</button>
                <hr />
                <div>
                    <h3>Infos Display</h3>
                    {
                        this.state.infos.map(
                            info => {
                                return <Item
                                    key={info.content}
                                    info={info}
                                    deleteHandle={this.deleteHandler}
                                    processCheck={this.processCheck}
                                />
                            }
                        )
                    }
                </div>
                <div>
                    <input type="checkbox" onChange={this.checkAllHandler} checked={checkeds === checkedsall && checkedsall !== 0 ? true : false} /> {checkeds}/{checkedsall} <button onClick={this.removeChecked}>Remove Checked</button>
                </div>
            </div>
        )
    }
}

