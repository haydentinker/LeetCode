class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        windowSum, left = 0 ,0 
        res = float('inf')
        for right in range(len(nums)):
            windowSum += nums[right]
            while windowSum >= target:
                res = min(res, (right - left + 1))
                windowSum -= nums[left]
                left +=1
        
        return res if res != float('inf') else 0