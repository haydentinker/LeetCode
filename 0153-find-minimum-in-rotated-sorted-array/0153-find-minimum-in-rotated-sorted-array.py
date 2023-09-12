class Solution:
    def findMin(self, nums: List[int]) -> int:
        #Set up left and right pointers
        left=0
        right=len(nums)-1
        #Binary Search Loop
        while left<right:
            #Calculate mid point
            mid=(right+left)>>1
            #If the first element is less than the last it isn't rotated
            if nums[left]<=nums[right]:
                return nums[left]
            #Update left and right pointers
            if nums[left]>nums[mid]:
                right=mid
            else:
                left=mid+1
        return nums[left]