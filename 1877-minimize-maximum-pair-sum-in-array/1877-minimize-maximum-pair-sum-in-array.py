class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        left=0
        right=len(nums)-1
        result=float('-inf')
        while left<right:
            curr=nums[left]+nums[right]
            result=max(curr,result)
            left+=1
            right-=1
        return result
