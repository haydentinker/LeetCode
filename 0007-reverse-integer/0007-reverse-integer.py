class Solution:
    def reverse(self, x: int) -> int:
        result=""
        for digit in str(x):
            if digit is not "-":
                result=digit+result
        if abs(int(result)) >(2**31-1):
            return 0
        elif x <0:
            return int(result)*-1
       
        else:
            return int(result)