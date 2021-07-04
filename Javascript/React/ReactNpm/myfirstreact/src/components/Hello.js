import React from 'react'


const Hello = () => {
    // return (<div>
    //     <h1>
    //         hello jsx
    //     </h1>
    // </div>)

    return React.createElement('div',{id:"hello"},React.createElement('h1',null,"hello jsssxxx"))
}

export default Hello