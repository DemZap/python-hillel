lst = [0, 1, 0, 12, 5, 0, 3]
n = lst.count(0)
i = 0
length = len(lst)

while i < length:
    if lst[i] == 0:
        lst.pop(i)
        length -= 1
    else:
        i += 1
lst.extend([0] * n)
print(lst)