class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        stack=['(']
        while stack:
            currItem=stack.pop()
            if currItem.count('(')==n and currItem.count(')')==n:
                result.append(currItem)
            else:
                if currItem.count('(')<n:
                    stack.append(currItem+'(')
                if currItem.count('(')>currItem.count(')'):
                    stack.append(currItem+')')
        return result