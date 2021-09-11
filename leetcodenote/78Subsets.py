class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[[]]
        # ! we consider different situation based on the input.
        # ! when having a new input, we will 
        for i in range(len(nums)):
            ans+=[curr + [nums[i]] for curr in ans]
        return ans