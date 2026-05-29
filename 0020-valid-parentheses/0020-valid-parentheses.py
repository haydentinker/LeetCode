class Solution:
    def isValid(self, s: str) -> bool:
        pMap = {
            '{':'}',
            '[':']',
            '(':')'
        }
        stack = []
        for i in s:
            if i =='(' or i =='{' or i =='[':
                stack.append(i)
            else:
                if not stack:
                    return False
                prevPar = stack.pop()
                if pMap[prevPar] != i:
                    return False

        return True if not stack else False