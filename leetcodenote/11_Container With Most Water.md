# 11_Container With Most Water.md

Two pointer, Array

描述

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.


        Input: height = [1,8,6,2,5,4,8,3,7]
        Output: 49
        Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.


![Example](/leetcodenote/imgs/question_11.jpg)


BF 暴力死磕，可以磕，但是会超时。所以暴力死磕不可取

Two Pointer 是一个解法。
一开始看这个解法没想通移动的方法，l和r移动的条件。[Youtuber solution ](https://www.youtube.com/watch?v=TI3e-17YAlc) 这个youtuber提到了一下

暂且说这些竖着的都是柱子把。每次移动，l和r，每一次移动都希望下一次的柱子更高，虽然没办法预测到哪个更高（对于我们来说可以获得更多的水），但是基于当前每一步可以获得的信息，我们可以在当前的两个柱子中淘汰最矮的那个。

如果左边的柱子小于右边的，那么左边柱子往右走一步；如果右边的柱子小于左边的柱子，右边的柱子往左走一步。同时通过对比然后决定是否淘汰当前最多的水。


**Two Pointer**

    class Solution {
    public int maxArea(int[] height) {
        int curr_max = 0;
        
        int head = 0;
        int tail = height.length-1;
        while(head<tail){
            
            curr_max=Math.max(curr_max, Math.min(height[head],height[tail])*(tail-head));
            if(height[head]<height[tail])
                head++;
            else
                tail--;
        }
        return curr_max;
    }
}


***BF 超时方法***

    class Solution {
    public int maxArea(int[] height) {
        int maxarea = 0;
        for (int i = 0; i < height.length; i++)
            for (int j = i + 1; j < height.length; j++)
                maxarea = Math.max(maxarea, Math.min(height[i], height[j]) * (j - i));
        return maxarea;
        }
    }


（写下这篇时候莫名想到了末位淘汰制，可能这就是人生吧，23333）