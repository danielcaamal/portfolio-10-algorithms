import time
# Given a roman numeral, convert it to an integer.
class Solution:
  def romanToInt(self, string: str) -> int:
    symbols = {
      "I": 1,
      "V": 5,
      "X": 10,
      "L": 50,
      "C": 100,
      "D": 500,
      "M": 1000,
    }
    m_accumulator = 0
    c_accumulator = 0
    d_accumulator = 0
    u_accumulator = 0
    for char in string:
      current_value = symbols.get(char)
      
      if char == 'I':
        u_accumulator += current_value
        
      if char == 'V' or char == 'X':
        d_accumulator += current_value - u_accumulator
        u_accumulator = 0
      
      if char == 'L' or char == 'C':
        c_accumulator += current_value - d_accumulator
        d_accumulator = 0
        
      if char == 'D' or char == 'M':
        m_accumulator += current_value - c_accumulator
        c_accumulator = 0
      
    return m_accumulator + c_accumulator + d_accumulator + u_accumulator
  
  def romanToInt2(self, s: str) -> int:
        roman_to_integer = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
        return sum(map(lambda x: roman_to_integer[x], s))

if __name__ == '__main__':
  start = time.time()
  solution = Solution()
  result1 = solution.romanToInt("III")
  expected1 = 3
  print(result1, expected1)
  result2 = solution.romanToInt("LVIII")
  expected2 = 58
  print(result2, expected2)
  result3 = solution.romanToInt("MCMXCIV")
  expected3 = 1994
  print(result3, expected3)
  result4 = solution.romanToInt("IX")
  expected4 = 9
  print(result4, expected4)
  result5 = solution.romanToInt("MCDXCIX")
  expected5 = 1499
  print(result5, expected5)
  end = time.time()
  print((end - start)*1000)