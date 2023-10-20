class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mySet=set()
        for item in nums:
            if item not in mySet:
                mySet.add(item)
            else:
                return True

        return False
        