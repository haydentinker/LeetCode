class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        right=1
        result=0

        while right<len(prices):
            while right-left>1:
                left+=1
            newProfit=prices[right]-prices[left]
            if newProfit>0:
                result+=newProfit
            if prices[left]>prices[right]:
                left=right
            right+=1
        return result
            