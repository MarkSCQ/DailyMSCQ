console.log("2333")

/**
 * data type
 * undefined, null, bollean, string, symbol, number, object
 * 
 */

// global 
var name = "123";
// within a scope where you declare it
let muname = "1233";
// constant cannot be changed
const na = "1230";

// javascript Capitalization sensitive


// objects

var dog={
    "name":"as",
    "legs":4,
    "friend":2
};

// add new key and value
dog.gg = "gga"
console.log(dog.name)
console.log(dog["friend"])
console.log(dog)

delete dog.gg
console.log(dog)

// ! JSON.parse()
// ! The JSON.parse() method parses a JSON string, constructing the JavaScript value or object described by the string. An optional reviver function can be provided to perform a transformation on the resulting object before it is returned.
// ! JSON.stringify()
// ! The JSON.stringify() method converts a JavaScript object or value to a JSON string, optionally replacing values if a replacer function is specified or optionally including only the specified properties if a replacer array is specified.

// import {function name} from './jscrashcourse.js'
// export in one file so you can import them in another file
// export 决定对外暴露的是什么，因为如果一旦引入文件 或模块 所有的都会被引入。export使用来限制引入模块的内容