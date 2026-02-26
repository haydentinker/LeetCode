class Solution:
    def binaryGap(self, n: int) -> int:
        num = bin(n)[2:]
        res = 0
        last1 = 0
        print(num)
        for i in range(1,len(num)):
            if num[i] == "1":
                res = max(res, i - last1)
                last1 = i  
        return res
