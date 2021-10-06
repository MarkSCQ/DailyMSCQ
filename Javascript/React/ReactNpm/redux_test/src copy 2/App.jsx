// 所有组件的外壳组件

import React, { Component } from 'react'

import CountUI from './container/Count'


export default class App extends Component {
  render() {
    return (
      <div>
        <CountUI />
      </div>
    )
  }
}
