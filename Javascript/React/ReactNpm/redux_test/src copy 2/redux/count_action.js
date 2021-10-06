import { ADD, MINUS } from './constants'

export const add = (value) => {
    return { type: ADD, data: value }
}


export const minus = (value) => {
    return { type: MINUS, data: value }
}

