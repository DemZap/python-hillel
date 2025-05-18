seconds = int(input("Введіть кількість секунд: "))

days, number_seconds = divmod(seconds, 86400)

hours, number_seconds = divmod(number_seconds, 3600)

minutes, number_seconds = divmod(number_seconds, 60)

seconds = number_seconds

if 10 <= days % 100 or days % 10 == 0:
    day = "днів"
elif days % 10 == 1:
    day = "днів"
else:
    day = "днів"

formatted_time = f"{days} {day}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"

print(formatted_time)
pass