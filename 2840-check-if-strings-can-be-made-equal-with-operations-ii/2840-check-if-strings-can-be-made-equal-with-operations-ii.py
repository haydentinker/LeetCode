class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        even_count=[0] * 26
        odd_count= [0] * 26

        for i in range(len(s1)):
            if i % 2 == 0:
                even_count[ord(s1[i]) - 97] += 1
                even_count[ord(s2[i]) - 97] -= 1
            else:
                odd_count[ord(s1[i]) - 97] += 1
                odd_count[ord(s2[i]) - 97] -= 1
    
        return not any(even_count) and not any(odd_count)