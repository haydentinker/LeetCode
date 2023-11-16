class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # valuesAvailable=(2**len(nums[0]))
        # decimalList=[]
        # for i in nums:
        #     decimalList.append(int(i,2))
        # for i in range(valuesAvailable):
        #     if i not in decimalList:
        #         return bin(i)[2:].zfill(len(nums[0]))
        # Cantor's Diagnoal Arg
        result=[]
        for i in range(len(nums)):
            if nums[i][i]=='1':
                result.append('0')
            else:
                result.append('1')
        return ''.join(result)
        