

const initial = {
    inputVal: "2333",
    infos: ['info 1 ... ',
        'info 2 ... ',
        'info 3 ... ',
        'info 4 ... ']
}

export default function reducerFun(preState = initial, action) {

    // 业务逻辑

    console.log(preState, action)
    let localState;
    if (action.type === "addData") {
        let localState = JSON.parse(JSON.stringify(preState))
        localState.inputVal = action.type
        return localState

    }
    return preState
}