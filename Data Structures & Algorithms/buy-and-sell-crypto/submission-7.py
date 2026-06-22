class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buyPrice = prices[0]
        maximumProfit = 0
        
        for i in range(1, len(prices)):
            if(buyPrice > prices[i]): # 10>1 true, 1>5 false, 1>6 false, 1>7 false, 1>1 false
                buyPrice = prices[i]

            else:
                currentProfit = prices[i] - buyPrice # 5-1 = 4, 6-1 =5, 7-1 =6, 1-1 = 0
                maximumProfit = max(currentProfit, maximumProfit) 

        return maximumProfit

if __name__ == "__main__":

    prices = [10, 1, 5, 6, 7, 1]
    sol = Solution()
    result = sol.maxProfit(prices)
    print(result)

        
        