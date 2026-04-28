class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flat_grid = [item for row in grid for item in row]
        if len(flat_grid) < 2:
            return 0 
        n = len(flat_grid)
        flat_grid.sort()
        median = flat_grid[n//2]
        common_remainder = median % x
        res = 0
        for num in flat_grid:
            if num % x != common_remainder:
                return -1
            elif num == median:
                continue
            else:
                res += abs(median - num) // x

        return res