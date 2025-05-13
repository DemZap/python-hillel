import random

some_list = random.sample(range(1, 100), random.randint(3, 10))
new_list = [some_list[0], some_list[2], some_list[-2]]

print("Початковий список:", some_list)
print("Новий список:", new_list)

pass
