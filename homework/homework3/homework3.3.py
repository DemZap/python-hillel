# some_list = [12, 13, 445, 111, 22, 9]
# some_list = [1, 2, 3, 4, 5, 6]
# some_list = [1, 2, 3]
# some_list = [1, 2, 3, 4, 5]
# some_list = [1]
some_list = []

slicing_list = (len(some_list) + 1) // 2
slice_data = some_list[:slicing_list]
slice_data1 = some_list[slicing_list:]

slice_data2_str = [slice_data] + [slice_data1]

print(slice_data2_str)
pass
