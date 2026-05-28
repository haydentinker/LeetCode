class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right, res = 0, 1, 0 
        while right < len(prices):
            res = max(res, prices[right] - prices[left])
            if prices[right] < prices[left]:
                left = right
            right +=1


        return res



