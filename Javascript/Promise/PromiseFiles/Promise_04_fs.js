/**
 * 封装一个函数 myReadFile 用于读取文件内容
 * params: path 文件路径
 * return: promise 文件对象
 */

const myReadFile = (path) => {
    return new Promise((resolve, reject) => {
        require('fs').readFile(path, (err, data) => {
            if (err) {
                reject(err);
            }
            resolve(data);
        });
    });
};

// ! 如此封装的好处是可以直接拿来用，自定义异常处理？

myReadFile("./TestingFiles//test_1.txt").then(value => {
    console.log(value.toString())
}, err => {
    console.log(err)
})