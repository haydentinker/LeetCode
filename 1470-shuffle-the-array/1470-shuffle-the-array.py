class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
  
        a = nums[:n]
        b = nums[n:]
        return [item for pair in zip(a, b) for item in pair]