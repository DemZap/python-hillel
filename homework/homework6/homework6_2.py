# Отримуємо введене число від користувача
seconds = int(input("Введіть кількість секунд: "))

# Обчислюємо кількість днів
days, remaining_seconds = divmod(seconds, 86400)

# Обчислюємо години
hours, remaining_seconds = divmod(remaining_seconds, 3600)

# Обчислюємо хвилини
minutes, remaining_seconds = divmod(remaining_seconds, 60)

# Останні секунди
seconds = remaining_seconds

# Формуємо коректне написання слова "день/дні"
if 10 <= days % 100 <= 20 or days % 10 >= 5 or days % 10 == 0:
    day_word = "днів"
elif days % 10 == 1:
    day_word = "день"
else:
    day_word = "дні"

# Форматуємо вивід
formatted_time = f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"

print(formatted_time)
pass
