def multiply_list_items(lst, factor):
    return [x * factor for x in lst]

lst = [1, 2, 3, 4, 5]
factor = 2

result = multiply_list_items(lst, factor)
print(result)