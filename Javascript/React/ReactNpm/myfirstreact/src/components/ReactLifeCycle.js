import React, { Component } from 'react'
import ReactDOM from 'react-dom';

class ReactLifeCycle extends Component {

    state = { opacity: 1 }
    death = () => {
        const getdom = document.getElementById("test")
        console.log(getdom)
        ReactDOM.unmountComponentAtNode(document.getElementById("test"));
    }

    // 组件挂在完毕
    componentDidMount() {
        this.timer = setInterval(() => {
            let { opacity } = this.state

            opacity -= 0.1

            if (opacity <= 0) {
                opacity = 1
            }
            this.setState({ opacity })

        }, 200);
    }
    // 组件将要卸载
    componentWillUnmount() {
        clearInterval(this.timer)

    }
    render() {


        return (
            <div >
                <div>
                    <h2 id="test" style={{ opacity: this.state.opacity }} > 老子学不会</h2>
                </div>
                <button onClick={this.death}>嗝屁</button>
            </div>
        )
    }
}

export default ReactLifeCycle
