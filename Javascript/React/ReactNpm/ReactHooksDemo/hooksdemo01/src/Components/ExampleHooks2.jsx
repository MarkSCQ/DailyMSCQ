import React, { useState, useEffect } from 'react'


export default function ExampleHooks2() {


    const [count, setCount] = useState(233) // deconstructing array in es6. useState(val) initialize the state value using val

    // componentDidMount + componentDidUpdate 
    useEffect(() => {
        console.log("you have clicked ", count)
    })
    return (
        <div>
            <h1>The current num is {count}</h1>
            <button onClick={() => setCount(count + 1)}>+1s</button>


        </div>
    )
}
