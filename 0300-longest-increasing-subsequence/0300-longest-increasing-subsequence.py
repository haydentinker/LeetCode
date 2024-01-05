class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        result=[nums.pop(0)]
        for i in nums:
            if i<=result[-1]:
                result[bisect_left(result,i)]=i
            else:
                result.append(i)
                
        return len(result)