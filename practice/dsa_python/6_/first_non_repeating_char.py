def first_non_repeating_char(string):
    new_dict = {}
    # { key: [position, iteration]}
    for index, char in enumerate(string):
       if char in new_dict:
           new_dict[char][1] += 1
       else:
           new_dict[char] = [index, 1]
           
    first_non_repeating_char = [char for char, pos_iter in new_dict.items() if pos_iter[1] <= 1]
    if not first_non_repeating_char: 
      return None 
    else: 
      return first_non_repeating_char[0]


print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )



"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""