a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

print("Что нужно сделать ?")
c = (input("Требуемая операция: "))
if c == "+":
    print("Решение: " , a + b)
elif c == "-":
    print("Решение: " , a - b)
elif c == "*":
    print("Решение: " , a * b)
elif c == "/" and b!= 0:
    print("Решение: " , a / b)
else:
    print(" На ноль делить нельзя!")










