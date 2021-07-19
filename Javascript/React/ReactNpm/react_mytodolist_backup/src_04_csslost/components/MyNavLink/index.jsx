import React, { Component } from 'react'
import { NavLink } from 'react-router-dom'

export default class MyNavLink extends Component {
    render() {
        const { to, children } = this.props

        return (
            <div>
                {/* 写法一 props 传递 标签内容 */}
                {/* <NavLink activeClassName="Mark" className="list-group-item" to={to}>{content}</NavLink> */}
                {/* 写法二 标签体传递标签内容 */}
                <NavLink activeClassName="Mark" className="list-group-item" to={to}>{children}</NavLink>
            </div>
        )
    }
}
