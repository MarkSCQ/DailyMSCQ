import React from 'react'

function MemoComp() {

    console.log('rendering memo')
    return (
        <div>
            MemoComp
        </div>
    )
}

// higher order component
export default React.memo(MemoComp)


 