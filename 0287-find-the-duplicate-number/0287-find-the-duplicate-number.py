class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # First soltion that uses O(n) extra space
        # Result: 522 ms and 32.2 MB
        # Faster but uses a little bit more memory
        # foundNums=set()
        # for i in nums:
        #     if i in foundNums:
        #         return i
        #     foundNums.add(i)
        # return 0
        # Floyd's algorithm
        # Result: 551ms and 30.9 MB
        # Slow but uses less memory
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