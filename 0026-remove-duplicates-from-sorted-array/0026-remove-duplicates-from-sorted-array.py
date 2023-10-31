class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numbers={}
        index=0
        while index<len(nums):
            if nums[index] in numbers:
                nums.remove(nums[index])
                index-=1
            else:
                numbers[nums[index]]=index
            index+=1
        print(len(numbers.values()))
        return len(numbers.values())