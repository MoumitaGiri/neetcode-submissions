class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buyPrice = prices[0]
        maximumProfit = 0
        
        for i in range(1, len(prices)):
            if(buyPrice > prices[i]):
                buyPrice = prices[i]

            else:
                currentProfit = prices[i] - buyPrice
                maximumProfit = max(currentProfit, maximumProfit)

        return maximumProfit

if __name__ == "__main__":

    prices = [10, 1, 5, 6, 7, 1]
    sol = Solution()
    result = sol.maxProfit(prices)
    print(result)

        
        