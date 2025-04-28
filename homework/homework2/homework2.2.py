number = int(input("Введіть 5-значне число:"))

number1, ten_thousandths = divmod(number, 10000)
number2, thousands = divmod(ten_thousandths, 1000)
number3, hundreds = divmod(thousands, 100)
number4, number5 = divmod(hundreds, 10)

revers_number = (
    (number5 * 10000) + (number4 * 1000) + (number3 * 100) + (number2 * 10) + number1
)
print("Перевернуте число:", revers_number)
