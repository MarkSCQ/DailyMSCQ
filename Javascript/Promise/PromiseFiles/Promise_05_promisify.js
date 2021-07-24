/**
 * util.promisify
 */

// 将回调函数风格 转换成Promise风格

const util = require('util')
const fs = require('fs')

let myReadFile = util.promisify(fs.readFile);

myReadFile('./TestingFiles/test_1.txt').then((value) => {
    console.log(value.toString())
},
    (err) => {
        console.log(err)
    }
)