class Solution:
    def canJump(self, nums: List[int]) -> bool:
        result=len(nums)-1

        for i in range(len(nums)-2,-1,-1):
            if nums[i]+i>=result:
                result=i
        return True if result==0 else False