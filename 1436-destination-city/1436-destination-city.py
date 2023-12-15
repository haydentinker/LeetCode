class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        sourceCity=[]
        destination=[]
        for i in paths:
            sourceCity.append([i[0]])
            destination.append([i[1]])
        for i in destination:
            if i not in sourceCity:
                return i[0]
        return ""