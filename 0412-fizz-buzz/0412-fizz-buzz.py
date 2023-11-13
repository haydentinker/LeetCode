class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result=[]
        for i in range(1,n+1):
            curr=""
            if i%3==0:
                curr=curr+"Fizz"
            if i%5==0:
                curr=curr+"Buzz"
            if curr=="":
                curr=str(i)
            result.append(curr)
        return result