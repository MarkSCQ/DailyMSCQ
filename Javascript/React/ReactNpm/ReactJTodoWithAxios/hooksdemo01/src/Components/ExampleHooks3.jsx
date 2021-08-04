import React, { useState, useEffect } from 'react'
import { BrowserRouter, Route, Link } from 'react-router-dom'


function INDEX() {

    useEffect(() => {
        console.log("INDEX has come")
        // component 解绑
        return ()=>{
            console.log("INDEX has gone")
        }
    },[])
    // 只要状态发生变化 都会执行一次解绑。useEffect第二个参数等于空，解绑后才执行；
    return <h1>MAIN PAGE</h1>
}
function LIST() {
    useEffect(() => {
        console.log("LIST has come")
        return ()=>{
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
                        <Link to="/">
                            Main page
                        </Link>
                    </li>
                    <li>
                        <Link to="/list/">
                            List
                        </Link>
                    </li>
                </ul>
                <Route path="/" exact component={INDEX} />
                <Route path="/list/" component={LIST} />
            </BrowserRouter>
        </div>
    )
}
