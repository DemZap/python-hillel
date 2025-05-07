# some_list = [0, 1, 7, 2, 4, 8]
some_list = [1, 3, 5]
# some_list = [6]
# some_list = []

if some_list:
    some_list = sum(some_list[::2]) * some_list[-1]
print(some_list)
pass
