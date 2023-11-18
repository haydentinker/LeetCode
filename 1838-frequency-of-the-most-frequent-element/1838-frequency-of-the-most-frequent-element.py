class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left,right=0,0
        result=0
        window_sum=0
        while right<len(nums):
            window_sum+=nums[right]
            while nums[right]*(right-left+1)-window_sum>k:
                window_sum-=nums[left]
                left+=1
            result=max(result,right-left+1)
            right+=1
        return result

        