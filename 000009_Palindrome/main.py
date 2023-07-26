import time
# Given an integer x, return true if x is a palindrome, and false otherwise.
class Solution:
    # def isPalindrome(self, x: int) -> bool:
    #   if x < 0:
    #     return False
      
    #   x = str(x)
      
    #   if x[::-1] == x:
    #     return True
      
    #   return False
    
    def isPalindrome(self, x: int) -> bool:
      aux_x = x
      reverse_x = 0
      while aux_x > 0:
        last_digit = aux_x % 10
        aux_x = aux_x // 10
        reverse_x = reverse_x * 10 + last_digit
      
      return x == reverse_x

if __name__ == '__main__':
  start = time.time()
  solution = Solution()
  result1 = solution.isPalindrome2(121)
  expected1 = True
  print(result1, expected1)
  result2 = solution.isPalindrome2(-121)
  expected2 = False
  print(result2, expected2)
  result3 = solution.isPalindrome2(10)
  expected3 = False
  print(result3, expected3)
  end = time.time()
  print((end - start)*1000)