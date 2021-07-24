import { ADD, MINUS } from './constants'

const iniState = 0
export const countReducer = (preState = iniState, action) => {
    let { type, data } = action
    console.log(preState, data)
    switch (type) {
        case ADD:
            return preState + data
        case MINUS:
            return preState - data
        default:
            return preState;
    }
}