// https://www.youtube.com/watch?v=wtAP6REoWco
class Commitment {
    static PENDING = "PENDING"
    static FULFILLED = "FULFILLED"
    static REJECTED = "REJECTED"

    constructor(func) {

        this.status = Commitment.PENDING
        this.result = null
        this.resolveCallbacks = []
        this.rejectCallbacks = []
        // avoid this loss
        try {
            func(this.resolve.bind(this), this.reject.bind(this))
        }
        catch (e) {
            // 这里是直接执行而不是创建对象后再执行，所以这里不需要this binding
            this.reject(e)
        }
    }

    resolve(result) {
        setTimeout(() => {
            if (this.status === Commitment.PENDING) {
                this.status = Commitment.FULFILLED
                this.result = result
                this.resolveCallbacks.forEach(callbacks => { callbacks(result) })
            }
        })

    }
    reject(result) {
        setTimeout(() => {
            if (this.status === Commitment.PENDING) {
                this.status = Commitment.REJECTED
                this.result = result
                this.rejectCallbacks.forEach(callbacks => { callbacks(result) })

            }
        })

    }

    then(onFulfilled, onRejected) {
        return new Commitment((resolve, reject) => {
            // 如果 onFulfilled onRejected 是函数 那么就给他一个空函数，否则就把原来的东西给他
            onFulfilled = typeof onFulfilled === 'function' ? onFulfilled : () => { }
            onRejected = typeof onRejected === 'function' ? onRejected : () => { }

            if (this.status === Commitment.PENDING) {
                this.resolveCallbacks.push(onFulfilled)
                this.rejectCallbacks.push(onRejected)
            }
            if (this.status === Commitment.FULFILLED) {
                setTimeout(() => {
                    onFulfilled(this.result)
                })
            }
            if (this.status === Commitment.REJECTED) {
                setTimeout(() => {
                    onRejected(this.result)
                })
            }
        })
    }
}

let pro = new Commitment((resolve, reject) => {
    resolve("NEXT TIME"),
    reject("123")
}).then(
    result => {
        console.log(result)
    },
    result => {
        console.log(result)
    })