import string
import keyword


name = input("enter your name: ")
examination = not name[0].isdigit()
examination = examination and name.count('_') <= 1
examination = examination and all(not (char.isupper() or char in string.punctuation.replace('_', '') or char.isspace()) for char in name)
examination = examination and not keyword.iskeyword(name)
print(examination)
