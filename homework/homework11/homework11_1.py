def is_prime(n):
    """Перевіряє, чи є число простим."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # Перевіряємо дільники до кореня з числа
        if n % i == 0:
            return False
    return True


def prime_generator(end):
    """Генерує прості числа до верхньої межі 'end'."""
    for num in range(2, end + 1):
        if is_prime(num):
            yield num


# Тестування
from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, "Test0"
assert list(prime_generator(10)) == [2, 3, 5, 7], "Test1"
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], "Test2"
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], "Test3"

print("Ok")  # Якщо всі тести проходять, код працює правильно
pass
# ✔ is_prime(n) — окрема функція, яка перевіряє, чи є число простим.
# ✔ for num in range(2, end + 1) — перебираємо всі числа від 2 до end.
# ✔ if is_prime(num): yield num — повертаємо лише прості числа.
# ✔ Генератор не зберігає всі числа в пам'яті, а видає їх поступово.
