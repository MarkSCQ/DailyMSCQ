刷尚学堂视频

Day.1 

1. Java中注释 @author @param 。。。
2. 标志符可以_$开头
3. java 采用**unicode**字符集 所以中英文都一样，被认为是普通字符
4. 数字不能作为标志符开头
5. 命名规则 驼峰规则 int ageSalaryStudent...
6. 表示类名的标志符 每个单词首字母大写
7. 表示函数的韩变量的标志符每个名字 第一个单词小写 其余的首字母大写
8. 变量 可操作的存储空间，空间的位置是确定的，但其中的值不确定。空间的大小和内容不确定。
9. java是强类型语言
10. double 8字节 byte, 一个byte 8 bit
11. 基本类型 引用类型



变量分类作用域
<img src="imgs/Capture.PNG">
1. 局部变量  在哪儿定义的就属于哪里
2. 成员变量  实例变量 类内 方法外
3. 静态变量 类内 static修饰
        
        使用Static定义，充数鱼类，生命周期伴随类始终。从类加载到卸载。如果不自动行初始化，与成员变量相同，会自动初始化成该类型的默认初始值、


常量 constant 
1. 一个固定的值,不变的量
2. 专用
3. 通常用 final 来修饰


基本数据类型

1. 基本类型
   1. 数值型
      1. 整数类型   byte short int long
      2. 浮点类型   doublt float
   2. 字符型
   3. 布尔型
2. 引用类型 4字节(byte)
   1. 类
   2. 接口
   3. 数组

1 byte = 8 bit


整型
byte    1 byte      -128 - 127
short   2 byte      -2^15 - 2^15-1
int     4 byte      -2^31 - 2^31-1 约20亿
long    8 byte      -2^63 - 2^63-1

整型常数默认为int类型  
        long f = 5555555;
        long ff = 555555555555L;


浮点型 有误差的

-------占用空间

float------4byte   单精度类型 精确到7位有效数字

double---8byte

BigDecimal类帮助计算

float f = 1.65F

注意浮点数之间的比较 有概率出错




字符型

char a = 'a'; 也可以用unicode

char b= '\u0061';

Java 字符串 String不是一个基础类型 而是一个类




Java 中的boolean类型  true false 小写。 Python 中的bool True和False
boolean单独使用四个byte
在数组中使用 一个byte



自增 子
int b = 3
int a = b++ 先赋值再自增
int a = ++b 先自增再赋值


逻辑与 & 两个都为true 结果才位true 否则是false

逻辑或 | 两个操作有一个操作数是true 结果就是true

短路与 && 只要有一个为false 则直接返回false

短路或 || 只要有一个为true 则直接返回true

逻辑异或 ^ 

非 !


P46 <br>
https://www.bilibili.com/video/BV1oy4y1H7R6?p=45

位运算符，位运算指的是进行二进制运算

~ 按位取反<br>
& 按位与<br>
| 按位或<br>
^ 按位异或<br>
<< 左移运算符<br>
\>\> 右移运算符<br>
左移等同于*2
右移等同于/2