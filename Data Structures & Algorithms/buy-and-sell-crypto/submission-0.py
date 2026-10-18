class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        p=[]
        n = len(prices)
        for i in range(n):
            if prices[i]<min_price:
                min_price = prices[i]
            else:
                p.append(prices[i]-min_price)
        return max(p)

            



        
        