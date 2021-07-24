import { ADD, MINUS } from './constant'


const iniState = 0
const countReducer = (preState = iniState, action) => {
    const { type, data } = action
    switch (type) {
        case ADD:
            return preState + data
        case MINUS:
            return preState - data
        default:
            return preState;
    }

}

export default countReducer