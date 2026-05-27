class Solution:
    def isValid(self, s: str) -> bool:
        pMap={
            '{':'}',
            '(':')',
            '[':']'
        }
    
        pStack=[]
        for i in s:
            if i == '{' or i=='(' or i =='[':
                pStack.append(i)
            else:
                if len(pStack):
                    curr = pStack.pop()
                    if pMap[curr] != i:
                        return False
                else:
                    return False
        return True if len(pStack) == 0 else False
