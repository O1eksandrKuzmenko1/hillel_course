from random import randint
lst = [randint(0, 10) for i in range(randint(3, 10))]
lst_copy = []
print(lst)
lst_copy = [lst[0], lst[1], lst[-2]]
print(lst_copy)




