import React, { useState } from 'react'

function HookCounter3() {
    // ! update data in state using hooks need to use ...object
    const [name, setName] = useState({ firstname: "", lastname: "" })

    return (
        <div>
            <form>
                <input
                    type="text"
                    value={name.firstname}
                    onChange={e => setName({ ...name, firstname: e.target.value })}
                />
                <input
                    type="text"
                    value={name.lastname}
                    onChange={e => setName({ ...name, lastname: e.target.value })}
                />
            </form>

            <h2>firstname: {name.firstname}</h2>
            <h2>lastname: {name.lastname}</h2>


        </div>
    )
}

export default HookCounter3
