class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s)==len(t):
            return False

        counter1=Counter(s)
        counter2=Counter(t)
        if not counter1==counter2:
            return False

        return True