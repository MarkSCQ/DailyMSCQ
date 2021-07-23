import { connect } from 'react-redux'

import { creatorAddition, creatorMinus, creatorAdditionAsync } from '../../redux/count_action'
import CountUI from '../../componnets/Count'
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



)(CountUI)


