## SECTION 1

```js
var a = 10;
function foo() {
  console.log(this.a);
}
foo();
```

```js
"use strict";
var a = 10;
function foo() {
  console.log("this1", this);
  console.log(window.a);
  console.log(this.a);
}
console.log(window.foo);
console.log("this2", this);
foo();
```

```js
let a = 10;
const b = 20;

function foo() {
  console.log(this.a);
  console.log(this.b);
}
foo();
console.log(window.a);
```

```js
var a = 1;
function foo() {
  var a = 2;
  console.log(this);
  console.log(this.a);
}

foo();
```

```js
var a = 1;
function foo() {
  var a = 2;
  function inner() {
    console.log(this.a);
  }
  inner();
}

foo();
```

## SECTION 2

```js
function foo() {
  console.log(this.a);
}
var obj = { a: 1, foo };
var a = 2;
obj.foo();
```

## SECTION 3

```js
function foo() {
  console.log(this.a);
}
var obj = { a: 1, foo };
var a = 2;
var foo2 = obj.foo;

obj.foo();
foo2();
```

```js
function foo() {
  console.log(this.a);
}
var obj = { a: 1, foo };
var a = 2;
var foo2 = obj.foo;
var obj2 = { a: 3, foo2: obj.foo };

obj.foo();
foo2();
obj2.foo2();
```

```js
function foo() {
  console.log(this.a);
}
function doFoo(fn) {
  console.log(this);
  fn();
}
var obj = { a: 1, foo };
var a = 2;
doFoo(obj.foo);
```

```js
function foo() {
  console.log(this.a);
}
function doFoo(fn) {
  console.log(this);
  fn();
}
var obj = { a: 1, foo };
var a = 2;
var obj2 = { a: 3, doFoo };

obj2.doFoo(obj.foo);
```

## SECTION 4

```js
function foo() {
  console.log(this.a);
}
var obj = { a: 1 };
var a = 2;

foo();
foo.call(obj);
foo.apply(obj);
foo.bind(obj);
```

```js
var obj1 = {
  a: 1,
};
var obj2 = {
  a: 2,
  foo1: function () {
    console.log(this.a);
  },
  foo2: function () {
    setTimeout(function () {
      console.log(this);
      console.log(this.a);
    }, 0);
  },
};
var a = 3;

obj2.foo1();
obj2.foo2();
```

```js
var obj1 = {
  a: 1,
};
var obj2 = {
  a: 2,
  foo1: function () {
    console.log(this.a);
  },
  foo2: function () {
    setTimeout(
      function () {
        console.log(this);
        console.log(this.a);
      }.call(obj1),
      0
    );
  },
};
var a = 3;
obj2.foo1();
obj2.foo2();
```

```js
var obj1 = {
  a: 1,
};
var obj2 = {
  a: 2,
  foo1: function () {
    console.log(this.a);
  },
  foo2: function () {
    function inner() {
      console.log(this);
      console.log(this.a);
    }
    inner();
  },
};
var a = 3;
obj2.foo1();
obj2.foo2();
```

```js
function foo() {
  console.log(this.a);
}
var obj = { a: 1 };
var a = 2;

foo();
foo.call(obj);
foo().call(obj);
```

```js
function foo() {
  console.log(this.a);
  return function () {
    console.log(this.a);
  };
}
var obj = { a: 1 };
var a = 2;

foo();
foo.call(obj);
foo().call(obj);
```

```js
function foo() {
  console.log(this.a);
  return function () {
    console.log(this.a);
  };
}
var obj = { a: 1 };
var a = 2;

foo();
foo.bind(obj);
foo().bind(obj);
```

```js
function foo() {
  console.log(this.a);
  return function () {
    console.log(this.a);
  };
}
var obj = { a: 1 };
var a = 2;

foo.call(obj)();
```

```js
var obj = {
  a: "obj",
  foo: function () {
    console.log("foo:", this.a);
    return function () {
      console.log("inner:", this.a);
    };
  },
};
var a = "window";
var obj2 = { a: "obj2" };

obj.foo()();
obj.foo.call(obj2)();
obj.foo().call(obj2);
```

```js
var obj = {
  a: 1,
  foo: function (b) {
    b = b || this.a;
    return function (c) {
      console.log(this.a + b + c);
    };
  },
};
var a = 2;
var obj2 = { a: 3 };

obj.foo(a).call(obj2, 1);
obj.foo.call(obj2)(1);
```

## SECTION 5

```js
function foo1() {
  console.log(this.a);
}
var a = 1;
var obj = {
  a: 2,
};

var foo2 = function () {
  foo1.call(obj);
};

foo2();
foo2.call(window);
```

```js
function foo1(b) {
  console.log(`${this.a} + ${b}`);
  return this.a + b;
}
var a = 1;
var obj = {
  a: 2,
};

var foo2 = function () {
  return foo1.call(obj, ...arguments);
};

var num = foo2(3);
console.log(num);
```

```js
function foo(item) {
  console.log(item, this.a);
}
var obj = {
  a: "obj",
};
var a = "window";
var arr = [1, 2, 3];

// arr.forEach(foo, obj)
// arr.map(foo, obj)
arr.filter(function (i) {
  console.log(i, this.a);
  return i > 2;
}, obj);
```

## SECTION 6

```js
function Person(name) {
  this.name = name;
}
var name = "window";
var person1 = new Person("LinDaiDai");
console.log(person1.name);
```

```js
function Person(name) {
  this.name = name;
  this.foo1 = function () {
    console.log(this.name);
  };
  this.foo2 = function () {
    return function () {
      console.log(this.name);
    };
  };
}
var person1 = new Person("person1");
person1.foo1();
person1.foo2()();
```

```js
var name = "window";
function Person(name) {
  this.name = name;
  this.foo = function () {
    console.log(this.name);
    return function () {
      console.log(this.name);
    };
  };
}
var person2 = {
  name: "person2",
  foo: function () {
    console.log(this.name);
    return function () {
      console.log(this.name);
    };
  },
};

var person1 = new Person("person1");
person1.foo()();
person2.foo()();
```

```js
var name = "window";
function Person(name) {
  this.name = name;
  this.foo = function () {
    console.log(this.name);
    return function () {
      console.log(this.name);
    };
  };
}
var person1 = new Person("person1");
var person2 = new Person("person2");

person1.foo.call(person2)();
person1.foo().call(person2);
```

## SECTION 7

```js
var obj = {
  name: "obj",
  foo1: () => {
    console.log(this.name);
  },
  foo2: function () {
    console.log(this.name);
    return () => {
      console.log(this.name);
    };
  },
};
var name = "window";
obj.foo1();
obj.foo2()();
```

```js
var name = "window";
var obj1 = {
  name: "obj1",
  foo: function () {
    console.log(this.name);
  },
};

var obj2 = {
  name: "obj2",
  foo: () => {
    console.log(this.name);
  },
};

obj1.foo();
obj2.foo();
```

```js
var name = "window";
var obj1 = {
  name: "obj1",
  foo: function () {
    console.log(this.name);
    return function () {
      console.log(this.name);
    };
  },
};
var obj2 = {
  name: "obj2",
  foo: function () {
    console.log(this.name);
    return () => {
      console.log(this.name);
    };
  },
};
var obj3 = {
  name: "obj3",
  foo: () => {
    console.log(this.name);
    return function () {
      console.log(this.name);
    };
  },
};
var obj4 = {
  name: "obj4",
  foo: () => {
    console.log(this.name);
    return () => {
      console.log(this.name);
    };
  },
};

obj1.foo()();
obj2.foo()();
obj3.foo()();
obj4.foo()();
```

```js
var name = "window";
function Person(name) {
  this.name = name;
  this.foo1 = function () {
    console.log(this.name);
  };
  this.foo2 = () => {
    console.log(this.name);
  };
}
var person2 = {
  name: "person2",
  foo2: () => {
    console.log(this.name);
  },
};
var person1 = new Person("person1");
person1.foo1();
person1.foo2();
person2.foo2();
```

```js
var name = "window";
function Person(name) {
  this.name = name;
  this.foo1 = function () {
    console.log(this.name);
    return function () {
      console.log(this.name);
    };
  };
  this.foo2 = function () {
    console.log(this.name);
    return () => {
      console.log(this.name);
    };
  };
  this.foo3 = () => {
    console.log(this.name);
    return function () {
      console.log(this.name);
    };
  };
  this.foo4 = () => {
    console.log(this.name);
    return () => {
      console.log(this.name);
    };
  };
}
var person1 = new Person("person1");
person1.foo1()();
person1.foo2()();
person1.foo3()();
person1.foo4()();
```

```js
var name = "window";
var obj1 = {
  name: "obj1",
  foo1: function () {
    console.log(this.name);
    return () => {
      console.log(this.name);
    };
  },
  foo2: () => {
    console.log(this.name);
    return function () {
      console.log(this.name);
    };
  },
};
var obj2 = {
  name: "obj2",
};
obj1.foo1.call(obj2)();
obj1.foo1().call(obj2);
obj1.foo2.call(obj2)();
obj1.foo2().call(obj2);
```

## SECTION 8

```js
var name = "window";
var person1 = {
  name: "person1",
  foo1: function () {
    console.log(this.name);
  },
  foo2: () => console.log(this.name),
  foo3: function () {
    return function () {
      console.log(this.name);
    };
  },
  foo4: function () {
    return () => {
      console.log(this.name);
    };
  },
};
var person2 = { name: "person2" };

person1.foo1();
person1.foo1.call(person2);

person1.foo2();
person1.foo2.call(person2);

person1.foo3()();
person1.foo3.call(person2)();
person1.foo3().call(person2);

person1.foo4()();
person1.foo4.call(person2)();
person1.foo4().call(person2);
```

```js
var name = "window";
function Person(name) {
  this.name = name;
  (this.foo1 = function () {
    console.log(this.name);
  }),
    (this.foo2 = () => console.log(this.name)),
    (this.foo3 = function () {
      return function () {
        console.log(this.name);
      };
    }),
    (this.foo4 = function () {
      return () => {
        console.log(this.name);
      };
    });
}
var person1 = new Person("person1");
var person2 = new Person("person2");

person1.foo1();
person1.foo1.call(person2);

person1.foo2();
person1.foo2.call(person2);

person1.foo3()();
person1.foo3.call(person2)();
person1.foo3().call(person2);

person1.foo4()();
person1.foo4.call(person2)();
person1.foo4().call(person2);
```

```js
var name = "window";
function Person(name) {
  this.name = name;
  this.obj = {
    name: "obj",
    foo1: function () {
      return function () {
        console.log(this.name);
      };
    },
    foo2: function () {
      return () => {
        console.log(this.name);
      };
    },
  };
}
var person1 = new Person("person1");
var person2 = new Person("person2");

person1.obj.foo1()();
person1.obj.foo1.call(person2)();
person1.obj.foo1().call(person2);

person1.obj.foo2()();
person1.obj.foo2.call(person2)();
person1.obj.foo2().call(person2);
```

```js
function foo() {
  console.log(this.a);
}
var a = 2;
(function () {
  "use strict";
  foo();
})();
```

## SECTION 9

```js
手写一个new实现;
function Person(name) {
  this.name = name;
}
Person.prototype.eat = function () {
  console.log("Eatting");
};
var lindaidai = new Person("LinDaiDai");
console.log(lindaidai);
lindaidai.eat();

function create() {
  // 1. 获取构造函数，并且删除 arguments 中的第一项
  var Con = [].shift.call(arguments);
  // 2. 创建一个空的对象并链接到构造函数的原型，使它能访问原型中的属性
  var obj = Object.create(Con.prototype);
  // 3. 使用apply改变构造函数中this的指向实现继承，使obj能访问到构造函数中的属性
  var ret = Con.apply(obj, arguments);
  // 4. 优先返回构造函数返回的对象
  return ret instanceof Object ? ret : obj;
}

// 1.有返回值且为对象
function Person(name, sex) {
  this.name = name;
  return {
    sex: sex,
  };
}
// 2. 没有返回值
function Person(name) {
  this.name = name;
}
// 3. 返回值为基本类型
function Person(name) {
  this.name = name;
  return "str";
}

function Person(name) {
  this.name = name;
}
Person.prototype.eat = function () {
  console.log("Eatting");
};
function create() {
  // 1. 获取构造函数，并且删除 arguments 中的第一项
  var Con = [].shift.call(arguments);
  // 2. 创建一个空的对象并链接到构造函数的原型，使它能访问原型中的属性
  var obj = Object.create(Con.prototype);
  // 3. 使用apply改变构造函数中this的指向实现继承，使obj能访问到构造函数中的属性
  var ret = Con.apply(obj, arguments);
  // 4. 优先返回构造函数返回的对象
  return ret instanceof Object ? ret : obj;
}
var lindaidai = create(Person, "LinDaiDai");
console.log(lindaidai); // Person{ name: 'LinDaiDai' }
lindaidai.eat(); // 'Eatting'
```

```js
手写一个call函数实现;

Function.prototype.call3 = function (context) {
  context =
    context !== null && context !== undefined ? Object(context) : window;
  var fn = Symbol();
  context[fn] = this;

  let args = [...arguments].slice(1);
  let result = context[fn](...args);

  delete context[fn];
  return result;
};
function fnFactory(context) {
  var unique_fn = "fn";
  while (context.hasOwnProperty(unique_fn)) {
    unique_fn = "fn" + Math.random();
  }
  return unique_fn;
}
Function.prototype.call2 = function (context) {
  // 1. 若是传入的context是null或者undefined时指向window;
  // 2. 若是传入的是原始数据类型, 原生的call会调用 Object() 转换
  context =
    context !== null && context !== undefined ? Object(context) : window;
  // 3. 创建一个独一无二的fn函数的命名
  var fn = fnFactory(context);
  // 4. 这里的this就是指调用call的那个函数
  // 5. 将调用的这个函数赋值到context中, 这样之后执行context.fn的时候, fn里的this就是指向context了
  context[fn] = this;
  // 6. 定义一个数组用于放arguments的每一项的字符串: ['agruments[1]', 'arguments[2]']
  var args = [];
  // 7. 要从第1项开始, 第0项是context
  for (var i = 1, l = arguments.length; i < l; i++) {
    args.push("arguments[" + i + "]");
  }
  // 8. 使用eval()来执行fn并将args一个个传递进去
  var result = eval("context[fn](" + args + ")");
  // 9. 给context额外附件了一个属性fn, 所以用完之后需要删除
  delete context[fn];
  // 10. 函数fn可能会有返回值, 需要将其返回
  return result;
};
var obj = {
  name: "objName",
};

function consoleInfo(sex, weight) {
  console.log(this.name, sex, weight);
}
var name = "globalName";
consoleInfo.call2(obj, "man", 100); // 'objName' 'man' 100
consoleInfo.call3(obj, "woman", 120); // 'objName' 'woman' 120
```

```js
手写一个apply实现;
Function.prototype.apply3 = function (context, arr) {
  context = context ? Object(context) : window;
  let fn = Symbol();
  context[fn] = this;

  let result = arr ? context[fn](...arr) : context[fn]();
  delete context[fn];
  return result;
};

function fnFactory(context) {
  var unique_fn = "fn";
  while (context.hasOwnProperty(unique_fn)) {
    unique_fn = "fn" + Math.random();
  }
  return unique_fn;
}
Function.prototype.apply2 = function (context, arr) {
  // 1. 若是传入的context是null或者undefined时指向window;
  // 2. 若是传入的是原始数据类型, 原生的call会调用 Object() 转换
  context = context ? Object(context) : window;
  // 3. 创建一个独一无二的fn函数的命名
  var fn = fnFactory(context);
  // 4. 这里的this就是指调用call的那个函数
  // 5. 将调用的这个函数赋值到context中, 这样之后执行context.fn的时候, fn里的this就是指向context了
  context[fn] = this;

  var result;
  // 6. 判断有没有第二个参数
  if (!arr) {
    result = context[fn]();
  } else {
    // 7. 有的话则用args放每一项的字符串: ['arr[0]', 'arr[1]']
    var args = [];
    for (var i = 0, len = arr.length; i < len; i++) {
      args.push("arr[" + i + "]");
    }
    // 8. 使用eval()来执行fn并将args一个个传递进去
    result = eval("context[fn](" + args + ")");
  }
  // 9. 给context额外附件了一个属性fn, 所以用完之后需要删除
  delete context[fn];
  // 10. 函数fn可能会有返回值, 需要将其返回
  return result;
};
```

```js
手写一个bind函数实现;
函数内的this表示的就是调用的函数;
可以将上下文传递进去, 并修改this的指向;
返回一个函数;
可以传入参数;
柯里化;
一个绑定的函数也能使用new操作法创建对象, 且提供的this会被忽略;

Function.prototype.bind2 = function (context) {
  if (typeof this !== "function") {
    throw new Error(
      "Function.prototype.bind - what is trying to be bound is not callable"
    );
  }
  var self = this;
  var args = Array.prototype.slice.call(arguments, 1);

  var fBound = function () {
    var innerArgs = Array.prototype.slice.call(arguments);
    return self.apply(
      this instanceof fNOP ? this : context,
      args.concat(innerArgs)
    );
  };

  var fNOP = function () {};
  fNOP.prototype = this.prototype;
  fBound.prototype = new fNOP();
  return fBound;
};

Function.prototype.bind2 = function (context) {
  // 1. 判断调用bind的是不是一个函数
  if (typeof this !== "function") {
    throw new Error(
      "Function.prototype.bind - what is trying to be bound is not callable"
    );
  }
  // 2. 外层的this指向调用者(也就是调用的函数)
  var self = this;
  // 3. 收集调用bind时的其它参数
  var args = Array.prototype.slice.call(arguments, 1);

  // 4. 创建一个返回的函数
  var fBound = function () {
    // 6. 收集调用新的函数时传入的其它参数
    var innerArgs = Array.prototype.slice.call(arguments);
    // 7. 使用apply改变调用函数时this的指向
    // 作为构造函数调用时this表示的是新产生的对象, 不作为构造函数用的时候传递context
    return self.apply(
      this instanceof fNOP ? this : context,
      args.concat(innerArgs)
    );
  };
  // 5. 创建一个空的函数, 且将原型指向调用者的原型(为了能用调用者原型中的属性)
  // 下面三步的作用有点类似于 fBoun.prototype = this.prototype 但有区别
  var fNOP = function () {};
  fNOP.prototype = this.prototype;
  fBound.prototype = new fNOP();
  // 8. 返回最后的结果
  return fBound;
};
```
