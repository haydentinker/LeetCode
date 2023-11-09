class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        windowSum=sum(nums[:k])
        result=windowSum/k
        for i in range(k,len(nums)):
            windowSum=windowSum-nums[i-k]+nums[i]
            result=max(result,windowSum/k)
        return result