while True:
    number1 = int(input("Введіть число: "))
    operation = input("Зробіть операцію (+, -, *, /): ")
    number2 = int(input("Введіть друге число: "))
    if operation == "+":
        result = number1 + number2
    elif operation == "-":
        result = number1 - number2
    elif operation == "*":
        result = number1 * number2
    elif operation == "/":
        if number2 == 0:
            print("Помилка: Ділення на нуль неможливо!")
            continue
        else:
            result = number1 / number2
    else:
        print("Помилка: Невідома операція!")
        continue
    print("Результат:", result)
    continue_calc = input("Продовжити обчислення? (y/n): ").lower()
    if continue_calc != "y":
        print("Результат:")
        break

pass
