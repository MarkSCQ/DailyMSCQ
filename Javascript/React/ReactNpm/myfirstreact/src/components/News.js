import React, { Component } from 'react'
import './NewsCSS.css'
class News extends Component {

    constructor(props) {
        super(props)

        this.state = {
            newsArr: []
        }
        this.listRef = React.createRef()

    }




    componentDidMount() {
        setInterval(() => {
            const { newsArr } = this.state
            const news = 'NEWS ' + (newsArr.length + 1)

            this.setState({ newsArr: [news, ...newsArr] })
        }, 1000)
    }
    getSnapshotBeforeUpdate() {
        return this.listRef.scrollHeight
    }
    componentDidUpdate(preProps, preState, snapshotValue) {
        this.listRef.scrollTop += this.listRef.scrollHeight + snapshotValue
    }
    render() {
        return (
            <div>
                <div className="list" ref={this.listRef}>
                    {
                        this.state.newsArr.map((n, index) => {
                            return <div className="news" key={index}>{n}</div>
                        })
                    }
                    {/* <div className="news">NEW 7</div>
                    <div className="news ">NEW 6</div>
                    <div className="news">NEW 5</div>
                    <div className="news">NEW 4</div>
                    <div className="news">NEW 3</div>
                    <div className="news">NEW 2</div>
                    <div className="news">NEW 1</div> */}
                </div>
            </div>
        )
    }
}

export default News
