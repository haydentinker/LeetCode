class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        ans = 1 if grid[0][0] <=k else 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                elif i==0:
                    grid[i][j] += + grid[i][j-1]
                elif j==0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] = grid[i-1][j] + grid[i][j-1]- grid[i-1][j-1] + grid[i][j] 
                if grid[i][j] <= k:
                    ans +=1
        return ans