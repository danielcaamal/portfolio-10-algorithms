
def merge(left_arr, right_arr):
  result = []
  i, j = 0, 0
  while i < len(left_arr) and j < len(right_arr):
    if left_arr[i] < right_arr[j]:
      result.append(left_arr[i])
      i += 1
    else:
      result.append(right_arr[j])
      j += 1
    
  while i < len(left_arr):
    result.append(left_arr[i])
    i += 1
  
  while j < len(right_arr):
    result.append(right_arr[j])
    j += 1
  
  return result

def merge_sort(arr:list):
  
  if len(arr) < 2:
    return arr[:]
  else:
    middle = int(len(arr)/2)
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    return merge(left, right)
  
  
  return arr



arr = [8,3,1,7,0,10,2]
res = merge_sort(arr)
print(res)

arr = [81,3,12,73,0,10,22,14,38,31]
res = merge_sort(arr)
print(res)