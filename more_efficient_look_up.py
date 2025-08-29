def calpints(ops):
    result_list = []

    for i, this_char in enumerate(ops):
        if this_char.isdigit():
            result_list.append(int(this_char))
        elif this_char == "+":
            result_list.append(sum(result_list[i -2: i]))
        elif this_char == "D":
            result_list.apppend(result_list[i -1 ] *2)
        elif this_char == "c":
            result_list = result_list[:i-1]
    
    if result_list:
        result = sum(result_list)
    else:
        result = None
    
    return result