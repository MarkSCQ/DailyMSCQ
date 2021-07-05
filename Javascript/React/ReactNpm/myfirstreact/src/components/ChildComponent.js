import React from 'react'

function ChildComponent(props) {
    return (
        <div>
            <button onClick={()=>props.greetHandler("!!KID")}>click me</button>
        </div>
    )
}

export default ChildComponent
