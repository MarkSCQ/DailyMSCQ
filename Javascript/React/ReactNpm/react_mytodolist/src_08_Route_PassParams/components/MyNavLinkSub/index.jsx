import React, { Component } from 'react'
import { NavLink } from 'react-router-dom'

export default class MyNavLinkSub extends Component {
    render() {
        const { to, children } = this.props

        return (
            <div>
                <NavLink activeClassName="MarkSub" className="list-group-item" to={to}>{children}</NavLink>
            </div>
        )
    }
}
