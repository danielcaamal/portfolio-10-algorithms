class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        result = ""
        carry = 0
        
        for i in range(max_len - 1, -1, -1):
            res = int(a[i]) + int(b[i]) + carry
            carry = 0
            if res > 1:
                carry = 1
            res = res % 2
            result = str(res) + result 
        
        if carry:
            result = "1" + result
        
        return result



if __name__ == '__main__':
    solution = Solution()
    
    solution1 = solution.addBinary("11", "1")
    print('Solution1:', solution1)
    
    solution2 = solution.addBinary("1010", "1011")
    print('Solution2:', solution2)


