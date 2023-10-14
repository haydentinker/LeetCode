class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left=0
        if len(s1)>len(s2):
            return False
        s1_count={}
        for i in range(len(s1)):
            s1_count[s1[i]]=s1_count.get(s1[i],0)+1
        s2_count={}
        for right in range(len(s2)):
            s2_count[s2[right]]=s2_count.get(s2[right],0)+1
            while s2_count[s2[right]]>s1_count.get(s2[right],0):
                s2_count[s2[left]]-=1
                left+=1    
            if(right-left+1==len(s1)):
                return True
            

        return False