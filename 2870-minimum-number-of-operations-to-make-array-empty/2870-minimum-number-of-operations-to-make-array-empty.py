class Solution:
    def minOperations(self, nums: List[int]) -> int:
        numCounter=Counter(nums)
        result=0
        for val in numCounter.values():
            if val==1: return -1
            result+=ceil(val/3)
                
        return result