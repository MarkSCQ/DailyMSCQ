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
????????????new??????;
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
  // 1. ????????????????????????????????? arguments ???????????????
  var Con = [].shift.call(arguments);
  // 2. ?????????????????????????????????????????????????????????????????????????????????????????????
  var obj = Object.create(Con.prototype);
  // 3. ??????apply?????????????????????this???????????????????????????obj????????????????????????????????????
  var ret = Con.apply(obj, arguments);
  // 4. ???????????????????????????????????????
  return ret instanceof Object ? ret : obj;
}

// 1.????????????????????????
function Person(name, sex) {
  this.name = name;
  return {
    sex: sex,
  };
}
// 2. ???????????????
function Person(name) {
  this.name = name;
}
// 3. ????????????????????????
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
  // 1. ????????????????????????????????? arguments ???????????????
  var Con = [].shift.call(arguments);
  // 2. ?????????????????????????????????????????????????????????????????????????????????????????????
  var obj = Object.create(Con.prototype);
  // 3. ??????apply?????????????????????this???????????????????????????obj????????????????????????????????????
  var ret = Con.apply(obj, arguments);
  // 4. ???????????????????????????????????????
  return ret instanceof Object ? ret : obj;
}
var lindaidai = create(Person, "LinDaiDai");
console.log(lindaidai); // Person{ name: 'LinDaiDai' }
lindaidai.eat(); // 'Eatting'
```

```js
????????????call????????????;

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
  // 1. ???????????????context???null??????undefined?????????window;
  // 2. ????????????????????????????????????, ?????????call????????? Object() ??????
  context =
    context !== null && context !== undefined ? Object(context) : window;
  // 3. ???????????????????????????fn???????????????
  var fn = fnFactory(context);
  // 4. ?????????this???????????????call???????????????
  // 5. ?????????????????????????????????context???, ??????????????????context.fn?????????, fn??????this????????????context???
  context[fn] = this;
  // 6. ???????????????????????????arguments????????????????????????: ['agruments[1]', 'arguments[2]']
  var args = [];
  // 7. ?????????1?????????, ???0??????context
  for (var i = 1, l = arguments.length; i < l; i++) {
    args.push("arguments[" + i + "]");
  }
  // 8. ??????eval()?????????fn??????args?????????????????????
  var result = eval("context[fn](" + args + ")");
  // 9. ???context???????????????????????????fn, ??????????????????????????????
  delete context[fn];
  // 10. ??????fn?????????????????????, ??????????????????
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
????????????apply??????;
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
  // 1. ???????????????context???null??????undefined?????????window;
  // 2. ????????????????????????????????????, ?????????call????????? Object() ??????
  context = context ? Object(context) : window;
  // 3. ???????????????????????????fn???????????????
  var fn = fnFactory(context);
  // 4. ?????????this???????????????call???????????????
  // 5. ?????????????????????????????????context???, ??????????????????context.fn?????????, fn??????this????????????context???
  context[fn] = this;

  var result;
  // 6. ??????????????????????????????
  if (!arr) {
    result = context[fn]();
  } else {
    // 7. ???????????????args????????????????????????: ['arr[0]', 'arr[1]']
    var args = [];
    for (var i = 0, len = arr.length; i < len; i++) {
      args.push("arr[" + i + "]");
    }
    // 8. ??????eval()?????????fn??????args?????????????????????
    result = eval("context[fn](" + args + ")");
  }
  // 9. ???context???????????????????????????fn, ??????????????????????????????
  delete context[fn];
  // 10. ??????fn?????????????????????, ??????????????????
  return result;
};
```

```js
????????????bind????????????;
????????????this??????????????????????????????;
??????????????????????????????, ?????????this?????????;
??????????????????;
??????????????????;
?????????;
?????????????????????????????????new?????????????????????, ????????????this????????????;

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
  // 1. ????????????bind????????????????????????
  if (typeof this !== "function") {
    throw new Error(
      "Function.prototype.bind - what is trying to be bound is not callable"
    );
  }
  // 2. ?????????this???????????????(????????????????????????)
  var self = this;
  // 3. ????????????bind??????????????????
  var args = Array.prototype.slice.call(arguments, 1);

  // 4. ???????????????????????????
  var fBound = function () {
    // 6. ????????????????????????????????????????????????
    var innerArgs = Array.prototype.slice.call(arguments);
    // 7. ??????apply?????????????????????this?????????
    // ???????????????????????????this??????????????????????????????, ???????????????????????????????????????context
    return self.apply(
      this instanceof fNOP ? this : context,
      args.concat(innerArgs)
    );
  };
  // 5. ????????????????????????, ????????????????????????????????????(???????????????????????????????????????)
  // ???????????????????????????????????? fBoun.prototype = this.prototype ????????????
  var fNOP = function () {};
  fNOP.prototype = this.prototype;
  fBound.prototype = new fNOP();
  // 8. ?????????????????????
  return fBound;
};
```
