class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #set left to first day, right to second day
        l, r = 0, 1
        maxP = 0

        #while right hasn't reached the last day
        while r<len(prices):

            #if price on left day is less than price on right day
            if prices[l]<prices[r]:
                #compute profit
                profit = prices[r] - prices[l]
                #set it to max profit if its the largest we've seen
                maxP = max(maxP, profit)
            #otherwise if the price on right day is lower than left day, set left day to right day
            else: l = r
            #move right day up
            r += 1
        return maxP
        