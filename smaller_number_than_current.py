def smaller_number_than_current(arr: list) -> list:
    new_sorted_array = sorted(arr)
    number_count = []

    num_to_number_of_items_smaller_than_it = {}
    for i, num in enumerate(new_sorted_array):
        if num in num_to_number_of_items_smaller_than_it:
            continue
        else:
            num_to_number_of_items_smaller_than_it[num] = i
    
    for each_num in arr:
        number_count.append(num_to_number_of_items_smaller_than_it[each_num])
    
    return number_count