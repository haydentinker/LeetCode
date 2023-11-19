class Solution:
    def reductionOperations(self, nums: List[int]) -> int:    
        result=0
        occurrences=Counter(nums)
        heap=[]
        for key,val in occurrences.items():
            heappush(heap,(key,val))
        minNum=heappop(heap)[0]
        count=1
        while heap:
            cur=heappop(heap)
            if cur[0]==minNum:
                continue
            result+=cur[1]*count
            count+=1
         
        return result