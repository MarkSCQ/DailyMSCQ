const arr = [1, 2, 3, 4, 5]

arr.reduce((proObj, currVal) => {
    return proObj.then(() => {
        return new Promise(resolve => {
            setTimeout(() => { resolve(console.log(currVal)) }, 1000)
        })
    })

}, Promise.resolve())