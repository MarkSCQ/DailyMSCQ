import React, { Component } from 'react'
import { unmountComponentAtNode } from 'react-dom'


class Lifecycle2 extends Component {

    constructor(props) {
        console.log("count --- Constructor")
        super(props)
        this.state = { count: 0 }
    }
    add = () => {
        // 获取当前state并且更新 count
        this.setState({ count: this.state.count + 1 })
    }

    death = () => {
        unmountComponentAtNode(document.getElementById("root"))
    }

    force = () => {
        this.forceUpdate()
    }


    // static getDerivedStateFromProps() {
    //     console.log("count --- getDerivedStateFromProps")
    //     return null;
    // }

    // 组件将要挂载
    // componentWillMount() {
    //     console.log("count --- componentWillMount")
    // }

    // // 组件挂在完毕
    // componentDidMount() {
    //     console.log("count --- componentDidMount")
    // }

    getSnapshotBeforeUpdate() {
        console.log("count --- getSnapshotBeforeUpdate")
        return "xwb"
    }

    componentWillUnmount() {
        console.log("count --- componentWillUnmount")
    }

    shouldComponentUpdate() {
        console.log("count --- shouldComponentUpdate")
        return true;
    }

    // componentWillUpdate() {
    //     console.log("count --- componentWillUpdate")
    // }

    componentDidUpdate(preProps, preState, snapshotValue) {
        console.log("count --- componentDidUpdate", preProps, preState, snapshotValue)
    }




    render() {
        const { count } = this.state
        console.log("count --- render")

        return (
            <div >
                <div>
                    <h2 id="test">当前数字：{count} </h2>
                </div>
                <button onClick={this.add} >+1s</button>
                <button onClick={this.death}>death</button>
                <button onClick={this.force}>不更改数据，强制更新</button>
            </div>
        )
    }
}

export default Lifecycle2
