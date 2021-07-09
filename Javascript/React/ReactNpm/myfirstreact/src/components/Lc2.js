import React, { Component } from 'react'

export class Lc2 extends Component {

    constructor(props) {
        super(props)

        this.state = {
            name: "2333"
        }
        console.log("lc2 constructor")
    }

    static getDerivedStateFromProps(props, state) {
        console.log("lc2 getDerivedStateFromProps")
        return null;
    }

    componentDidMount() {
        console.log("lc2 componentDidMount");

    }

    shouldComponentUpdate() {
        console.log("lc2 shouldComponentUpdate");
        return true;
    }

    getSnapshotBeforeUpdate(prevProps, prevState) {
        console.log("lc2 getSnapshotBeforeUpdate");
        return null;

    }

    componentDidUpdate(prevProps, prevSate, snapshot) {
        console.log("lc2 componentDidUpdate");
    }
    render() {
        console.log("lc2 render");
        return (

            <div>
                lc2
            </div>
        )
    }
}

export default Lc2
