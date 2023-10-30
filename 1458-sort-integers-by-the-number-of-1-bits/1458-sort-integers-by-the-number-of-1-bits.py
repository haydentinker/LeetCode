class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        sortedArr=sorted(arr,key=lambda x: (bin(x).count('1'),x))
        return sortedArr