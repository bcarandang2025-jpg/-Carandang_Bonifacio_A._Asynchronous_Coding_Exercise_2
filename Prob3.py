lst = [1, 2, 3, 2, 4, 2, 5]
elem_to_remove = []

def remove_all_occurrences(lst, elem_to_remove):
    if lst == []:
        print("Empty List")
    elif elem_to_remove not in lst:
        print("Not Found")
    else:
        new_list = [x for x in lst if x != elem_to_remove]
    print(new_list)