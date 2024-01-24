class Solution:

    def plusOne2(self, digits):
        carry = 0
        digits[-1] = digits[-1] + 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] = digits[i] + carry
            if digits[i] > 9:
                digits[i] = 0
                carry = 1
            else:
              carry = 0
            
        if carry:
            digits.insert(0, 1)
        
        return digits

    def plusOne(self, digits):
        digits_str = [str(i) for i in digits]
        num = str(int("".join(digits_str)) + 1)
        return [int(i) for i in num]


if __name__ == '__main__':
    solution = Solution()
    
    solution1 = solution.plusOne([1,2,3])
    print('Solution1:', solution1)
    
    solution2 = solution.plusOne([4,3,2,1])
    print('Solution2:', solution2)
    
    solution3 = solution.plusOne([9])
    print('Solution3:', solution3)
    
    solution4 = solution.plusOne([9,8,7,6,5,4,3,2,1,0])
    print('Solution4:', solution4)
    
    solution5 = solution.plusOne([9,9])
    print('Solution5:', solution5)



