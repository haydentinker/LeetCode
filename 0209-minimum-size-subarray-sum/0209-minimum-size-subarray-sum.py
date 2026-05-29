class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, window = 0, 0
        res = float('inf')
        for right in range(len(nums)):
            window += nums[right]
            while window >= target:
                res = min(res, right - left + 1)
                window -= nums[left]
                left += 1

        return 0 if res == float('inf') else res