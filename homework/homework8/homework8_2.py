import re


def is_palindrome(text):
    # Видаляємо всі знаки пунктуації та пробіли
    cleaned_text = re.sub(r"[^a-zA-Z0-9]", "", text).lower()

    # Перевіряємо, чи є рядок паліндромом
    return cleaned_text == cleaned_text[::-1]


# Тестування
assert is_palindrome("A man, a plan, a canal: Panama") == True, "Test1"
assert is_palindrome("0P") == False, "Test2"
assert is_palindrome("a.") == True, "Test3"
assert is_palindrome("aurora") == False, "Test4"

print("ОК")  # Всі тести повинні пройти
pass
#  re.sub(r'[^a-zA-Z0-9]', '', text) — видаляє всі символи, які не є літерами чи цифрами.
# ✔ .lower() — переводить рядок у нижній регістр для коректного порівняння.
# ✔ [::-1] — перевертає рядок, щоб порівняти його з оригіналом.
