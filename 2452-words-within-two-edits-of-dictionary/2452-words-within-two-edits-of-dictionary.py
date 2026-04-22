class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def isValid(word1,word2):
            count = 0
            for i in range(len(word1)):
                if word1[i]!=word2[i]:
                    count+=1
                if count==3:
                    return False
            return True

        validQuery = []
        for query in queries:
            for d in dictionary:
                dist = isValid(query,d)
                if dist:
                    validQuery.append(query)
                    break
        return validQuery