import React, { useState, useEffect } from 'react'

function HookCounterOne() {
    const [count, setCounter] = useState(0)


    useEffect(() => {
        document.title = `${count} times`

    })

    return (
        <div>
            <button onClick={() => { setCounter(count + 1) }}>{count} times</button>
        </div>
    )
}

export default HookCounterOne
