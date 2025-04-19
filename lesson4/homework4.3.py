import random

lst = random.sample(range(1, 100), random.randint(3, 10))
new_lst = [lst[0], lst[2], lst[-2]]

print("Початковий список:", lst)
print("Новий список:", new_lst)

