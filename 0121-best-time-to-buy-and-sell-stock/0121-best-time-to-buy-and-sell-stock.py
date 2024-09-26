class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_price = 0
        min_purchase = prices[0]


        for i in range(len(prices)):
            if prices[i] > min_purchase:
                best_price = (
                    prices[i] - min_purchase
                    if prices[i] - min_purchase > best_price
                    else best_price
                )
            min_purchase = min(prices[i], min_purchase)

        return best_price
        
        