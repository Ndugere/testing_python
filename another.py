def complex_delete(a_dictionary, value):

    if not a_dictionary:
        return a_dictionary
    
    
    keys_to_be_deleted = []

    for each_key in a_dictionary:
        if a_dictionary[each_key] == value:
            keys_to_be_deleted.append(each_key)
    

    for key in keys_to_be_deleted:
        del a_dictionary[key]
    


    return a_dictionary