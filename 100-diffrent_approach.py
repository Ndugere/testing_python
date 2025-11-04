def weight_average(my_list=None):
    if not my_list:
        return 0
    
    total_score = sum(x * y for x, y in my_list)
    total_weight = sum(y for _, y in my_list)

    return total_score / total_weight if total_weight != 0 else 0
