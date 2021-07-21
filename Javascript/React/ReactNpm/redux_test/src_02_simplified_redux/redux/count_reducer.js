// 该文件 创建一个为count服务的reducer  reducer 本质就是一个函数
// reducre 会接受到两个参数，一个是之前的状态prestate，一个是动作对象action



const initState = 0
// reducer只用于处理核心问题
function countReducer(preState = initState, action) {
    console.log(preState, action)
    const { type, data } = action

    switch (type) {
        case "add":
            return preState + data;
        case "minus":
            return preState - data;

        default:
            return preState

    }
}

export default countReducer
