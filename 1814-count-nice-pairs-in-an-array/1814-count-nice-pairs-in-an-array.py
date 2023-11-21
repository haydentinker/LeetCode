class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        result=0
        for i in range(len(nums)):
            num=str(nums[i])
            nums[i]=nums[i]-int(num[::-1])
        frequency=Counter(nums)
        for val in frequency.values():
            while val>=2:
                result+=val-1
                val-=1
        return result%(10**9+7)
        


