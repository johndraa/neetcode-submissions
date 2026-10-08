class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        best = 0
        for price in prices:
            if price < low: low = price
            else: best = max(best, price-low)
        return best



# iterate through prices, find the day (prices[i]) where the price is the lowest, and where it is the highest
# if the lowest price comes after the highest price in the array, return 0

        