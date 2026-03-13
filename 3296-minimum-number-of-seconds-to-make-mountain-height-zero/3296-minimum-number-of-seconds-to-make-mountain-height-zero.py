class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        low, high = 1, 10**16

        while low < high:
            mid = (low + high) >> 1
            total = 0
            for time in workerTimes : 
                total += int(math.sqrt(mid / time * 2 + 0.25) - 0.5)
                if total >= mountainHeight: break
            if total >= mountainHeight: 
                high = mid
            else:
                low = mid + 1
        return low