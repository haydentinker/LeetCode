class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # First soltion that uses O(n) extra space
        # foundNums=set()
        # for i in nums:
        #     if i in foundNums:
        #         return i
        #     foundNums.add(i)
        # return 0
        # Floyd's algorithm
        fast,slow=0,0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if fast ==slow:
                break
        slow2=0
        while True:
            slow2=nums[slow2]
            slow=nums[slow]
            if slow==slow2:
                return slow
        return 0