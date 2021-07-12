import React, { Component } from 'react'

import hello from './hello.module.css'

class Hello extends Component {
    render() {
        return (
            <div>
                <h1 className={hello.title}>Hello</h1>
            </div>
        )
    }
}

export default Hello
