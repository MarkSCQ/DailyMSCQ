
const iniSate = 0
export default function counterReducer(preState = iniSate, action) {
    const { type, data } = action
    console.log(type, " ", data, " ", preState)
     switch (type) {
        case "addition":
            return preState + data

        case "substract":
            return preState - data

        case "multiplication":
            return preState * data

        case "division":
            return preState / data

        case "remainder":
            return preState % data

        default:
            return preState
    }

}