import React, { useState, useEffect } from 'react'

export default function ExampleHooks() {


    const [count, setCount] = useState(233) // deconstructing array in es6. useState(val) initialize the state value using val



    return (
        <div>
            <h1>The current num is {count}</h1>
            <button onClick={() => setCount(count + 1)}>+1s</button>


        </div>
    )
}
