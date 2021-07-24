

const fs = require("fs");
const { resolve } = require("path");


// fs.readFile("./TestingFiles/test_1.txt", (err, data) => {
//     if (err)
//         throw err;

//     console.log(data.toString())
// })

// Promise的形式


let datacollector;
let promise_ = new Promise((resolve, reject) => {
    fs.readFile("./TestingFiles/test_1.txt", (err, data) => {
        if (err) {
            reject(err)
        }
        resolve(data)

    })
})

promise_.then((value) => {
    console.log(value.toString())

},
    (err) => {
        console.log(err.toString())
    }
)