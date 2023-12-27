class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        result=0
        l=0
        r=1
        while r<len(neededTime):
            if colors[l]==colors[r]:
                if neededTime[l]<neededTime[r]:
                    result+=neededTime[l]
                    l=r
                else:
                    result+=neededTime[r]
            else:
                l=r
            r+=1
        return result