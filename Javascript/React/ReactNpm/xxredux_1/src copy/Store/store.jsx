import { applyMiddleware, createStore } from 'redux'
import thunk from 'redux-thunk'

import math from '../Reducers/math'


// ! thunk 对于一部任务的解决方法
export default createStore(math, applyMiddleware(thunk))


