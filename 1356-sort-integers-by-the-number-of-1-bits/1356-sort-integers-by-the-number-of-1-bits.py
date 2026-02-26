class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        activeBitMap = {}
        for num in arr:
            activeBitCount = num.bit_count()
            if activeBitCount in activeBitMap:
                activeBitMap[activeBitCount].append(num)
            else:
                activeBitMap[activeBitCount] = [num]

        res = []
        for bitCount in sorted(activeBitMap.keys()):
            sortedVals = sorted(activeBitMap[bitCount])
            res.extend(sortedVals)
        return res