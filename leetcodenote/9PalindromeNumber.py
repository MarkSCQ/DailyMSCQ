class Solution:
    def isPalindrome(self, x):
        
        if not (0 <= x <= 2147483647):
            return False
        # ! Revert half of the number
        # ! store the first half in store_num
        store_num = []
        while x > 0:
            t = x % 10
            store_num.append(t)
            x = int(x / 10)
        returnFlag = True
        # ! compare the store_num with the second half of the array
        for i in range(int(len(store_num)/2)):
            if store_num[i] != store_num[len(store_num)-1 - i]:
                returnFlag = False
                return returnFlag
        return True
