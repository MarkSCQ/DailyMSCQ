
const redLight = () => {
    console.log("RED")
}

const greenLight = () => {
    console.log("GREEN")
}


const yellowLight = () => {
    console.log("YELLOW")
}

const lightSettings = {
    red: {
        time: 3000,
        cb: redLight
    },
    green: {
        time: 2000,
        cb: greenLight
    },
    yellow: {
        time: 1000,
        cb: yellowLight
    },
}

// play traffic light

const playLight = (light) => {
    return new Promise(resolve => {
        setTimeout(() => {
            lightSettings[light].cb()
            resolve()
        }, lightSettings[light].time)
    }
    )
}

// make it a loop using promise
const loopTraffic = () => {

    // * why writing code in this way
    // * understanding and explanations
    // * 1. using promise and then chaining to simulate traffic lights
    // * 2. inside the then, why using return and why we need it? The reason is 
    // *    1) we need to use the changing of promise's state
    // *       because .then() will be fired when state is changed from pending to fulfilled or rejected 
    // *    2) normally when there is no return value, then() will return a undefined fulfilled promise. and then() will only be triggered when the state is changed
    //  *   3) if we implement a promise that changes its own state after some seconds, then the next then() can be triggerd by the changing of previous promise state.
    // *  3. in playLight function, the resolve is put inside the setTimeout function. When the function, playLight(), is called, a new promise containing setTimeout will be put in the marco task queue. Lets take a look at the first several steps. 
    // *     1) when the loopTraffic is being called, it will first put .then(()=>redlight) in to microtask queue. 
    // *     2) This microtask contain all the stuff below. Since the previous promise state has been changed, then we can enqueue this then redlight can call the return. 
    // *     3) The return, it will first make a new promise object, at this time the state of this to be returned promise is pending. since the current promise is pending, the next then() cannot be triggered and put into microtask queue. 
    // *     4) Now there is no tasks in micro task queue, but we have one marco task setTimeout in marcotask queue. Run the marco task settimeout, and after some seconds, the current promise state is changed from pending to fulfilled. Thus, the next then is able to be triggered.
    // *
    Promise.resolve()
        .then(() => {
            return playLight("red")
        })
        .then(() => {
            return playLight("yellow")
        })
        .then(() => {
            return playLight("green")
        })
        .then(() => {
            return loopTraffic()
        })
}


loopTraffic()









// ! based on ES6 ruanyifeng

// function Point(x, y) {
//     this.x = x;
//     this.y = y
// }

// Point.prototype.toString = function () {
//     return '(' + this.x + ',' + this.y + ')'
// }

// var p = new Point(1, 2)

// console.log(p)
// console.log(p.toString())
// console.log(p.getOwnPropertyNames(Point.prototype))



// Promise.resolve('ok')
//     .then(function onFulfilled(){return "off"},function onRejected(){return "oRJ"})
//     .then(res=>console.log(res));

// alert(console.log(3))
// new Promise((re,rj)=>{
//   rj("rej")
// })
// .then(value=>{console.log('success',value)},
//      value=>{console.log('failure',value)})
// .then(value=>{console.log('success',value)},
//      value=>{console.log('failure',value)})
// .catch(reason=>{console.log("fail", reason)})

// const arr = [1, 2, 3]
// arr.reduce((p, x) => {
//   return p.then(() => {
//     return new Promise(r => {
//       setTimeout(() => r(console.log(x)), 1000)
//     })
//   })
// }, Promise.resolve(console.log("new resolve")))


// Promise.resolve(console.log("this is resolve"))
//     .then(() => {
//         return new Promise(r => {
//             setTimeout(() => {
//                 r(
//                   console.log("1")
//                 )
//             }, 1000)
//         })
//     })
//     .then(() => {
//         return new Promise(r => {
//             setTimeout(() => {
//                 r(console.log(2))
//             }, 1000)
//         })
//     })
//     .then(() => {
//         return new Promise(r => {
//             setTimeout(() => {
//                 r(console.log(3))
//             }, 1000)
//         })
//     })

