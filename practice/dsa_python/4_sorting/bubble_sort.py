import operator

def bubble_sort(arr: list):
  iteration = len(arr) - 1
  for _ in arr:
    for index in range(iteration):
      if operator.gt(arr[index],arr[index + 1]):
        arr[index], arr[index + 1] = arr[index + 1], arr[index]
    iteration += 1
  
  return arr

arr = [8,3,1,7,0]
res = bubble_sort(arr)
print(res)
arr2 = [8,3,3,42,11,7,0,6,3,12,31,21]
res2 = bubble_sort(arr2)
print(res2)

