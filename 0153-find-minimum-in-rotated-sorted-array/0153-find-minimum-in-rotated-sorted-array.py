class Solution:
    def findMin(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        while left<right:
            mid=(right+left)>>1
            if nums[left]<=nums[right]:
                return nums[left]
            if nums[left]>nums[mid]:
                right=mid
            else:
                left=mid+1
        return nums[left]