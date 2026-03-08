class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        result=[]
        for i in range(len(nums)):
            if nums[i][i]=='1':
                result.append('0')
            else:
                result.append('1')
        return ''.join(result)