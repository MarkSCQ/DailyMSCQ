// 所有组件的外壳组件

import React, { Component } from 'react'

import store from './redux/store'

import Count from './containers/Count'


export default class App extends Component {
  render() {
    return (
      <div>
        {/* 渲染容器组件，给容器组件传递store */}

        <Count />
      </div>
    )
  }
}
