def remove_duplicates(lst):
    return list(set(lst))

numbers = [1, 2, 2, 3, 4, 3, 5, 1]
duplicated = remove_duplicates(numbers)
print(duplicated)