class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        right=1
        result=0
        while right<len(prices):
            newResult=prices[right]-prices[left]
            result=max(newResult,result)
            if prices[left]>prices[right]:
                left=right
            
            right+=1
        return result