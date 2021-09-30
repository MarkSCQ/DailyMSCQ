# **Leetcode weekly challenge - Find Leaves of Binary Tree**

Requirements:

Given the root of a binary tree, collect a tree's nodes as if you were doing this:
* Collect all the leaf nodes.
* Remove all the leaf nodes.
* Repeat until the tree is empty.

![Example](/leetcodenote/imgs/findallleaves.PNG)

        Input: root = [1,2,3,4,5]
        Output: [[4,5,3],[2],[1]]
        Explanation:
        [[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since per each level it does not matter the order on which elements are returned.


非常有迷惑性的一题啊，看到remove就迫不及待的set null，然后最后一个看input output，人傻了。

这题和remove其实没有特别大的关系。切入点是每个节点的高度。指的是从当前节点到最底层node的高度。比如说1的高度是2，2的高度是1，,3，4和5的高度是0

通过这些高度，形成一个hashtable然后对应输出。其实，这里的hashtable也不是必要的。下面第一个方法，使用hashtable。比较繁琐，效率很低。



        public static int HeightHelper_1(TreeNode tmpNode) {
            if (tmpNode == null) {
                return 0;
            } else {
                int lheight = HeightHelper_1(tmpNode.left);
                int rheight = HeightHelper_1(tmpNode.right);

                if (lheight > rheight) {
                    return lheight + 1;
                } else
                    return rheight + 1;
            }
        }

        public static void Node_Heights(TreeNode root, Hashtable<Integer, List<Integer>> Height) {
            if (root == null) {
                return;
            } else {
                // count height and add to hastable
                if (!Height.containsKey(HeightHelper_1(root))) {
                    List<Integer> arr = new ArrayList<>();
                    arr.add(root.val);
                    Height.put(HeightHelper_1(root), arr);
                } else {
                    Height.get(HeightHelper_1(root)).add(root.val);
                }
            }
            Node_Heights(root.left, Height);
            System.out.println(root.val);
            Node_Heights(root.right, Height);
        }

        public static List<List<Integer>> deleteLeaves_2(TreeNode root) {
            List<List<Integer>> leaves = new ArrayList<>();
            Hashtable<Integer, List<Integer>> numbers = new Hashtable<Integer, List<Integer>>();
            Node_Heights(root, numbers);
            List<Integer> ks = new ArrayList<>(numbers.keySet());
            Collections.sort(ks);
            for (int i = 0; i < ks.size(); i++) {
                leaves.add(numbers.get(ks.get(i)));
            }
            return leaves;
        }

第二个方法

非常简洁，没有用到之前用的hashtable，而是通过数组index的方式。

1. 遍历整个树
2. 遍历的同时计算每个节点的高度，然后对应把当前节点的值加入到对应的array中。
3. 最精髓的就是 if(res.size() == level) res.add(new ArrayList<>()); 之前有考虑过这种方法，但是因为考虑到不知道如何插入一个arraylist，所以就放弃了，现在想了一下，这句简直精辟。 当当前level和arraylist size一样的时候 添加一个空的arraylist。


        List<List<Integer>> res;
        public List<List<Integer>> findLeaves(TreeNode root) {
            res = new ArrayList<>();
            helper(root);
            return res;
        }
        
        int helper(TreeNode root) {
            if(root == null) return -1;
            int left = helper(root.left);
            int right = helper(root.right);
            int level = Math.max(left, right) + 1;
            if(res.size() == level) res.add(new ArrayList<>());
            res.get(level).add(root.val);
            return level;
        }