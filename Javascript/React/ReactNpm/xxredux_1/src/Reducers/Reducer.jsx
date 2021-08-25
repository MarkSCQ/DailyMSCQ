


const reducer = (state = 10, action) => {
    switch (action.type) {
        case "ADD":
            return state + action.num
        case "MULTI":
            return state  * action.num
        case "MINUS":
            return state - action.num
        case "REMIN":
            return state % action.num
        case "RESET":
            return action.num
        default:
            return state
    }
}

export default reducer