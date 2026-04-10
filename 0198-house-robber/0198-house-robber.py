class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dp(index, robbedPrevious):
            if index >= len(nums):
                return 0 
            if robbedPrevious:
                return dp(index +1, False)
            return max(nums[index]+ dp(index+1,True),dp(index+1, False) )
        
        return dp(0,False)