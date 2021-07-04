import React from 'react'



const Greet = (props) => {
    return <div>
        <h1>
            hello react {props.name} and {props.nickName}
        </h1>
        {props.children}
    </div>
}


export default Greet