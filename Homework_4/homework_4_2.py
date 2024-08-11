a = []
last_element = 0
result = 0
for index, element in enumerate(a):
    if index % 2 == 0:
        result += element
if len(a) != 0:
    last_element = a[-1]
result = result * last_element
print(result)















