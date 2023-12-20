class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        price=prices[0]+prices[1]
        if price>money:
            return money
        return money-price