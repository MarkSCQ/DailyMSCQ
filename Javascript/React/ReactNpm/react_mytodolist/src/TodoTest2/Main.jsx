import React, { Component } from 'react'
import { nanoid } from 'nanoid'
import axios from 'axios'

import Item from './Item'
import { instanceOf } from 'prop-types'
export default class Main extends Component {
    constructor(props) {
        super(props)
        this.state = {
            infos: [
                { content: "content 1", id: 1, status: false },
                { content: "content 2", id: 2, status: false },
                { content: "content 3", id: 3, status: false },
                { content: "content 4", id: 4, status: false },
                { content: "content 5", id: 5, status: false }
            ],
            urldata: ""
        }
        this.inputRef = React.createRef()

        this.inputURLRef = React.createRef()
        this.inputFieldRef = React.createRef()

    }

    axiosGetData = async (urlAdd) => {
        return await axios.get(urlAdd)
    }
    //https://randomuser.me/api
    addAxiosData = (urlAdd, field) => {
        return this.axiosGetData(urlAdd).then(response => {
            console.log("@  ", response.data.results[0])

            return response.data.results[0][field]["large"]
        })
    }
    addAPIData = () => {
        const inputValsURL = this.inputURLRef.current.value
        const inputValsField = this.inputFieldRef.current.value
        this.addAxiosData(inputValsURL, inputValsField)
            .then(
                data => {
                    if (data === true) {
                        console.log(data)
                        this.setState({ urldata: data })
                        // set data
                    }
                    else if (data instanceof Object) {
                        this.setState({ urldata: JSON.stringify(data) })
                    }
                    else {
                        console.warn(data)
                    }
                })
            .catch(err => {
                console.warn(err)
            })
        // this.inputURLRef.current.value = ""
        // this.inputFieldRef.current.value = ""
    }

    addProcess = () => {
        const inputVals = this.inputRef.current.value
        console.log(inputVals)
        const newInfo = { content: inputVals, id: nanoid(), status: false }
        this.setState({ infos: [...this.state.infos, newInfo] })
        this.inputRef.current.value = ""
    }

    removeProcess = (id) => {
        console.log("removeProcess ", id)
        const newInfos = this.state.infos.filter(info => {
            return info.id !== id
        })
        this.setState({ infos: newInfos })
    }

    render() {
        const { infos } = this.state
        return (
            <div>
                <div>
                    <input type="text" placeholder="add info" ref={this.inputRef} />
                    <button onClick={this.addProcess}>add info</button>
                </div>
                <ul>
                    {
                        infos.map(info => {
                            return (
                                <Item
                                    key={info.id}
                                    info={info}
                                    removeProcess={this.removeProcess}
                                />
                            )
                        }
                        )
                    }
                </ul>

                <input type="text" placeholder="URL" ref={this.inputURLRef} />
                <input type="text" placeholder="Field" ref={this.inputFieldRef} />
                <button onClick={this.addAPIData}>GetData</button>
                <div>{this.state.urldata}</div>
                <img src={this.state.urldata} />
            </div>
        )
    }
}
