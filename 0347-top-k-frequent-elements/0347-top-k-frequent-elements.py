from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        sortedList = sorted(counts, key=counts.get, reverse=True)
        return sortedList[:k]
        