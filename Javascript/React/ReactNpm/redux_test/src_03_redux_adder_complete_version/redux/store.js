// 该文件用于暴露store 整个应用只有一个store对象

// 用于创建store
import { createStore } from 'redux'

import countReducer from './count_reducer'



export default createStore(countReducer)





