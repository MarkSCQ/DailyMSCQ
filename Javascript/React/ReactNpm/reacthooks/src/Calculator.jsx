import React, { useState, userReducer } from "react";

const Calculator = (params) => {
    const [state, setCount] = useState({ type: "add", value: 0 })

    const onClick = (params) => {
        // ! 合理的setCount是一个异步操作
        // setCount(count + 1)
        setCount((preState) => {
            if (preState&&preState.type==="add") {
                return { ...preState, value: preState.value + 1 }
            }
            return preState
        })
    }

    return (
        <div>
            <div>{state.value}</div>

            <button onClick={() => { onClick() }}>BTN</button>
        </div>
    )

}

export default Calculator