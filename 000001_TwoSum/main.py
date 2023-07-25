import time

def twoSum2(nums: list[int], target: int) -> list[int]:
  tmp = {}
  for i, num in enumerate(nums):
    if target - num in tmp:
      return [tmp[target - num], i]
    tmp[num] = i
  assert "No two sum solution"

if __name__ == '__main__':
  start = time.time()
  result1 = twoSum2([2,7,11,15],9)
  print(result1)
  result2 = twoSum2([3,2,4],6)
  print(result2)
  result3 = twoSum2([3,3],6)
  print(result3)
  end = time.time()
  print((end - start)*1000)