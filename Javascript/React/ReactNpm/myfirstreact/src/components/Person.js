import React from 'react'

function Person({ person }) {
    return (
        <div>
            {person.name},
            {person.id},
            {person.age}
        </div>
    )
}

export default Person
