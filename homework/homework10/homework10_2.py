import re


def first_word(text):
    """Пошук першого слова у рядку"""
    return re.search(r"[a-zA-Z']+", text).group()


# Тестування
assert first_word("Hello world") == "Hello", "Test1"
assert first_word("greetings, friends") == "greetings", "Test2"
assert first_word("don't touch it") == "don't", "Test3"
assert first_word(".., and so on ...") == "and", "Test4"
assert first_word("hi") == "hi", "Test5"
assert first_word("Hello.World") == "Hello", "Test6"

print("ОК")  # Всі тести повинні пройти
pass

# ✔ Використовує re.search() для знаходження першого слова у тексті
# ✔ r"[a-zA-Z']+" — регулярний вираз, який шукає слово (включаючи апострофи ')
# ✔ .group() повертає знайдене слово
# ✔ Проходить всі тестові випадки
