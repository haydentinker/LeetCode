class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        cols=defaultdict(list)
        rows=defaultdict(list)
        for index,col in enumerate(zip(*grid)):
            cols[index].append(col.count(0))
            cols[index].append(col.count(1))
        for index,row in enumerate(grid):
            rows[index].append(row.count(0))
            rows[index].append(row.count(1))
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                grid[i][j]=rows[i][1]+cols[j][1]-rows[i][0]-cols[j][0]
        return grid