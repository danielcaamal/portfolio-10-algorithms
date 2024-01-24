class Solution:
    def maxProfit(self, prices) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        
        return max_profit
      

if __name__ == '__main__':
    solution = Solution()
    
    solution1 = solution.maxProfit([7,1,5,3,6,4])
    print('Solution1:', solution1)
    
    solution2 = solution.maxProfit([7,6,4,3,1])
    print('Solution2:', solution2)
    