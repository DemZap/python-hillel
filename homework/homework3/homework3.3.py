# some_list = [12, 13, 445, 111, 22, 9]
# some_list = [1, 2, 3, 4, 5, 6]
some_list = [1, 2, 3]
# some_list = [1, 2, 3, 4, 5]
# some_list = [1]
# some_list = []

slicing_list = len(some_list) // 2
slice_data = some_list[:slicing_list]
slice_data1 = some_list[slicing_list:]

# if len(slice_data) >= len(slice_data1):
#     slice_data2 = slice_data + slice_data1
# elif len(slice_data) <= len(slice_data1):
#     slice_data2 = slice_data + slice_data1
# elif some_list == []:
#     slice_data2 = []
slice_data2_str = str(slice_data) + str(slice_data1)

print(slice_data2_str)
pass
