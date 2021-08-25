import React from 'react'

import { squareAction, addAction, getAction } from "../Actions/Actions";

import { connect } from 'react-redux'
import store from '../Store/store';

function Container(props) {
    const { num, add, square, get } = props
    console.log(props)
    return (
        <div>

            <div>{num}</div>
            <button
                onClick={() => {
                    add(1);
                }}
            >
                +1
            </button>
            <button
                onClick={() => {
                    add(2);
                }}
            >
                +2
            </button>
            <button
                onClick={() => {
                    square()
                }}
            >
                **2
            </button>
            <button onClick={() => {
                get()
            }}>
                GET
            </button>
        </div>
    )
}

// connect(mapStateToProps,mapDispatchToProps)(containerName)

const mapStateToProps = (state) => {
    return {
        num: state
    }
}

const mapDispatchToProps = (dispatch) => {
    return {
        add: (val) => dispatch(addAction(val)),
        square: () => dispatch(squareAction()),
        get: () => dispatch(getAction())
    }
}


export default connect(mapStateToProps, mapDispatchToProps)(Container)

