const STATES = {
    PENDING: "pending",
    FULFILLED: "fulfilled",
    REJECTED: "rejected"
}

const isThenable = maybePromise => {
    return maybePromise && typeof maybePromise.then === "function"
}


class myPromise {

    constructor(executor) {
        // * initialize state and valuea
        this.state = STATES.PENDING
        this.value = undefined
        this.reason = undefined

        this.thenQueue = []
        this.finallyQueue = []

        if (typeof executor === 'function') {
            setTimeout(() => {
                try {
                    // * bind function to current class, cause this point to undefined when used in class 
                    executor(
                        this._onFulfilled.bind(this),
                        this._onRejected.bind(this)
                    )
                } catch (error) {
                    this._onRejected(error)
                }
            });
        }
    }

    _propagateFulfilleds() {
        // ! this might be needed for preprocessing the queues???
        if (this.thenQueue.length > 0) { }
        else { }
        if (this.finallyQueue.length > 0) { }
        else { }

        this.thenQueue.forEach(([controlledPromise, fulfilledFn]) => {
            if (typeof fulfilledFn === "function") {
                // * if fulfilledFn,
                // * which is the function that is about to process contrllledPromise is function then do ...
                const valueOrPromise = fulfilledFn(this.value)
                if (isThenable(valueOrPromise)) {
                    valueOrPromise.then(
                        resolveVal => this._onFulfilled(resolveVal),
                        rejectRea => this._onRejected(rejectRea)
                    )
                }
                else {
                    controlledPromise._onFulfilled(valueOrPromise)
                }
            }
            else {
                // * if the fulfilledFn is not a function then do ...
                return controlledPromise._onFulfilled(this.value)
            }
        })

        this.finallyQueue.forEach(([controlledPromise, sideEffect]) => {
            sideEffect()
            return controlledPromise._onFulfilled(this.value)
        })
        this.thenQueue = []
        this.finallyQueue = []
    }


    static resolve(value) {
        return new myPromise(resolveFn => resolveFn(value))
    }
    static reject(reason) {
        return new myPromise((_, rejectFn) => rejectFn(reason))
    }

    _propagateRejected() {
        this.thenQueue.forEach(([controlledPromise, _, catchFn]) => {
            if (typeof catchFn === "function") {
                const valueOrPromise = catchFn(this.reason)
                if (isThenable(valueOrPromise)) {
                    valueOrPromise.catch(catchFn)
                }
                else {
                    controlledPromise._onRejected(valueOrPromise)
                }
            }
            else {
                return controlledPromise._onRejected(this.reason)
            }
        })
        this.finallyQueue.forEach(([controlledPromise, sideEffect]) => {
            sideEffect()
            return controlledPromise._onRejected(this.value)
        })

        this.thenQueue = []
        this.finallyQueue = []
    }

    _onFulfilled(value) {
        if (this.state === STATES.PENDING) {
            this.state = STATES.FULFILLED
            this.value = value
            this._propagateFulfilleds()
        }
    }
    _onRejected(reason) {
        if (this.state === STATES.PENDING) {
            this.state = STATES.REJECTED
            this.reason = reason
            this._propagateRejected()
        }
    }

    then(fulfilledFn, catchFn) {
        const controlledPromise = new myPromise()

        this.thenQueue.push([controlledPromise, fulfilledFn, catchFn])

        if (this.state === STATES.FULFILLED) {
            this._propagateFulfilleds()
        }
        if (this.state === STATES.REJECTED) {
            this._propagateRejected()
        }

        return controlledPromise
    }

    catch(catchFn) {
        return this.then(undefined, catchFn)
    }

    finally(sideEffectFn) {
        // if not pending
        if (this.state !== STATES.PENDING) {
            sideEffectFn()
            return this.state === STATES.FULFILLED ?
                myPromise().resolve(this.value) : myPromise.reject(this.reason)
            // if pending return what it is
        }
        const controlledPromise = new myPromise()
        this.finallyQueue.push([controlledPromise, sideEffectFn])
        return controlledPromise
    }
}


/**
    0:00 Victory
    5:01 Unbreakable
    9:10 Heart of Courage
    11:07 Star Sky
    16:35 Bravestone
    19:44 Empire of Angels
    24:49 Never Back Down
    27:39 Blackheart
    32:03 Final Frontier (FT. Merethe Soltvedt)
    36:41 Freedom Fighters (Remix)
    39:05 El Dorado
    43:15 Stallion
    47:10 Skyworld
    50:17 For The Win
    52:23 Pegasus
    56:44 Starfall
    59:56 Cry
    1:03:52 Immortal
    1:07:48 United We Stand, Divided We Fall
    1:11:42 Archangel
    1:14:18 Riders
    1:17:34 Cannon in D Minor
    1:20:32 Skulls & Trombones
    1:24:30 Creation of Earth
    1:30:09 Blizzard
    1:32:56 Enchantress
    1:41:00 Breathe
    1:43:45 Undying Love
    1:46:34 The Fire In Her Eyes
    1:52:02 Emerald Princess (Avicii Tribute)
 */