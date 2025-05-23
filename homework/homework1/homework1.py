number = int(input("Введіть 4-значне число:"))

number1, thousands = divmod(number, 1000)
number2, hundreds = divmod(thousands, 100)
number3, number4 = divmod(hundreds, 10)

print(number1)
print(number2)
print(number3)
print(number4)
