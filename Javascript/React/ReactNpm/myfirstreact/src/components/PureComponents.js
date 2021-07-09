import React, { PureComponent } from 'react'

class PureComponents extends PureComponent {

    render() {
        console.log("pure rerender")

        return (
            <div>
                PureComponent  s
            </div>
        )
    }
}

export default PureComponents
