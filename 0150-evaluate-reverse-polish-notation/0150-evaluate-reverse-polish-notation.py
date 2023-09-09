class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for token in tokens:
            print(token)
            if token not in '-+/*':
                stack.append(int(token))
            else:
                x,y=int(stack.pop()),int(stack.pop())
                if token=='*':
                    stack.append(x*y)
                elif token=="/":
                    stack.append(y/x)
                elif token=='+':
                    stack.append(x+y)
                else:
                    stack.append(y-x)

        return int(stack[-1])
