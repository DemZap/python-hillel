import string

first_letter, last_letter = input("Введіть дві літери через дефіс : ").split("-")
letters = string.ascii_letters
first_letter = letters.index(first_letter)
last_letter = letters.index(last_letter)
result = letters[first_letter : last_letter + 1]

print(result)
pass
