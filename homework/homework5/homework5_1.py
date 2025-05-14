import keyword

name = input("Введіть ім'я змінної: ").strip()
variable = True
if name == "":
    variable = False
if variable and name[0].isdigit():
    variable = False
if variable and name in keyword.kwlist:
    variable = False
if variable and name.count("_") == len(name) and len(name) > 1:
    variable = False

print(variable)

pass
