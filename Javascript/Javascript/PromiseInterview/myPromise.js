
        if (typeof computation === 'function') {
            setTimeout(() => {
                try {
                    computation(
                        this._onFulfilled.bind(this),
                        this._onRejected.bind(this)
                    )
                }
                catch (ex) {

                }
            })
        }

    }

    then(fulfilledFn, catchFn) {
        const controllPromise = new myPromise()
        this.then._thenQueue.push([controllPromise, fulfilledFn, catchFn])
    }
    catch() {
    }
    finally() {

    }
    _propagateFulfilled() {

    }

    _propagateRejected() {

    }

    _onFulfilled(value) {
        if (this._state === states.PENDING) {
            this._state = states.FULFILLED
            this._value = value
            this._propagateFulfilled()
        }
    }
    _onRejected(reason) {
        if (this._state === states.REJECTED)
            this._state = states.FULFILLED
        this.reason = reason
        this._propagateRejected()
    }
}