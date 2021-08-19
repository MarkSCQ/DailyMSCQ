
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
	return new Promise(resolve=> {  
    setTimeout(() => {
			 lightSettings[light].cb()
       resolve()
    },lightSettings[light].time)
  }
  )
}

// make it a loop using promise


const loopTraffic = () => {
    // we do not care the resolve value
    Promise.resolve().then(() => {
      return playLight("red")
    })
    .then(() => {
     return playLight("yellow")
    })
    .then(() => {
     return playLight("green")
    })
  	.then(()=>{
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

