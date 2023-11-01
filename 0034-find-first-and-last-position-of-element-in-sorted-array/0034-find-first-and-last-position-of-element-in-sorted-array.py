class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==1:
            if nums[0]==target:
                return [0,0]
            else:
                return [-1,-1]
        startIndex=-1
        endIndex=-1
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(r+l)//2
            if nums[mid]>target:
                r=mid-1
            elif nums[mid]<target:
                l=mid+1
            if nums[mid]==target:
                startIndex=mid
                print(startIndex)
                if startIndex>0:
                    while startIndex>=0 and nums[startIndex]==target:
                        startIndex-=1
                    startIndex+=1
                if endIndex<len(nums):
                    endIndex=mid
                    while endIndex<len(nums) and nums[endIndex]==target:
                        endIndex+=1
                    endIndex-=1
                break
        return [startIndex,endIndex]
