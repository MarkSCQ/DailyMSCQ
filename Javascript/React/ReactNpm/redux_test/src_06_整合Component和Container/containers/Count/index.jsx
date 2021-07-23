import { connect } from 'react-redux'
import React, { Component, createRef } from 'react'

import { creatorAddition, creatorMinus, creatorAdditionAsync } from '../../redux/count_action'
// import creatorAddition, creatorMinus } from '../../redux/count_action'

// 1. mapStateToProps() 函数返回的是一个对象
// 2. 返回的对象中的key作为传递给UI组件props的key，value作为传递给UI组件props的value
// 3. mapStateToProps() 用于传递状态
// const mapStateToProps = (state) => {
// return { count: state }
// }

// 1. mapDispatchToProps() 函数返回的是一个对象
// 2. 返回的对象中的key作为传递给UI组件props的key，value作为传递给UI组件props的value
// 3. mapDispatchToProps() 用于传递方法
// const mapDispatchToProps = (dispatch) => {
//     return {
//         addition: (value) => {
//             dispatch(creatorAddition(value))
//         },
//         minus: (value) => {
//             dispatch(creatorMinus(value))
//         },
//         additionAsync: (value) => {
//             dispatch(creatorAdditionAsync(value, 500))
//         }
//     }
// }

// export default connect(mapStateToProps, mapDispatchToProps)(CountUI)

// 获取redux中store的状态


class Count extends Component {
    selectRef = React.createRef();

    state = { car: "BMW", currentNumber: 0 }


    addHandler = () => {
        console.log("addHandler")
        const userAdder = this.selectRef.current.value
        this.props.addition(userAdder * 1)
        //通知redux加

        // this.setState({ currentNumber: parseInt(this.state.currentNumber) + parseInt(userAdder) })

    }

    minusHandler = () => {
        console.log("minusHandler")
        const userAdder = this.selectRef.current.value
        this.props.minus(userAdder * 1)
    }

    addIfOddHandler = () => {
        console.log("addOddHandler")
        const userAdder = this.selectRef.current.value
        if (this.props.count % 2 !== 0) {
            this.props.addition(userAdder * 1)
        }

    }

    addIfAsyncHandler = () => {
        console.log("addAsyncHandler")
        const userAdder = this.selectRef.current.value
        this.props.additionAsync(userAdder * 1)
        // setTimeout(() => {
        //     store.dispatch(creatorAddition(userAdder*1))
        // }, 500)
    }

    // ! 第一种更新state的写
    render() {
        console.log("@", this.props)

        return (
            <div>

                <h1>Current : {this.props.count}</h1>
                <select ref={this.selectRef}>
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                </select>
                <button onClick={this.addHandler}>+</button>
                <button onClick={this.minusHandler}>-</button>
                <button onClick={this.addIfOddHandler}>add when odd</button>
                <button onClick={this.addIfAsyncHandler}>async add</button>
            </div>
        )
    }
}



// 一种编码角度的优化
export default connect(
    state => {
        return { count: state }
    }
    ,
    dispatch => {
        return {
            addition: (value) => {
                dispatch(creatorAddition(value))
            },
            minus: (value) => {
                dispatch(creatorMinus(value))
            },
            additionAsync: (value) => {
                dispatch(creatorAdditionAsync(value, 500))
            }
        }
    }
    // mapDispatchToProps的简写
    // {
    //     addition: creatorAddition,
    //     minus: creatorMinus,
    //     additionAsync: creatorAdditionAsync
    // }
)(Count)


