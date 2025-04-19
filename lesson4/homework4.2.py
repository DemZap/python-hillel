lst = [1, 0, 13, 0, 0, 0, 5]

index_el = []
index_el.append(lst[0])
index_el.append(lst[2])
index_el.append(lst[4])

lst = (index_el[0] + index_el[1] + index_el[2]) * lst[-1]
print(lst)