import React, { Component } from 'react'

import { Button } from 'antd';

import './App.less';
// import FetchWithClass from './Components/FetchWithClass';
// import AxiosWithClass from './Components/AxiosWithClass';
import GetData from './Components4/GetData';


// import 'antd/dist/antd.css'

export default class App extends Component {
    render() {
        return (
            <div>
                {/* <button>iambutton</button><br />
                <Button type="primary">Primary Button</Button> <br />
                <Button type="ghost">Ghost Button</Button> <br />
                <Button type="dash">Dash Button</Button> <br />
                <Button type="link">Link Button</Button> <br />
                <Button type="text">Text Button</Button> <br />
                <Button type="default">Default Button</Button> <br /> */}
                <GetData />
                <hr />
                {/* <FetchWithClass /> */}
                <hr />
                {/* <XHRwithClass /> */}
                {/* <AxiosWithClass /> */}
            </div>
        )
    }
}
