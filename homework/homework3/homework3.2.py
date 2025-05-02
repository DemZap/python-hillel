some_list = [121, 13, 47, 110, 35]
# some_list = [1]
# some_list = []

if some_list:
    last_element = some_list.pop()
    some_list.insert(0, last_element)

print(some_list)
pass
