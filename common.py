def common_elements(set_1, set_2):
    set_of_common_elements = set()

    if len(set_1) < len(set_2):
        for each_item in set_1:
            if each_item in set_2:
                set_of_common_elements.add(each_item)
    else:
        for each_item in set_2:
            if each_item in set_1:
                set_of_common_elements.add(each_item)
    
    return set_of_common_elements

    