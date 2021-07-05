import React, { Component } from 'react'
import ChildComponent from './ChildComponent'
class ParentComponent extends Component {
    constructor(props) {
        super(props)
        this.state = {
            parentName: "parent"
        }
        this.greetparent = this.greetparent.bind(this)

    }
    greetparent(kid) {
        alert(`sssdfs ${this.state.parentName} and ${kid}`)
    }
    render() {
        return (
            <div>
                <ChildComponent greetHandler={this.greetparent} />
            </div>
        )
    }
}

export default ParentComponent
