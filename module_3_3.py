def print_params(a = 2, b = "Строка", c = True):
    print(a, b, c)
print_params(8, "Wow")
print_params(55)
print_params("Snow", False, 18 )
print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list_2 = [33, True, "New"]
values_dict = {"a": 22, "b": None,"c": 25.5}
print_params(*values_list_2 )
print_params(**values_dict)
values_list_2 = [100, "Winter"]
print_params(*values_list_2, 42)




