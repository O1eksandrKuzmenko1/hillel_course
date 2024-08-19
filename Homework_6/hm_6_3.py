num = input("enter your numbers: ")
while True:
    result = 1
    for i in num:
        result *= int(i)
    if result <= 9:
        print(result)
        break
    num = str(result)












