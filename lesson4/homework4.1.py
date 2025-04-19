lst = [1, 0, 13, 0, 0, 0, 5]
lst_1 = lst.count(0)
lst.remove(0)
lst.extend([0] * lst_1)
print(lst)