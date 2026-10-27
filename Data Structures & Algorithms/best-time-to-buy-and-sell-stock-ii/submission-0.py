class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        maxProfitVal = 0
        for num in prices:
            if num < minPrice:
                minPrice = num
            if max(0,num-minPrice) >0:
                maxProfitVal +=num-minPrice
                minPrice = num
        return maxProfitVal
        


        