import React, { Component } from 'react'

class RefCreateRef extends Component {
    // React.createRef() 调用后可以返回一个容器，该容器可以存储被ref表示的节点，该容器“专人专用”。只能存一个。多次反复存储会产生覆盖。
    myRef = React.createRef();
    myRef2 = React.createRef();

    showData = () => {
        // current is fixed current是固定的属性 不能更改
        // console.log(this.myRef.current.value)
        // const { input1 } = this
        alert(this.myRef.current.value)
    }
    showData2 = () => {
        // const { input2 } = this
        // alert(input2.value)
        alert(this.myRef.current.value)
    }

    render() {
        return (
            <div>
                {/* input is storeed in myRef */}
                <input ref={this.myRef} type="text" /> &nbsp;

                <button onClick={this.showData} >click</button> &nbsp;

                <input onBlur={this.showData2} ref={this.myRef2} type="text" />

            </div>
        )
    }
}

export default RefCreateRef
