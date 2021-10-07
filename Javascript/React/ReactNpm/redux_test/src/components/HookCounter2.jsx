import React, { useState } from 'react'
// ! previous state in setState
function HookCounter2() {

    const initialCount = 0
    const [count, setCount] = useState(initialCount)
    const increaseSix = () => {
        for (let i = 0; i < 6; i++) {
            setCount(prevCount => {
                return prevCount + 1
            })
        }
    }
    return (
        <div>
            Count: {count}
            <button onClick={() => { setCount(initialCount) }}>RESET</button>
            <button onClick={() => {
                setCount(prevCount => {
                    return prevCount + 1
                })
            }}>INCREAMENT</button>
            <button onClick={() => {
                setCount(prevCount => {
                    return prevCount - 1
                })
            }}>DECREAMENT</button>
            <button onClick={increaseSix}>SIX</button>
        </div>
    )
}

export default HookCounter2
