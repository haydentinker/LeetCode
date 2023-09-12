class Solution:
    def search(self, nums: List[int], target: int) -> int:
        high=len(nums)-1
        low=0
        while low<=high:
            partition= (high+low)//2
            if nums[partition]<target:
                low+=1
            elif nums[partition]>target:
                high-=1
            elif nums[partition]==target:
                return partition
        return -1