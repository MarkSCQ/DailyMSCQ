import { ADD, MINUS } from './constant'


export const addCreator = (value) => {
    return {type:ADD,data:value}
}

export const minusCreator = (value) => {
    return {type:MINUS,data:value}
}

