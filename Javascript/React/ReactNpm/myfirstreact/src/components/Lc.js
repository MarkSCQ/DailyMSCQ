import React, { Component } from 'react'
import Lc2 from './Lc2'
export class Lc extends Component {

    constructor(props) {
        super(props)

        this.state = {
            name: "2333"
        }
        console.log("lc constructor")
    }

    static getDerivedStateFromProps(props, state) {
        console.log("lc getDerivedStateFromProps")
        return null;
    }

    componentDidMount() {
        console.log("lc componentDidMount");
    }

    shouldComponentUpdate() {
        console.log("lc shouldComponentUpdate");
        return true;
    }

    getSnapshotBeforeUpdate(prevProps, prevState) {
        console.log("lc getSnapshotBeforeUpdate");
        return null;
    }

    componentDidUpdate(prevProps, prevSate, snapshot) {
        console.log("lc componentDidUpdate");
    }

    changestate = () => {
        this.setState({ name: '12312321321' })
    }

    render() {
        console.log("lc render");
        return (

            <div>
                <div>
                    lc
                </div>
                <button onClick={this.changestate}>change state</button>
                <div>
                    <Lc2 />
                </div>
            </div>
        )
    }
}

export default Lc
