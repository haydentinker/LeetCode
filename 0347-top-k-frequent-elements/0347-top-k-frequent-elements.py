class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsDict={}
    
        for i in nums:
            if i in numsDict.keys():
                numsDict[i]+=1
            else:
                numsDict[i]=1
        numsDict=sorted(numsDict.items(),key=lambda x:x[1],reverse=True)
        return [numsDict[x][0] for x in range(k) ]
