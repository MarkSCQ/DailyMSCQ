import React, { Component } from 'react'

import { Button } from 'antd';
import 'antd/dist/antd.css'

export default class App extends Component {
    render() {
        return (
            <div>
                <button>iambutton</button><br />
                <Button type="primary">Primary Button</Button> <br />
                <Button type="ghost">Ghost Button</Button> <br />
                <Button type="dash">Dash Button</Button> <br />
                <Button type="link">Link Button</Button> <br />
                <Button type="text">Text Button</Button> <br />
                <Button type="default">Default Button</Button> <br />


            </div>
        )
    }
}
