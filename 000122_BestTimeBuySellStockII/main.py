class Solution:
    def maxProfit(self, prices) -> int:
        if not prices:
            return 0
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i-1] > 0:
                max_profit += (prices[i] - prices[i-1])
        return max_profit
      

if __name__ == '__main__':
    solution = Solution()
    
    solution1 = solution.maxProfit([7,1,5,3,6,4])
    print('Solution1:', solution1)
    
    solution2 = solution.maxProfit([1,2,3,4,5])
    print('Solution2:', solution2)
    
    solution3 = solution.maxProfit([7,6,4,3,1])
    print('Solution3:', solution3)
    