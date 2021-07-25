import React, { useState, useEffect } from 'react'

export default function ExampleHooks() {


    const [count, setCount] = useState(233) // deconstructing array in es6. useState(val) initialize the state value using val


    const [age, setAge] = useState(123)
    const [gender, setGender] = useState("Male")
    const [work, setWork] = useState("Coding")

    
    return (
        <div>
            {/* <h1>The current num is {count}</h1>
            <button onClick={() => setCount(count + 1)}>+1s</button> */}
            <p>age: {age}</p>           <button onClick={() => setAge(age + 1)}>+1s</button>
            <p>gender: {gender}</p>     <button onClick={() => setGender("Female")}>Female</button>
            <p>work: {work}</p>         <button onClick={() => setWork("cooking")}>cooking</button>

        </div>
    )
}
