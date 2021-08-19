Promise.resolve()
    .then(() => {
        return new Promise(r => {
            setTimeout(() => {
                r(console.log(1))
            }, 1000)
        })
    })
    .then(() => {
        return new Promise(r => {
            setTimeout(() => {
                r(console.log(2))
            }, 1000)
        })
    })
    .then(() => {
        return new Promise(r => {
            setTimeout(() => {
                r(console.log(3))
            }, 1000)
        })
    })

