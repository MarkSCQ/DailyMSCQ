import React, { Component } from 'react'

import axios from 'axios'
import moment from 'moment'
import { getAllData } from '../Todo/Methods/getdata'
import { getByDate } from '../Todo/Methods/getdata'
import { Fragment } from 'react-is'
import ColumnGroup from 'antd/lib/table/ColumnGroup'

export default class Userdata extends Component {

    state = {
        info: "",
        sendDate: { year: 0, month: 0, day: 0 },
        listdata: []
    }

    inputYearRef = React.createRef()
    inputMonthRef = React.createRef()
    inputDayRef = React.createRef()


    btnAxio = () => {
        axios.get("getData/apicore/taskList")
            .then(response => { return response.data })
            .then(data => { console.log(JSON.stringify(data)) })
    }



    inputSet = (dateFiledName) => {
        return (event) => {
            console.log(dateFiledName, " ", event.target.value)
            this.setState({
                sendDate: {
                    ...this.state.sendDate,
                    [dateFiledName]: event.target.value
                }
            })
        }
    }


    // btnAxio2 = (date) => {
    //     axios.get("getData/api/taskList")
    //         .then(response => { return response.data })
    //         .then(data => { console.log(JSON.stringify(data)) })
    // }

    resetInputs = (isReset) => {
        if (isReset) {
            this.inputYearRef.current.value = ""
            this.inputMonthRef.current.value = ""
            this.inputDayRef.current.value = ""
        }
    }


    submitAll = (event) => {
        event.preventDefault();

        const year = this.state.sendDate.year
        const month = this.state.sendDate.month
        const day = this.state.sendDate.day

        console.log("@@ ", this.state.sendDate)

        // axios.get(`getData/api/getByDate/${year}/${month}/${day}`)
        //     .then((response) => {
        //         console.log("@", response)
        //         console.log("@@", response.data)
        //         this.setState({ info: JSON.stringify(response.data) })
        //         return response.data
        //     })
        //     .catch((err) => {
        //         console.warn(err)
        //     })

        // axios.post('getData/apicore/getByDatePost', {
        //     year: year,
        //     month: month,
        //     day: day,
        // })
        //     .then((response) => {
        //         console.log("@", response)
        //         console.log("@@", response.data)
        //         this.setState({ info: JSON.stringify(response.data) })
        //         return response.data
        //     })
        //     .catch((err) => {
        //         console.warn(err)
        //     })
        const formData = new FormData();

        formData.append('year', year);
        formData.append('month', month);
        formData.append('day', day); 
        console.log("$!@", formData)
        axios({
            method: "post",
            url: "getData/apicore/getByDatePost",
            data: {
                year: year,
                month: month,
                day: day
            }
        })
            .then((response) => {
                console.log("@", response)
                console.log("@@", response.data)
                this.setState({ info: JSON.stringify(response.data) })
                return response.data
            })
            .catch((err) => {
                console.warn(err)
            })

        this.resetInputs(true)
    }

    componentDidMount() {
        let year = 2021
        let month = 8
        let day = 1
        getByDate(`getData/apicore/getByDate/${year}/${month}/${day}`)
            .then(response => {
                console.log(response.data)
                let d = response.data[0].date
                let testd = moment(d).format('MMMM Do YYYY')
                console.log(testd)

                console.log(moment(d).format('ll'))
                console.log(moment(d).format('LLL'))
                console.log(moment(d).format('llll'))
                console.log(moment(d).format('LL , H:mm'))
                console.log(moment(d).format('MMMM Do YYYY, H:mm:ss'))

                // this.setState({ info: testd })
                return response.data
            })
        // getAllData("getData/apicore/taskList")
        //     .then(response => {
        //         console.log("@", response.data)

        //         this.setState({ listdata: response.data })
        //         return response.data
        //     })

    }

    render() {
        let year = 2021
        let month = 7
        let day = 29
        console.log(this.state.sendDate)
        getAllData("getData/apicore/taskList")
            .then(response => {
                console.log(response.data)
                return response.data
            })


        return (
            <div style={{ margin: "50px" }}>

                <div>
                    <h2>this is all data</h2>
                    <button onClick={this.btnAxio}>click</button>
                </div>

                <div>
                    <h2>this is choose data</h2>
                    <form onSubmit={this.submitAll}>

                        <input ref={this.inputYearRef} onChange={this.inputSet("year")} placeholder="Year" /><br />
                        <input ref={this.inputMonthRef} onChange={this.inputSet("month")} placeholder="Month" /><br />
                        <input ref={this.inputDayRef} onChange={this.inputSet("day")} placeholder="Day" /><br />
                        <input type="submit" value="Submit" />
                    </form>
                </div>

                <div>
                    Year: {this.state.sendDate.year}<br />
                    Month: {this.state.sendDate.month}<br />
                    Day: {this.state.sendDate.day}<br />
                    info: {this.state.info}<br />
                </div>

                {/* <div>
                    {
                        this.state.listdata.map(data => {
                            console.log(data.content)
                            return <div key={data.id}>{data.content}</div>
                        })
                    }
                </div> */}

            </div>
        )
    }
}
