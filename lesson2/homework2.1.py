# Запитуємо у користувача 4-значне число
x = int(input("Введіть 4-значне число: "))

num1 = (x // 1000)
num2 = (x % 1000) // 100
num3 = (x % 100) // 10
num4 = (x % 10)

print(num1)
print(num2)
print(num3)
print(num4)