import React, { Component } from 'react'
import Lifecycle4 from './Lifecycle4'

class Lifecycle3 extends Component {
    state = {
        carname: "bmw",
        carname1: "bz",
        iscar: true
    }

    changeCar = () => {
        this.setState({ iscar: !this.state.iscar })
    }
    render() {
        const { carname, carname1, iscar } = this.state
        return (
            <div>
                This is parent Lifecycle3

                <div>this is {iscar ? carname : carname1} </div>
                <button onClick={this.changeCar}>change car</button>
                <Lifecycle4 carName={iscar ? carname : carname1} />

            </div>
        )
    }
}

export default Lifecycle3
