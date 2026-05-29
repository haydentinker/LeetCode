class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = sum(nums[:k])
        res = window
        for i in range(k, len(nums)):
        
            window += nums[i] - nums[i - k]
            res = max(window, res)

        return res / k 
