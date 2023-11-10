def quick_sort(arr: list):
  if len(arr) <= 1:
    return arr
  else:
    pivot = arr[-1]
    left = [x for x in arr[:len(arr) - 1] if x < pivot]
    right = [x for x in arr[:len(arr) - 1] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


arr = [8,3,1,7,0,10,2]
res = quick_sort(arr)
print(res)

arr = [81,3,12,73,0,10,22,14,38,31]
res = quick_sort(arr)
print(res)