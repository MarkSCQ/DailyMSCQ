1.   Assign Cookies
2.   


Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.


The g and s can be very confusing in this question. :X

计算的是可以满足的孩子的个数


1. sort两个序列
2. 对于饼干进行遍历。如果当前的饼干满足当前孩子的饥饿度，孩子count+1，由于孩子和饼干的数量可能不一致，且以计算孩子为主，所以将for 中的内容设置为饼干.
3. 计算基于饼干序列满足条件的孩子的个数

其实这题用for比较麻烦，换做用while更便于思考



