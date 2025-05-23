# some_list = [0, 1, 0, 12, 5, 0, 3]
# some_list = [0]
some_list = [1, 0, 13, 0, 0, 0, 5]
# some_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

zero_list = some_list.count(0)
zero = 0
length = len(some_list)

while zero <= 0:
    if some_list == 0:
        some_list.remove(zero)
some_list.extend([0] * zero_list)

print(some_list)

pass
