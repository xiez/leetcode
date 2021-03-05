class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        min_price = prices[0]
        max_prof = 0
        
        for p in prices:
            if p < min_price:
                min_price = p
                
            max_prof = max(max_prof, p - min_price)
            #print(max_prof)            
        return max_prof
