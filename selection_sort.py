def selection_sort(arr = [2, 5, 1, 1, 0]):
    #[2, 3, 1, 0]

    new_sorted_list = []

    while len(arr) > 0:
        smallest_value = float("inf")
        smallest_index = -1
        for i, current_value in enumerate(arr):
            if current_value < smallest_value:
                smallest_value = current_value
                smallest_index = i
        new_sorted_list.append(smallest_value)
        arr.pop(smallest_index)
    print(new_sorted_list)

selection_sort()
        
   


        


