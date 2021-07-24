
import React, { Component } from 'react'
import { connect } from 'react-redux'

import { addCreator, minusCreator } from '../../redux/createAction'

const mapStateToProps = (data) => {
    return { state: data }
}

const mapDispatchToProps = (dispatcher) => {
    return {
        add: (value) => { return dispatcher(addCreator(value)) },
        minus: (value) => { return dispatcher(minusCreator(value)) },
        oddAdd: (value) => { return dispatcher(addCreator(value)) },
        asyncAdd: (value) => {
            return setTimeout(() => {
                dispatcher(addCreator(value))
            }, 300)
        }
    }
}
class Count extends Component {

    numRef = React.createRef()

    addHandler = () => {
        const numSelect = this.numRef.current.value*1
        this.props.add(numSelect)
        console.log(numSelect)
        console.log(this.props)

    }

    minusHandler = () => {
        const numSelect = this.numRef.current.value*1
        this.props.minus(numSelect)
    }

    oddAddHandler = () => {

    }

    asyncAddHandler = () => {

    }

    render() {
        return (
            <div>
                <h2>current num: {this.props.state}</h2>
                <br />

                <select ref={this.numRef}>
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                    <option value="4">4</option>
                </select>

                <br />
                <button onClick={this.addHandler}>+</button>
                <button onClick={this.minusHandler}>-</button>
                <button onClick={this.oddAddHandler}>Odd, +</button>
                <button onClick={this.asyncAddHandler}>Async,+</button>

            </div>
        )
    }
}




export default connect(mapStateToProps, mapDispatchToProps)(Count)

