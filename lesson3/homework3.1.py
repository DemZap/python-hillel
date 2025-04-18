num1 = int(input("Введіть число: "))
operation = input("Зробіть операцію  (+, -, *, /): ")
num2 = int(input("Введіть друге число: "))
if operation == "+":
    result = num1 + num2
    print(result)
elif operation == "-":
    result = num1 - num2
    print(result)
elif operation == "*":
    result = num1 * num2
    print(result)
elif operation == "/":
    if num2 == 0:
        print("Помилка: Ділення на нуль неможно!")
    else:
        result = num1 / num2
        print(result)