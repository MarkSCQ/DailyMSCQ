import React, { Component } from 'react'

class ReactEventHandle extends Component {
    // React.createRef() 调用后可以返回一个容器，该容器可以存储被ref表示的节点，该容器“专人专用”。只能存一个。多次反复存储会产生覆盖。
    myRef = React.createRef();
    // myRef2 = React.createRef();

    showData = () => {
        alert(this.myRef.current.value)
    }

    showData2 = (event) => {
        console.log(event.target.value)
    }

    render() {
        return (
            <div>
                {/* input is storeed in myRef */}
                <input ref={this.myRef} type="text" /> &nbsp;

                <button onClick={this.showData} >click</button> &nbsp;

                {/*  发生事件的元素和将要操作的DOM元素是同一个 ，可以不写ref*/}
                <input onBlur={this.showData2} type="text" />

            </div>
        )
    }
}

export default ReactEventHandle
