class Solution:
    def myAtoi(self, s: str) -> int:
        result=""
        sign=1
        validSign=True
        for i in s:
                if i.isnumeric():
                    validSign=False
                    result=result+i
                elif i=="-":
                    if not validSign:
                        break
                    validSign=False
                    sign=sign*-1
                elif i=="+":
                    if not validSign:
                        break
                    validSign=False
                elif i.isspace():
                    if not validSign:
                        break
                    continue
                else:
                    break
        if result=="":
            return 0
        resultInt=int(result)*sign
        if resultInt>2**31-1:
            return 2**31-1
        elif resultInt<-2**31:
            return -2**31
        return int(result)*sign
            