def is_even(digit):
    """Перевірка чи є парним число"""
    return digit % 2 == 0


# Тестування
assert is_even(2) == True, "Test1"
assert is_even(5) == False, "Test2"
assert is_even(0) == True, "Test3"

print("ОК")  # Якщо всі тести проходять, код працює правильно
pass
# ✔ digit % 2 == 0 — перевіряє, чи число ділиться на 2 без залишку
# ✔ Якщо залишку немає (% 2 == 0), число парне → повертає True
# ✔ Якщо є залишок, число непарне → повертає False
