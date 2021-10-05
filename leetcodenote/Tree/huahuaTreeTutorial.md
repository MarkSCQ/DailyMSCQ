- Definition of a Binary Tree
  ![Example](/leetcodenote/imgs/hhtree.PNG)

  - 有向无环图，入度 1 出度最多为 2

  - 逻辑上如左图，在程序中右图
  - 通过创建对象的形式产生出来。通常是在堆上。
    ![Example](/leetcodenote/imgs/hhtree_1.PNG)
  - left,right 存的是另一个对象在堆上的地址
  - 鉴于堆上的无序，且空间不是连续，用 tree 做排序并不是非常高效

- Binary search tree
  ![Example](/leetcodenote/imgs/hhtree_2.PNG)

  - BST 需要满足值得形式但不一定需要 balanced (correct but might not be efficient)
  - 上图中的最右边的 tree local 满足条件 但是全局上看 4 不满足条件，所以不是 BST

- Balanced binary tree
  ![Example](/leetcodenote/imgs/hhtree_4.PNG)
  平衡，左右子树高度差不能超过 1

- Binary tree traversal
  ![Example](/leetcodenote/imgs/hhtree_8.PNG)

  - Pre-order/**In-order**/Post-order
  - 什么时候处理 print.
  - 对于 inorder，bst 是有序的

- How to create a BST
  ![Example](/leetcodenote/imgs/hhtree_7.PNG)

- Key to tree problems: recursion
  ![Example](/leetcodenote/imgs/hhtree_6.PNG)
	1 precheck
	2 left tree and right tree recursion
	3 return the results

- Templates!

  - Single root/ Two roots
  - Time complexity: O(n)
  - Space complexity: O(h)

  - One Root
    ![Example](/leetcodenote/imgs/hhtree_template.PNG)
	- 


  - Two Roots
    ![Example](/leetcodenote/imgs/hhtree_template_1.PNG)


<!-- https://www.youtube.com/watch?v=PbGl8_-bZxI stop at 26:30  -->