import { ADD, SQUARE } from "../Constants/ActionTypes"


const addAction = (num) => {
    return {
        type: ADD,
        num
    }
}
const squareAction = (num) => {
    return {
        type: SQUARE

    }
}
const getAction = () => {
    return (dispatch, getState) => {

        Promise.resolve(1)
            .then(() => {
                dispatch({
                    type: "GET",
                    num: 233
                })
            })
    }
}



export {
    addAction,
    squareAction,
    getAction
}