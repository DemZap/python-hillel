def pow(x):
    return x**2


def some_gen(begin, end, func):
    """
    begin: перший елемент послідовності
    end: кількість елементів у послідовності
    func: функція, яка формує значення для послідовності
    """
    value = begin
    for _ in range(end):
        yield value
        value = func(value)  # Формуємо наступний член послідовності


from inspect import isgenerator

# Тестування
gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, "Test1"
assert list(gen) == [2, 4, 16, 256], "Test2"

print("ОК")  # Якщо всі тести проходять, код працює правильно
pass

# ✔ Створюємо змінну value, яка приймає початкове значення begin
# ✔ Запускаємо цикл for _ in range(end), щоб видати n членів послідовності
# ✔ yield value повертає поточний елемент
# ✔ value = func(value) змінює value на наступне значення за заданим законом
