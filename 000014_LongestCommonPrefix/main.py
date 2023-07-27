import time
# Write a function to find the longest common prefix string amongst an array of strings.
class Solution:
  def longestCommonPrefix(self, strs: list[str]) -> str:
    s = sorted(strs)
    first = s[0]
    last = s[-1]
    ans = 0
    while (ans < len(first) and ans < len(last) and first[ans] == last[ans]):
      ans += 1
    
    return first[0:ans]

if __name__ == '__main__':
  start = time.time()
  solution = Solution()
  result1 = solution.longestCommonPrefix(["flower","flow","flight"])
  expected1 = "fl"
  print(result1, expected1)
  result2 = solution.longestCommonPrefix(["dog","racecar","car"])
  expected2 = ""
  print(result2, expected2)
  end = time.time()
  print((end - start)*1000)
  
"flight"
"flow"
"flower"
"for"