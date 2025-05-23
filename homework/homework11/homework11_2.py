def generate_cube_numbers(end):
    """Генерує куби чисел, починаючи з 2 до заданого 'end'"""
    num = 2
    while True:
        cube = num**3
        if cube > end:
            return  # Завершуємо генератор, коли куб перевищує 'end'
        yield cube
        num += 1


# Тестування
from inspect import isgenerator

gen = generate_cube_numbers(1)
assert isgenerator(gen) == True, "Test0"
assert list(generate_cube_numbers(10)) == [8], "оскільки воно менше 10."
assert list(generate_cube_numbers(100)) == [
    8,
    27,
    64,
], "5 у кубі це 125, а воно вже більше 100"
assert list(generate_cube_numbers(1000)) == [
    8,
    27,
    64,
    125,
    216,
    343,
    512,
    729,
    1000,
], "10 у кубі це 1000"

print("ОК")  # Якщо всі тести проходять, код працює правильно
pass
# ✔ Цикл while True забезпечує безперервну генерацію кубів чисел.
# ✔ cube = num ** 3 обчислює куб поточного числа.
# ✔ Якщо куб більше end, використовується return для завершення генератора.
# ✔ yield cube повертає наступне значення куба перед збільшенням num.
