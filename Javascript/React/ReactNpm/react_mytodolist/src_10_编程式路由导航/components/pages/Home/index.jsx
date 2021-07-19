import React, { Component } from 'react'
import News from './News'
import Message from './Message'
import MyNavLink from '../../MyNavLink'
import { Redirect, Route, Switch } from 'react-router'
import MyNavLinkSub from '../../MyNavLinkSub'
export default class Home extends Component {
    render() {
        return (
            <div>
                <h3>Home Page</h3>
                <div>
                    <ul className="nav nav-tabs">
                        <li>
                            <MyNavLinkSub  to="/home/news">News</MyNavLinkSub>

                        </li>
                        <li>
                            <MyNavLinkSub  to="/home/message">Message</MyNavLinkSub>
                        </li>
                    </ul>
                </div>

                <Switch>
                    <Route path="/home/news" component={News} />
                    <Route path="/home/message" component={Message} />
                    <Redirect to="/home/news" />
                </Switch>
            </div>
        )
    }
}
