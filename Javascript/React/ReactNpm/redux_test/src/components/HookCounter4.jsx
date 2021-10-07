import React, { useState } from 'react'

function HookCounter4() {
    const [items, setItems] = useState([])
    const addItem = () => {
        setItems([...items,
        {
            id: items.length,
            value: Math.floor(Math.random() * 10) + 1
        }])
    }
    return (
        <div>
            <button onClick={addItem}>Click Me To Add</button>
            <ul>
                {
                    items.map(item => {
                        return <li key={item.id}>{item.value}</li>
                    })
                }
            </ul>

        </div>
    )
}

export default HookCounter4
