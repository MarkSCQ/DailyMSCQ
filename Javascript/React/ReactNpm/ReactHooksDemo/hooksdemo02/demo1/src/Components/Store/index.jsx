import { createStore } from 'redux'

import Reducer from '../Reducer'

export default createStore(Reducer,
    window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__())