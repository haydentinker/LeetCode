class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        result=[[]]
        for i in nums:
            put=False
            for row in result:
                if not i in row:
                    put=True
                    row.append(i)
                    break
            if not put:
                result.append([i])
        return result