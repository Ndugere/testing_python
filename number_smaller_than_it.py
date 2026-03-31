def number_smaller_than_it(nums: list) -> list:
    res = []
    num_to_num_of_nums_smaller_than_it = {}
    for i, v in enumerate(sorted(nums)):
        if v not in num_to_num_of_nums_smaller_than_it:
            num_to_num_of_nums_smaller_than_it[v] = i
        else:
            continue
    
    for num in nums:
        res.append(num_to_num_of_nums_smaller_than_it[num])
    
    return res
