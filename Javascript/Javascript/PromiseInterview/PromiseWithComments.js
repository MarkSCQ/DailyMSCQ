// from https://www.youtube.com/watch?v=vAp0aNIVsXU&list=PL_Ykv8s0HisskfGeMXVudS_MtTtSrZM-V&index=79

// ! 定义三种状态
const states = {
    PENDING: "pending",
    FULFILLED: "fulfilled",
    REJECTED: "rejected"
}

// ! 判断当前的输入值 maybePromise 是不是一个Promise
// ! 因为只有promise才能够拥有then，且then为一个函数
const isThenable = (maybePromise) => {
    return maybePromise && typeof maybePromise.then === 'function'
}


class myPromise {
    constructor(computation) {
        // ! 初始化promise状态。
        this._state = states.PENDING

        this._value = undefined
        this._reason = undefined

        this._thenQueue = []
        this._finallyQueue = []

        if (typeof computation === 'function') {
            // ! 利用setTimeout实现异步
            setTimeout(() => {
                // ! 捕捉在初始化阶段 onResolved和onRejected两个函数的异常
                // ! 比如说我们可以throw new Error("...") 这里的trycatch就可以捕获这种异常
                try {
                    // ! 这里需要使用bind 因为在class中使用严格模式，this默认指向undefined。
                    // ! 利用bind让这两个函数指向当前的对象
                    computation(
                        this._onFulfilled.bind(this),
                        this._onRejected.bind(this)
                    )
                }
                catch (ex) {
                    this._onRejected(ex)
                }
            })
        }
    }

    _onFulfilled(value) {
        if (this._state === states.PENDING) {
            this._state = states.FULFILLED
            this._value = value
            this._propagateFulfilled()
        }
    }
    _onRejected(reason) {
        if (this._state === states.PENDING) {
            this._state = states.REJECTED
            this._reason = reason
            this._propagateRejected()
        }
    }

    // ! 两个static方法提供了原生Promise的 Promise.resolve()和Promise.reject()
    static resolve(value) {
        return new myPromise(resolve => resolve(value))
    }
    static reject(reason) {
        return new myPromise((_, reject) => reject(reason))
    }

    then(fulfilledFn, catchFn) {
        // ! 新建一个Promise
        const controlledPromise = new myPromise()

        // ! 将当前新建的promise和对应的fulfilledFn和catchFn入队
        this._thenQueue.push([controlledPromise, fulfilledFn, catchFn])

        // ! 因为当前的promise和对应的函数入队，判断上一级promise的状态。
        // ! 在propagate函数中对于当前的promise进行了赋值的处理
        // ! 所以在return中返回的不会是一个空的promise（除非上级promise的值是undefined）
        if (this._state === states.FULFILLED) {
            this._propagateFulfilled()
        }
        else if (this._state === states.REJECTED) {
            this._propagateRejected()
        }

        return controlledPromise
    }


    catch(catchFn) {
        // ! 在MDN中 关于catch有这样一段描述  
        // ! The catch() method returns a Promise and deals with rejected cases only. 
        // ! It behaves the same as calling Promise.prototype.then(undefined, onRejected)
        // ! catch 内部调用了 then
        return this.then(undefined, catchFn)
    }

    // ! finally中存在的function，从Promise中对于Finally的描述 Finally最终需要return一个上级promise
    // ! finally中提供一个callback，sideEffectFn 就是那个callback函数，如果不是pending，执行sideEffect
    // ! 
    finally(sideEffectFn) {
        if (this._state !== states.PENDING) {
            sideEffectFn()
            return this._state === states.PENDING ?
                myPromise.resolve(this._value) : myPromise.reject(this._reason)
        }
        // if the promise is still pending
        const controlledPromise = new myPromise()
        this._finallyQueue.push([controlledPromise, sideEffectFn])
        return controlledPromise
    }


    // logic with queue
    _propagateFulfilled() {
        // console.log("current thenqueue is ", this._thenQueue)
        // ! 解构当前的 thenqueue 中的每一个元素。这里的每一个元素，fulfilledFn处理controlledPromise
        this._thenQueue.forEach(([controlledPromise, fulfilledFn]) => {
            // ! 如果fulfilledFn是function 那么就直接处理
            if (typeof fulfilledFn === 'function') {
                // ! 但是要考虑到当前处理的promise结果 是否能够进行then的操作？
                // ! notice: 这里的fulfilledFn不是当前class中定义的 _onFulfilled
                // ! notice：这里的fulfilledFn 是一个函数，他是可以有返回值的
                const valueOrPromise = fulfilledFn(this._value)
                console.log(fulfilledFn)
                /** 
                 * * 举个例子
                 * * 比如说当前的fulfilledFn为 (value)=>{console.log(value)}
                 * * 这个function是没有返回值的 也就是说当前的这个valueOrPromise是个undefined
                 * * 既然是个undefined，那么他是绝不可能拥有then也就不是thenable
                 * * 但是如果当前的valueOrPromise是一个Promise对象，那么就可以进入这个isThenable
                 * * 因为Promise对象拥有then的方法
                 */
                console.log("current valueOrPromise", valueOrPromise)
                console.log("current isThenable", isThenable(valueOrPromise))
                // ? 如果这个valueOrPromise有then可以调用，那么直接进行处理。思考什么时候会有这种情况
                if (isThenable(valueOrPromise)) {
                    valueOrPromise.then(
                        value => controlledPromise._onFulfilled(value),
                        reason => controlledPromise._onRejected(reason))
                }
                else {
                    // ! 如果不能then，当前的 value 进行fulfilled处理
                    controlledPromise._onFulfilled(valueOrPromise)
                }
            }
            else {
                // ! 如果不是function 那么也就是说完成了所谓的值穿透，那么直接把上一级的promise的value往上怼就行了
                return controlledPromise._onFulfilled(this._value)
            }
        })
        // ! 如果finallyQueue中有元素，那么直接就运行。
        this._finallyQueue.forEach(([controlledPromise, sideEffectFn]) => {
            sideEffectFn()
            controlledPromise._onFulfilled(this._value)
        })
        this._finallyQueue = []
        this._thenQueue = []
    }

    _propagateRejected() {
        this._thenQueue.forEach(([controlledPromise, _, catchFn]) => {
            if (typeof catchFn === "function") {
                const valueOrPromise = catchFn(this._reason)
                if (isThenable(valueOrPromise)) {
                    valueOrPromise.then(
                        value => controlledPromise._onFulfilled(value),
                        reason => controlledPromise._onRejected(reason))
                }
                else {
                    controlledPromise._onFulfilled(valueOrPromise)
                }
            }
            else {
                return controlledPromise._onRejected(this._reason)
            }
        })

        this._finallyQueue.forEach(([controlledPromise, sideEffectFn]) => {
            sideEffectFn()
            controlledPromise._onRejected(this._reason)
        })
        this._finallyQueue = []

        this._thenQueue = []
    }


}

// MyPromise.js

// myPromise.deferred = function () {
//     var result = {};
//     result.promise = new MyPromise(function (resolve, reject) {
//         result.resolve = resolve;
//         result.reject = reject;
//     });

//     return result;
// }
// module.exports = myPromise;

// const p = new myPromise(
//     (resolve, reject) => {
//         setTimeout(() => {
//             resolve("resolve")
//             console.log(p._onFulfilled)

//         }, 1000);
//         // throw new Error("ERROR!")
//     })
//     // .catch(err => {
//     //     console.log("something went wrong", err)
//     //     return err
//     // })


// const ft = p.then(value => {
//     console.log("promise value is", value)
//     return value + 1
// })


// const ft1 = p.then(value => {
//     console.log("promise value is", value)
//     return value + 1
// })

