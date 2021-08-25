import {
    ADD,
    MULTI,
    MINUS,
    REMIN,
    RESET
} from '../Constants/CONSTANTS'


const addAction = (num) => {
    return {
        type: ADD,
        num
    }
}

const multiAction = (num) => {
    return {
        type: MULTI,
        num
    }
}

const minusAction = (num) => {
    return {
        type: MINUS,
        num
    }
}

const reminAction = (num) => {
    return {
        type: REMIN,
        num
    }
}
const resetAction = () => {
    return (dispatch) => {
        Promise.resolve()
            .then(() => {
                dispatch({
                    type: RESET,
                    num: 0
                })
            })
    }
}

export {
    addAction,
    multiAction,
    minusAction,
    reminAction,
    resetAction
}