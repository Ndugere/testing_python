def weight_average(my_list=[]):
    if my_list:
        score = 0
        weight = 0
        for each_tuple in my_list:
            score += (each_tuple[0] * each_tuple[1])
            weight += each_tuple[1]
        
        return score/weight
    else:
        return 0
