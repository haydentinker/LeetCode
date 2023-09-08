class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s)==len(t):
            return False

        counter1=Counter(s)
        counter2=Counter(t)
        for i in s:
            if not counter1[i] == counter2[i]:
                return False 

        return True