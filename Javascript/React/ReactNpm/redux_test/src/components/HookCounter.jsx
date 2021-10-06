import React from 'react'
import { useState } from 'react'

// only call hoooks at the top level
// only call hooks from react fucntions
function HookCounter() {

    const [count, setCount] = useState(0)
    return (
        <div>
            {/* <button onClick={() => setCount(count + 1)}>Hook Counter {count}</button> */}
            <button onClick={() => setCount(count + 1)}>Hook Counter {count}</button>
        </div>
    )
}

export default HookCounter
