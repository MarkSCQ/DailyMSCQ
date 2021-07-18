# var let const 区别

var 可以重复定义变量，声明提升（例如在54行写了 var a=3; 那么程序会提前在程序开头声明 var a;）

let 不可以重复定义 允许修改value,没有声明提升

const 不能重复定义 不允许修改，在某些情况下允许修改内容，没有声明提升


<img src="../imgs/varconstlet.PNG">