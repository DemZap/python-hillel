number1 = int(input("Введіть число: "))
operation = input("Зробіть операцію  (+, -, *, /): ")
number2 = int(input("Введіть друге число: "))
if operation == "+":
    result = number1 + number2
    print("Результат:", result)
elif operation == "-":
    result = number1 - number2
    print("Результат:", result)
elif operation == "*":
    result = number1 * number2
    print("Результат:", result)
elif operation == "/":
    if number2 == 0:
        print("Помилка: Ділення на нуль неможно!")
    else:
        result = number1 / number2
        print("Результат:", result)
