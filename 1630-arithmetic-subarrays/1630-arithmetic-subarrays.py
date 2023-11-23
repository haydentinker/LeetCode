class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result=[]
        for i in range(len(l)):
            sub=nums[l[i]:r[i]+1]
            sub.sort()
            firstDif=sub[1]-sub[0]
            isArithmetic=True
            for i in range(1,len(sub)-1):
                if not sub[i+1]-sub[i]==firstDif:
                    isArithmetic=False
                    break
            result.append(isArithmetic)
        return result
