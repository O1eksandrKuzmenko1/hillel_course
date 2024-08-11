numbers = [6, 7, 0, 8, 9, 0, 1, 0, 5]
for i in numbers:
    if i == 0:
        numbers.remove(i)
        numbers.append(i)
print(numbers)









