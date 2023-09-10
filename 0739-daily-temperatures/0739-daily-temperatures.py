class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0]*len(temperatures)
        stack=[]
        for index,temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<temp:
                currentTemp=stack.pop()
                result[currentTemp]=index-currentTemp
            stack.append(index)
        return result