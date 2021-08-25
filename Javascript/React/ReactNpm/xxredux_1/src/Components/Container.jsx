import { connect } from 'react-redux'


import {
    addAction,
    multiAction,
    minusAction,
    reminAction,
    resetAction
} from '../Actions/Action'


function Container(props) {
    const { num, add, multi, minus, remin, reset } = props
    console.log(num, add, multi, minus, remin, reset)
    return (
        <div>
        
            <div><h1>{num}</h1></div>
            <button onClick={() => { add(1) }}>
                ADD
            </button>

            <button onClick={() => { minus(2) }}>
                MINUS
            </button>

            <button onClick={() => { multi(3) }}>
                MULTI
            </button>

            <button onClick={() => { remin(2) }}>
                REMIN
            </button>

            <button onClick={() => { reset() }}>
                RESET
            </button>

        </div>
    )
}


const mapStateToProps = (state) => {
    return { num: state }
}
const mapDispatchToProps = (dispatch) => {
    return {
        add: (val) => dispatch(addAction(val)),
        multi: (val) => dispatch(multiAction(val)),
        minus: (val) => dispatch(minusAction(val)),
        remin: (val) => dispatch(reminAction(val)),
        reset: () => dispatch(resetAction())

    }
}


export default connect(mapStateToProps, mapDispatchToProps)(Container)