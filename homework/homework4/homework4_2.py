some_list = [0, 1, 7, 2, 4, 8]
# some_list = [1, 3, 5]
# some_list = [6]
# some_list = []

index_element = [some_list[index] for index in [0, 2, 4] if index < len(some_list)]
some_list = sum(index_element) * some_list[-1]
print(some_list)
pass
