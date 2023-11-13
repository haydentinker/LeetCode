class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # One Solution
        # nums.sort()

        left=0
        right=len(nums)-1

        while left<=right:
            print(nums)
            curNum=nums[left]
            del nums[left]
            if curNum==0:
                left+=1
                nums.insert(0,0)
            elif curNum==2:
                right-=1
                nums.append(2)
            else:
                nums.insert(left,1)
                left+=1
            