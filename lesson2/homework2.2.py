# Запитуємо у користувача 5-значне число
x = int(input("Введіть 5-значне число: "))

num1 =x % 10                # остання цифра
num2 = (x// 10) % 10        # четверта цифра
num3 = (x // 100) % 10       # третя цифра
num4 = (x // 1000) % 10      # друга цифра
num5 = (x // 10000) % 10     # перша цифра

print(num1,num2,num3,num4,num5)