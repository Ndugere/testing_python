def complex_delete(a_dictionary, value):

    if not a_dictionary:
        return a_dictionary

    key_to_be_deleted = []

    for key in a_dictionary:
        if a_dictionary[key] == value:
            key_to_be_deleted.append(key)
    
    for each_key in key_to_be_deleted:
        del a_dictionary[each_key]
    

    return a_dictionary

