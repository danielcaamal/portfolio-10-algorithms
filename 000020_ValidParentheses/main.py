import time

class Solution(object):
    def isValid(self, s: str) -> bool:
        map = {
          '(': ')',
          '[': ']',
          '{': '}',
        }
        
        stack = []
        
        for char in s:
          if (char in map):
            stack.append(char)
          elif (len(stack) == 0 or map.get(stack.pop()) != char):
            return False
          
        return len(stack) == 0

if __name__ == '__main__':
  start = time.time()
  solution = Solution()
  result1 = solution.isValid("()")
  expected1 = True
  print(result1, expected1)
  result2 = solution.isValid("()[]{}")
  expected2 = True
  print(result2, expected2)
  result3 = solution.isValid("(]")
  expected3 = False
  print(result3, expected3)
  end = time.time()
  print((end - start)*1000)