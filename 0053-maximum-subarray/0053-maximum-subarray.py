class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        l=0
        r=0
        curSum,result=0,float('-inf')
        while r<len(nums):
            curSum+=nums[r]
            r+=1
            result=max(result,curSum)
            while l<r and l<len(nums) and curSum<=0:
                curSum-=nums[l]
                l+=1
        return result
