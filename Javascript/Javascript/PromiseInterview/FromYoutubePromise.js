// from https://www.youtube.com/watch?v=vAp0aNIVsXU&list=PL_Ykv8s0HisskfGeMXVudS_MtTtSrZM-V&index=79


const states = {
    PENDING: "pending",
    FULFILLED: "fulfilled",
    REJECTED: "rejected"
}

const isThenable = maybePromise => { return maybePromise && typeof maybePromise.then === 'function ' }
class myPromise {
    constructor(computation) {
        this._state = states.PENDING

        this._value = undefined
        this._reason = undefined

        this._thenQueue = []
        this._finallyQueue = []

        if (typeof computation === 'function') {
            setTimeout(() => {
                try {
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

    static resolve(value) {
        return new myPromise(resolve => resolve(value))
    }
    static reject(reason) {
        return new myPromise((_, reject) => reject(reason))
    }

    then(fulfilledFn, catchFn) {
        const controlledPromise = new myPromise()
        this._thenQueue.push([controlledPromise, fulfilledFn, catchFn])

        if (this._state === states.FULFILLED) {
            this._propagateFulfilled()
        }
        else if (this._state === states.REJECTED) {
            this._propagateRejected()
        }
        return controlledPromise
    }


    catch(catchFn) {
        return this.then(undefined, catchFn)
    }


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
        this._thenQueue.forEach(([controlledPromise, fulfilledFn]) => {
            if (typeof fulfilledFn === 'function') {
                const valueOrPromise = fulfilledFn(this._value)
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
                return controlledPromise._onFulfilled(this._value)
            }
        })

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
}


const p = new myPromise(
    (resolve, reject) => {
        setTimeout(() => {
            resolve("reject")
        }, 1000);
        throw new Error("ERROR!")
    })
    .catch(err => {
        console.log("something went wrong", err)
        return err
    })


// const ft = p.then(value => {
//     console.log("promise value is", value)
//     return value + 1
// })


// const ft1 = p.then(value => {
//     console.log("promise value is", value)
//     return value + 1
// }) 

const fs = require('fs');
const path = require('path');

const readFile = (filename, encoding) => new LLJSPromise((resolve, reject) => {
    fs.readFile(filename, encoding, (err, value) => {
        if (err) {
            return reject(err);
        }
        resolve(value);
    })
});

const delay = (timeInMs, value) => new LLJSPromise(resolve => {
    setTimeout(() => {
        resolve(value);
    }, timeInMs);
});