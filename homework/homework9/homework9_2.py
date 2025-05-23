def difference(*args):
    if not args:
        return 0  # Якщо немає аргументів, повертаємо 0

    return round(max(args) - min(args), 2)  # Округлення до двох знаків після коми


# Тестування
assert difference(1, 2, 3) == 2, "Test1"
assert difference(5, -5) == 10, "Test2"
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, "Test3"
assert difference() == 0, "Test4"

print("ОК")  # Якщо всі тести проходять, код працює коректно
pass

# ✔ *args дозволяє передавати змінну кількість аргументів
# ✔ Перевіряємо, чи є аргументи (if not args:) — якщо немає, повертаємо 0
# ✔ Обчислюємо різницю max(args) - min(args)
# ✔ Округлюємо до двох знаків round(..., 2) для коректного тесту assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4
#
