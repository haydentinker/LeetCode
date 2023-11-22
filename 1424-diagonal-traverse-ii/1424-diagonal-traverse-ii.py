class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        result=[]
        heap=[]
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                heappush(heap,[i+j,j,i])
        while heap:
            heapVal,col,row=heappop(heap)
            if col<len(nums[row]):
                result.append(nums[row][col])
        return result
