class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        s1List = list(s1)
        s2List = list(s2)
        if s1List == s2List:
            return True
        if s1List[0] != s2List[0] or s1List[2] !=s2List[2]:
            s1List[0], s1List[2] = s1List[2], s1List[0]
        if s1List[1] != s2List[1] or s1List[3] !=s2List[3]:
            s1List[3], s1List[1] = s1List[1], s1List[3]
        

        return s1List == s2List