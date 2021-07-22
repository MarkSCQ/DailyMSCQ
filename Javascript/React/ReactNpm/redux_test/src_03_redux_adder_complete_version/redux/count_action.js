import { ADD, MINUS } from './constant'

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
