import React, { Component } from 'react'

import Todo from './Todo'
import Userdata from './Userdata'
export default class App extends Component {
  render() {
    return (
      <div>
        <Todo />
        <Userdata />

      </div>
    )
  }
}
