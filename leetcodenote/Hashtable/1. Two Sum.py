class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # ! store data of nums in one dictionary,
        # ! key is nums value, value is index
        targetDic = {}
        for i in range(len(nums)):
            targetDic[nums[i]]=i
            
            
        for i in range(len(nums)):
            # ! answer = target-nums[i] 
            # ! answer is used to help with searching
            ans = target-nums[i]
            # ! if ans in targetDic and the index is not equal to the current i
            # ! for the first one is that we have the answer,
            # ! for the second one is that the answer is not itself
            if ans in targetDic and targetDic[ans]!=i:
                return [i,targetDic[ans]]


"""
! One Pass
"""
class Solution2:
    def twoSum(self, nums, target) :
        # store data of nums in one dictionary,
        # key is nums value, value is index
        targetDic = {}

        for i in range(len(nums)):
            ltarget = target-nums[i]
            if ltarget in targetDic:
                return [i,targetDic[ltarget]]
                
            targetDic[nums[i]]=i
        