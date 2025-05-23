def popular_words(text, words):
    # Перетворюємо текст у нижній регістр та розбиваємо його на слова
    text_words = text.lower().split()

    # Створюємо словник для підрахунку зустрічей кожного слова
    word_count = {word: text_words.count(word) for word in words}

    return word_count


# Тестування
assert popular_words(
    """When I was One I had just begun When I was Two I was nearly new """,
    ["i", "was", "three", "near"],
) == {"i": 4, "was": 3, "three": 0, "near": 0}, "Test1"

print("ОК")  # Всі тести повинні пройти
pass

# ✔ Перетворює текст у нижній регістр (text.lower()) для правильної перевірки слів незалежно від їхнього написання.
# ✔ Розбиває текст на слова (split()) для створення списку всіх слів.
# ✔ Використовує генератор словника {word: text_words.count(word) for word in words}, який перевіряє кожне слово зі списку words та підраховує його появи у тексті.
# ✔ Якщо слово не знайдено, у словнику буде 0
