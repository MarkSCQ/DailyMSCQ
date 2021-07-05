import React from 'react'

function FunctionClick() {
    const fun = () => {
        console.log("sssfff")
    }
    function sss() {
        console.log("sss")

    }
    return (
        <div>
            <button onClick={sss}>
                sss
            </button>
        </div>
    )
}

export default FunctionClick
