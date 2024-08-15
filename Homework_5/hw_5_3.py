import string

string_in = input("enter your string: ")
words = string_in.title()
string_normal = "".join(char for char in words if char not in string.punctuation and char != " ")
if len(string_normal) > 140:
    string_normal = string_normal[:140]
print("#" + string_normal)



