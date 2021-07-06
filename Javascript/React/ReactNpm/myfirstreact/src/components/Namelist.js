import React from 'react'
import Person from './Person'
function Namelist() {
    const names = ['aaa', 'bbb', 'ccc']
    const infos = [
        {
            id: 1,
            name: "aaa",
            age: 11,
            skill:'react'
        },
        {
            id: 2,
            name: "bbb",
            age: 12,
            skill:'TypeScript'

        },
        {
            id: 3,
            name: "ccc",
            age: 13,
            skill:'angular'

        },
    ]

    //Method 2
    // const displayinfo = infos.map(x => (
    //     <ul>
    //         <li>name: {x["name"]}</li>
    //         <li>id: {x["id"]}</li>
    //         <li>age: {x["age"]}</li>
    //     </ul>
    // ))
    //method 3 
    const displayinfo2 = infos.map((x,index) => (
        <Person person={x} key={index} />
    ))
    return (

        // method 1
        // <div>
        //     {infos.map(x => (<div>
        //         <div>name: {x["name"]}</div>
        //         <div>id: {x["id"]}</div>
        //         <div>age: {x["age"]}</div>
        //     </div>))}
        // </div>
        //Method 2


        <div>{displayinfo2}</div>
    )
}

export default Namelist
