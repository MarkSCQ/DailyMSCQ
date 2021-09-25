'''
https://leetcode.com/problems/trapping-rain-water/

'''



# ! solution 1 two poiniter
# ! head -> tail 
# ! tail -> head
# ! leftmax
# !
# !
class Solution:
    def trap(self, height):

        head = 0
        tail = len(height)-1

        leftmax = 0
        rightmax = 0

        ans = 0

        while head < tail:

            if height[head] < height[tail]:
                if height[head] >= leftmax:
                    leftmax = height[head]
                else:
                    ans += leftmax-height[head]
                head += 1
            else:
                if height[tail] >= rightmax:
                    rightmax = height[tail]
                else:
                    ans += rightmax-height[tail]
                tail -= 1
        return ans
