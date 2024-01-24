class Solution:
    def mySqrt(self, x: int) -> int:
        guess = result = x
        for _ in range(50):
            result = guess = 0.5 * ( x / guess + guess )
        return int(result)



if __name__ == '__main__':
    solution = Solution()
    
    solution1 = solution.mySqrt(121)
    print('Solution1:', solution1)
    
    solution2 = solution.mySqrt(8)
    print('Solution2:', solution2)


