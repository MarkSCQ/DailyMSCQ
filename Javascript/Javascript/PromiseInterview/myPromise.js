// based on https://juejin.cn/post/6844903607968481287#heading-9

const STATE = {
    PENDING: "pending",
    FULFILLED: "fulfilled",
    REJECTED: "rejected"
}

// if promise is not undefind or null and the promise then is a function
const isThen = (promise) => { return typeof promise.then === "function" && promise }

class myPromise {
    constructor(executor) {
        this.state = STATE.PENDING
        this.value = undefined

        this.callbacks = []
        // ! 在运行时是否会出错
        try {
            executor(this.resolve.bind(this), this.reject.bind(this))
        }
        catch (ex) {
            // console.log(ex)
            this.reject(ex)
        }
    }

    resolve(value) {
        // ! 根据promise定义 只有pending才可以跳转到别的状态
        if (this.state === STATE.PENDING) {
            this.state = STATE.FULFILLED
            this.value = value
            // ! 满足异步特性
            setTimeout(() => {
                this.callbacks.map(callback => {
                    callback.onFulfilled(this.value)
                })
            });

        }

    }
    reject(reason) {
        // ! 根据promise定义 只有pending才可以跳转到别的状态
        if (this.state === STATE.PENDING) {
            this.state = STATE.REJECTED
            this.reason = reason
            // ! 满足异步特性
            setTimeout(() => {
                this.callbacks.map(callback => {
                    callback.onRejected(this.reason)
                })
            });

        }
    }

    then(onFulfilled, onRejected) {

        // ! onFulfilled onRejected是否是函数？
        // ! 在Promise中定义如果不为函数，则会继承上一个then中返回的promise的值

        if (typeof onFulfilled !== 'function') {
            onFulfilled = () => {
            }
        }

        if (typeof onRejected !== 'function') {
            onRejected = () => {
            }
        }

        if (this.state === STATE.PENDING) {
            this.callbacks.push({
                onFulfilled: value => {
                    try {
                        onFulfilled(value)
                    } catch (error) {
                        onRejected(error)

                    }
                },
                onRejected: reason => {
                    try {
                        onRejected(reason)
                    } catch (error) {
                        onRejected(error)
                    }
                }
            })
        }

        // 如果当前是 fulfilled 状态
        if (this.state === STATE.FULFILLED) {
            setTimeout(() => {
                try {
                    onFulfilled(this.value)
                }
                catch (error) {
                    onRejected(error)
                }
            })

        }
        // 如果当前是 rejected 状态
        if (this.state === STATE.REJECTED) {
            setTimeout(() => {
                try {
                    onRejected(this.reason)
                }
                catch (error) {
                    onRejected(error)
                }
            })

        }
    }
}
