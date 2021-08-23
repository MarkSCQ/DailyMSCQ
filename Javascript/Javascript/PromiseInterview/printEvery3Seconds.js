function printPromise(func, content) {
    // console.log(content)
    return new Promise(resolve => {
        setTimeout(() => {
            func(content)
            resolve()
        }, 3000)
    })
}


function repeat(func, times, wait) {
    return (content) => {
        Promise.resolve()
            .then(() => {
                return printPromise(func, content)
            })
            .then(() => {
                return printPromise(func, content)
            })
            .then(() => {
                return printPromise(func, content)
            })
            .then(() => {
                return printPromise(func, content)
            })
    }
}


function repeat_1(func, times, wait) {
    return (content) => {
        for (let i = 1; i <= times; i++) {
            setTimeout(() => {
                console.log(i)
                // func.apply(null, [content])
                func.call(null, content)
            }, i * wait)
        }
    }
}