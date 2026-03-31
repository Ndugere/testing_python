def square_of_sorted_list(nums: list) -> list:
    if not nums:
        return []
    
    if nums[0] >= 0:
        return [x * x for x in nums]
    
    idx_pos = 0

    while idx_pos < len(nums):
        if nums[idx_pos] < 0:
            idx_pos += 1
        else:
            break
    
    left_list = [ x * x for x in reversed(nums[:idx_pos])]
    right_list = [ x * x for x in nums[idx_pos: ]]

    i, j = 0,0
    res = []

    while i < len(left_list) and j < len(right_list):
        if left_list[i] < right_list[j]:
            res.append(left_list[i])
            i += 1
        else:
            res.append(right_list[j])
            j += 1
    
    while i < len(left_list):
        res.append(left_list[i])
        i+=1
    while j < len(right_list):
        res.append(right_list[j])
        j+=1
    
    return res


