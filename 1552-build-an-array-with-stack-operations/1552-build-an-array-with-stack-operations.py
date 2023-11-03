class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result=[]
        n=1
        for num in target:
            while not n == num:
                result.append("Push")
                result.append("Pop")
                n+=1
            result.append("Push")
            n+=1
        return result
            