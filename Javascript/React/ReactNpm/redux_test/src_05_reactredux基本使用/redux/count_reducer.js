import { ADD, MINUS } from './constant'
// 该文件 创建一个为count服务的reducer  reducer 本质就是一个函数
// reducre 会接受到两个参数，一个是之前的状态prestate，一个是动作对象action



const initState = 0
// reducer只用于处理核心问题
function countReducer(preState = initState, action) {
    console.log("From Reducer ",preState, action)
    const { type, data } = action

    switch (type) {
        case ADD:
            return preState + data;
        case MINUS:
            return preState - data;

        default:
            return preState

    }
}

export default countReducer
