class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        result=0 
        rows=[]
        for i in mat:
            total=sum(i)
            if total==1:
                rows.append(i.index(1))
        cols=Counter(rows)
        for idx, col in enumerate(zip(*mat)):
            if idx in rows and sum(col) == 1:
                result+=1
            
        return result