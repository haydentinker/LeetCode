class Solution:
    def isValid(self, s: str) -> bool:
        myStack=[]
        for i in s:
            #If it is an opening add to stack
            if (i=='(') or (i=='{') or (i=='['):
                myStack.append(i)
            else:
                #Check to make sure there are items on the stack
                if not myStack:
                    return False
                else:
                    #If there is a closing bracket pop off stack and if it doesn't match
                    # return false
                    if i ==']':
                        if not myStack.pop()=='[':
                            return False
                    elif i ==')':
                        if not myStack.pop()=='(':
                            return False 
                    elif i=='}':
                        if not myStack.pop()=='{':
                            return False 
        #If there are still elements on the stack after loop return false
        if myStack:
            return False 
        return True