const time = (timer) => {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve()
        }, timer)
    })
}


const ajax1 = () => time(2000).then(() => {
    // console.log(1)
    return 1
})

const ajax2 = () => time(2000).then(() => {
    // console.log(2)
    return 2
})

const ajax3 = () => time(2000).then(() => {
    // console.log(3)
    return 3
})



function mergePromise(ajaxArr) {
    // process each ajax and put data in the array of promise and then return 
    const nums = []

    // ! using one resolved promise to wrap the nums content and return this promise object,
    // ! so that the promise in merge promise can using then chains to extract the data within
    let np = Promise.resolve()
    ajaxArr.forEach(element => {
        // ! the element cannot be used directly here. take a look at the ajax functions, 
        // ! its not a normal arrow function, it has a nested function that contains one promise called
        np = np.then(element).then(data => {
            nums.push(data)
            console.log(np)
            return nums
        })
    });

    return np
}


// function mergePromise(ajaxArray) {
//     // 存放每个ajax的结果
//     const data = [];
//     let promise = Promise.resolve();
//     ajaxArray.forEach(ajax => {
//         // 第一次的then为了用来调用ajax
//         // 第二次的then是为了获取ajax的结果
//         promise = promise.then(ajax).then(res => {
//             data.push(res);
//             return data; // 把每次的结果返回
//         })
//     })
//     // 最后得到的promise它的值就是data
//     return promise;
// }



// example of calling
// mergePromise([ajax1, ajax2, ajax3]).then(data => {
//     console.log("done");
//     console.log(data); // data 为 [1, 2, 3]
// });

console.log("object")

let res = mergePromise([ajax1, ajax2, ajax3]).then(data => {
    console.log("done");
    console.log(data); // data 为 [1, 2, 3]
});