def print_params(a = 1, b = 'строка', c = True):
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"c = {c}")
    print()


print_params()
print_params(10)
print_params(10, 'тест')
print_params(10, 'тест', False)
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = [100, 'список', False]
values_dict = {"a": 200, "b": 'словарь', "c": [4, 5, 6]}
print_params(*values_list)
print_params(**values_dict)


values_list_2 = ["элемент1", True]
print_params(*values_list_2, 42)



