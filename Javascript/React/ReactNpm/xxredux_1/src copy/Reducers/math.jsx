const math = (state = 10, action) => {
    switch (action.type) {
        case "ADD":
            return action.num + state
        case "SQUARE":
            return state * state
        case "GET":
            return action.num
        default:
            return state
    }
}


export default math;