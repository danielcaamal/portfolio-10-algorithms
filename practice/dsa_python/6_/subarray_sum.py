def subarray_sum(nums, target):
    print('target ' + str(target))
    new_dict = {0:-1}
    initial_sum = 0
    for index in range(len(nums)):
        initial_sum += nums[index]
        
        print(new_dict, initial_sum)
        if initial_sum - target in new_dict:
            return [new_dict[initial_sum - target] + 1, index]
        
        new_dict[initial_sum] = index
    
    return []
        
        
        




nums = [1, 2, 3, 4, 5]
target = 9
print ( subarray_sum(nums, target) )

nums = [-1, 2, 3, -4, 5]
target = 0
print ( subarray_sum(nums, target) )

nums = [2, 4, 5, 3, 6]
target = 3
print ( subarray_sum(nums, target) )

nums = []
target = 0
print ( subarray_sum(nums, target) )



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 3]
    [0, 3]
    [1, 1]
    []

"""
