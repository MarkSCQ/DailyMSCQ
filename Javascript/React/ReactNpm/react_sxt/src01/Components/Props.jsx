import React, { Component } from 'react'

export default class Props extends Component {
    render() {
        return (
            <div>
                {this.props.children}
            </div>
        )
    }
}