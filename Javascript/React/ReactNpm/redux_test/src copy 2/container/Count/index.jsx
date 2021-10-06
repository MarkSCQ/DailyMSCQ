import React, { Component } from 'react'
import { connect } from 'react-redux'

import { add, minus } from '../../redux/count_action'




class Count extends Component {

    numRef = React.createRef()


    addHandler = () => {
        const selectedNum = this.numRef.current.value * 1
        this.props.add(selectedNum)
    }
    minusHandler = () => {
        const selectedNum = this.numRef.current.value * 1
        this.props.minus(selectedNum)

    }

    render() {
        return (
            <div>
                <h1> This is Count UI  {this.props.data}</h1>
                <select ref={this.numRef}>
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                    <option value="4">4</option>
                </select>
                <button onClick={this.addHandler}> + </button>
                <button onClick={this.minusHandler}> - </button>


            </div>


        )
    }
}


const mapStateToProps = (state) => {
    return { data: state }
}

const mapDispatchToProps = (dispatch) => {

    return {
        add: (value) => { dispatch(add(value)) },
        minus: (value) => { dispatch(minus(value)) },
        oddAdd: (value) => { dispatch(add(value)) },
        asyncAdd: (value) => { dispatch(add(value)) }

    }

}


export default connect(mapStateToProps, mapDispatchToProps)(Count)