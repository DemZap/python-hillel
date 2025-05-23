number = int(input("Введіть число: "))

while number >= 9:
    result = 1
    for numbers in str(number):
        result *= int(numbers)
    number = result

print(number)
pass
