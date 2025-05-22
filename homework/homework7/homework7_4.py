def common_elements():
    elements_of_3 = {num for num in range(100) if num % 3 == 0}
    elements_of_5 = {num for num in range(100) if num % 5 == 0}
    return elements_of_3 & elements_of_5


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("ОК")
pass
