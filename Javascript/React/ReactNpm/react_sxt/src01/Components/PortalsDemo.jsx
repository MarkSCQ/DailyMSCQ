import React from 'react'
import ReactDOM from 'react-dom'

import Props from './Props'

function PortalsDemo() {
    return ReactDOM.createPortal(
        <div>
            <h1>PortalsDemo</h1>
            <Props><h2>2sdzfds3333</h2></Props>
        </div>,
        document.getElementById("portal-root")
    )
}

export default PortalsDemo
