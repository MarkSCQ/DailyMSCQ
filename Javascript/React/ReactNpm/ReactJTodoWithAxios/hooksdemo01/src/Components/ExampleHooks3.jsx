import React, { useState, useEffect } from 'react'
import { BrowserRouter, Route, Link } from 'react-router-dom'


function INDEX() {

    useEffect(() => {
        console.log("INDEX has come")
        return () => {
            console.log("INDEX has gone")
        }
    })
    return <h1>MAIN PAGE</h1>
}
function LIST() {
    useEffect(() => {
        console.log("LIST has come")
        return () => {
            console.log("LIST has gone")
        }
    })
    return <h1>LIST PAGE</h1>
}

export default function ExampleHooks3() {


    const [count, setCount] = useState(233) // deconstructing array in es6. useState(val) initialize the state value using val

    // componentDidMount + componentDidUpdate 
    useEffect(() => {
        console.log("you have clicked ", count)
    })
    return (
        <div>
            <h1>The current num is {count}</h1>
            <button onClick={() => setCount(count + 1)}>+1s</button>

            <BrowserRouter>
                <ul>
                    <li>
                        <Link to="/">MAIN</Link>
                    </li>
                    <li>
                        <Link to="/LIST/">LIST</Link>
                    </li>
                </ul>
                <Route path="/" exact component={INDEX} />
                <Route path="/LIST/" component={LIST} />
            </BrowserRouter>


        </div>
    )
}
