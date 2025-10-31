def search_replace(my_list, search, replace):
    new_list = []
    for i, each_int in enumerate(my_list):
        if each_int == search:
            new_list.append(replace)
        else:
            new_list.append(my_list[i])
    return new_list