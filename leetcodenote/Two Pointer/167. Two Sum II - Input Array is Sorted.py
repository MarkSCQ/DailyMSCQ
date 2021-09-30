class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        head = 0
        tail = len(numbers)-1
        
        
        while head<tail:
            
            sm = numbers[head]+numbers[tail]
            
            if sm==target:
                return [head+1,tail+1]
            elif sm<target:
                head+=1
            else:
                tail-=1
        return [-1,-1]