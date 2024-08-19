import string

letters = input("Введите две буквы через дефис: ")
start_letter, end_letter = letters.split("-")
all_letters = string.ascii_letters
start_letter = all_letters.index(start_letter)
end_letter = all_letters.index(end_letter)
result_letters = all_letters[start_letter:end_letter+1]
print(result_letters)




