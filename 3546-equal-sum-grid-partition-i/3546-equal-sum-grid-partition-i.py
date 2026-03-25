class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        tot = 0 
        m, n = len(grid), len(grid[0])
        cols = [0] * n
        rows = [0] * m

        for i in range(m):
            for j in range(n):
                tot += grid[i][j]
                rows[i] += grid[i][j]
                cols[j] += grid[i][j]
        if tot % 2 != 0:
            return False
        curr = 0 
        target = tot // 2
        for i in range(m-1):
            curr += rows[i]
            if curr == target:
                return True
        curr = 0 
        for i in range(n-1):
            curr += cols[i]
            if curr == target:
                return True
        return False