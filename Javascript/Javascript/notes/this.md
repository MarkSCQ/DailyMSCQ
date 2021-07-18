# this 绑定规则

函数中使用，默认指向window对象

```
function girl(){
    console.log(this)
}
girl() // window对象
```
对象中使用 

隐式绑定，调用对象自己的属性

硬绑定
 <img src="../imgs/yb1.PNG">
 <img src="../imgs/yb2.PNG">

构造函数绑定
<img src="../imgs/gbd.PNG">

