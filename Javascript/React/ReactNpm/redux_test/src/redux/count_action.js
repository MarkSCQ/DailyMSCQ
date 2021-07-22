import { ADD, MINUS } from './constant'
import store from './store'
// 该文件专门为count组件生成action对象


export const creatorAddition = (data) => {
    return { type: ADD, data: data }
}
// 另一种写箭头函数+返回值的方式
// 因为只有一个参数，data外的括号去掉，因为只想要返回一个object，利用括号包着object的形式可以代替return。不过个人觉得这种写法可读性太差。当然，大佬们随意发挥吧。2333
// export default const creatorAddition = data => ({ type: "add", data: data })

export const creatorMinus = (data) => {
    return { type: MINUS, data: data }
}


// 异步action，就是指action的值为函数，异步action中一般都会调用同步action
// 异步action，不是必须要用
export const creatorAdditionAsync = (data, time) => {
    setTimeout(() => {
        // ! 另一种写法 store.dispatch(creatorAddition(data)) 
        store.dispatch({ type: ADD, data: data })

    }, time);
}