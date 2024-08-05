import math
list = [1, 2, 3]
half_list = len(list)/2
half_list = math.ceil(half_list)
list = [list[:half_list],list[half_list:]]

print(list)
